# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch_after_status_pr_merge: main
base_branch: main
current_task: resume DIREITO-011 by publishing the exact audited direito-processual-penal rc.1 PDF and proving canonical binary identity
current_pack: direito-processual-penal_0.1.0-rc.1_release_candidate_incomplete_pdf_transport_blocked
last_validated_pack: direito-penal_0.1.0-rc.1_validated_release_candidate
last_released_pack: portugues_2.0.0

canonical_state_at_direito_011_start:
  main_head: 947ea624d7abfa3b1db4481064aa4abf9743be19
  source: GitHub branch main
  open_pull_requests: 0
  direito_010_pr: 29
  direito_010_state: merged

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
  - DIREITO-011 frozen Markdown source identity proven against GitHub
  - DIREITO-011 local searchable PDF candidate generated from frozen rc.1 Markdown
  - DIREITO-011 textual readback passed on exact preferred local candidate
  - DIREITO-011 visual inspection passed on 28 of 28 pages of exact preferred local candidate

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
  status: release_candidate_incomplete_pdf_transport_blocked
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
  notebooklm_live_qa: not_started_blocked_until_canonical_pdf
  qa_artifact: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md
  pdf:
    local_candidate:
      status: pass_local_candidate
      pages: 28
      page_size: A4
      format: PDF_1.4
      bytes: 37894
      sha256: 608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0
      expected_git_blob: 4eabdacec7858120792cf792ca227335e41730b6
      searchable: true
      text_readback: pass
      visual_inspection: pass_28_of_28
      practice_start_page: 17
      answer_key_start_page: 27
    canonical:
      path: materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf
      status: blocked_not_versioned
      remote_git_blob: not_proven
      canonical_binary_identity: not_proven
    prior_rejected_transport_attempt:
      candidate_bytes: 56319
      candidate_sha256: 946bac9ce3206ad97009e0f23c641945a61b345e754c89a1ce342194069d59e8
      expected_git_blob: 97426cc526c542de6f07ed7e07698984a629ceb5
      orphan_remote_blob: dd10a124a6226cf1bd63e7fa5104033c00d52788
      outcome: rejected_mismatch_never_referenced_by_tree_commit_branch_or_pr
  baseline: 2025-07-29
  cpp_584_paragraph_4_post_cutoff: excluded_from_baseline

validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    attempted_at: 2026-09-15
    checkout_attempt: git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d011
    exit_code: 128
    error: Could not resolve host: github.com
    policy: documented_under_DEC_0009_not_a_pass
  pdf_local_qa:
    source_markdown_identity: pass
    text_readback: pass
    visual_inspection: pass_28_of_28
    canonical_binary_identity: not_proven

next_gate:
  id: DIREITO-011
  name: canonical_pdf_direito_processual_penal
  pack: direito-processual-penal
  target_version: 0.1.0-rc.1
  state: open_transport_blocked
  target_state: canonical_pdf_validated_or_block_explicitly_documented
  required_work:
    - transport exact audited candidate bytes to canonical APOSTILA.pdf path using a binary-safe mechanism
    - read remote Git blob after publication
    - require remote Git blob equals 4eabdacec7858120792cf792ca227335e41730b6
    - reject any mismatch and keep gate open
    - only after exact identity update QA manifest changelog and continuity to PASS_CANONICAL_BINARY_IDENTITY
    - only after canonical PDF validation advance to live NotebookLM smoke
    - rerun python tools/verify.py or re-document current impossibility

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

merge_status: DIREITO_011_local_pdf_qa_pass_canonical_transport_blocked

not_started:
  - successful canonical binary publication for direito-processual-penal
  - direito-processual-penal live NotebookLM smoke
  - direito-processual-civil
  - direito-constitucional
  - direito-administrativo
  - legislacao-interna
```