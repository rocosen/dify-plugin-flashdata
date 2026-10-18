# Repository-link package update — 2026-10-18

The 15 dedicated plugins at **0.1.2** and compatibility bundle at **0.2.3** ship the migrated `rocosen/dify-plugin-flashdata` source and workflow URLs inside the installation packages. The 0.1.1/0.2.2 release assets still contain the former `flashdata-dev` GitHub URLs; moving the repository did not rewrite those immutable packages.

## Compatibility

The Marketplace publisher remains `flashdata-dev`. Plugin, provider, tool and credential IDs are unchanged. Each package differs from its previous release only in `manifest.yaml` and `README.md`; all runtime code, dependencies, tool schemas, permissions and task boundaries are byte-identical. Existing 0.1.1 workflow examples remain compatible and are not republished as new platform templates.

## Validation

All 30 existing unit/SDK/HTTP-fixture tests passed. All 16 packages passed the official Dify Marketplace local validator with zero blocking or execution failures. The validator reports API billing terminology and network/dependency review information; it does not certify Marketplace approval. PR-body sensitive-capability disclosure, Marketplace duplicate-version checks and installation/upload checks were not run by this local validation. See [exact package hashes, comparison and validator reports](repository-link-validation-2026-10-18.json).

The package audit found no old `github.com/flashdata-dev/` or `raw.githubusercontent.com/flashdata-dev/` links in any of the 16 packages. Manifest changes are limited to version and repository URL. The old release assets are preserved.

This patch has not been installed in CE or Dify Cloud, and no real LLM agent execution was performed. No paid API query, model call or customer-storage write was made. Prior installation evidence is historical and is not a test of these exact packages.

## Release and Marketplace status

The new GitHub release tags are `task-plugins-v0.1.2` and `v0.2.3`; publication is recorded separately in GTM. As last observed on 2026-10-18, the public Marketplace serves dedicated **0.1.0** and bundle **0.2.1**. Earlier update PRs #3322–3337 return 404 from the authorized `rocosen` GitHub account; that does not establish approval, rejection or closure.

No replacement Marketplace PR is submitted by this source update. The existing submission/ownership path must be resolved before submitting an update without duplicating an inaccessible review. Follow the official one-package-per-version-update PR rule. GitHub releases do not update the Marketplace automatically; verify actual Marketplace version, README and repository links before search acceptance. The 15 existing public plugin IDs and URLs remain valid.

FlashData API usage remains paid. Attribution work and all prior pause, billing, storage and product-deployment boundaries are unchanged.
