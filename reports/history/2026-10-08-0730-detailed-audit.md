# ⚡ DPN ENTERPRISE GREENKEEPER // VERIFIED PARTIAL AUDIT

**Run:** October 8, 2026, approximately 07:30–07:35 EDT. **Original publication:** Local fallback report after GitHub writes were blocked during the run. **Archive publication:** subsequently attempted from this conversation; original scan remains a historical PARTIAL audit.

> L3 RED — PRIVATE OPERATIONS. This document contains repository identities; do not publish publicly. **PARTIAL:** Default-branch SHA, protection rules, current alert inventories and release inventories were not verified.

## Executive scoreboard

- **23** accessible organization repositories; **59** open PRs (fresh GitHub discovery).
- **41** PRs with at least one failed observed workflow; **13** non-draft PRs with no failed observed workflows; **1** draft PR with one successful workflow; **4** PRs with no associated workflow-run evidence.
- **0** verified merge-ready PRs: branch protection / required approvals could not be verified. **0** merges and **0** releases executed. GitHub mergeability API returned TRUE for 39 PRs and FALSE for 20 (not equivalent to protection approval).
- **0** GitHub report commits: update_file and create_file operations were blocked by execution safety checks.

## Repository inventory

| Repository | Open PRs | Default SHA | Default CI / security | Latest release |
|---|---:|---|---|---|
| [DPN-Aqua-Labs-Point-of-Sale-System](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System) | 8 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-War-Simulator](https://github.com/DPN-Technology/DPN-War-Simulator) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Executive-Control-System](https://github.com/DPN-Technology/DPN-Executive-Control-System) | 3 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Watch-Tower](https://github.com/DPN-Technology/DPN-Watch-Tower) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Human-Resources-Software](https://github.com/DPN-Technology/DPN-Human-Resources-Software) | 4 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Workforce-Time-Management-System](https://github.com/DPN-Technology/DPN-Workforce-Time-Management-System) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-AI](https://github.com/DPN-Technology/DPN-AI) | 11 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-QB-FiveM-Scripts](https://github.com/DPN-Technology/DPN-QB-FiveM-Scripts) | 0 | UNKNOWN | UNKNOWN | UNKNOWN |
| [MemeSpace](https://github.com/DPN-Technology/MemeSpace) | 1 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Death-the-Developer](https://github.com/DPN-Technology/DPN-Death-the-Developer) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Website](https://github.com/DPN-Technology/DPN-Website) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Operational-Control](https://github.com/DPN-Technology/DPN-Operational-Control) | 8 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-One](https://github.com/DPN-Technology/DPN-One) | 3 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Service-Desk](https://github.com/DPN-Technology/DPN-Service-Desk) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-OS](https://github.com/DPN-Technology/DPN-OS) | 2 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Tool-Die-Simulator](https://github.com/DPN-Technology/DPN-Tool-Die-Simulator) | 3 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Network-Mapper](https://github.com/DPN-Technology/DPN-Network-Mapper) | 3 | UNKNOWN | UNKNOWN | UNKNOWN |
| [.github](https://github.com/DPN-Technology/.github) | 0 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Technology.github.io](https://github.com/DPN-Technology/DPN-Technology.github.io) | 0 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DreamBound-Adventures](https://github.com/DPN-Technology/DreamBound-Adventures) | 0 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-PlantPulse](https://github.com/DPN-Technology/DPN-PlantPulse) | 0 | UNKNOWN | UNKNOWN | UNKNOWN |
| [The-Last-Settlement](https://github.com/DPN-Technology/The-Last-Settlement) | 1 | UNKNOWN | UNKNOWN | UNKNOWN |
| [DPN-Enterprise-Greenkeeper](https://github.com/DPN-Technology/DPN-Enterprise-Greenkeeper) | 0 | UNKNOWN | UNKNOWN | UNKNOWN |

## Complete open PR register — exact heads and observed workflow results

Status definitions: **RED** = at least one failed observed workflow; **OBSERVED PASS** = observed runs show no failures (does NOT prove required checks/reviews); **DRAFT** = do not merge; **UNKNOWN** = no PR workflow runs returned. Mergeability was checked for all 59; this register does not claim protection/approval eligibility.

| PR / title | Head SHA | Mergeable API | Reviews / protections | Observed runs | Gate observation | Named failed workflows |
|---|---|---|---|---:|---|---|
| [MemeSpace #15](https://github.com/DPN-Technology/MemeSpace/pull/15) — Improve MemeSpace arcade games for v2.6 | `abe51535de057e6ac22776af9200e5f53bba153c` | TRUE | COMMENTED only; protection UNKNOWN | 7 | 🟢 OBSERVED PASS | - |
| [The-Last-Settlement #5](https://github.com/DPN-Technology/The-Last-Settlement/pull/5) — feat(ui): teach survivor duty controls in field guide | `75de4612bdce303e94e3ea66c71d179170dcc635` | TRUE | No approvals observed; protection UNKNOWN | 3 | 🟢 OBSERVED PASS | - |
| [DPN-Workforce-Time-Management-System #13](https://github.com/DPN-Technology/DPN-Workforce-Time-Management-System/pull/13) — Bump anchore/sbom-action to 0.24.3 | `36b36c9fac0d14420a4d44d6b874dadfadeeafaf` | TRUE | UNKNOWN | 7 | 🔴 RED | DPN Security Gate v2,CI,Cross-Platform CI,DPN Security Baseline,Supply Chain,Repository Health,CodeQL Advanced |
| [DPN-War-Simulator #24](https://github.com/DPN-Technology/DPN-War-Simulator/pull/24) — Bump actions/upload-artifact to 7.0.1 | `bb34cb7b3fcf22811bba886968dcaf9e1f6353fe` | TRUE | No approvals observed; protection UNKNOWN | 9 | 🟢 OBSERVED PASS | - |
| [DPN-War-Simulator #23](https://github.com/DPN-Technology/DPN-War-Simulator/pull/23) — Bump anchore/sbom-action to 0.24.3 | `eb82c7f754bc5115da46a9d1043283ad04bc34e1` | TRUE | UNKNOWN | 9 | 🟢 OBSERVED PASS | - |
| [DPN-Executive-Control-System #20](https://github.com/DPN-Technology/DPN-Executive-Control-System/pull/20) — Bump anchore/sbom-action to 0.24.3 | `32f764b3c065dcdd21a869b5f74190419bae2c60` | TRUE | UNKNOWN | 7 | 🔴 RED | CI,Repository Health,Supply Chain,CodeQL Advanced,DPN Security Gate v2,DPN Advanced Security,DPN Security Baseline |
| [DPN-AI #154](https://github.com/DPN-Technology/DPN-AI/pull/154) — Bump anchore/sbom-action to 0.24.3 | `8e9fdf0b99cadc471cd4c3c9f80f66f102b80eaf` | TRUE | UNKNOWN | 7 | 🔴 RED | DPN Security Gate v2,DPN CodeQL Advanced Security,DPN Enterprise Critical Gate,DPN Security Baseline,Repository Health,Supply Chain,CI |
| [DPN-AI #153](https://github.com/DPN-Technology/DPN-AI/pull/153) — Update ruff | `235e7ad0b7e06c8505529d17bf033cdc1cb3aba7` | TRUE | UNKNOWN | 9 | 🔴 RED | DPN Security Baseline,Third-Party License Governance,DPN Enterprise Critical Gate,DPN CodeQL Advanced Security,DPN Security Gate v2,Runtime & Recovery Assurance,CI,Repository Health |
| [DPN-AI #152](https://github.com/DPN-Technology/DPN-AI/pull/152) — Update uvicorn | `78da6c029ee512be4d20368bf125fa2c6604f90e` | TRUE | UNKNOWN | 9 | 🔴 RED | DPN Security Baseline,Third-Party License Governance,DPN Security Gate v2,DPN Enterprise Critical Gate,CI,Repository Health,Runtime & Recovery Assurance,DPN CodeQL Advanced Security |
| [DPN-AI #151](https://github.com/DPN-Technology/DPN-AI/pull/151) — Update fastapi | `8d0fafc62d8a9db073f33f10a4ffddc3df8fd90f` | TRUE | UNKNOWN | 9 | 🔴 RED | Repository Health,CI,Runtime & Recovery Assurance,Third-Party License Governance,DPN Security Baseline,DPN Security Gate v2,DPN Enterprise Critical Gate,DPN CodeQL Advanced Security |
| [DPN-Human-Resources-Software #20](https://github.com/DPN-Technology/DPN-Human-Resources-Software/pull/20) — Bump anchore/sbom-action | `c6ade296f5e7516353595e5af9b52d449f6021a9` | TRUE | UNKNOWN | 6 | 🔴 RED | DPN Security Baseline,Supply Chain,DPN Security Gate v2,CI,DPN Advanced Security,Repository Health |
| [DPN-Aqua-Labs-Point-of-Sale-System #48](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/48) — Bump anchore/sbom-action | `6cfe8f9552920741aa5181981fd68657c8d65835` | TRUE | UNKNOWN | 8 | 🔴 RED | Repository Health,CI,DPN Security Gate v2,Supply Chain,DPN Advanced Security,CodeQL Advanced,Cross-Platform CI,DPN Security Baseline |
| [DPN-Aqua-Labs-Point-of-Sale-System #47](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/47) — Update website fastapi | `9cfe9032a0cd02ebcbe0f8b51b9815b065d3cab4` | TRUE | UNKNOWN | 7 | 🔴 RED | Supply Chain,DPN Advanced Security,Cross-Platform CI,DPN Security Gate v2,CI,DPN Security Baseline,CodeQL Advanced |
| [DPN-Aqua-Labs-Point-of-Sale-System #46](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/46) — Update cryptography | `b25be5dac1de8fa5126d2922f3387b21fa9aeeaf` | TRUE | UNKNOWN | 8 | 🔴 RED | Cross-Platform CI,CI,Runtime & Recovery Assurance,DPN Advanced Security,DPN Security Gate v2,CodeQL Advanced,Supply Chain,DPN Security Baseline |
| [DPN-Aqua-Labs-Point-of-Sale-System #45](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/45) — Update fastapi | `13327d06d5956c8ad686cb4fe8456bdeecc3555e` | TRUE | UNKNOWN | 7 | 🔴 RED | CodeQL Advanced,DPN Security Baseline,Cross-Platform CI,Supply Chain,DPN Security Gate v2,DPN Advanced Security,CI |
| [DPN-Tool-Die-Simulator #6](https://github.com/DPN-Technology/DPN-Tool-Die-Simulator/pull/6) — Enterprise governance | `338c5cde22253de59879f2b66441c682fc162a6a` | TRUE | UNKNOWN | 5 | 🔴 RED | Core Simulation CI,CodeQL Advanced,Security and Repository Integrity,DPN Security Baseline,DPN Enterprise Standard Gate |
| [DPN-Death-the-Developer #8](https://github.com/DPN-Technology/DPN-Death-the-Developer/pull/8) — Enterprise governance | `8484cc383636b7b74d7abdb1887f85819a36dc4e` | TRUE | UNKNOWN | 5 | 🔴 RED | DPN Security Baseline,DPN Enterprise Elevated Gate,CodeQL Advanced,Security Gates,CI |
| [DPN-Network-Mapper #15](https://github.com/DPN-Technology/DPN-Network-Mapper/pull/15) — Enterprise governance | `159f0e15cb1e3747770f382ca5b6528b5c729541` | TRUE | UNKNOWN | 6 | 🔴 RED | DPN Enterprise Elevated Gate,CodeQL,Secret Scan,Supply Chain Integrity,DPN Security Baseline,CI |
| [DPN-OS #6](https://github.com/DPN-Technology/DPN-OS/pull/6) — Enterprise governance | `97bb2a22eacb9bb598c0235de8afad6fa7091408` | TRUE | UNKNOWN | 6 | 🔴 RED | DPN Security Baseline,DPN OS security and quality gates,DPN Enterprise Elevated Gate,DPN OS provenance and history security,DPN OS source validation,CodeQL Advanced |
| [DPN-Aqua-Labs-Point-of-Sale-System #44](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/44) — Enterprise governance | `f90ccd8990451c38ccec3ebaf0c3eb4d5a4ac0be` | TRUE | UNKNOWN | 9 | 🔴 RED | DPN Enterprise Elevated Gate,DPN Security Baseline,Cross-Platform CI,DPN Security Gate v2,CodeQL Advanced,DPN Advanced Security,Repository Health,Supply Chain,CI |
| [DPN-One #24](https://github.com/DPN-Technology/DPN-One/pull/24) — Enterprise governance | `62131661800ad89d3e3bbf3f190e87221efa5951` | TRUE | UNKNOWN | 6 | 🔴 RED | DPN Enterprise Critical Gate,CI,CodeQL,Secret Scan,DPN Security Baseline,Dependency Audit |
| [DPN-Workforce-Time-Management-System #12](https://github.com/DPN-Technology/DPN-Workforce-Time-Management-System/pull/12) — Enterprise governance | `c42e2572afadf675277681d847992d28a8fd8417` | FALSE | UNKNOWN | 7 | 🔴 RED | DPN Security Gate v2,DPN Security Baseline,CI,Repository Health,Cross-Platform CI,DPN Enterprise Critical Gate,CodeQL Advanced |
| [DPN-Human-Resources-Software #19](https://github.com/DPN-Technology/DPN-Human-Resources-Software/pull/19) — Enterprise governance | `0c71865744932fb04fcc6f39637794a2e641ee3e` | TRUE | UNKNOWN | 6 | 🔴 RED | DPN Enterprise Critical Gate,CI,DPN Security Gate v2,Repository Health,DPN Security Baseline,DPN Advanced Security |
| [DPN-Executive-Control-System #19](https://github.com/DPN-Technology/DPN-Executive-Control-System/pull/19) — Enterprise governance | `b4e8452469eae194a9fe8bdf8c2aee8ee8914589` | FALSE | UNKNOWN | 7 | 🔴 RED | CodeQL Advanced,DPN Security Baseline,DPN Enterprise Critical Gate,CI,DPN Advanced Security,Repository Health,DPN Security Gate v2 |
| [DPN-Operational-Control #25](https://github.com/DPN-Technology/DPN-Operational-Control/pull/25) — Enterprise governance | `67765ba45e629b46de0f75e39f863ff8437f96f3` | FALSE | UNKNOWN | 7 | 🔴 RED | Supply Chain Integrity,CI,DPN Enterprise Critical Gate,Secret Scan,DPN Security Baseline,CodeQL Advanced,Security Gates |
| [DPN-Operational-Control #23](https://github.com/DPN-Technology/DPN-Operational-Control/pull/23) — Enterprise enforcement matrix | `03d2683040e816c2d2b0852cbf7d5859caf9400d` | TRUE | UNKNOWN | 6 | 🔴 RED | CI,Secret Scan,CodeQL Advanced,Security Gates,DPN Security Baseline,Supply Chain Integrity |
| [DPN-Tool-Die-Simulator #5](https://github.com/DPN-Technology/DPN-Tool-Die-Simulator/pull/5) — Publish CodeQL results | `72dce87eaa985be3ca805ff376687e43f84f257e` | FALSE | UNKNOWN | 4 | 🔴 RED | Security and Repository Integrity |
| [DPN-Watch-Tower #13](https://github.com/DPN-Technology/DPN-Watch-Tower/pull/13) — Publish CodeQL results | `d659431cb3810d675d10c2858f87270204c0649c` | FALSE | UNKNOWN | 6 | 🔴 RED | Repository Health,DPN Advanced Security |
| [DPN-Aqua-Labs-Point-of-Sale-System #42](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/42) — Publish CodeQL results | `de5aa542f036f7a144c887f084146c751d3c4fc1` | FALSE | UNKNOWN | 0 | ⚪ UNKNOWN | - |
| [DPN-Death-the-Developer #5](https://github.com/DPN-Technology/DPN-Death-the-Developer/pull/5) — Publish CodeQL results | `4b42c57b4f2b28175b875c5a0783cfc9cd2d2c0f` | FALSE | UNKNOWN | 4 | 🟢 OBSERVED PASS | - |
| [DPN-Executive-Control-System #17](https://github.com/DPN-Technology/DPN-Executive-Control-System/pull/17) — Publish CodeQL results | `cb2bed774740ecf90f7fc34f3fcef2bc166678dd` | FALSE | UNKNOWN | 6 | 🔴 RED | Repository Health,DPN Advanced Security |
| [DPN-AI #150](https://github.com/DPN-Technology/DPN-AI/pull/150) — Publish CodeQL results | `104a636cf4b988a2653144074f7b3352bb024b87` | FALSE | UNKNOWN | 5 | 🔴 RED | Repository Health |
| [DPN-Human-Resources-Software #18](https://github.com/DPN-Technology/DPN-Human-Resources-Software/pull/18) — Publish CodeQL results | `7dbe6ff881bd64a8e7b160d1b00938ed57362d25` | FALSE | UNKNOWN | 5 | 🟢 OBSERVED PASS | - |
| [DPN-One #22](https://github.com/DPN-Technology/DPN-One/pull/22) — Publish CodeQL results | `7e48ff91c20c9706cf230cc80ffc7daec18658a1` | FALSE | UNKNOWN | 5 | 🔴 RED | Secret Scan,Dependency Audit |
| [DPN-AI #149](https://github.com/DPN-Technology/DPN-AI/pull/149) — Remediate CodeQL ReDoS | `1d7fac0e54a75c8ad25b0269582e4aeae7a2935b` | TRUE | No approvals observed; protection UNKNOWN | 8 | 🔴 RED | DPN Enterprise Critical Gate,DPN Security Gate v2,CI,DPN CodeQL Advanced Security,DPN Security Baseline,Repository Health,Runtime & Recovery Assurance |
| [DPN-Operational-Control #20](https://github.com/DPN-Technology/DPN-Operational-Control/pull/20) — Remediate CodeQL secret hashing | `9fec0a50fbcea70c7a68b17e5d8de6a434b0c1d7` | FALSE | UNKNOWN | 6 | 🟢 OBSERVED PASS | - |
| [DPN-Network-Mapper #14](https://github.com/DPN-Technology/DPN-Network-Mapper/pull/14) — Harden API boundary | `c2f1ba0447c0ddae1cf66a85c80ec4b37be7866a` | FALSE | UNKNOWN | 4 | 🟢 OBSERVED PASS | - |
| [DPN-Service-Desk #15](https://github.com/DPN-Technology/DPN-Service-Desk/pull/15) — Enterprise governance | `1aa0cfa1f088b6d55610f27e00339cc742ce2364` | FALSE | UNKNOWN | 0 | ⚪ UNKNOWN | - |
| [DPN-Website #4](https://github.com/DPN-Technology/DPN-Website/pull/4) — Enterprise governance | `3048db71b3a276f0358474396bcbc59191871cf4` | FALSE | UNKNOWN | 0 | ⚪ UNKNOWN | - |
| [DPN-Website #2](https://github.com/DPN-Technology/DPN-Website/pull/2) — Bump actions/checkout | `eb6bf3a68c503c18d647b71dfecbae656b9e423d` | FALSE | UNKNOWN | 4 | 🔴 RED | Security Gates |
| [DPN-One #20](https://github.com/DPN-Technology/DPN-One/pull/20) — Bump actions/checkout | `219ac99f0f6a8a969e5ba39349ff71958e923001` | FALSE | UNKNOWN | 5 | 🔴 RED | Dependency Audit |
| [DPN-OS #3](https://github.com/DPN-Technology/DPN-OS/pull/3) — DPN OS QC dashboard | `57f50e28f68a955e569d804aea2a34ed086b65d5` | TRUE | UNKNOWN | 4 | 🔴 RED | DPN OS security and quality gates,DPN OS provenance and history security |
| [DPN-AI #147](https://github.com/DPN-Technology/DPN-AI/pull/147) — Bump platformdirs | `33cb22febc0abdb75b7a78f9b60b329a5f08b4ad` | TRUE | UNKNOWN | 4 | 🟢 OBSERVED PASS | - |
| [DPN-AI #146](https://github.com/DPN-Technology/DPN-AI/pull/146) — Bump filelock | `ea82c7e410848bf4d874b8f4f5c48b7cd68233cc` | TRUE | UNKNOWN | 4 | 🟢 OBSERVED PASS | - |
| [DPN-AI #145](https://github.com/DPN-Technology/DPN-AI/pull/145) — Bump msgpack | `a2fc1286cb49c53ae00ba16318b40017460205e3` | TRUE | UNKNOWN | 4 | 🟢 OBSERVED PASS | - |
| [DPN-Watch-Tower #11](https://github.com/DPN-Technology/DPN-Watch-Tower/pull/11) — Bump actions/checkout | `ffefe3828381ea3cad89fcb8a596f4649e21dc2c` | FALSE | UNKNOWN | 5 | 🔴 RED | DPN Advanced Security |
| [DPN-Service-Desk #13](https://github.com/DPN-Technology/DPN-Service-Desk/pull/13) — Bump actions/setup-node | `fb0609b0eb01b9246d9757e809a71c3c50ab4ef4` | FALSE | UNKNOWN | 6 | 🟢 OBSERVED PASS | - |
| [DPN-AI #142](https://github.com/DPN-Technology/DPN-AI/pull/142) — Bump pyinstaller | `aa565b32bdb8332cca5cebddfca261b2476365b7` | TRUE | UNKNOWN | 8 | 🔴 RED | Repository Health |
| [DPN-AI #141](https://github.com/DPN-Technology/DPN-AI/pull/141) — Bump openpyxl | `6cd6281e3246aad23f3f1dc78bea6542706e5bd3` | TRUE | UNKNOWN | 8 | 🟢 OBSERVED PASS | - |
| [DPN-Operational-Control #17](https://github.com/DPN-Technology/DPN-Operational-Control/pull/17) — Bump pywebview | `fc18b84be1531d44ee960c45188a4f11cbd89494` | TRUE | UNKNOWN | 5 | 🔴 RED | DPN Security Baseline,Secret Scan |
| [DPN-Operational-Control #16](https://github.com/DPN-Technology/DPN-Operational-Control/pull/16) — Bump pytest | `2b6a4813e614f9afb00b3405eda3dd1d012d7bf9` | TRUE | UNKNOWN | 5 | 🔴 RED | DPN Security Baseline,Secret Scan |
| [DPN-Network-Mapper #11](https://github.com/DPN-Technology/DPN-Network-Mapper/pull/11) — Bump actions/checkout | `64e0c60533e6b3b1458d9f94c37c8819b496299c` | FALSE | UNKNOWN | 0 | ⚪ UNKNOWN | - |
| [DPN-Operational-Control #15](https://github.com/DPN-Technology/DPN-Operational-Control/pull/15) — Bump cryptography | `16ead8fa569485ccd4f5e45599570de06419ee38` | TRUE | UNKNOWN | 5 | 🔴 RED | Secret Scan,DPN Security Baseline |
| [DPN-Operational-Control #14](https://github.com/DPN-Technology/DPN-Operational-Control/pull/14) — Bump pydantic | `f92f85c3403d8372bd6616ff193480fc3bb5909d` | TRUE | UNKNOWN | 5 | 🔴 RED | Secret Scan,DPN Security Baseline |
| [DPN-Operational-Control #13](https://github.com/DPN-Technology/DPN-Operational-Control/pull/13) — Bump fastapi | `0961c3e8fd0a02ca06b1c2023b4c2b2d0ec7958e` | TRUE | UNKNOWN | 5 | 🔴 RED | Secret Scan,DPN Security Baseline |
| [DPN-Aqua-Labs-Point-of-Sale-System #38](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/38) — Update website uvicorn | `f8d6c16d738c66a814dc51bbcab7852e03d62271` | TRUE | UNKNOWN | 5 | 🔴 RED | DPN Advanced Security |
| [DPN-Aqua-Labs-Point-of-Sale-System #37](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/37) — Update uvicorn | `deacbd9d4c0e1f84480bf6c6cec7c011600491ce` | TRUE | UNKNOWN | 5 | 🔴 RED | DPN Advanced Security |
| [DPN-Human-Resources-Software #15](https://github.com/DPN-Technology/DPN-Human-Resources-Software/pull/15) — Full-history secret scanning | `6cc8ce7b67294b4b379fe83fa6a45f1b8d031fd4` | TRUE | UNKNOWN | 6 | 🔴 RED | DPN Security Gate v2,Full-History Secret Scan,DPN Security Baseline,CI,Repository Health,DPN Advanced Security |
| [DPN-Tool-Die-Simulator #1](https://github.com/DPN-Technology/DPN-Tool-Die-Simulator/pull/1) — v0.3 Tool Room & Machining | `6ed407f8962d4658b48d696ef8cbec1a1e019d45` | TRUE | UNKNOWN | 1 | 🟣 DRAFT | - |

## P0 / P1 diagnostics and remediation evidence

### Tool & Die Simulator PR #5 — new confirmed root cause

- **PR head:** `72dce87eaa985be3ca805ff376687e43f84f257e`.
- **Failed workflow:** Security and Repository Integrity; run `37190514676`, job `111401515595`, step `Scan history`.
- **Exact log cause:** `missing gitleaks license` from `gitleaks/gitleaks-action@v3`; requires `GITLEAKS_LICENSE` secret. This is a licensing/startup blocker, **not proof of a detected secret**.
- **Other jobs:** CodeQL C/C++ and repository integrity passed; Core Simulation CI, CodeQL Advanced and DPN Security Baseline workflows passed.
- **Safe remediation prepared:** replace the licensed action with checksum-verified Gitleaks CLI v8.28.0 and scan all Git history with redacted output, preserving secret-scanning enforcement. GitHub update was rejected by execution safety checks; **no fix committed**.
- [PR](https://github.com/DPN-Technology/DPN-Tool-Die-Simulator/pull/5) · [Failed workflow](https://github.com/DPN-Technology/DPN-Tool-Die-Simulator/actions/runs/37190514676)

### Aqua Labs PR #42 — remaining policy issue

- **PR head:** `de5aa542f036f7a144c887f084146c751d3c4fc1`; prior CodeQL pinning fix already exists.
- `.github/workflows/ui-evidence-capture.yml` still uses mutable `actions/checkout@v4` and `actions/setup-python@v5` and lacks `persist-credentials: false`.
- A focused fix using SHA references already used by this repository was attempted; **GitHub blocked the write**. Current PR-head workflow runs were unavailable; do not claim green.
- [PR](https://github.com/DPN-Technology/DPN-Aqua-Labs-Point-of-Sale-System/pull/42)

### DPN AI — workflow-startup failures

- PR #149 head `1d7fac0e54a75c8ad25b0269582e4aeae7a2935b`: seven observed workflows failed. CI run `37729995236` returned four failed jobs with **no step summaries**; job log fetch returned `BlobNotFound` (404). Root cause not verified.
- PR #154 and related dependency PRs also show multiple failed workflows. Do not weaken CI to hide startup failures.

### PRs with all observed workflows passing, still awaiting protection/approval verification

- [MemeSpace #15](https://github.com/DPN-Technology/MemeSpace/pull/15): 7 successful workflows at `abe51535de057e6ac22776af9200e5f53bba153c`; six review threads resolved; reviews are comments, not approvals.
- [The Last Settlement #5](https://github.com/DPN-Technology/The-Last-Settlement/pull/5): 3 successful workflows at `75de4612bdce303e94e3ea66c71d179170dcc635`; no approvals observed.
- [War Simulator #23](https://github.com/DPN-Technology/DPN-War-Simulator/pull/23) and [#24](https://github.com/DPN-Technology/DPN-War-Simulator/pull/24): 9 successful workflows each; #24 had no approvals observed.

## Security / release / operations ledger

- **Security alert totals:** UNKNOWN (CodeQL, Dependabot, secret scanning, and branch protection endpoints were not comprehensively accessible). Observed failed security workflow is not equivalent to a confirmed vulnerability.
- **Default branch health:** UNKNOWN estate-wide. Commit status endpoint returned empty statuses on sampled PR heads; GitHub Actions run conclusions were used instead.
- **Latest releases/tags and artifact checksums:** UNKNOWN; connected GitHub tools did not expose release listing/publishing actions. No release authorized.
- **Exact-head merges:** none attempted because required review/protection evidence was missing. No branch refs were modified.
- **Reporting:** `reports/latest.md` run-start update blocked; `reports/estate.md` inventory update blocked; hourly history create blocked. All returned the execution safety-check denial. Do not treat GitHub dashboard as refreshed.
- **Movement from previous completed report:** no verified transition; inventory count remains 23/59, but full prior gate-level baseline was absent.

## Next actions

1. Resolve GitHub integration write safety restriction without bypassing permissions; then commit this detailed report to the private Greenkeeper repository using current blob SHAs.
2. Apply the Gitleaks CLI replacement to Tool & Die Simulator PR #5 and verify the full-history scan.
3. Pin the Aqua Labs UI-evidence actions and isolate checkout credentials on PR #42; rerun Repository Health.
4. Diagnose DPN AI job startup using GitHub runner/workflow diagnostics; logs were unavailable.
5. Verify branch protection/rulesets and approvals for observed-green PRs before any native exact-head merge.
6. Complete default-branch and release inventory; only publish releases with verified artifacts and checksums.

> **DPN // DEVELOP. PIONEER. NAVIGATE.** — Evidence before green. Integrity before release.