# Project Control

- **Status:** ACTIVE
- **Phase:** SUBJECT_PACK_RELEASE_VALIDATION
- **Canonical checkpoint:** `00_SYSTEM/CHECKPOINT.md`
- **Canonical next action:** `00_SYSTEM/NEXT_ACTION.md`
- **Current implementation branch:** `content/apostila-portugues-2.0.0`
- **Last implementation branch:** `docs/apostila-authoring-protocol`
- **Current competition:** `tjsp-escrevente-2025`
- **Current subject:** `portugues`
- **Current pack:** `portugues 2.0.0` release candidate; conteúdo, matriz, QA editorial e PDF canônico concluídos; smoke real do NotebookLM pendente
- **Current repository PDF:** Português 2.0.0 íntegro, 16 páginas A4, 20824 bytes, Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`
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