# Display-name update — 0.2.1

The plugin display name and README heading are now **Google Search & YouTube Tools**. This is a metadata-only patch to the already published 0.2.0; the original release remains available. The provider ID, tool IDs, parameters, runtime implementation, dependencies and 17 examples are unchanged.

Package SHA-256: `84207fcb09fc99a763b1eb8cbe93154526af7bb6e9b9d4a269713ab40cc26576`. Size: 37031 bytes. ZIP entry comparison against the 0.2.0 release changed exactly `manifest.yaml`, `provider/flashdata.yaml` and `README.md`. All other packaged files are byte-identical.

The CE 17-tool discovery/17-workflow imports and 27 fixture tests in [the 0.2.0 evidence](ce-test-results-2026-10-13.json) remain historical evidence for that runtime. No new billable source requests or storage writes were made for this name change. Cloud/live Agent limitations remain unchanged.

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

The separate PR-body check also passed. This package updates the existing Marketplace PR3303; a released GitHub package does not mean the Marketplace page has updated.
