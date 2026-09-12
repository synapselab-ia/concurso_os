# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: main
base_branch: main
last_implementation_branch: research/direito-b2-gate3-banca
current_task: build B2 Gate 4 coverage and authoring matrices for all six Direito SubjectPacks
current_pack: none_in_progress
last_released_pack: portugues 2.0.0
completed:
  - repository foundation and chat-independent continuity active
  - autonomous merge policy active under DEC-0009
  - TJSP 2025 adapter, edital map, blueprint and source registry created
  - historical exams 2021/2023/2024/2025 registered
  - GitHub + ChatGPT + NotebookLM stack established
  - DEC-0016 and DEC-0017 clean-corpus + native conversation configuration architecture established
  - DEC-0018 APOSTILA_AUTHORING_PROTOCOL adopted as mandatory
  - Portuguese 2.0.0 fully released with editorial, PDF and NotebookLM QA passed
  - Portuguese 2.0.0 release merged to main at e6ce9d2571e9c68a8947701c08187c07e986d567
  - B2 Gate 1 closed under DEC-0019 with six SubjectPacks
  - exact Normas da Corregedoria recuts from the edital recorded in SYLLABUS.md
  - duplicate Capitulo XI reference preserved as an official-source anomaly
  - PR 13 B2 Gate 1 preparation merged to main at 540765b17e224a319b90a4e9da5272dd4db0684e
  - B2 Gate 2 federal source audit closed and merged through PR 14 at 228f2225c3b7655d8fd47c325f7c5a2db40bf0a0
  - B2 Gate 2 state and TJSP audit closed and merged through PR 15 at fa0fb7c66f6db2d83df98bedf75b2708f51baad3
  - DIREITO_SOURCES.md promoted to closed with cutoff 2025-07-29 and post-cutoff drift separated
  - B2 Gate 3 source binaries reverified locally against SOURCES.json hashes and sizes
  - B2 Gate 3 classified 150 legal questions from 2021, 2023, 2024 and 2025
  - DIREITO_B2_BANCA_ANALYSIS.md created with reproducible taxonomy, per-question classification, domain synthesis and editorial signals
  - observed legal-question counts recorded as 40 in 2021, 40 in 2023, 40 in 2024 and 30 in 2025
  - Gate 3 preserves historical frequencies as descriptive evidence only and does not override current syllabus
  - BANCA_PROFILE.md updated to reference reproducible Direito evidence
  - DIREITO_B2_AUTHORING_PLAN.md Gate 3 promoted to closed
  - PR 18 reviewed and merged under DEC-0009
  - B2 Gate 3 historical banca analysis merged to main at c3e7e75c65ab612cd05c86cfe9c0bcadb8d66008
b2_source_gate:
  status: closed
  edital_cutoff: 2025-07-29
  verified_at: 2026-09-11
  inventory: competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md
  federal_subgate:
    status: closed
    drift_mapped:
      - CPP art. 584 paragraph 4 by Lei 15.358/2026
      - CPC art. 998 by Lei 15.484/2026
      - CPC art. 196 and art. 529-A by Lei 15.479/2026 with one-year vacatio
      - CF art. 37 XVI b by EC 138/2025
    no_scoped_textual_drift:
      - Codigo Penal
      - Lei 9.099/1995
      - Lei 12.153/2009
      - Lei 8.429/1992
  state_tjsp_subgate:
    status: closed
    drift_mapped:
      - Lei Estadual 10.261/1968 art. 78 by Lei 18.473/2026
      - LC Estadual 1.111/2010 by Lei 18.373/2025 and LC 1.441/2026
      - Regimento Interno by Assento 592/2025 and Assentos 593-596/2026
      - NSCGJ literal Capitulo XI by Provimentos CG 30/2025 and 04/2026
    no_direct_textual_drift_located:
      - Resolucao TJSP 850/2021 after Resolucao 864/2022 compilation
      - Resolucao TJSP 963/2025
    official_ambiguity:
      - edital repeats Tomo I Capitulo XI in the final two NSCGJ recuts; preserved without inferred correction
b2_banca_gate:
  status: closed
  verified_at: 2026-09-12
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md
  questions_classified: 150
  by_year:
    2021: 40
    2023: 40
    2024: 40
    2025: 30
  source_integrity: all four local exam PDFs matched SOURCES.json sha256 and byte size
  authority_rule: current syllabus remains controlling; observed distributions are non-predictive
next_gate:
  id: DIREITO-004
  name: coverage_authoring_matrices
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md
  packs:
    - direito-penal
    - direito-processual-penal
    - direito-processual-civil
    - direito-constitucional
    - direito-administrativo
    - legislacao-interna
not_started:
  - close Gate 4 coverage/authoring matrices for all six B2 SubjectPacks
  - authorize Gate 5 drafting
validation:
  portuguese_editorial_qa: pass
  portuguese_notebooklm_live: pass
  portuguese_pdf_qa:
    result: pass
    material_version: 2.0.0
    pages: 16
    page_size: A4
    bytes: 20824
    sha256: b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931
    git_blob: 640efaed13dd43cc83f6904c62fdb86131b9124a
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    reason: local runtime cannot resolve github.com, preventing a valid canonical checkout
    attempted_at: 2026-09-12
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    error: Could not resolve host github.com
    policy: impossibility documented under DEC-0009; not treated as pass
ci: disabled
last_subject_pack_pull_request: 12
last_b2_preparation_pull_request: 13
last_b2_source_pull_request: 15
last_b2_banca_pull_request: 18
merge_status: b2_gate3_closed_gate4_pending
last_b2_banca_merge_commit: c3e7e75c65ab612cd05c86cfe9c0bcadb8d66008
last_b2_source_merge_commit: fa0fb7c66f6db2d83df98bedf75b2708f51baad3
last_b2_preparation_merge_commit: 540765b17e224a319b90a4e9da5272dd4db0684e
last_release_merge_commit: e6ce9d2571e9c68a8947701c08187c07e986d567
```
