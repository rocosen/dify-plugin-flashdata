# Independent plugin package validation

All 15 final packages passed the official local validator with zero blocking failures. Warnings concern external API billing terms, fixed outbound domains and dependency scan information. All three pinned dependencies had no known vulnerabilities in this scan; this is not a guarantee about all transitive dependencies.

## google_search

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:56: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## google_news

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:58: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## google_images

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:57: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## google_shopping

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:25: Read `results[0].shopping`. Compare `title`, `productId`, merchant `source`, `price` and `link`. Keep variants and currencies separate; an offer snapshot does not guarantee invento
  - payment processing: README.md:57: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## google_videos

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:56: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## google_places

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:56: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_search

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:55: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_search_extended

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:55: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_metadata

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:51: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_transcript

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:57: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_captions

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:59: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_trainability

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:38: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_channel

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:54: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_suggestions

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:51: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

## youtube_download

## Local DIFYPKG Validation Summary

- Report directory: /privatelocal per-package report directory
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
  - payment processing: README.md:50: The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_
  - payment processing: flashdata/client.py:42: "The query outcome is unknown and may already be charged. "
- access_domains:
  - detected 2 outbound domain(s) by static scan:
  -   api.flashdata.dev [domain] (flashdata/client.py:8, flashdata/client.py:11)
  -   data.flashdata.dev [domain] (flashdata/client.py:9, flashdata/client.py:10)
- dependency_vulnerabilities:
  - dependency source: requirements.txt (3 pinned, 0 unpinned)
  - no known vulnerabilities in the pinned dependency set

