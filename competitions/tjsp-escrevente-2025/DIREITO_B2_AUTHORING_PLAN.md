# DIREITO B2 - Plano canônico de autoria

**Competition:** `tjsp-escrevente-2025`  
**Syllabus block:** `B2 - Conhecimentos em Direito`  
**Authority:** `SRC-TJSP-EDITAL-2025-02`  
**Status:** `direito-penal 0.1.0-rc.1` validado; `direito-processual-penal 0.1.0-rc.2` com PDF corrigido validado e vínculo canônico recuperado; smoke regressivo curto pendente

## Objetivo

Transformar o bloco B2 do edital em unidades de autoria, fonte e QA sem perder a unidade estatística da prova. O edital mantém Conhecimentos em Direito como um bloco de 30 questões; a divisão em packs é editorial e pedagógica, não uma previsão de distribuição de questões.

## Fronteira de B2

DEC-0019 divide a entrega em seis SubjectPacks:

1. `direito-penal`;
2. `direito-processual-penal`;
3. `direito-processual-civil`;
4. `direito-constitucional`;
5. `direito-administrativo`;
6. `legislacao-interna`.

## Escopo canônico por pack

### `direito-penal`
Código Penal: arts. 293-305; 307; 308; 311-A; 312-317; 319-333; 336-337; 339-347; 357; 359.

### `direito-processual-penal`
CPP: arts. 251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667.  
Lei n.º 9.099/1995: arts. 60-83; 88-89.

### `direito-processual-civil`
CPC: arts. 144-155; 188-275; 294-311; 318-538; 994-1026.  
Lei n.º 9.099/1995: arts. 3-19.  
Lei n.º 12.153/2009: integral.

### `direito-constitucional`
Constituição Federal: Título II, Caps. I-III; Título III, Cap. VII, Seções I-II; art. 92.

### `direito-administrativo`
Lei Estadual n.º 10.261/1968: arts. 1-86; 171-175; 239-323.  
Lei Federal n.º 8.429/1992: integral.

### `legislacao-interna`
Resoluções TJSP n.º 850/2021 e 963/2025; LC Estadual n.º 1.111/2010; Regimento Interno do TJSP; Normas da Corregedoria nos recortes literais do edital. A duplicidade de referência ao Capítulo XI é preservada sem correção inferida.

## Gate 2 - fontes e versões

`DIREITO_SOURCES.md` fecha o baseline em `2025-07-29` e separa drift posterior.

Pontos de manutenção relevantes:

- CPP art. 584, § 4º: incluído pela Lei n.º 15.358/2026, posterior ao cutoff;
- CPC arts. 196, 529-A e 998: alterações posteriores mapeadas;
- CF art. 37, XVI, `b`: alteração posterior ao cutoff;
- Lei Estadual n.º 10.261/1968 art. 78: alteração posterior;
- LC Estadual n.º 1.111/2010: alterações posteriores;
- Regimento Interno: baseline inclui Assento 591/2025 e exclui 592-596;
- NSCGJ: alterações posteriores ao cutoff ficam separadas.

Para Processual Penal, `SRC-B2-CPP` é `cutoff_closed_drift_mapped` e `SRC-B2-L9099` é `cutoff_closed_no_scoped_drift`.

## Gate 3 - banca

`DIREITO_B2_BANCA_ANALYSIS.md` classifica 150 questões de Direito de 2021, 2023, 2024 e 2025. Os sinais históricos servem para engenharia silenciosa de literalidade, fluxo, prazo, competência, requisito, contraste e distratores. Não criam peso futuro nem alteram o syllabus.

## Gate 4 - matriz

`DIREITO_B2_COVERAGE_MATRIX.md` fecha o contrato de cobertura, profundidade, contraste, prática e QA para os seis packs. Nenhuma row pode ser omitida por baixa frequência histórica.

## Gates 5 a 7 - Direito Penal

- Gate 5: `0.1.0-draft.1`, DP-01...DP-10 e 30 questões autorais, PR 20.
- Gate 6: QA resultou em `0.1.0-draft.3`, conteúdo/prática aprovados, PR 21.
- Gate 7: `0.1.0-rc.1` validado com PDF canônico e smoke real do NotebookLM `pass_with_observations`, PRs 22-26. As observações não bloqueantes foram vazamento de IDs `DP-*` nos títulos e formulação epistemológica excessivamente categórica sobre conteúdo ausente do corpus.

## Gate 8 - primeiro draft de Direito Processual Penal

`0.1.0-draft.1` implementou DPP-01...DPP-25 em 25 unidades, 52 questões autorais, nenhum `DPP-*` em título estudável e controle do cutoff. PR 27, merge `fedd24f8607b6d2b68d4aa9352ff949529680f1e`.

Estado: `closed_as_draft`.

## Gate 9 - QA semântico/normativo de Direito Processual Penal

A revisão integral produziu `0.1.0-draft.2` com:

- DPP-01...DPP-25: `pass_after_corrections`;
- revisão normativa: `pass_after_corrections`;
- didática/fluxos/contrastes: `pass`;
- prática final: `60/60 pass`;
- requisitos `Q-LIT`, `Q-CMP`, `Q-CAS`, `Q-FLX`, `Q-VER` e `Q-FULL`: `pass`;
- corpus Markdown: `pass_for_markdown`;
- IDs de backoffice em títulos: `pass_absent`.

Correções relevantes incluíram art. 262; arts. 363-365; arts. 394-A, 398 e 400-A; art. 537 revogado e art. 538; expansão de 574-603; tratamento artigo a artigo de 604-620, incluindo art. 611 revogado; tratamento de 632-646; art. 647-A; e completude dos arts. 60-83 da Lei 9.099/1995.

PR 28, merge `70a5103d3f8ceb6132908d68963a2a55732665ec`.

Estado: `closed`.

## Gate 10 - release candidate estático de Direito Processual Penal

`0.1.0-rc.1` foi preparado a partir do conteúdo aprovado do `draft.2`, sem reabertura semântica.

Executado:

- identidade de `APOSTILA.md`, `MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md` sincronizada para `0.1.0-rc.1`;
- mudança no corpo de `APOSTILA.md` restrita a metadados de versão/status;
- `METODOLOGIA_NOTEBOOKLM.md` criada como configuração da conversa, não como fonte estudável;
- QA estático do corpus e tutor: `pass_static`;
- baseline `2025-07-29` e isolamento do art. 584, § 4º, de 2026 preservados.

PR 29, merge `947ea624d7abfa3b1db4481064aa4abf9743be19`.

Estado: `closed_static_ready_for_pdf`.

## Gate 11 - PDF canônico de Direito Processual Penal

Em `2026-09-15`, a fonte Markdown usada na geração foi comprovada idêntica ao `APOSTILA.md` canônico pelo Git blob:

`11a41d18ff3a8b03150923ec68d44087bded7267`

O PDF final possui:

- 28 páginas A4;
- PDF 1.4 pesquisável;
- 37.894 bytes;
- SHA-256 `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob esperado `4eabdacec7858120792cf792ca227335e41730b6`;
- readback textual `pass`;
- inspeção visual `28/28 pass`;
- questões e gabarito estruturalmente separados.

O transporte binário final foi feito por Git Data API com conteúdo base64. O GitHub criou o blob `4eabdacec7858120792cf792ca227335e41730b6`, exatamente igual ao Git blob esperado do candidato auditado. O mesmo SHA foi confirmado no caminho remoto versionado.

Resultado:

`PASS_CANONICAL_BINARY_IDENTITY`

PR 30 preservou o bloqueio intermediário real. PR 31 publicou o binário exato e foi mergeada em `b63f9a8f4b51894bf37e070eee3feeb481781855`.

O gate determinístico continua `not_executed_current_environment`: nova tentativa de `git clone` em `2026-09-15` falhou com `Could not resolve host: github.com`, exit 128. Isso não é PASS.

Estado: `closed_pdf_validated`.

## Gate 12 - smoke real do NotebookLM de Direito Processual Penal

O usuário executou manualmente o smoke real sobre o PDF de `0.1.0-rc.1` e forneceu evidência de:

- chat explicativo coerente;
- treino A-E uma questão por vez e sem gabarito antes da tentativa;
- correção ancorada no corpus;
- disciplina epistemológica em pergunta sobre jurisprudência externa;
- amostras úteis de `Teste`, `Cartões` e `Mapa mental`;
- ausência observada de IDs `DPP-*`, QA, gates ou metadados de backoffice.

Resultado comportamental: `PASS_BEHAVIORAL_ON_RC1`.

O gate de release não foi fechado porque, na revisão final, foi confirmado defeito semântico no próprio corpus: atribuição incorreta ao art. 371 do CPP. O PDF usado no smoke foi invalidado.

Estado: `interrupted_by_semantic_defect`.

## Gate 13 - recuperação semântica de Direito Processual Penal

Em `2026-09-18`, a fonte oficial do CPP foi reaberta para os arts. 370-372. Confirmou-se que:

- art. 371 admite intimação por despacho na petição em que for requerida, observado o art. 357;
- art. 372 trata do adiamento da instrução criminal e da marcação imediata de dia e hora para prosseguimento na presença de partes e testemunhas, com termo nos autos.

A Unidade 5 foi corrigida em `0.1.0-draft.3`. DPP-05 passou em QA direcionado após a correção. O PDF de `0.1.0-rc.1` mantém seu histórico de identidade binária, mas foi invalidado semanticamente e removido do caminho canônico.

PR 33 registra a recuperação. Estado: `closed_targeted_semantic_recovery` após o merge.

## Gate 14 - novo RC de Direito Processual Penal

`0.1.0-draft.3` foi promovido para `0.1.0-rc.2` sem nova mudança jurídica. `APOSTILA.md` mudou somente em metadados de versão/status; `SOURCES`, `MANIFEST`, `METODOLOGIA_NOTEBOOKLM` e `CHANGELOG` foram sincronizados. O Markdown rc.2 ficou congelado no Git blob `8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18`.

PR 34 registra a promoção. Estado: `closed_static_ready_for_pdf` após o merge.

## Gate 15 - novo PDF corrigido

O PDF rc.2 foi gerado exclusivamente do Markdown congelado de Git blob `8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18`.

Resultado:

- 28 páginas A4;
- PDF 1.4 pesquisável;
- 37.917 bytes;
- SHA-256 `aeaa44ac6a275623d79098d0699c18899f83d6ade75be8661f71a3ad9dfc36fe`;
- Git blob `6374969ba722451dd6740364e24c41f25e730b54`;
- readback textual `pass`;
- inspeção visual `28/28 pass`;
- identidade binária remota `PASS_CANONICAL_BINARY_IDENTITY`.

PR 35 registra o PDF corrigido. Estado: `closed_pdf_validated` após o merge.

## Gate 15R - recuperação do vínculo canônico do PDF

Em `2026-09-24`, a auditoria do tree real de `main` mostrou que a PR #35 havia mesclado a documentação de `DIREITO-015`, mas não o caminho `APOSTILA.pdf`. O blob auditado `6374969ba722451dd6740364e24c41f25e730b54` continuava existente com `37.917` bytes.

A recuperação religa exatamente esse blob ao caminho canônico, sem regenerar o PDF e sem mudança semântica.

PR 36 registra a recuperação. Estado: `closed_repository_linkage_recovery` após o merge.

## Gate 16 - smoke regressivo curto

O usuário deve carregar somente o PDF rc.2 corrigido no NotebookLM e confirmar a correção dos arts. 371-372, um treino A-E sem vazamento antecipado e ausência de metadados internos. Não é necessário repetir a bateria completa já observada no rc.1.

Estado: `next`.

## Lições obrigatórias para os próximos packs

- coverage IDs, gate labels e outros identificadores de backoffice não entram em títulos visíveis do StudentContent;
- rastreabilidade fica em matriz, manifest e QA;
- ausência na fonte é limite do corpus, não prova de inexistência externa;
- smoke final deve verificar vazamento de metadados em Teste, Cartões e Mapa mental;
- smoke final deve incluir pergunta cuja resposta dependa de informação ausente do corpus;
- hash local de PDF não substitui prova de identidade binária do arquivo versionado.

## Ordem de produção

1. concluído - inventário e versão de fontes de B2;
2. concluído - análise histórica reproduzível;
3. concluído - matrizes dos seis packs;
4. concluído como draft - Direito Penal;
5. concluído - QA de Direito Penal;
6. concluído com observações - RC/PDF/NotebookLM de Direito Penal;
7. concluído como draft - Direito Processual Penal;
8. concluído - QA de Direito Processual Penal;
9. concluído - preparação estática do RC de Direito Processual Penal;
10. concluído - PDF canônico de Direito Processual Penal;
11. interrompido por defeito semântico após evidência comportamental - smoke de Direito Processual Penal;
12. concluído após merge de DIREITO-013 - recuperação semântica DPP-05 e retorno a draft.3;
13. próximo - novo RC corrigido de Direito Processual Penal;
14. novo PDF corrigido e smoke regressivo curto;
15. Direito Processual Civil;
13. Direito Constitucional;
14. Direito Administrativo;
15. Legislação Interna.

## Gates

| Gate | Estado | Critério |
|---|---|---|
| 1 - fronteira | `closed` | seis SubjectPacks definidos |
| 2 - fontes/versões | `closed` | baseline, proveniência e drift mapeados |
| 3 - banca | `closed` | 150 questões classificadas |
| 4 - matriz | `closed` | recortes do syllabus rastreados |
| 5 - draft penal | `closed_as_draft` | DP-01...DP-10 implementados |
| 6 - QA penal | `closed` | conteúdo e prática aprovados |
| 7 - RC penal | `closed_with_observations` | PDF e NotebookLM validados com observações não bloqueantes |
| 8 - draft processual penal | `closed_as_draft` | DPP-01...DPP-25 e prática inicial implementados |
| 9 - QA processual penal | `closed` | cobertura, norma, didática, prática e corpus Markdown aprovados após correções |
| 10 - RC processual penal | `closed_static_ready_for_pdf` | identidade rc.1, tutor e QA estático concluídos sem reabertura semântica |
| 11 - PDF processual penal | `closed_pdf_validated` | PDF canônico versionado e Git blob remoto idêntico ao candidato auditado |
| 12 - NotebookLM processual penal | `interrupted_by_semantic_defect` | comportamento real observado como pass no rc.1, mas corpus posteriormente invalidado |
| 13 - recuperação DPP-05 | `closed_targeted_semantic_recovery` | arts. 370-372 rechecados; art. 371 corrigido em draft.3; PDF rc.1 invalidado |
| 14 - novo RC processual penal | `closed_static_ready_for_pdf` | rc.2 congelado a partir do draft.3 corrigido, sem nova mudança semântica |
| 15 - novo PDF processual penal | `closed_pdf_validated` | PDF rc.2 auditado com identidade binária exata; publicação documental da PR #35 precisou de recuperação de vínculo |
| 15R - recuperação de vínculo do PDF | `closed_repository_linkage_recovery` | mesmo blob auditado relinkado ao caminho canônico sem regeneração |
| 16 - regressão NotebookLM processual penal | `next` | smoke curto sobre o PDF corrigido; depois avançar para processo civil se passar |

## Regra de autoridade

O edital vigente determina escopo e prevalece sobre provas históricas, conforme DEC-0010. A autoria e o QA seguem `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e a política de fontes canônica.
