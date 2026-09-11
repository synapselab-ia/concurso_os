# Project Control

- **Status:** ACTIVE
- **Phase:** SUBJECT_PACK_AUTHORING_PREP
- **Canonical checkpoint:** `00_SYSTEM/CHECKPOINT.md`
- **Canonical next action:** `00_SYSTEM/NEXT_ACTION.md`
- **Current implementation branch:** `main`
- **Last implementation branch:** `content/apostila-portugues-2.0.0`
- **Current competition:** `tjsp-escrevente-2025`
- **Current subject:** `conhecimentos-em-direito` — próximo domínio canônico a preparar
- **Last released pack:** `portugues 2.0.0` — final, com QA editorial/PDF/NotebookLM concluídos
- **Portuguese repository PDF:** 16 páginas A4, 20824 bytes, Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`
- **Next subject evidence:** o syllabus vigente atribui **30 questões** a Conhecimentos em Direito, maior bloco ainda sem SubjectPack; a fronteira interna inclui Direito Penal, Processual Penal, Processual Civil, Constitucional, Administrativo e Legislação Interna
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