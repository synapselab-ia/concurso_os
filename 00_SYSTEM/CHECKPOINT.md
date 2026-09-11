# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_content_rebuild
branch: main
last_implementation_branch: docs/notebooklm-conversation-config
current_task: APOSTILA-002 rebuild Portuguese apostila for NotebookLM
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
  - DEC-0016 adopted: APOSTILA is student content; analysis/source/manifest/changelog stay backoffice
  - content-first architecture merged in PR 9
  - NotebookLM custom conversation configuration observed in real UI
  - DEC-0017 adopted: tutor instructions belong in native conversation configuration, not notebook sources
  - Portuguese MANIFEST/METODOLOGIA advanced to 1.0.3 without changing apostila/PDF bytes
  - METODOLOGIA_NOTEBOOKLM now contains a pasteable canonical configuration block
  - project spec, architecture, data model and stack aligned with source-vs-conversation-config separation
in_progress:
  - hand off to next chat for Portuguese apostila rebuild as primary NotebookLM study source
not_started:
  - APOSTILA-002 content audit and rewrite
  - new Portuguese PDF release after rewrite
  - NotebookLM validation using rebuilt apostila as clean corpus
  - SubjectPacks for remaining subjects
blockers: []
validation:
  command: python tools/verify.py
  result: not_executed_current_environment
  reason: local runtime cannot resolve github.com; clone of docs/notebooklm-conversation-config failed before gate execution
  attempted_at: 2026-09-11
  clone_error: Could not resolve host github.com
  static_diff_review: pass
  branch_base: 0099aea4309e99143c587052838f7bd6fd2695cf
  change_scope: documentation_and_notebooklm_configuration_only
  changed_files_reviewed_before_checkpoint: 10
  binary_changes: none
  apostila_md_changed: false
  apostila_pdf_changed: false
  critical_readback: pass
ci: disabled
last_adapter_pull_request: 4
last_architecture_pull_request: 6
last_subject_pack_pull_request: 7
last_usability_pull_request: 8
last_content_first_pull_request: 9
```
