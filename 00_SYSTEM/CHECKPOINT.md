# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch_after_release_pr_merge: main
base_branch: main
current_task: execute DIREITO-012 live NotebookLM smoke for direito-processual-penal 0.1.0-rc.1
current_pack: direito-processual-penal_0.1.0-rc.1_pdf_validated_pending_notebooklm_smoke
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_state_at_direito_011_resume:
  main_head: 89f0c44056c798a13addd44ad41d14a41bd16f8f
  source: GitHub branch main
  open_pull_requests_before_release_pr: 0
  direito_011_status_pr: 30
  direito_011_status_pr_state: merged
  release_branch: release/direito-processual-penal-0.1.0-rc.1-pdf
  release_pr: 31

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
  - Direito Penal pipeline validated through canonical PDF and NotebookLM smoke
  - DIREITO-008 first Direito Processual Penal draft merged through PR 27
  - DIREITO-009 semantic and normative QA merged through PR 28
  - DIREITO-010 release candidate identity tutor configuration and static corpus QA merged through PR 29
  - DIREITO-011 source Markdown identity proven
  - DIREITO-011 searchable PDF candidate generated from frozen rc.1 Markdown
  - DIREITO-011 textual readback passed
  - DIREITO-011 visual inspection passed on 28 of 28 pages
  - DIREITO-011 exact binary versioned at canonical APOSTILA.pdf path
  - DIREITO-011 remote Git blob matched expected Git blob exactly
  - DIREITO-011 PASS_CANONICAL_BINARY_IDENTITY

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
  version: 0.1.0-rc.1
  status: pdf_validated_pending_notebooklm_smoke
  content_base: 0.1.0-draft.2
  semantic_content_changed_in_rc: false
  path: materials/tjsp-escrevente-2025/direito-processual-penal
  units: 25
  coverage: DPP-01_through_DPP-25
  coverage_qa: pass_after_corrections
  normative_qa: pass_after_corrections
  didactic_qa: pass
  practice_questions_total: 60
  practice_qa: pass_60_of_60
  practice_requirements: pass_Q_LIT_Q_CMP_Q_CAS_Q_FLX_Q_VER_Q_FULL
  markdown_corpus_qa: pass_for_markdown
  visible_backoffice_ids_in_headings: false
  frozen_markdown:
    version: 0.1.0-rc.1
    git_blob_github: 11a41d18ff3a8b03150923ec68d44087bded7267
    git_blob_local: 11a41d18ff3a8b03150923ec68d44087bded7267
    sha256_local: da3f1b0c75e4300d22584d2393cab3a3ee4d88f0bd5199ec5a0761a2d2f62fa1
    bytes_local: 69109
    identity: pass_source_markdown_identity
  tutor_configuration:
    artifact: materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md
    role: ConversationInstruction
    static_qa: pass_static
    corpus_limit_rule: absence_in_source_is_not_universal_negative
  notebooklm_static_qa: pass_static
  notebooklm_live_qa: not_started
  qa_artifact: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md
  pdf:
    path: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf
    status: pass_canonical_binary_identity
    pages: 28
    page_size: A4
    format: PDF_1.4
    bytes: 37894
    sha256: 608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0
    local_expected_git_blob: 4eabdacec7858120792cf792ca227335e41730b6
    remote_git_blob: 4eabdacec7858120792cf792ca227335e41730b6
    source_markdown_identity: pass
    searchable: true
    text_readback: pass
    visual_inspection: pass_28_of_28
    canonical_binary_identity: pass
    practice_start_page: 17
    answer_key_start_page: 27
  baseline: 2025-07-29
  cpp_584_paragraph_4_post_cutoff: excluded_from_baseline

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-15
    checkout_attempt: git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d011_cont
    exit_code: 128
    error: Could not resolve host: github.com
    policy: documented_under_DEC_0009_not_a_pass
  pdf_qa:
    source_markdown_identity: pass
    text_readback: pass
    visual_inspection: pass_28_of_28
    canonical_binary_identity: pass

next_gate:
  id: DIREITO-012
  name: notebooklm_live_smoke_direito_processual_penal
  pack: direito-processual-penal
  target_version: 0.1.0-rc.1
  state: not_started
  prerequisite: DIREITO-011 merged with PASS_CANONICAL_BINARY_IDENTITY
  required_work:
    - load only canonical APOSTILA.pdf as NotebookLM source
    - place METODOLOGIA_NOTEBOOKLM operational block in native conversation configuration
    - test explanatory chat and one-question-at-a-time A-E training
    - test correction behavior without answer leakage before attempt
    - test Teste Cartoes and Mapa mental for useful corpus-grounded output
    - verify no DPP coverage IDs or backoffice metadata leak into study artifacts
    - ask at least one out-of-corpus question and require corpus-limit language rather than universal negative
    - record exact observations without presuming external interactions not performed
    - update QA manifest changelog checkpoint and next action
    - rerun python tools/verify.py or document current impossibility

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
  direito_processual_penal_qa_pr: 28
  direito_processual_penal_rc_pr: 29
  direito_processual_penal_pdf_status_pr: 30
  direito_processual_penal_pdf_publication_pr: 31

merge_status: DIREITO_011_merged_next_DIREITO_012

not_started:
  - direito-processual-penal live NotebookLM smoke
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```