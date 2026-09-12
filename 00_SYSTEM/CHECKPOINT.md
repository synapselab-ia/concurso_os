# CHECKPOINT

```yaml
project_state: active
phase: subject_pack_authoring_prep
branch: content/direito-penal-v0.1-draft
base_branch: main
last_implementation_branch: content/direito-b2-gate4-matrices
current_task: review and merge the first Direito Penal draft, then run pack-specific editorial and normative QA under DIREITO-006
current_pack: direito-penal_0.1.0-draft.1
last_released_pack: portugues 2.0.0
completed:
  - repository foundation and chat-independent continuity active
  - autonomous merge policy active under DEC-0009
  - TJSP 2025 adapter, edital map, blueprint and source registry created
  - historical exams 2021/2023/2024/2025 registered
  - GitHub + ChatGPT + NotebookLM stack established
  - DEC-0016 and DEC-0017 clean-corpus + native conversation configuration architecture established
  - DEC-0018 APOSTILA_AUTHORING_PROTOCOL adopted as mandatory
  - Portuguese 2.0.0 fully released with editorial, PDF and NotebookLM QA passed
  - Portuguese 2.0.0 release merged to main at e6ce9d2571e9c68a8947701c08187c07e986d567
  - B2 Gate 1 closed under DEC-0019 with six SubjectPacks
  - exact Normas da Corregedoria recuts from the edital recorded in SYLLABUS.md
  - duplicate Capitulo XI reference preserved as an official-source anomaly
  - PR 13 B2 Gate 1 preparation merged to main at 540765b17e224a319b90a4e9da5272dd4db0684e
  - B2 Gate 2 federal source audit closed and merged through PR 14 at 228f2225c3b7655d8fd47c325f7c5a2db40bf0a0
  - B2 Gate 2 state and TJSP audit closed and merged through PR 15 at fa0fb7c66f6db2d83df98bedf75b2708f51baad3
  - DIREITO_SOURCES.md promoted to closed with cutoff 2025-07-29 and post-cutoff drift separated
  - B2 Gate 3 source binaries reverified locally against SOURCES.json hashes and sizes
  - B2 Gate 3 classified 150 legal questions from 2021, 2023, 2024 and 2025
  - DIREITO_B2_BANCA_ANALYSIS.md created with reproducible taxonomy, per-question classification, domain synthesis and editorial signals
  - Gate 3 preserves historical frequencies as descriptive evidence only and does not override current syllabus
  - BANCA_PROFILE.md updated to reference reproducible Direito evidence
  - PR 18 B2 Gate 3 analysis merged to main at c3e7e75c65ab612cd05c86cfe9c0bcadb8d66008
  - DIREITO_B2_COVERAGE_MATRIX.md created with six independent pack matrices
  - all B2 syllabus recuts mapped to stable coverage_id entries without orphaned ranges or diplomas
  - all Gate 2 source_ids associated to coverage units and normative drift attached to affected rows
  - Gate 3 empirical signals converted into pedagogical forms, contrasts and practice/QA requirements without predictive weighting
  - duplicate NSCGJ Capitulo XI reference preserved in the coverage matrix without inferred correction
  - B2 Gate 4 closed and Gate 5 authorized for direito-penal
  - PR 19 B2 Gate 4 coverage matrices reviewed and merged under DEC-0009
  - B2 Gate 4 coverage matrices merged to main at 5784e8bb9d904c677cb655dfbb069146e688b4e3
  - direito-penal workspace created at materials/tjsp-escrevente-2025/direito-penal
  - direito-penal MANIFEST.md, SOURCES.md and CHANGELOG.md created for 0.1.0-draft.1
  - direito-penal APOSTILA.md first pass drafted for DP-01 through DP-10
  - 30 original A-E Direito Penal practice questions added with separated commented answer key
  - preliminary source spot-check performed against official Planalto text for key scoped provisions; full normative QA remains pending
b2_source_gate:
  status: closed
  edital_cutoff: 2025-07-29
  verified_at: 2026-09-11
  inventory: competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md
  federal_subgate:
    status: closed
    drift_mapped:
      - CPP art. 584 paragraph 4 by Lei 15.358/2026
      - CPC art. 998 by Lei 15.484/2026
      - CPC art. 196 and art. 529-A by Lei 15.479/2026 with one-year vacatio
      - CF art. 37 XVI b by EC 138/2025
    no_scoped_textual_drift:
      - Codigo Penal
      - Lei 9.099/1995
      - Lei 12.153/2009
      - Lei 8.429/1992
  state_tjsp_subgate:
    status: closed
    drift_mapped:
      - Lei Estadual 10.261/1968 art. 78 by Lei 18.473/2026
      - LC Estadual 1.111/2010 by Lei 18.373/2025 and LC 1.441/2026
      - Regimento Interno by Assento 592/2025 and Assentos 593-596/2026
      - NSCGJ literal Capitulo XI by Provimentos CG 30/2025 and 04/2026
    no_direct_textual_drift_located:
      - Resolucao TJSP 850/2021 after Resolucao 864/2022 compilation
      - Resolucao TJSP 963/2025
    official_ambiguity:
      - edital repeats Tomo I Capitulo XI in the final two NSCGJ recuts; preserved without inferred correction
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
  source_integrity: all four local exam PDFs matched SOURCES.json sha256 and byte size
  authority_rule: current syllabus remains controlling; observed distributions are non-predictive
b2_coverage_gate:
  status: closed
  verified_at: 2026-09-12
  artifact: competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md
  packs: 6
  coverage_result: complete
  authority_rule: syllabus controls scope; matrix rows are authoring and QA contracts, not new syllabus
  first_authorized_pack: direito-penal
  first_pack_contract:
    - DP-01
    - DP-02
    - DP-03
    - DP-04
    - DP-05
    - DP-06
    - DP-07
    - DP-08
    - DP-09
    - DP-10
direito_penal_draft:
  status: draft_implemented
  version: 0.1.0-draft.1
  path: materials/tjsp-escrevente-2025/direito-penal
  files:
    - APOSTILA.md
    - SOURCES.md
    - MANIFEST.md
    - CHANGELOG.md
  coverage_rows_drafted: 10
  practice_questions: 30
  pdf_status: not_created
  notebooklm_status: not_tested
  semantic_qa_status: pending
  source_review_status: preliminary_spot_check_only
  baseline: 2025-07-29
  cp_scoped_drift: none_identified_by_gate2
next_gate:
  id: DIREITO-006
  name: qa_direito_penal_draft
  pack: direito-penal
  qa_artifact: materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md
  required:
    - full DP-01 through DP-10 coverage audit
    - full normative review against SRC-B2-CP
    - didactic and contrast review
    - semantic review of all 30 original questions
    - corpus structure review before release candidate
not_started:
  - close DIREITO-006 semantic QA for direito-penal
  - create a release candidate only if the semantic QA passes
  - create and inspect APOSTILA.pdf only after content stabilization
  - perform NotebookLM smoke before final release
  - continue remaining five B2 SubjectPacks only after the first pack pipeline is validated
validation:
  portuguese_editorial_qa: pass
  portuguese_notebooklm_live: pass
  portuguese_pdf_qa:
    result: pass
    material_version: 2.0.0
    pages: 16
    page_size: A4
    bytes: 20824
    sha256: b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931
    git_blob: 640efaed13dd43cc83f6904c62fdb86131b9124a
  direito_penal_semantic_qa:
    result: not_executed_yet
    policy: first-pass draft is not treated as semantic QA pass
  canonical_gate:
    command: python tools/verify.py
    result: not_executed_current_environment
    reason: local runtime cannot resolve github.com, preventing a valid canonical checkout
    attempted_at: 2026-09-12
    network_probe: git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
    error: Could not resolve host github.com
    policy: impossibility documented under DEC-0009; not treated as pass
ci: disabled
last_subject_pack_pull_request: 12
last_b2_preparation_pull_request: 13
last_b2_source_pull_request: 15
last_b2_banca_pull_request: 18
last_b2_matrix_pull_request: 19
merge_status: direito_penal_draft_ready_for_pr
last_b2_matrix_merge_commit: 5784e8bb9d904c677cb655dfbb069146e688b4e3
last_b2_banca_merge_commit: c3e7e75c65ab612cd05c86cfe9c0bcadb8d66008
last_b2_source_merge_commit: fa0fb7c66f6db2d83df98bedf75b2708f51baad3
last_b2_preparation_merge_commit: 540765b17e224a319b90a4e9da5272dd4db0684e
last_release_merge_commit: e6ce9d2571e9c68a8947701c08187c07e986d567
```
