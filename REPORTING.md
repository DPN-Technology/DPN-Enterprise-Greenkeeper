# Reporting Contract

1. Start with fresh paginated repository and open-PR discovery; disclose missing access and incomplete pages.
2. Record exact PR head SHA, title, draft, mergeability, reviews, branch protections, individual check conclusions, and release relevance. Unknown is not green.
3. Prioritize security/default-branch red gates, then actionable PR blockers, then verified merges and releases.
4. Fix root causes on existing PR branches where safe. Never weaken security or tests for green status.
5. Refetch and verify exact-head checks, approvals and protections immediately before native merge with expected_head_sha; verify post-merge default branch.
6. Publish releases only after green default-branch and release gates, valid versions, artifacts, checksums and notes.
7. Update reports/latest.md, append a timestamped history report, and maintain per-PR diagnostics. README.md should show the last *verified* report timestamp and links, not stale live claims.
8. Never post credentials, tokens, sensitive private logs or unverifiable claims. Report denied writes or missing data explicitly.
9. Send ChatGPT notifications only for meaningful remediation, merges, releases, security discoveries, or required approvals. Dashboard updates should not spam issues.
