# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_content_rebuild
branch: main
last_implementation_branch: docs/apostila-authoring-protocol
current_task: APOSTILA-002 rebuild Portuguese apostila using canonical authoring protocol
completed:
  - repository foundation merged
  - chat-independent continuity active
  - autonomous merge policy active
  - TJSP 2025 adapter, edital map, blueprint and source registry created
  - historical exams 2021/2023/2024/2025 registered
  - GitHub + ChatGPT + NotebookLM stack established
  - answer-level mastery/scheduler removed from V0.1 critical path
  - Portuguese edital slice mapped across 13 content fronts
  - 88 Portuguese questions from 2021/2023/2024/2025 classified reproducibly
  - Portuguese banca analysis 1.0.0 produced
  - Portuguese apostila/PDF 1.0.0 produced and QA reviewed
  - Portuguese SubjectPack 1.0.0 merged in PR 7
  - Studio-first usability patch 1.0.1 merged in PR 8
  - real NotebookLM smoke test exposed source-role problem
  - native Test with methodology selected generated question about methodology itself
  - native Test without methodology generated quiz directly about apostila content
  - NotebookLM chat followed operational methodology substantially better than native Test
  - DEC-0015 superseded by DEC-0016
  - content-first architecture merged in PR 9
  - NotebookLM custom conversation configuration observed in real UI
  - DEC-0017 adopted and conversation-config architecture merged in PR 10
  - Portuguese MANIFEST/METODOLOGIA advanced to 1.0.3 without changing apostila/PDF bytes
  - DEC-0018 adopted: canonical apostila authoring protocol required for major creation/rebuilds
  - APOSTILA_AUTHORING_PROTOCOL created with coverage matrix, domain profiles, NotebookLM engineering and 10 QA gates
  - AGENTS and START_HERE require/read the authoring protocol for apostila work
  - PROJECT_SPEC and ARCHITECTURE aligned with protocol-driven authoring
  - QA_PROTOCOL extended to require semantic editorial QA in addition to deterministic verify
  - APOSTILA-002 rewritten to apply the protocol explicitly
in_progress:
  - hand off to next chat for Portuguese 2.0.0 reconstruction under APOSTILA_AUTHORING_PROTOCOL
not_started:
  - APOSTILA-002 audit of current Portuguese apostila
  - Portuguese coverage/authoring matrix
  - new pedagogical outline
  - Portuguese 2.0.0 content rewrite
  - semantic QA gates for Portuguese 2.0.0
  - new Portuguese PDF release and PDF QA
  - NotebookLM validation using rebuilt apostila as clean corpus
  - SubjectPacks for remaining subjects
blockers: []
validation:
  command: python tools/verify.py
  result: not_executed_current_environment
  reason: local runtime cannot resolve github.com; clone of docs/apostila-authoring-protocol failed before gate execution
  attempted_at: 2026-09-11
  clone_error: Could not resolve host github.com
  static_diff_review: pending_before_pr
  branch_base: b2bfd8248e744c61e77278e4c975192e86f4429c
  change_scope: documentation_and_authoring_protocol_only
  binary_changes: none
  apostila_md_changed: false
  apostila_pdf_changed: false
ci: disabled
last_adapter_pull_request: 4
last_architecture_pull_request: 6
last_subject_pack_pull_request: 7
last_usability_pull_request: 8
last_content_first_pull_request: 9
last_conversation_config_pull_request: 10
```
