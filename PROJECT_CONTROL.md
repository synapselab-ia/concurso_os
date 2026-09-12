# Project Control

- **Status:** ACTIVE
- **Phase:** SUBJECT_PACK_AUTHORING_PREP
- **Canonical checkpoint:** `00_SYSTEM/CHECKPOINT.md`
- **Canonical next action:** `00_SYSTEM/NEXT_ACTION.md`
- **Current implementation branch:** `content/direito-b2-authoring-prep`
- **Last implementation branch:** `content/apostila-portugues-2.0.0`
- **Current competition:** `tjsp-escrevente-2025`
- **Current subject:** `B2 — Conhecimentos em Direito` — fronteira editorial fechada em seis SubjectPacks; fechamento de fontes/versões em andamento
- **Planned B2 SubjectPacks:** `direito-penal`, `direito-processual-penal`, `direito-processual-civil`, `direito-constitucional`, `direito-administrativo`, `legislacao-interna`
- **Current pack:** nenhum; redação bloqueada até Gates 2–4
- **Last released pack:** `portugues 2.0.0` — final, com QA editorial/PDF/NotebookLM concluídos
- **Portuguese repository PDF:** 16 páginas A4, 20824 bytes, Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`
- **B2 authoring plan:** `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md`
- **B2 source inventory:** `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`
- **B2 boundary decision:** DEC-0019
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