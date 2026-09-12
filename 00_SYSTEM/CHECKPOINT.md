# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: main
base_branch: main
last_implementation_branch: qa/direito-penal-v0.1
current_task: prepare direito-penal release candidate under DIREITO-007 without promoting pending PDF or NotebookLM gates
current_pack: direito-penal_0.1.0-draft.3_semantic_qa_passed_release_candidate_pending
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
  - exact Normas da Corregedoria recuts preserved, including duplicate Capitulo XI anomaly
  - PR 13 B2 Gate 1 preparation merged at 540765b17e224a319b90a4e9da5272dd4db0684e
  - B2 Gate 2 federal source audit merged through PR 14 at 228f2225c3b7655d8fd47c325f7c5a2db40bf0a0
  - B2 Gate 2 state/TJSP audit merged through PR 15 at fa0fb7c66f6db2d83df98bedf75b2708f51baad3
  - B2 Gate 3 classified 150 legal questions and merged through PR 18 at c3e7e75c65ab612cd05c86cfe9c0bcadb8d66008
  - B2 Gate 4 coverage matrices closed and merged through PR 19 at 5784e8bb9d904c677cb655dfbb069146e688b4e3
  - direito-penal Gate 5 first draft implemented as 0.1.0-draft.1 with DP-01 through DP-10 and 30 original A-E questions
  - direito-penal draft merged through PR 20 at c0208494c1acd343572254d4d8b991d97f6cf8fc
  - DIREITO-006 full normative review against SRC-B2-CP completed
  - direito-penal promoted internally to 0.1.0-draft.2 after normative/didactic corrections
  - interim semantic QA found Q12 review requirement and Q29 ambiguity
  - Q12 reformulated to isolate CP art. 311-A paragraph 2 consequence
  - Q29 reformulated to isolate CP art. 359 using judicially suspended private activity
  - explicit CP art. 324 x art. 359 contrast added without inventing jurisprudential concurrence rule
  - direito-penal promoted to 0.1.0-draft.3
  - 30 of 30 original practice questions passed final semantic review
  - Q-LIT Q-CMP Q-CAS requirements satisfied across DP-01 through DP-10
  - DIREITO-006 semantic QA closed; Markdown authorized for release candidate preparation
  - PR 21 Direito Penal semantic QA reviewed and merged under DEC-0009
  - PR 21 merged to main at d89b7aefd69db3f3fc653807eb98f036755f6f2e

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
      - edital repeats Tomo I Capitulo XI in final two NSCGJ recuts; preserved without inferred correction

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

b2_coverage_gate:
  status: closed
  verified_at: 2026-09-12
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md
  packs: 6
  coverage_result: complete
  authority_rule: syllabus controls scope; matrix rows are authoring and QA contracts, not new syllabus
  first_authorized_pack: direito-penal
  first_pack_contract:
    - DP-01
    - DP-02
    - DP-03
    - DP-04
    - DP-05
    - DP-06
    - DP-07
    - DP-08
    - DP-09
    - DP-10

direito_penal_draft:
  status: semantic_qa_passed_release_candidate_not_created
  version: 0.1.0-draft.3
  path: materials/tjsp-escrevente-2025/direito-penal
  files:
    - APOSTILA.md
    - SOURCES.md
    - MANIFEST.md
    - CHANGELOG.md
    - APOSTILA_QA_0.1.0.md
  coverage_rows: 10
  coverage_status: pass
  normative_qa: pass_after_corrections
  didactic_qa: pass
  practice_questions: 30
  practice_qa: pass_30_of_30
  matrix_practice_contract: pass
  markdown_corpus_qa: pass_for_markdown
  banca_coherence: pass
  pdf_status: not_created
  notebooklm_status: not_tested
  baseline: 2025-07-29
  cp_scoped_drift: none_identified_by_gate2
  release_status: blocked_until_release_candidate_pdf_notebooklm_gates
  qa_pull_request: 21
  qa_merge_commit: d89b7aefd69db3f3fc653807eb98f036755f6f2e

next_gate:
  id: DIREITO-007
  name: prepare_direito_penal_release_candidate
  pack: direito-penal
  target_version: 0.1.0-rc.1
  required:
    - create METODOLOGIA_NOTEBOOKLM.md as conversation configuration, not study source
    - synchronize RC metadata without silently changing approved content
    - generate searchable APOSTILA.pdf from approved Markdown
    - run textual and visual PDF QA
    - run static NotebookLM corpus QA and real smoke when interface access is available
    - keep final release blocked if any applicable gate remains pending

not_started:
  - create direito-penal METODOLOGIA_NOTEBOOKLM.md
  - promote coherent candidate metadata to 0.1.0-rc.1
  - generate and inspect direito-penal APOSTILA.pdf
  - execute NotebookLM smoke or record it as pending when external UI is unavailable
  - release direito-penal
  - continue remaining five B2 SubjectPacks after first legal pipeline is fully validated

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
  direito_penal_semantic_qa:
    result: pass
    material_version: 0.1.0-draft.3
    coverage: pass
    normative: pass_after_corrections
    didactic: pass
    questions: pass_30_of_30
    corpus_markdown: pass_for_markdown
    artifact: materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    reason: local runtime cannot resolve github.com, preventing a valid canonical checkout
    attempted_at: 2026-09-12
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    error: Could not resolve host github.com
    policy: impossibility documented under DEC-0009; not treated as pass

ci: disabled
last_subject_pack_pull_request: 21
last_b2_preparation_pull_request: 13
last_b2_source_pull_request: 15
last_b2_banca_pull_request: 18
last_b2_matrix_pull_request: 19
last_direito_penal_draft_pull_request: 20
last_direito_penal_qa_pull_request: 21
merge_status: direito_penal_semantic_qa_merged_release_candidate_pending
last_direito_penal_qa_merge_commit: d89b7aefd69db3f3fc653807eb98f036755f6f2e
last_direito_penal_draft_merge_commit: c0208494c1acd343572254d4d8b991d97f6cf8fc
last_b2_matrix_merge_commit: 5784e8bb9d904c677cb655dfbb069146e688b4e3
last_b2_banca_merge_commit: c3e7e75c65ab612cd05c86cfe9c0bcadb8d66008
last_b2_source_merge_commit: fa0fb7c66f6db2d83df98bedf75b2708f51baad3
last_b2_preparation_merge_commit: 540765b17e224a319b90a4e9da5272dd4db0684e
last_release_merge_commit: e6ce9d2571e9c68a8947701c08187c07e986d567
```
