# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: qa/direito-processual-penal-v0.1
base_branch: main
base_main_sha: fedd24f8607b6d2b68d4aa9352ff949529680f1e
current_task: review and merge DIREITO-009, then prepare DIREITO-010 release candidate work
current_pack: direito-processual-penal_0.1.0-draft.2_semantic_qa_passed
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_state_before_direito_009:
  main_head: fedd24f8607b6d2b68d4aa9352ff949529680f1e
  source: GitHub branch main
  open_pull_requests: 0
  direito_008_pr: 27
  direito_008_state: merged

completed:
  - repository foundation and chat-independent continuity active
  - autonomous merge policy active under DEC-0009
  - GitHub + ChatGPT + NotebookLM stack established
  - APOSTILA_AUTHORING_PROTOCOL mandatory under DEC-0018
  - Portuguese 2.0.0 released
  - B2 Gate 1 boundary closed with six SubjectPacks
  - B2 Gate 2 source/version inventory closed at cutoff 2025-07-29
  - B2 Gate 3 banca analysis closed with 150 classified legal questions
  - B2 Gate 4 coverage matrix closed
  - Direito Penal draft, QA, canonical PDF and NotebookLM smoke completed through DIREITO-007
  - DIREITO-008 first Direito Processual Penal draft merged through PR 27
  - DIREITO-009 semantic and normative QA executed on qa/direito-processual-penal-v0.1

b2_source_gate:
  status: closed
  cutoff: 2025-07-29
  processual_penal:
    cpp_source: SRC-B2-CPP
    l9099_source: SRC-B2-L9099
    cpp_584_paragraph_4_2026: excluded_from_baseline
    l9099_scoped_drift: none_identified_in_gate_2

b2_banca_gate:
  status: closed
  questions_classified: 150
  authority_rule: syllabus_controls_scope_history_is_descriptive_non_predictive

b2_coverage_gate:
  status: closed
  processual_penal_rows: 25
  first_id: DPP-01
  last_id: DPP-25

right_penal_validated_rc:
  version: 0.1.0-rc.1
  status: validated_release_candidate
  semantic_content: pass
  canonical_pdf: pass_canonical_binary_identity
  notebooklm_live_qa: pass_with_observations
  final_promotion: deferred_nonblocking

right_processual_penal:
  version: 0.1.0-draft.2
  status: draft_semantic_qa_passed_ready_for_rc_preparation
  path: materials/tjsp-escrevente-2025/direito-processual-penal
  implementation_branch: qa/direito-processual-penal-v0.1
  units: 25
  coverage: DPP-01_through_DPP-25
  coverage_qa: pass_after_corrections
  normative_qa: pass_after_corrections
  didactic_qa: pass
  practice_questions_original: 52
  practice_questions_added_in_qa: 8
  practice_questions_total: 60
  practice_qa: pass_60_of_60
  practice_requirements: pass_Q_LIT_Q_CMP_Q_CAS_Q_FLX_Q_VER_Q_FULL
  markdown_corpus_qa: pass_for_markdown
  visible_backoffice_ids_in_headings: false
  qa_artifact: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md
  material_corrections:
    - CPP art 262 literal rule added
    - CPP arts 363 to 365 clarified including revoked references
    - CPP art 394-A added
    - CPP art 398 identified revoked
    - CPP art 400-A added
    - CPP art 537 identified revoked and art 538 clarified
    - CPP arts 574 to 603 deepened
    - CPP arts 604 to 620 fully reconciled including art 611 revoked
    - CPP arts 632 to 646 fully reconciled
    - CPP art 647-A and HC flow added
    - Lei 9099 arts 60 to 83 deepened including art 81 paragraph 1-A
  pdf: not_created_by_design
  notebooklm: not_started

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-14
    checkout_attempt: git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_verify
    exit_code: 128
    error: Could not resolve host: github.com
    policy: documented_under_DEC_0009_not_a_pass
  branch_readback:
    apostila_version: 0.1.0-draft.2
    visible_DPP_ids_in_studentcontent: none_found
    final_question_number: 60

next_gate:
  id: DIREITO-010
  name: prepare_release_candidate_direito_processual_penal
  pack: direito-processual-penal
  prerequisite: DIREITO-009 merged
  target_state: release_candidate_prepared_not_final_release
  required_work:
    - create and QA tutor configuration for legal corpus
    - preserve epistemic limit lesson from Direito Penal smoke
    - synchronize APOSTILA, MANIFEST, SOURCES and CHANGELOG identity
    - perform static NotebookLM corpus and tutor QA
    - only then enter PDF candidate generation and PDF QA
    - later run live NotebookLM smoke before final release decision

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
  direito_processual_penal_draft_pr: 27

merge_status: DIREITO_009_ready_for_final_diff_review_and_pr

not_started:
  - DIREITO-010 release candidate preparation for direito-processual-penal
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```
