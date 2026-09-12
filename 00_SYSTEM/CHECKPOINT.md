# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: main
base_branch: main
last_implementation_branch: research/direito-b2-gate2-state-tjsp
current_task: start B2 Gate 3 by classifying Direito questions from the 2021, 2023, 2024 and 2025 TJSP/VUNESP exams reproducibly
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
  - Portuguese 1.0.0 audited
  - Portuguese 2.0.0 authoring matrix closed with B1.1-B1.13 covered
  - Portuguese 2.0.0 APOSTILA.md reconstructed across 9 pedagogical units
  - 30 original A-E practice questions added with commented answer key
  - Portuguese QA-1 through QA-9 passed, including live NotebookLM and final PDF publication
  - Portuguese 2.0.0 release merged to main at e6ce9d2571e9c68a8947701c08187c07e986d567
  - B2 Gate 1 closed under DEC-0019
  - B2 editorial boundary defined as six SubjectPacks: direito-penal, direito-processual-penal, direito-processual-civil, direito-constitucional, direito-administrativo and legislacao-interna
  - exact Normas da Corregedoria recuts from the edital recorded in SYLLABUS.md
  - duplicate Capitulo XI reference in the edital preserved as an official-source anomaly instead of being silently corrected
  - DIREITO_B2_AUTHORING_PLAN.md created with gate order and production boundary
  - PR 13 B2 Gate 1 preparation merged to main at 540765b17e224a319b90a4e9da5272dd4db0684e
  - B2 Gate 2 federal source audit closed and merged through PR 14 at 228f2225c3b7655d8fd47c325f7c5a2db40bf0a0
  - Codigo Penal closed with no post-cutoff textual drift inside the syllabus recut
  - CPP post-cutoff drift mapped at art. 584 paragraph 4 by Lei 15.358/2026
  - Lei 9.099/1995 closed with no direct post-cutoff textual drift identified in the scoped recuts
  - CPC post-cutoff drift mapped at arts. 196, 529-A and 998 with vigency controlled
  - Lei 12.153/2009 closed with no direct post-cutoff textual drift identified
  - Constituicao post-cutoff drift mapped at art. 37 XVI b by EC 138/2025
  - Lei 8.429/1992 closed with no effective post-cutoff textual drift from Lei 15.269/2025 because the proposed provision was vetoed
  - Lei Estadual 10.261/1968 cutoff reconstructed; scoped post-cutoff drift mapped at art. 78 by Lei 18.473/2026; LC 1.437/2025 affects arts. 176-179 outside the syllabus recut
  - LC Estadual 1.111/2010 cutoff reconstructed with 16/07/2025 staffing acts included; post-cutoff Lei 18.373/2025 and LC 1.441/2026 mapped
  - Resolucao TJSP 850/2021 baseline closed using official compilation through Resolucao 864/2022; no later direct textual amendment located
  - Resolucao TJSP 963/2025 baseline closed at DJE 29/05/2025; no direct textual amendment located; later eproc complements tracked separately
  - Regimento Interno TJSP cutoff reconstructed from official annotated consolidation: Assento 591/2025 included and Assentos 592-596 excluded
  - NSCGJ Tomo I cutoff reconstructed from official historical-text PDF; post-cutoff drift mapped in literal Capitulo XI by Provimentos CG 30/2025 and 04/2026
  - duplicate Capitulo XI remains documented as unresolved official ambiguity; second literal recut subsumes the first without correcting the edital
  - DIREITO_SOURCES.md promoted to status closed
  - DIREITO_B2_AUTHORING_PLAN.md Gate 2 promoted to closed
  - PR 15 reviewed and merged under DEC-0009
  - B2 Gate 2 state and TJSP source audit merged to main at fa0fb7c66f6db2d83df98bedf75b2708f51baad3
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
next_gate:
  id: DIREITO-003
  name: historical_banca_analysis
  sources:
    - SRC-TJSP-PROVA-2021
    - SRC-TJSP-PROVA-2023
    - SRC-TJSP-PROVA-2024
    - SRC-TJSP-PROVA-2025
  required_fields_per_question:
    - domain
    - source_or_institute
    - cognitive_operation
    - literalness_vs_application
    - distractor_pattern
    - relevant_legal_contrast
not_started:
  - complete Gate 3 reproducible classification of Direito questions from 2021/2023/2024/2025
  - create Gate 4 coverage/authoring matrices for the six B2 SubjectPacks
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
    attempted_at: 2026-09-11
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    error: Could not resolve host github.com
    policy: impossibility documented under DEC-0009; not treated as pass
ci: disabled
last_subject_pack_pull_request: 12
last_b2_preparation_pull_request: 13
last_b2_source_pull_request: 15
merge_status: b2_gate2_closed_gate3_pending
last_b2_source_merge_commit: fa0fb7c66f6db2d83df98bedf75b2708f51baad3
last_b2_preparation_merge_commit: 540765b17e224a319b90a4e9da5272dd4db0684e
last_release_merge_commit: e6ce9d2571e9c68a8947701c08187c07e986d567
```
