# Chinese website links — 2026-10-21

Dedicated plugins 0.1.3 and compatibility bundle 0.2.4 use `/zh/docs` and `/zh/pricing` links in their existing README files, preserving every attribution query parameter. API-key setup URLs remain `/app/api-keys`; the website now preserves the selected language through authentication and console navigation.

All 16 packages were compared with the published 0.1.2/0.2.3 packages. Only `README.md` and the manifest version differ; runtime code, dependencies, schemas, provider/tool identities, credentials, permissions and icons are byte-identical. All 30 existing tests pass after updating the documentation URL expectation. All 16 packages passed the official Marketplace local validator with zero blocking or execution failures. No paid query, model call or storage write was performed. These exact packages have not been installed in CE or Cloud; package release and local validation do not imply Marketplace approval.

The previous 0.1.2/0.2.3 versions are active in Marketplace. New version updates follow the existing publisher and one-package-per-PR submission path. Approval and public README readback are recorded in GTM.
