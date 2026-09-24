# MANIFEST - SubjectPack Direito Processual Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-processual-penal`  
**Pack version:** `0.1.0-rc.2`  
**Status:** `release_candidate_corrected_pdf_validated_pending_notebooklm_regression`  
**RC date:** `2026-09-14`  
**PDF QA update:** `2026-09-15`  
**NotebookLM smoke evidence:** `real_user_smoke_recorded_2026-09-18_on_invalidated_rc1`  
**Semantic recovery:** `2026-09-18`  
**RC2 preparation:** `2026-09-18`  
**Repository linkage recovery:** `2026-09-24`

## Objetivo

Este SubjectPack cobre Direito Processual Penal no recorte do Edital de Abertura n.º 02/2025 e segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DPP-01...DPP-25` de `DIREITO_B2_COVERAGE_MATRIX.md`.

`DIREITO-009` aprovou o conteúdo em `0.1.0-draft.2`; `DIREITO-010/011` promoveram `0.1.0-rc.1` e publicaram PDF com identidade binária exata. Em `DIREITO-012`, o usuário executou smoke real com evidência comportamental satisfatória. Antes do fechamento do gate, porém, foi confirmado erro normativo na atribuição do art. 371 do CPP. `DIREITO-013` reabriu o QA direcionado de DPP-05, corrigiu a fonte em `0.1.0-draft.3` e invalidou o PDF anterior para uso corrente.

## Escopo oficial

- CPP: `arts. 251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`;
- Lei n.º 9.099/1995: `arts. 60-83; 88-89`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fontes normativas principais:

- `SRC-B2-CPP`;
- `SRC-B2-L9099`.

Baseline: `2025-07-29`.

O art. 584, § 4º, do CPP, incluído pela Lei n.º 15.358/2026, permanece fora do StudentContent do edital e rastreado apenas como drift pós-cutoff.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md`: `0.1.0-rc.2`, conteúdo jurídico congelado do `0.1.0-draft.3`, 25 unidades, sem coverage IDs em títulos ou subtítulos, com 60 questões autorais A-E e gabarito comentado separado; DPP-05 corrigido contra a fonte oficial.
- `APOSTILA.pdf`: PDF corrigido de `0.1.0-rc.2`, publicado no caminho canônico e aprovado em `DIREITO-015` com `PASS_CANONICAL_BINARY_IDENTITY`.

Identidade histórica do PDF `0.1.0-rc.1` invalidado semanticamente:

- caminho: `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`;
- páginas: `28`;
- página: `A4`;
- formato: `PDF 1.4`;
- tamanho: `37.894 bytes`;
- SHA-256: `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob local esperado: `4eabdacec7858120792cf792ca227335e41730b6`;
- Git blob remoto observado: `4eabdacec7858120792cf792ca227335e41730b6`;
- readback textual: `PASS_TEXT_READBACK`;
- inspeção visual: `PASS_VISUAL_28_OF_28`;
- identidade binária: `PASS_CANONICAL_BINARY_IDENTITY`.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md`: `0.1.0-rc.2`, configuração persistente do tutor; não integra o corpus estudável; comportamento inalterado em relação ao rc.1.

### BackofficeArtifact

- `MANIFEST.md`: identidade, escopo e estado dos gates;
- `SOURCES.md`: proveniência e controle de versão;
- `CHANGELOG.md`: histórico editorial;
- `APOSTILA_QA_0.1.0.md`: QA semântico/normativo, QA estático do RC e QA do PDF;
- `NOTEBOOKLM_SMOKE_0.1.0.md`: estado e evidência do gate externo `DIREITO-012`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Recuperação de vínculo do PDF em DIREITO-015R

A auditoria do estado real do GitHub em `2026-09-24` encontrou uma divergência entre a documentação de fechamento de `DIREITO-015` e o tree efetivamente mesclado: `APOSTILA.pdf` não estava presente no `main` de head `ad004ba538c0e34b2c3739f563d4f09230d1f6f5`.

O blob previamente auditado `6374969ba722451dd6740364e24c41f25e730b54`, com `37.917` bytes, permanecia existente no repositório. `DIREITO-015R` apenas o religa ao caminho canônico. Não há regeneração do PDF nem mudança em seu conteúdo.

Depois do merge dessa recuperação, o estado declarado acima volta a corresponder ao tree real e o gate seguinte permanece `DIREITO-016`.

## Rastreabilidade de cobertura

Os IDs abaixo são backoffice e não aparecem como rótulos estudáveis.

| coverage_id | recorte | estado semântico do conteúdo congelado |
|---|---|---|
| DPP-01 | CPP 251-258 | qa_pass |
| DPP-02 | CPP 261-267 | qa_pass |
| DPP-03 | CPP 274 | qa_pass |
| DPP-04 | CPP 351-369 | qa_pass |
| DPP-05 | CPP 370-372 | qa_pass_after_correction |
| DPP-06 | CPP 394-405 | qa_pass_after_corrections |
| DPP-07 | CPP 406-421 | qa_pass |
| DPP-08 | CPP 422-431 | qa_pass |
| DPP-09 | CPP 432-452 | qa_pass |
| DPP-10 | CPP 453-474 | qa_pass |
| DPP-11 | CPP 475-491 | qa_pass |
| DPP-12 | CPP 492-497 | qa_pass |
| DPP-13 | CPP 531-538 | qa_pass_after_corrections |
| DPP-14 | CPP 541-548 | qa_pass |
| DPP-15 | CPP 574-580 | qa_pass_after_corrections |
| DPP-16 | CPP 581-592 | qa_pass_after_corrections |
| DPP-17 | CPP 593-603 | qa_pass_after_corrections |
| DPP-18 | CPP 604-620 | qa_pass_after_corrections |
| DPP-19 | CPP 621-631 | qa_pass |
| DPP-20 | CPP 632-646 | qa_pass_after_corrections |
| DPP-21 | CPP 647-667 | qa_pass_after_corrections |
| DPP-22 | Lei 9.099, 60-68 | qa_pass_after_corrections |
| DPP-23 | Lei 9.099, 69-76 | qa_pass |
| DPP-24 | Lei 9.099, 77-83 | qa_pass_after_corrections |
| DPP-25 | Lei 9.099, 88-89 | qa_pass |

## Resultado acumulado

| gate | resultado |
|---|---|
| cobertura DPP-01...DPP-25 | `pass_after_corrections` |
| revisão normativa integral | `targeted_reopen_dpp05_pass_after_correction` |
| didática/fluxos/contrastes | `pass` |
| prática autoral | `pass_60_of_60` |
| requisitos Q-LIT/Q-CMP/Q-CAS/Q-FLX/Q-VER/Q-FULL | `pass` |
| corpus Markdown | `pass_for_markdown_after_targeted_correction` |
| coerência com banca sem overfitting | `pass` |
| ausência de IDs de backoffice em títulos | `pass` |
| configuração do tutor | `pass_static` |
| corpus/tutor NotebookLM estático | `pass_static` |
| identidade da fonte Markdown usada para o PDF rc.1 | `historical_pass_source_markdown_identity` |
| PDF rc.1 - readback textual | `historical_pass_text_readback` |
| PDF rc.1 - visual | `historical_pass_visual_28_of_28` |
| PDF rc.1 - identidade binária | `historical_pass_canonical_binary_identity_but_semantically_invalidated` |
| `APOSTILA.pdf` vigente | `pass_canonical_binary_identity_rc2` |
| NotebookLM smoke real | `pass_behavioral_on_rc1_corpus_invalidated` |
| `python tools/verify.py` | `not_executed_current_environment` por falha DNS ao obter checkout canônico, não tratado como PASS |

## DIREITO-011 - fechamento do PDF

O PDF foi produzido exclusivamente a partir do Markdown congelado cujo Git blob é `11a41d18ff3a8b03150923ec68d44087bded7267`. O candidato passou por readback textual e inspeção visual integral de `28/28` páginas antes da publicação.

Na publicação final, o GitHub criou o blob `4eabdacec7858120792cf792ca227335e41730b6`, exatamente igual ao Git blob calculado para o candidato auditado. O mesmo SHA foi observado no caminho remoto versionado. Nenhuma alteração jurídica foi introduzida durante geração ou transporte.

## DIREITO-012 - smoke real e interrupção do release

O usuário executou o smoke real e forneceu evidência de chat explicativo, treino A-E, correção após tentativa, disciplina fora do corpus, Teste, Cartões e Mapa mental. O comportamento foi satisfatório nas amostras e não houve vazamento observado de IDs `DPP-*` ou metadados internos.

Esse resultado é registrado como `PASS_BEHAVIORAL_ON_RC1`, mas não fecha o release porque o corpus `rc.1` foi posteriormente invalidado pelo erro do art. 371.

Detalhes: `NOTEBOOKLM_SMOKE_0.1.0.md`.

## DIREITO-013 - recuperação semântica

A Unidade 5 foi corrigida em `0.1.0-draft.3` contra `SRC-B2-CPP`. DPP-05 está `qa_pass_after_correction`. O PDF antigo foi invalidado e removido do caminho canônico para evitar uso acidental.

A tentativa de executar o gate determinístico em `2026-09-18` não chegou a `python tools/verify.py`: o clone da branch falhou por DNS, exit `128`. Estado: `NOT_EXECUTED_CURRENT_ENVIRONMENT`.

## Próximo estágio

Preparar novo release candidate a partir do `0.1.0-draft.3`, sem nova mudança semântica. Depois, gerar e auditar novo PDF. O smoke final pode ser curto e regressivo, pois o comportamento geral do NotebookLM já foi efetivamente observado no RC anterior.


## DIREITO-014 - novo release candidate corrigido

`0.1.0-rc.2` foi preparado exclusivamente a partir do `0.1.0-draft.3` corrigido. No `APOSTILA.md`, a promoção alterou apenas metadados de versão/status; o corpo jurídico, a prática e o gabarito não foram reabertos.

Estado de saída: `STATIC_READY_FOR_NEW_PDF`. O caminho canônico `APOSTILA.pdf` permanece ausente até que um novo binário seja gerado e auditado a partir deste RC.

Gate determinístico em DIREITO-014: `NOT_EXECUTED_CURRENT_ENVIRONMENT` por falha DNS no clone da branch rc.2, exit `128`; não tratado como PASS.


## DIREITO-015 - PDF corrigido

O PDF canônico de `0.1.0-rc.2` foi gerado exclusivamente do Markdown congelado de Git blob `8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18` e auditado antes da publicação.

Identidade do artefato atual:

- caminho: `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`;
- 28 páginas A4, PDF 1.4, pesquisável;
- 37.917 bytes;
- SHA-256 `aeaa44ac6a275623d79098d0699c18899f83d6ade75be8661f71a3ad9dfc36fe`;
- Git blob `6374969ba722451dd6740364e24c41f25e730b54`;
- readback textual: `PASS`;
- inspeção visual: `PASS_VISUAL_28_OF_28`;
- identidade binária remota: `PASS_CANONICAL_BINARY_IDENTITY`.

O rc.1 continua historicamente registrado, mas semanticamente invalidado. O artefato vigente é somente o rc.2 acima.

Gate determinístico: `NOT_EXECUTED_CURRENT_ENVIRONMENT`; o clone da branch falhou por DNS em `2026-09-18`, exit `128`.

## Próximo estágio após DIREITO-015

Executar smoke curto de regressão no NotebookLM com somente o PDF rc.2 corrigido como fonte. A bateria comportamental completa não precisa ser repetida.
