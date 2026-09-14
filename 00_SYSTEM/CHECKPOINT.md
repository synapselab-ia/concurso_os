# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: content/direito-processual-penal-v0.1-draft
base_branch: main
last_implementation_branch: docs/direito-penal-notebooklm-smoke
current_task: review and merge DIREITO-008 first draft, then execute DIREITO-009 semantic and normative QA
current_pack: direito-processual-penal_0.1.0-draft.1
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_state_observed_before_direito_008:
  main_head: 0249631f512fe76d6f34b7759532daf097e38a8e
  observed_at: 2026-09-14
  open_pull_requests: 0
  note: this head is newer than the stale head_after_pr26 value previously recorded in this checkpoint; repository state was checked directly before starting the gate

completed:
  - repository foundation and chat-independent continuity active
  - autonomous merge policy active under DEC-0009
  - GitHub + ChatGPT + NotebookLM stack established
  - DEC-0016 and DEC-0017 clean-corpus plus native conversation configuration architecture established
  - DEC-0018 APOSTILA_AUTHORING_PROTOCOL adopted as mandatory
  - Portuguese 2.0.0 fully released with editorial, PDF and NotebookLM QA passed
  - B2 Gate 1 closed under DEC-0019 with six SubjectPacks
  - B2 Gate 2 source and version audit closed at cutoff 2025-07-29
  - B2 Gate 3 banca analysis closed with 150 legal questions classified
  - B2 Gate 4 coverage matrix closed with six pack matrices
  - direito-penal first draft, semantic QA and rc.1 pipeline completed
  - direito-penal canonical PDF QA-9 closed as PASS_CANONICAL_BINARY_IDENTITY
  - direito-penal NotebookLM live smoke accepted as PASS_WITH_OBSERVATIONS
  - DIREITO-007 closed_with_observations
  - DIREITO-008 first draft of direito-processual-penal implemented on content/direito-processual-penal-v0.1-draft

b2_source_gate:
  status: closed
  edital_cutoff: 2025-07-29
  inventory: competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md
  relevant_processual_penal_points:
    - SRC-B2-CPP is the primary CPP source
    - SRC-B2-L9099 is the primary Lei 9.099/1995 source
    - CPP art. 584 paragraph 4 was added after cutoff by Lei 15.358/2026 and must not contaminate the study baseline
    - Lei 9.099/1995 remained cutoff_closed_no_scoped_drift in the Gate 2 audit

b2_banca_gate:
  status: closed
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md
  questions_classified: 150
  authority_rule: syllabus controls scope; historical distribution is descriptive and non-predictive

b2_coverage_gate:
  status: closed
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md
  next_pack_contract:
    pack: direito-processual-penal
    coverage_rows: 25
    first_id: DPP-01
    last_id: DPP-25

right_penal_validated_rc:
  status: validated_release_candidate
  version: 0.1.0-rc.1
  path: materials/tjsp-escrevente-2025/direito-penal
  semantic_content: pass
  practice_questions: 30
  canonical_pdf: pass_canonical_binary_identity
  notebooklm_static_qa: pass_static
  notebooklm_live_qa: pass_with_observations
  formal_final_promotion: deferred_separate_from_b2_continuation

right_processual_penal_draft:
  status: draft_pending_semantic_normative_qa
  version: 0.1.0-draft.1
  path: materials/tjsp-escrevente-2025/direito-processual-penal
  branch: content/direito-processual-penal-v0.1-draft
  workspace_files:
    - MANIFEST.md
    - SOURCES.md
    - APOSTILA.md
    - CHANGELOG.md
  student_units: 25
  coverage_rows: DPP-01_through_DPP-25
  practice_questions: 52
  practice_format: five_options_A_to_E_with_separate_commented_answer_key
  visible_coverage_ids_in_student_headings: false_by_authoring_selfcheck
  main_content_engineering:
    - procedural flows
    - rule_exception and contrast tables where useful
    - deadlines subjects legitimacy competence admissibility and effects
    - jury flow from first phase through plenary and sentence
    - appeal and autonomous challenge contrasts
    - JECrim flow from preliminary phase through appeals and conditional suspension
  version_control:
    baseline: 2025-07-29
    cpp_584_paragraph_4_post_cutoff: excluded_from_baseline
  pdf: not_created_by_design
  notebooklm: not_started
  semantic_normative_qa: not_started

notebooklm_process_lessons_applied_to_draft:
  - coverage IDs, matrix IDs and gate labels kept out of visible StudentContent headings
  - traceability kept in manifest, matrix and future QA
  - corpus limitation principle preserved for future tutor configuration

next_gate:
  id: DIREITO-009
  name: semantic_normative_qa_direito_processual_penal
  pack: direito-processual-penal
  target_state: qa_closed_or_draft_corrected
  required_primary_sources:
    - SRC-B2-CPP
    - SRC-B2-L9099
  required_qa_artifact: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md
  mandatory_checks:
    - full DPP-01 through DPP-25 traceability
    - full article by article normative review
    - explicit treatment of revoked CPP provisions inside the scoped intervals
    - preserve cutoff and exclude 2026 CPP art. 584 paragraph 4
    - individual semantic review of all 52 questions
    - no PDF or release candidate before QA decision

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-14
    reason: no canonical local checkout can be obtained because the runtime cannot resolve github.com
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    exit_code: 128
    error: Could not resolve host: github.com
    policy: impossibility re-evaluated under DEC-0009 and not treated as pass
  structural_review:
    compare_base: main@0249631f512fe76d6f34b7759532daf097e38a8e
    content_branch: content/direito-processual-penal-v0.1-draft
    initial_content_diff_before_continuity_updates: 4 added files, 1963 added lines, 0 deletions
    note: final diff must be re-read after continuity updates and before merge

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

merge_status: DIREITO_008_ready_for_final_diff_review_then_pr

not_started:
  - DIREITO-009 semantic and normative QA of direito-processual-penal
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```
