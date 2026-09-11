# CHANGELOG — Português — TJSP Escrevente 2025

## 2.0.0 — 2026-09-11 — release

Reconstrução major da apostila de Língua Portuguesa sob `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`.

### Autoria e cobertura

- auditada a distribuição 1.0.0 em `APOSTILA_AUDIT_1.0.0.md`;
- criada e fechada a matriz `APOSTILA_AUTHORING_MATRIX_2.0.0.md`;
- B1.1–B1.13 explicitamente localizados e `covered`;
- `APOSTILA.md` reconstruída por dependências pedagógicas;
- 30 questões autorais A–E adicionadas com gabarito comentado separado.

### Conteúdo reconstruído

- leitura verbal, não verbal, multissemiótica, literária e não literária;
- literalidade, pressuposição, inferência, extrapolação, tema, tese, argumento e ponto de vista;
- progressão, coesão, pronomes relativos e relações lógico-semânticas;
- semântica contextual, sentido próprio/figurado, ambiguidade e modalização;
- classes de palavras em funcionamento;
- concordância, regência, pronomes, colocação, crase, pontuação e reescrita integrada.

### PDF 2.0.0

Distribuição final publicada e confirmada por readback:

- 16 páginas A4;
- 20824 bytes;
- SHA-256 `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`;
- Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- PDF 1.4 pesquisável, não criptografado;
- aproximadamente 54,5 mil caracteres extraídos;
- 16 páginas renderizadas e inspecionadas sem clipping/overlap observado.

Tentativas binárias intermediárias `5bea23e3...` e `82046b5d...` permanecem rejeitadas; o fallback 1.0.0 `2287be2b...` foi apenas temporário.

### QA editorial e NotebookLM

- QA-1 cobertura: pass;
- QA-2 exatidão/fonte: pass;
- QA-3 didática: pass;
- QA-4 distinções/casos-limite: pass;
- QA-5 prática: pass;
- QA-6 coerência com banca sem overfitting: pass;
- QA-7 estático: pass;
- QA-7 live: **pass** após reteste;
- QA-8 redundância/coerência: pass;
- QA-9 PDF textual/visual/publicação: pass;
- QA-10: parcial por impossibilidade de executar o gate determinístico neste runtime.

O primeiro smoke real do chat detectou formulação absoluta em inferência, rótulo inconsistente em exemplo sem crase, correção pouco específica de concordância e sugestão automática de interface com gabarito. `METODOLOGIA_NOTEBOOKLM.md` foi endurecida para `2.0.0-rc2`; o reteste passou.

O smoke final aprovou:

- chat configurado;
- Teste nativo, com amostras de concordância, sentido figurado e conectivos;
- Cartões, com amostras de enunciador, inferência, extrapolação e `cujo`;
- Mapa mental, que recuperou de forma inteligível sentido em textos, arquitetura/coerência, semântica/léxico, classes de palavras, concordância, regência/crase e pontuação/reescrita sem ser dominado por questões/gabaritos.

### Gate determinístico

O runtime local não resolveu `github.com`, impedindo checkout canônico e execução válida de `python tools/verify.py`. A impossibilidade ficou documentada conforme DEC-0009 e não foi tratada como `pass`.

---

## 1.0.3 — 2026-09-11

Patch de instalação após observar a configuração nativa de conversas do NotebookLM.

- `APOSTILA.pdf` permaneceu como fonte principal;
- `METODOLOGIA_NOTEBOOKLM.md` passou a ser copiada para `Configurar as conversas → Personalizado`, não carregada como fonte;
- tamanho de resposta `Padrão` mantido por default;
- DEC-0017 refinou DEC-0016.

---

## 1.0.2 — 2026-09-11

Patch arquitetural após smoke tests reais do NotebookLM.

- Teste nativo com metodologia como fonte gerou pergunta sobre metodologia;
- sem metodologia como fonte, gerou pergunta conceitual da apostila;
- decidiu-se manter `APOSTILA.pdf` como conteúdo e `METODOLOGIA_NOTEBOOKLM.md` como instrução exclusiva do chat;
- análise de banca, sources, manifest, changelog, edital e provas históricas permanecem backoffice.

---

## 1.0.1 — 2026-09-11

Patch de usabilidade para tornar o NotebookLM Studio-first e reduzir micro-orquestração.

- Teste, Cartões, Mapa mental, Relatórios e outros artefatos passam a ser usados diretamente sobre a apostila;
- chat permanece como camada de aprofundamento e correção.

---

## 1.0.0 — 2026-09-11

Primeira versão operacional do SubjectPack.

- cobertura dos 13 itens de Língua Portuguesa do edital 2025;
- apostila autoral pesquisável para NotebookLM;
- análise de 88 questões de Português das provas 2021/2023/2024/2025;
- metodologia específica para NotebookLM;
- manifesto, fontes e limites epistemológicos;
- PDF final de 8 páginas Letter, pesquisável e visualmente verificado.