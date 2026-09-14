# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: main
base_branch: main
last_implementation_branch: docs/direito-penal-notebooklm-smoke
current_task: start DIREITO-008 first draft of direito-processual-penal
current_pack: direito-processual-penal_not_started
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_main:
  head_after_pr26: dcc279a4e25d393036929fc7d640f544003ec436
  open_pull_requests_expected: 0

completed:
  - repository foundation and chat-independent continuity active
  - autonomous merge policy active under DEC-0009
  - GitHub + ChatGPT + NotebookLM stack established
  - DEC-0016 and DEC-0017 clean-corpus plus native conversation configuration architecture established
  - DEC-0018 APOSTILA_AUTHORING_PROTOCOL adopted as mandatory
  - Portuguese 2.0.0 fully released with editorial, PDF and NotebookLM QA passed
  - B2 Gate 1 closed under DEC-0019 with six SubjectPacks
  - B2 Gate 2 source and version audit closed
  - B2 Gate 3 banca analysis closed with 150 legal questions classified
  - B2 Gate 4 coverage matrix closed with six pack matrices
  - direito-penal Gate 5 first draft completed and merged through PR 20
  - direito-penal Gate 6 semantic and normative QA completed and merged through PR 21
  - direito-penal rc.1 tutor configuration and static NotebookLM QA prepared through PR 22
  - direito-penal canonical PDF publication blocker documented through PRs 23 and 24
  - exact audited APOSTILA.pdf manually uploaded and published through PR 25
  - direito-penal QA-9 closed as PASS_CANONICAL_BINARY_IDENTITY
  - direito-penal live NotebookLM smoke executed by user on 2026-09-14
  - direito-penal live NotebookLM smoke accepted as PASS_WITH_OBSERVATIONS
  - DIREITO-007 closed_with_observations
  - PR 26 recorded smoke evidence, process lessons and advancement to direito-processual-penal

b2_source_gate:
  status: closed
  edital_cutoff: 2025-07-29
  verified_at: 2026-09-11
  inventory: competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md
  federal_points:
    - CPP art. 584 paragraph 4 changed after cutoff by Lei 15.358/2026
    - CPC art. 998 changed after cutoff by Lei 15.484/2026
    - CPC arts. 196 and 529-A changed after cutoff by Lei 15.479/2026 with one-year vacatio
    - CF art. 37 XVI b changed after cutoff by EC 138/2025
    - Codigo Penal scoped text had no identified direct drift for direito-penal
    - Lei 9.099/1995 baseline stable for the scoped B2 audit
  state_tjsp_points:
    - Lei Estadual 10.261/1968 art. 78 changed after cutoff by Lei 18.473/2026
    - LC Estadual 1.111/2010 changed after cutoff by Lei 18.373/2025 and LC 1.441/2026
    - Regimento Interno baseline excludes Assentos 592-596
    - NSCGJ literal Capitulo XI recuts preserve the duplicated edital reference without inferred correction

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
  authority_rule: syllabus controls scope; historical distribution is descriptive and non-predictive

b2_coverage_gate:
  status: closed
  verified_at: 2026-09-12
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md
  packs: 6
  coverage_result: complete
  next_pack_contract:
    pack: direito-processual-penal
    coverage_rows: 25
    first_id: DPP-01
    last_id: DPP-25

right_penal_validated_rc:
  status: validated_release_candidate
  version: 0.1.0-rc.1
  path: materials/tjsp-escrevente-2025/direito-penal
  content_base: 0.1.0-draft.3
  semantic_content_frozen: true
  canonical_markdown_blob: 008c3ac439d8b7d4038fd0114e486c1daaf755b1
  coverage_status: pass
  normative_qa: pass_after_corrections
  didactic_qa: pass
  practice_questions: 30
  practice_qa: pass_30_of_30
  markdown_corpus_qa: pass_for_markdown
  banca_coherence: pass
  tutor_configuration: pass_static
  notebooklm_static_qa: pass_static
  notebooklm_live_qa: pass_with_observations
  notebooklm_smoke_artifact: materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md
  canonical_pdf:
    result: pass_canonical_binary_identity
    pages: 17
    page_size: A4
    bytes: 30167
    pdf_version: 1.4
    sha256: 42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394
    git_blob: 5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e
    source_git_blob: 008c3ac439d8b7d4038fd0114e486c1daaf755b1
    textual_readback: pass
    visual_pages_inspected: 17
    visual_result: pass
    publication_method: manual_github_upload
    upload_rename_commit: fd7f0f78b16f85d06979ab1e6cc86762c1bd1d00
    publication_pull_request: 25
    publication_merge_commit: eaaad8982691b961cfd9a44a2b04326dba77c5e3
  smoke_observations:
    - map rendered DP coverage IDs because they were present in visible StudentContent headings
    - jurisprudence limit response did not invent precedents but opened with a categorical negative before stating the corpus limit
  smoke_acceptance:
    result: pass_with_observations
    blocking: false
    rc2_required: false
    decision: carry improvements into subsequent SubjectPacks instead of regenerating direito-penal solely for these observations
  formal_final_promotion:
    status: deferred_separate_from_b2_continuation
    blocks_next_pack: false

notebooklm_process_lessons:
  - do not expose coverage IDs, matrix IDs, gate labels or backoffice identifiers in visible StudentContent headings
  - keep traceability in matrix, manifest and QA rather than study corpus headings
  - when a source does not support an external-world claim, state the corpus limitation instead of asserting universal nonexistence
  - future smoke must explicitly inspect Teste, Cartoes and Mapa mental for backoffice leakage
  - future smoke must include at least one question whose answer is absent from the corpus to test epistemic discipline

next_gate:
  id: DIREITO-008
  name: first_draft_direito_processual_penal
  pack: direito-processual-penal
  target_state: draft
  coverage_ids: DPP-01_through_DPP-25
  official_scope:
    cpp: arts_251_258_261_267_274_351_372_394_497_531_538_541_548_574_667
    lei_9099_1995: arts_60_83_88_89
  primary_sources:
    - SRC-B2-CPP
    - SRC-B2-L9099
  critical_version_note:
    - CPP art. 584 paragraph 4 must use cutoff 2025-07-29 text; Lei 15.358/2026 drift stays separate
  required_first_artifacts:
    - materials/tjsp-escrevente-2025/direito-processual-penal/MANIFEST.md
    - materials/tjsp-escrevente-2025/direito-processual-penal/SOURCES.md
    - materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.md
    - materials/tjsp-escrevente-2025/direito-processual-penal/CHANGELOG.md
  gate_rule:
    - cover all DPP-01 through DPP-25
    - do not expose DPP IDs in StudentContent headings
    - do not generate PDF or release candidate before semantic and normative QA of the draft

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-14
    reason: local runtime cannot resolve github.com for a valid canonical checkout
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    error: Could not resolve host github.com
    policy: impossibility re-evaluated under DEC-0009 and not treated as pass

pull_request_lineage:
  b2_preparation_pr: 13
  b2_source_prs: [14, 15]
  b2_banca_pr: 18
  b2_matrix_pr: 19
  direito_penal_draft_pr: 20
  direito_penal_qa_pr: 21
  direito_penal_rc_pr: 22
  direito_penal_pdf_continuity_pr: 23
  direito_penal_pdf_transport_pr: 24
  direito_penal_pdf_publication_pr: 25
  direito_penal_notebooklm_smoke_pr: 26
  last_subject_pack_pull_request: 26

merge_status: direito_penal_rc1_validated_with_observations_next_direito_processual_penal

not_started:
  - direito-processual-penal first draft
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```
