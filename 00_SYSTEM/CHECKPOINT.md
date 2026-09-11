# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_release_validation
branch: content/apostila-portugues-2.0.0
base_branch: main
base_sha: 29f92f11d822b426d6af239afa31a09829881844
last_implementation_branch: docs/apostila-authoring-protocol
current_task: APOSTILA-002 validate NotebookLM Mapa mental, then finalize Portuguese 2.0.0 release
current_pack: portugues 2.0.0 release-candidate
completed:
  - repository foundation merged
  - chat-independent continuity active
  - autonomous merge policy active
  - TJSP 2025 adapter, edital map, blueprint and source registry created
  - historical exams 2021/2023/2024/2025 registered
  - GitHub + ChatGPT + NotebookLM stack established
  - Portuguese edital slice mapped across 13 content fronts
  - 88 Portuguese questions from 2021/2023/2024/2025 classified reproducibly
  - Portuguese banca analysis 1.0.0 produced
  - Portuguese SubjectPack 1.0.0 merged in PR 7
  - NotebookLM source-role smoke tests completed for 1.x architecture
  - DEC-0016 and DEC-0017 established clean-corpus + native conversation configuration architecture
  - DEC-0018 adopted and APOSTILA_AUTHORING_PROTOCOL made mandatory
  - APOSTILA-002 audit of Portuguese 1.0.0 completed
  - Portuguese 2.0.0 coverage/authoring matrix closed with B1.1-B1.13 covered
  - new pedagogical outline implemented across 9 units
  - Portuguese APOSTILA.md reconstructed for learning, review and NotebookLM recovery
  - 30 original A-E practice questions added with separate commented answer key
  - semantic QA-1 through QA-6 passed
  - QA-7 static NotebookLM corpus review passed
  - QA-8 redundancy/coherence passed
  - initial truncated GitHub PDF upload detected by readback and rejected
  - fallback 1.0.0 PDF used temporarily to remove corruption
  - compact Portuguese 2.0.0 PDF distribution generated for connector-safe transport
  - compact PDF textual QA passed
  - compact PDF visual QA passed after rendering and inspecting 16 pages
  - exact 2.0.0 PDF blob published on implementation branch
  - GitHub readback confirmed PDF size and blob SHA byte-identical to local artifact
  - QA-9 PDF publication gate passed
  - first live NotebookLM chat smoke attempt executed by user
  - live smoke findings recorded: minor overstatement in inference explanation, incorrect label on valid no-crase example, under-specific concordance correction, UI suggestion leaking answer
  - METODOLOGIA_NOTEBOOKLM hardened to 2.0.0-rc2 based only on observed failures
  - configured-chat rc2 retest executed by user and passed controlled tutor behavior
  - rc2 concordance correction explained each relevant construction specifically, including fazer temporal, menos invariável, anexo agreement and dever + existir
  - tutor-generated answer leak was not observed in rc2 retest; interface suggestion chips remain an external UI risk
  - NotebookLM native Teste smoke passed on concordância, sentido figurado and relações lógico-semânticas samples
  - NotebookLM Cartões smoke passed on enunciador, inferência, extrapolação and pronome relativo cujo samples
  - PR 12 remains open in draft from content/apostila-portugues-2.0.0 to main
in_progress:
  - validate native NotebookLM Mapa mental over published APOSTILA.pdf 2.0.0
not_started:
  - promote Portuguese 2.0.0 release-candidate to final release
  - merge PR 12
  - SubjectPacks for remaining subjects
blockers:
  - remaining NotebookLM Mapa mental smoke requires authenticated interaction with the user's NotebookLM; no NotebookLM connector/browser session is available in this execution environment
validation:
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    reason: local runtime cannot resolve github.com, so a canonical checkout cannot be obtained for a valid repository-wide gate
    attempted_at: 2026-09-11
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    error: Could not resolve host github.com
  github_state_review:
    result: pass
    branch: content/apostila-portugues-2.0.0
    pull_request: 12
    pull_request_state: open_draft
    branch_behind_main: 0
    diff_readback: pass
  editorial_qa:
    qa_1_coverage: pass
    qa_2_accuracy_source: pass
    qa_3_didactics: pass
    qa_4_distinctions: pass
    qa_5_practice: pass
    qa_6_banca_without_overfit: pass
    qa_7_notebooklm_static: pass
    qa_7_notebooklm_live: partial_chat_test_cards_pass_map_pending
    qa_7_first_live_attempt: findings_recorded_not_passed
    qa_7_chat_rc2_retest: pass
    qa_7_native_test: pass
    qa_7_cards: pass
    qa_7_mind_map: pending
    qa_8_redundancy_coherence: pass
  notebooklm_live_findings:
    first_attempt:
      inference_wording: minor_overstatement
      crase_pair_label: inconsistent
      concordance_correction_specificity: insufficient
      answer_leak_suggestion: observed_in_ui_component_control_uncertain
    remediation: METODOLOGIA_NOTEBOOKLM_2.0.0-rc2
    rc2_retest:
      controlled_tutor_answer_leak: not_observed
      concordance_question_quality: pass
      concordance_correction_specificity: pass
      corrected_forms_explicit: pass
      followup_retest_quality: pass
      external_ui_suggestion_chips: still_possible_product_layer_risk
    native_test:
      concordancia_partitive_sample: pass
      figurative_semantics_sample: pass
      adversative_connective_sample: pass
      optional_hint_ui: observed_user_enabled_not_blocking
    cards:
      enunciador_sample: pass
      inferencia_sample: pass
      extrapolacao_sample: pass
      cujo_agreement_sample: pass
  pdf_qa:
    repository_distribution:
      result: pass
      material_version: 2.0.0
      pages: 16
      page_size: A4
      bytes: 20824
      sha256: b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931
      expected_git_blob: 640efaed13dd43cc83f6904c62fdb86131b9124a
      published_git_blob: 640efaed13dd43cc83f6904c62fdb86131b9124a
      searchable_text: pass
      extracted_text_chars_approx: 54500
      key_text_readback: pass
      rendered_pages_inspected: 16
      clipping_overlap: none_observed
    rejected_uploads:
      - git_blob: 5bea23e3bd98b307496a086e98effc51853a0cd7
        bytes: 7500
        result: invalid_truncated
      - git_blob: 82046b5da25a7565fd84763763be33ebac2556fc
        result: orphan_intermediate_not_promoted
ci: disabled
current_pull_request: 12
merge_status: withheld_until_notebooklm_mind_map_pass
last_adapter_pull_request: 4
last_architecture_pull_request: 6
last_subject_pack_pull_request: 7
last_usability_pull_request: 8
last_content_first_pull_request: 9
last_conversation_config_pull_request: 10
```
