# MANIFEST - SubjectPack Direito Processual Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-processual-penal`  
**Pack version:** `0.1.0-rc.1`  
**Status:** `release_candidate_incomplete_pdf_transport_blocked`  
**RC date:** `2026-09-14`  
**PDF QA update:** `2026-09-15`

## Objetivo

Este SubjectPack cobre Direito Processual Penal no recorte do Edital de Abertura n.º 02/2025 e segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DPP-01...DPP-25` de `DIREITO_B2_COVERAGE_MATRIX.md`.

`DIREITO-009` aprovou semanticamente o conteúdo em `0.1.0-draft.2`. `DIREITO-010` promoveu somente a identidade do conteúdo congelado para `0.1.0-rc.1`, criou a configuração do tutor e executou QA estático. `DIREITO-011` gerou e auditou localmente um candidato de PDF, mas a publicação do binário exato no GitHub permanece bloqueada; por isso o pack continua incompleto e não é release final.

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

- `APOSTILA.md`: `0.1.0-rc.1`, conteúdo jurídico congelado do `0.1.0-draft.2`, 25 unidades, sem coverage IDs em títulos ou subtítulos, com 60 questões autorais A-E e gabarito comentado separado;
- `APOSTILA.pdf`: **não versionado no GitHub**. Existe candidato local auditado, mas ele não é canônico enquanto a identidade binária remota não for comprovada.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md`: `0.1.0-rc.1`, configuração persistente do tutor; não integra o corpus estudável.

### BackofficeArtifact

- `MANIFEST.md`: identidade, escopo e estado dos gates;
- `SOURCES.md`: proveniência e controle de versão;
- `CHANGELOG.md`: histórico editorial;
- `APOSTILA_QA_0.1.0.md`: QA semântico/normativo, QA estático do RC e estado de `DIREITO-011`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Rastreabilidade de cobertura

Os IDs abaixo são backoffice e não aparecem como rótulos estudáveis.

| coverage_id | recorte | estado semântico |
|---|---|---|
| DPP-01 | CPP 251-258 | qa_pass |
| DPP-02 | CPP 261-267 | qa_pass |
| DPP-03 | CPP 274 | qa_pass |
| DPP-04 | CPP 351-369 | qa_pass |
| DPP-05 | CPP 370-372 | qa_pass |
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
| revisão normativa integral | `pass_after_corrections` |
| didática/fluxos/contrastes | `pass` |
| prática autoral | `pass_60_of_60` |
| requisitos Q-LIT/Q-CMP/Q-CAS/Q-FLX/Q-VER/Q-FULL | `pass` |
| corpus Markdown | `pass_for_markdown` |
| configuração do tutor | `pass_static` |
| corpus/tutor NotebookLM estático | `pass_static` |
| identidade Markdown usada para o PDF | `pass_source_markdown_identity` |
| candidato local PDF - textual | `pass_text_readback` |
| candidato local PDF - visual | `pass_visual_28_of_28` |
| candidato local PDF - formato/metadados | `pass_local_candidate` |
| `APOSTILA.pdf` canônico | `blocked_not_versioned` |
| identidade binária GitHub | `not_proven` |
| NotebookLM smoke real | `not_started` |
| `python tools/verify.py` | `not_executed_current_environment`, não tratado como PASS |

## Candidato local de DIREITO-011

O candidato preferido auditado em `2026-09-15` possui:

- páginas: `28`;
- formato: `PDF 1.4`;
- página: `A4`;
- tamanho: `37.894 bytes`;
- SHA-256: `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob esperado: `4eabdacec7858120792cf792ca227335e41730b6`;
- fonte Markdown: Git blob `11a41d18ff3a8b03150923ec68d44087bded7267`;
- readback textual: `PASS`;
- inspeção visual: `28/28 PASS`.

Esses metadados descrevem **um candidato local auditado**, não um artefato canônico do repositório.

## Bloqueio de transporte

O conector GitHub disponível neste runtime não expõe upload binário por referência de arquivo local. Uma tentativa anterior de transporte com outro candidato produziu blob remoto diferente do esperado e foi rejeitada; esse blob não foi ligado a tree, commit, branch ou PR.

A política de `DIREITO-011` exige identidade binária comprovada. Portanto nenhum hash local é promovido a hash canônico e nenhum `PASS_CANONICAL_BINARY_IDENTITY` é declarado.

## Próximo estágio

`DIREITO-011` permanece aberto. A próxima operação deve transportar exatamente o candidato auditado para:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`

Depois, deve conferir o Git blob remoto contra `4eabdacec7858120792cf792ca227335e41730b6`. Somente se houver identidade exata o gate poderá avançar para o smoke real do NotebookLM.