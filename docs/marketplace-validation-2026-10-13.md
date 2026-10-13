# Marketplace validation — 2026-10-13

Version: `0.2.0`. Toolkit commit: `57a21d1304b1108df3e6b90a15a4f5dd9f0915f9` (latest when checked). Dify CLI: `0.6.10`.

Package SHA-256: `211d4118be55b7d1d5a4c5eca805e542d9cfdd07868467b43a42ae98b6fd5ed0`. Package and source release publication are separate from Marketplace review.

## Local DIFYPKG Validation Summary

- Report directory: local validation output directory
- Blocking failures: 0
- Warning categories: 3
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
| `python_safety` | warning | PASS | No findings. |
| `prohibited_financial_activity` | warning | PASS | strong manual review required: official Dify Marketplace guidelines prohibit financial transactions, including payments, asset transfers, and token transfers |
| `access_domains` | warning | PASS | detected 2 outbound domain(s) by static scan: |
| `dependency_vulnerabilities` | warning | PASS | dependency source: requirements.txt (3 pinned, 0 unpinned) |
| `sensitive_capabilities` | blocking | PASS | No findings. |

### Skipped checks
- PR title/body language and template checks require GitHub PR metadata
- Marketplace duplicate-version check requires Marketplace/PR workflow context
- plugin install and upload-package tests are not run by this local validator

### Warnings for review
- prohibited_financial_activity:
  - strong manual review required: official Dify Marketplace guidelines prohibit financial transactions, including payments, asset transfers, and token transfers
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## Interpretation and limitations

All blocking checks passed. Sensitive-capability disclosure used the High risk category because optional downloads handle cloud-storage credentials and cause writes to customer storage. The financial keyword warning is about external API credits, not payment/asset/token actions. Two fixed API hosts were statically detected; the dynamic signed-result host is declared explicitly in the manifest. The dependency report covers three pinned direct dependencies and does not guarantee every transitive dependency.

Community Edition installation, 17 tool discovery and 17 workflow imports are recorded in [the CE results](ce-test-results-2026-10-13.json). The 27 tests use HTTP fixtures; no new billable source calls were performed. Dify Cloud and a live LLM Agent remain untested.

The named Plugin Developer Agreement has no canonical link in the current template. As in accepted PR #3268, that checkbox is left unchecked and the limitation disclosed; no legal acceptance is claimed.
