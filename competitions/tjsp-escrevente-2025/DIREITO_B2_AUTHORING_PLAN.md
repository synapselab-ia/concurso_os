# DIREITO B2 - Plano canônico de autoria

**Competition:** `tjsp-escrevente-2025`  
**Syllabus block:** `B2 - Conhecimentos em Direito`  
**Authority:** `SRC-TJSP-EDITAL-2025-02`  
**Status:** `direito-penal 0.1.0-rc.1` validado; `direito-processual-penal 0.1.0-rc.1` com PDF canônico validado e smoke real do NotebookLM bloqueado por acesso externo nesta execução

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

Usar somente o `APOSTILA.pdf` canônico como fonte estudável e o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md` na configuração nativa da conversa.

O smoke deve verificar:

- chat explicativo;
- treino A-E uma questão por vez, sem vazamento de gabarito;
- correção ancorada na fonte;
- disciplina epistemológica em pergunta fora do corpus;
- `Teste`, `Cartões` e `Mapa mental` úteis;
- ausência de IDs `DPP-*`, gate labels e metadados de backoffice nos artefatos estudáveis.

Na tentativa de `2026-09-15`, o runtime disponível não forneceu sessão autenticada do NotebookLM nem canal interativo já conectado para operar a interface. Nenhuma interação externa foi presumida.

Resultado da tentativa:

`EXTERNAL_SMOKE_NOT_EXECUTED`

Registro: `materials/tjsp-escrevente-2025/direito-processual-penal/NOTEBOOKLM_SMOKE_0.1.0.md`.

Estado: `blocked_external_access`.

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
11. bloqueado por acesso externo - smoke real do NotebookLM de Direito Processual Penal;
12. Direito Processual Civil;
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
| 12 - NotebookLM processual penal | `blocked_external_access` | smoke real ainda não executado; exige sessão efetiva do produto e evidência observada |

## Regra de autoridade

O edital vigente determina escopo e prevalece sobre provas históricas, conforme DEC-0010. A autoria e o QA seguem `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e a política de fontes canônica.
