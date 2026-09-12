# Project Control

- **Status:** ACTIVE
- **Phase:** SUBJECT_PACK_AUTHORING_PREP
- **Canonical checkpoint:** `00_SYSTEM/CHECKPOINT.md`
- **Canonical next action:** `00_SYSTEM/NEXT_ACTION.md`
- **Current implementation branch:** `main`
- **Last implementation branch:** `research/direito-b2-gate2-state-tjsp`
- **Current competition:** `tjsp-escrevente-2025`
- **Current subject:** `B2 — Conhecimentos em Direito` — fronteira editorial e fontes/versões fechadas; análise histórica da banca é o próximo gate
- **Planned B2 SubjectPacks:** `direito-penal`, `direito-processual-penal`, `direito-processual-civil`, `direito-constitucional`, `direito-administrativo`, `legislacao-interna`
- **Current pack:** nenhum; redação bloqueada até Gates 3–4
- **Last released pack:** `portugues 2.0.0` — final, com QA editorial/PDF/NotebookLM concluídos
- **Portuguese repository PDF:** 16 páginas A4, 20824 bytes, Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`
- **B2 authoring plan:** `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md`
- **B2 source inventory:** `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` — Gate 2 fechado em 2026-09-11
- **B2 boundary decision:** DEC-0019
- **Last B2 preparation PR:** `#13`, merged to `main` at `540765b17e224a319b90a4e9da5272dd4db0684e`
- **B2 federal source PR:** `#14`, merged to `main` at `228f2225c3b7655d8fd47c325f7c5a2db40bf0a0`
- **B2 state/TJSP source PR:** `#15`, merged to `main` at `fa0fb7c66f6db2d83df98bedf75b2708f51baad3`
- **Gate 2:** `closed` — federal, state and TJSP sources reconciled to cutoff `2025-07-29`, with post-cutoff drift separately mapped
- **Next Gate:** Gate 3 — classify Direito questions from 2021/2023/2024/2025 reproducibly before authoring matrices
- **Next subject evidence:** o syllabus vigente atribui **30 questões** a Conhecimentos em Direito; o bloco contém Direito Penal, Processual Penal, Processual Civil, Constitucional, Administrativo e Legislação Interna
- **Study stack:** GitHub + ChatGPT + NotebookLM
- **Primary NotebookLM UX:** `APOSTILA.pdf` como fonte; instruções de `METODOLOGIA_NOTEBOOKLM.md` na configuração personalizada da conversa
- **Apostila authoring:** `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` obrigatório para criação/reconstrução substancial
- **Backoffice:** edital, provas, análise de banca, fontes, QA e histórico ficam no GitHub/ChatGPT por padrão
- **Stack specification:** `docs/STACK_NOTEBOOKLM.md`
- **Validation gate:** `python tools/verify.py`
- **CI:** disabled during production
- **Repository visibility assumption:** public
- **Merge policy:** validated development PRs may be merged autonomously; see `00_SYSTEM/DECISION_LOG.md` DEC-0009

Este arquivo é um índice executivo. Não duplicar arquitetura, histórico ou protocolos aqui.