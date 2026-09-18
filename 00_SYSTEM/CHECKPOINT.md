# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch_after_recovery_pr_merge: main
base_branch: main
current_task: execute DIREITO-016 short NotebookLM regression for direito-processual-penal 0.1.0-rc.2 corrected PDF
current_pack: direito-processual-penal_0.1.0-rc.2_pdf_validated_pending_notebooklm_regression
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_state_at_direito_013_start:
  main_head: 8ffa9929903fe2c12f372d4ca876af76a98afadb
  source: GitHub branch main
  open_pull_requests: 0
  prior_notebooklm_status_pr: 32

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
  - DIREITO-011 historical rc1 PDF binary identity completed and merged through PR 31
  - DIREITO-012 real user NotebookLM smoke evidence collected on rc1 with behavioral pass
  - DIREITO-013 semantic defect in CPP art 371 confirmed against official source
  - DIREITO-013 DPP-05 corrected and targeted QA passed in draft.3
  - DIREITO-013 rc1 PDF invalidated for semantic use and removed from canonical path
  - DIREITO-014 corrected rc2 prepared from draft.3 with metadata-only StudentContent promotion
  - DIREITO-015 corrected rc2 PDF generated audited and published with exact remote binary identity

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
  version: 0.1.0-rc.2
  status: corrected_rc_pdf_validated_pending_notebooklm_regression
  content_base: 0.1.0-draft.3
  path: materials/tjsp-escrevente-2025/direito-processual-penal
  units: 25
  coverage: DPP-01_through_DPP-25
  coverage_qa: pass_after_corrections
  dpp_05_qa: pass_after_correction
  normative_qa: targeted_reopen_dpp05_pass_after_correction
  didactic_qa: pass
  practice_questions_total: 60
  practice_qa: pass_60_of_60
  practice_requirements: pass_Q_LIT_Q_CMP_Q_CAS_Q_FLX_Q_VER_Q_FULL
  markdown_corpus_qa: pass_for_markdown_after_targeted_correction
  visible_backoffice_ids_in_headings: false
  frozen_markdown:
    version: 0.1.0-rc.2
    git_blob_github: 8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18
    content_base_blob: 135592d9762b8f639a199ebe795ffcca71e747bd
    semantic_delta_from_draft3: false
    correction: CPP_art_371_and_372
    source_recheck_date: 2026-09-18
  tutor_configuration:
    artifact: materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md
    current_identity: 0.1.0-rc.2
    role: ConversationInstruction
    static_qa: pass_static
    corpus_limit_rule: absence_in_source_is_not_universal_negative
  notebooklm_static_qa: pass_static
  notebooklm_smoke:
    artifact: materials/tjsp-escrevente-2025/direito-processual-penal/NOTEBOOKLM_SMOKE_0.1.0.md
    result_on_rc1: pass_behavioral_on_rc1_corpus_invalidated
    final_regression_required_after_new_pdf: true
  qa_artifact: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md
  current_pdf:
    path: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf
    status: pass_canonical_binary_identity
    pages: 28
    page_size: A4
    format: PDF_1.4
    bytes: 37917
    sha256: aeaa44ac6a275623d79098d0699c18899f83d6ade75be8661f71a3ad9dfc36fe
    git_blob: 6374969ba722451dd6740364e24c41f25e730b54
    searchable: true
    text_readback: pass
    visual_inspection: pass_28_of_28
  historical_pdf_rc1:
    git_blob: 4eabdacec7858120792cf792ca227335e41730b6
    sha256: 608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0
    binary_identity: historical_pass
    text_readback: historical_pass
    visual_inspection: historical_pass_28_of_28
    semantic_eligibility: invalidated
  baseline: 2025-07-29
  cpp_584_paragraph_4_post_cutoff: excluded_from_baseline

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-18
    checkout_attempt: git clone --depth 1 --branch release/direito-processual-penal-0.1.0-rc.2-pdf https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d015
    exit_code: 128
    error: Could not resolve host: github.com
    policy: documented_under_DEC_0009_not_a_pass

next_gate:
  id: DIREITO-016
  name: notebooklm_short_regression_direito_processual_penal
  pack: direito-processual-penal
  target_version: 0.1.0-rc.2
  state: next
  prerequisite: DIREITO-015 corrected PDF with PASS_CANONICAL_BINARY_IDENTITY
  required_work:
    - user loads only corrected canonical APOSTILA.pdf as study source
    - keep METODOLOGIA_NOTEBOOKLM rc2 in native conversation configuration
    - ask a direct question about CPP arts 371 and 372 and confirm corrected behavior
    - run one A-E training question and verify no answer leak before attempt
    - verify no DPP coverage IDs QA gates or backoffice metadata leak
    - record exact observed evidence
    - if regression passes advance to direito-processual-civil

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
  direito_processual_penal_notebooklm_status_pr: 32
  direito_processual_penal_semantic_recovery_pr: 33
  direito_processual_penal_corrected_rc_pr: 34
  direito_processual_penal_corrected_pdf_pr: 35

merge_status: DIREITO_015_corrected_pdf_tracked_in_PR_35

not_started:
  - direito-processual-penal short regression NotebookLM smoke
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```
