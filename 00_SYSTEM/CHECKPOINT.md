# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: main
base_branch: main
current_task: execute DIREITO-011 canonical PDF pipeline for direito-processual-penal rc.1
current_pack: direito-processual-penal_0.1.0-rc.1_release_candidate_incomplete
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_state_before_direito_010:
  main_head: 70a5103d3f8ceb6132908d68963a2a55732665ec
  source: GitHub branch main
  open_pull_requests: 0
  direito_009_pr: 28
  direito_009_state: merged

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
  - Direito Penal draft QA canonical PDF and NotebookLM smoke completed through DIREITO-007
  - DIREITO-008 first Direito Processual Penal draft merged through PR 27
  - DIREITO-009 semantic and normative QA merged through PR 28
  - DIREITO-010 release candidate identity synchronized from approved draft.2
  - DIREITO-010 METODOLOGIA_NOTEBOOKLM.md created as ConversationInstruction
  - DIREITO-010 static NotebookLM corpus and tutor QA passed

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
  status: release_candidate_incomplete
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
  tutor_configuration:
    artifact: materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md
    role: ConversationInstruction
    static_qa: pass_static
    corpus_limit_rule: absence_in_source_is_not_universal_negative
  notebooklm_static_qa: pass_static
  notebooklm_live_qa: not_started
  qa_artifact: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md
  pdf:
    status: not_created
    canonical_qa: not_started
  baseline: 2025-07-29
  cpp_584_paragraph_4_post_cutoff: excluded_from_baseline

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-14
    checkout_attempt: git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d010
    exit_code: 128
    error: Could not resolve host: github.com
    policy: documented_under_DEC_0009_not_a_pass
  rc_identity_review:
    apostila_change_from_draft_2: metadata_only
    semantic_content_frozen: true
    tutor_configuration: pass_static
    notebooklm_static: pass_static

next_gate:
  id: DIREITO-011
  name: canonical_pdf_direito_processual_penal
  pack: direito-processual-penal
  target_version: 0.1.0-rc.1
  prerequisite: DIREITO-010 merged
  target_state: canonical_pdf_validated_or_block_explicitly_documented
  required_work:
    - generate APOSTILA.pdf exclusively from frozen rc.1 APOSTILA.md
    - prove source to PDF identity
    - textual readback of exact candidate
    - render and inspect every page
    - verify titles legal symbols tables questions and answer key separation
    - version exact audited binary in GitHub
    - record pages bytes sha256 and Git blob
    - do not mark canonical PDF pass until repository binary identity is proven
    - only after canonical PDF validation advance to live NotebookLM smoke

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

merge_status: DIREITO_010_release_candidate_prepared_pending_pdf_pipeline

not_started:
  - DIREITO-011 canonical PDF pipeline for direito-processual-penal
  - direito-processual-penal live NotebookLM smoke
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```
