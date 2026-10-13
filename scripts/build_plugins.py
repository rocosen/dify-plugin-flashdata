"""Build independent Dify plugins from the shared, tested FlashData runtime."""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "plugins/catalog.json").read_text())


def build_source(source: str, destination: Path) -> dict:
    config = CATALOG[source]
    destination.mkdir(parents=True, exist_ok=False)
    tools = [source]
    if source == "youtube_download":
        tools += ["get_job", "get_job_results"]

    manifest = yaml.safe_load((ROOT / "manifest.yaml").read_text())
    manifest.update(name=config["name"], version=config["version"],
                    label=config["label"], description=config["description"],
                    created_at="2026-10-13T06:00:00Z", tags=config["tags"])
    if source != "youtube_download":
        manifest["network"]["domains"] = ["api.flashdata.dev", "data.flashdata.dev"]

    provider = yaml.safe_load((ROOT / "provider/flashdata.yaml").read_text())
    provider["identity"].update(name=config["name"], label=config["label"],
                                description=config["description"], tags=config["tags"])
    provider["tools"] = [f"tools/{tool}.yaml" for tool in tools]
    credentials = provider["credentials_for_provider"]
    credentials["api_key"]["url"] = (
        "https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration"
        f"&utm_campaign=intent_gtm_2026q4&utm_content={source}-setup"
    )
    if source != "youtube_download":
        del credentials["download_storage"]

    for directory in ["provider", "tools", "flashdata", "_assets"]:
        (destination / directory).mkdir()
    for filename in ["main.py", "requirements.txt", "LICENSE", "SECURITY.md"]:
        shutil.copyfile(ROOT / filename, destination / filename)
    for filename in ["README.md", "PRIVACY.md"]:
        shutil.copyfile(ROOT / "plugins" / source / filename, destination / filename)
    shutil.copyfile(ROOT / "_assets/icon.svg", destination / "_assets/icon.svg")
    shutil.copyfile(ROOT / "provider/flashdata.py", destination / "provider/flashdata.py")
    for path in (ROOT / "flashdata").glob("*.py"):
        shutil.copyfile(path, destination / "flashdata" / path.name)
    catalog = json.loads((ROOT / "flashdata/sources.json").read_text())
    catalog["sources"] = {source: catalog["sources"][source]}
    (destination / "flashdata/sources.json").write_text(json.dumps(catalog, indent=2) + "\n")
    for tool in tools:
        for extension in ["py", "yaml"]:
            shutil.copyfile(ROOT / "tools" / f"{tool}.{extension}", destination / "tools" / f"{tool}.{extension}")
    (destination / "manifest.yaml").write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True))
    (destination / "provider/flashdata.yaml").write_text(yaml.safe_dump(provider, sort_keys=False, allow_unicode=True))
    return manifest


def workflow(source: str, tool: str) -> dict:
    config = CATALOG[source]
    data = yaml.safe_load((ROOT / "examples" / f"{tool}.yml").read_text())
    data = copy.deepcopy(data)
    data["app"]["name"] = f"{config['label']['en_US']} — {tool.replace('_', ' ').title()}"
    data["app"]["description"] = (
        f"Uses the independent {config['label']['en_US']} plugin "
        f"(flashdata-dev/{config['name']} {config['version']}). Configure its provider credential before running."
    )
    provider = f"flashdata-dev/{config['name']}/{config['name']}"
    for node in data["workflow"]["graph"]["nodes"]:
        if node["data"]["type"] == "tool":
            node["data"].update(provider_id=provider, provider_name=provider)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", choices=list(CATALOG))
    parser.add_argument("--cli", default="dify")
    parser.add_argument("--output", type=Path, default=ROOT / "dist/task-plugins")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    sources = [args.source] if args.source else list(CATALOG)
    packages = []
    for source in sources:
        with tempfile.TemporaryDirectory(prefix="flashdata-dify-") as stage:
            directory = Path(stage) / source
            manifest = build_source(source, directory)
            package = args.output / f"{manifest['name']}-{manifest['version']}.difypkg"
            subprocess.run([args.cli, "plugin", "package", str(directory), "-o", str(package.resolve())], check=True)
        packages.append({"source": source, "name": manifest["name"], "version": manifest["version"],
                         "package": package.name, "bytes": package.stat().st_size,
                         "sha256": hashlib.sha256(package.read_bytes()).hexdigest()})
    (args.output / "packages.json").write_text(json.dumps(packages, indent=2) + "\n")
    (args.output / "SHA256SUMS").write_text("".join(f"{p['sha256']}  {p['package']}\n" for p in packages))
    print(f"Built {len(packages)} independent plugins in {args.output}")


if __name__ == "__main__":
    main()
