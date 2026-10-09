# Marketplace validation — 2026-10-09

Toolkit commit: `57a21d1304b1108df3e6b90a15a4f5dd9f0915f9`. Package SHA-256: `aa345ad75a53722ea06c43b9f3780a42b265dd04c106fba4ee88218e47bbcdee`.

## Local DIFYPKG Validation Summary

- Report directory: local validation output directory
- Blocking failures: 0
- Warning categories: 4
- Environment/check execution failures: 0

| Check | Type | Status | Findings |
|---|---|---|---|
| `package_contents` | blocking | PASS | No findings. |
| `package_secrets` | blocking | PASS | No findings. |
| `package_binaries` | blocking | PASS | No findings. |
| `manifest_metadata` | blocking | PASS | No findings. |
| `readme_metadata` | blocking | PASS | No findings. |
| `package_dependencies` | blocking | PASS | No findings. |
| `python_compile` | blocking | PASS | No findings. |
| `python_safety` | warning | PASS | flashdata/client.py:25: return value may expose credential-like values: return client.request(method, url, json=body, headers={ "X-API-Key": self.api_key, "X-Request-Id": str(uuid… |
| `prohibited_financial_activity` | warning | PASS | strong manual review required: official Dify Marketplace guidelines prohibit financial transactions, including payments, asset transfers, and token transfers |
| `access_domains` | warning | PASS | detected 2 outbound domain(s) by static scan: |
| `dependency_vulnerabilities` | warning | PASS | dependency source: requirements.txt (2 pinned, 0 unpinned) |
| `sensitive_capabilities` | blocking | PASS | No findings. |

### Skipped checks
- PR title/body language and template checks require GitHub PR metadata
- Marketplace duplicate-version check requires Marketplace/PR workflow context
- plugin install and upload-package tests are not run by this local validator

### Warnings for review
- python_safety:
  - flashdata/client.py:25: return value may expose credential-like values: return client.request(method, url, json=body, headers={ "X-API-Key": self.api_key, "X-Request-Id": str(uuid4()), "Accept": "application/json", })
- prohibited_financial_activity:
  - strong manual review required: official Dify Marketplace guidelines prohibit financial transactions, including payments, asset transfers, and token transfers
  - payment processing: README.md:48: Invalid parameters fail before any query is sent. Errors distinguish invalid keys (401), insufficient credits (402), source access (403) and rate limits (429). The plugin never ret
  - payment processing: flashdata/client.py:33: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:6)
  -   data.flashdata.dev [domain] (flashdata/client.py:7)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (2 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## Interpretation

The credential-like return warning identifies the internal HTTP request that attaches the API key header, not a credential returned by a Dify tool. The financial warning identifies external API usage/credit documentation; no payment, asset-transfer or token-transfer action exists. Domain and pinned-dependency findings are informational. The OSV result covers the two pinned direct requirements, not a guarantee about every transitive dependency.

The separate PR body validator passed. Dify Community Edition installation and real workflow tests are documented in `ce-test-results-2026-10-09.json`; Cloud and live LLM Agent tests have not been run.
