# MANIFEST - SubjectPack Direito Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-penal`  
**Pack version:** `0.1.0-rc.1`  
**Status:** `validated_release_candidate`  
**RC date:** `2026-09-12`

## Objetivo

Este SubjectPack é a primeira implementação jurídica de B2. O conteúdo Markdown foi aprovado no QA editorial/normativo em `0.1.0-draft.3` e congelado para o release candidate. O `0.1.0-rc.1` foi validado como primeiro pipeline jurídico completo: PDF canônico e QA-9 concluídos, smoke real do NotebookLM aprovado com observações não bloqueantes e impossibilidade atual do gate determinístico reavaliada conforme DEC-0009.

A autoria segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DP-01`...`DP-10` de `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Escopo oficial

Código Penal: `arts. 293-305; 307; 308; 311-A; 312-317; 319-333; 336; 337; 339-347; 357; 359`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fonte normativa principal: `SRC-B2-CP` - Decreto-Lei n.º 2.848/1940, Código Penal, Planalto.

Baseline autoral: texto vigente em `2025-07-29`. O Gate 2 classificou o recorte como `cutoff_closed_no_scoped_drift`; alterações posteriores identificadas no Código Penal não atingem diretamente os dispositivos deste pack. O art. 338-A é posterior e está fora do recorte.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md` - `0.1.0-rc.1`; conteúdo editorial/normativo idêntico ao `0.1.0-draft.3`, salvo metadados de RC e nota de estado final.
- `APOSTILA.pdf` - versionado com identidade binária exata do candidato auditado: `17` páginas A4, `30.167` bytes, PDF 1.4, SHA-256 `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`, Git blob `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`. QA-9 textual e visual fechado por identidade binária exata e nova inspeção de 17/17 páginas em `2026-09-14`.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` - criado em `0.1.0-rc.1`; contém a configuração nativa do tutor jurídico e não integra o corpus estudável.

### BackofficeArtifact

- `SOURCES.md` - proveniência e regra de versão.
- `CHANGELOG.md` - histórico do draft e do RC.
- `APOSTILA_QA_0.1.0.md` - QA semântico fechado; QA-9 do PDF canônico fechado; NotebookLM estático e live smoke concluídos.
- `NOTEBOOKLM_SMOKE_0.1.0.md` - evidência do smoke real, resultado `PASS_WITH_OBSERVATIONS` e melhorias de processo para os próximos SubjectPacks.
- análise de banca - `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`.
- matriz de autoria - `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Estado dos gates do pack

| gate | resultado |
|---|---|
| cobertura/rastreabilidade DP-01...DP-10 | `pass` |
| revisão normativa completa contra `SRC-B2-CP` | `pass_after_corrections` |
| didática/contrastes | `pass` |
| 30 questões autorais | `pass` - 30/30 |
| requisitos Q-LIT/Q-CMP/Q-CAS | `pass` |
| estrutura do corpus Markdown | `pass_for_markdown` |
| coerência com banca sem overfitting | `pass` |
| configuração do tutor `METODOLOGIA_NOTEBOOKLM.md` | `pass_static` |
| NotebookLM corpus QA estático | `pass_static` |
| NotebookLM smoke real | `pass_with_observations` |
| `python tools/verify.py` | `not_executed_current_environment` - impossibilidade DNS reavaliada em 2026-09-14 e não tratada como PASS |
| `APOSTILA.pdf` canônico | `pass_canonical_binary_identity` |

## Cobertura do release candidate

| coverage_id | recorte | conteúdo | prática |
|---|---|---|---|
| DP-01 | arts. 293-295 | `qa_pass` | `qa_pass` |
| DP-02 | arts. 296-305 | `qa_pass` | `qa_pass` |
| DP-03 | arts. 307-308 | `qa_pass` | `qa_pass` |
| DP-04 | art. 311-A | `qa_pass` | `qa_pass` |
| DP-05 | arts. 312-317, incluindo dispositivos intercalares | `qa_pass` | `qa_pass` |
| DP-06 | arts. 319-327, incluindo art. 319-A | `qa_pass` | `qa_pass` |
| DP-07 | arts. 328-333 | `qa_pass` | `qa_pass` |
| DP-08 | arts. 336 e 337 | `qa_pass` | `qa_pass` |
| DP-09 | arts. 339-347 | `qa_pass` | `qa_pass` |
| DP-10 | arts. 357 e 359 | `qa_pass` | `qa_pass` |

## Histórico da revisão

O `draft.2` resultou da revisão normativa integral e aprofundou formas do art. 293, §§ previdenciários do art. 297, penas dos arts. 300-301, peculato culposo, excesso de exação, art. 317, § 2º, arts. 321-325, resistência e aumentos dos arts. 342-344.

O `draft.3` resolveu as duas pendências semânticas restantes: Q12 passou a testar isoladamente o art. 311-A, § 2º; Q29 passou a usar atividade privada suspensa por decisão judicial e o corpo ganhou contraste explícito `art. 324 x art. 359`.

O `rc.1` não reabriu o conteúdo aprovado. Criou a configuração do tutor jurídico, sincronizou a identidade do pack e executou os QAs estáticos possíveis no runtime. O candidato preferido de PDF foi regenerado do Markdown congelado, reduzido a 17 páginas e auditado integralmente. Em `2026-09-14`, o upload manual no GitHub produziu o Git blob exato `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`, idêntico ao candidato local de SHA-256 `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`. A inspeção textual e visual foi novamente confirmada sobre o binário de identidade idêntica.

O smoke real do NotebookLM foi executado pelo usuário em `2026-09-14` e aprovado como `PASS_WITH_OBSERVATIONS`. Teste, Cartões, chat explicativo e treino interativo funcionaram adequadamente na amostra observada. O Mapa mental expôs IDs `DP-*` presentes nos próprios títulos do StudentContent, e a resposta sobre jurisprudência foi mais categórica do que o ideal antes de declarar o limite da fonte. Nenhum dos dois pontos foi classificado como erro jurídico ou bloqueio.

## Próximo estágio

`DIREITO-007` está `closed_with_observations`. O primeiro pipeline jurídico é considerado validado em nível de release candidate, sem necessidade de `rc.2` para as duas observações do smoke.

A produção pode seguir para `direito-processual-penal`, aplicando desde a primeira autoria duas melhorias aprendidas neste smoke:

1. não colocar coverage IDs ou outros identificadores de backoffice em títulos visíveis do StudentContent;
2. quando a fonte não sustentar afirmação sobre conteúdo externo, formular explicitamente o limite do corpus em vez de converter ausência na fonte em negativa universal.

A promoção formal de `direito-penal` de `0.1.0-rc.1` para uma versão final pode ser tratada separadamente, sem bloquear a continuação de B2. O gate determinístico continua `not_executed_current_environment` e não deve ser chamado de PASS.

## Regra de distribuição

Este pack está validado como release candidate, não como versão final sem sufixo. Pode ser usado no fluxo de estudo e serve como pipeline de referência para os próximos SubjectPacks, preservadas as observações registradas em `NOTEBOOKLM_SMOKE_0.1.0.md`.
