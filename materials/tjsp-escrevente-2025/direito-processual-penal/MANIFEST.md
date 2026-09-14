# MANIFEST - SubjectPack Direito Processual Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-processual-penal`  
**Pack version:** `0.1.0-draft.2`  
**Status:** `draft_semantic_qa_passed_ready_for_rc_preparation`  
**QA date:** `2026-09-14`

## Objetivo

Este SubjectPack cobre Direito Processual Penal no recorte do Edital de Abertura n.º 02/2025 e segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DPP-01...DPP-25` de `DIREITO_B2_COVERAGE_MATRIX.md`.

`DIREITO-009` revisou integralmente o primeiro draft e produziu `0.1.0-draft.2`. O conteúdo Markdown está semanticamente aprovado para preparação de release candidate. Isso ainda não transforma o pack em RC ou release e não autoriza presumir QA de PDF ou NotebookLM.

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

- `APOSTILA.md`: `0.1.0-draft.2`, 25 unidades, sem coverage IDs em títulos ou subtítulos, com 60 questões autorais A-E e gabarito comentado separado.
- `APOSTILA.pdf`: não criado neste gate.

### BackofficeArtifact

- `MANIFEST.md`: identidade, escopo e estado dos gates;
- `SOURCES.md`: proveniência e controle de versão;
- `CHANGELOG.md`: histórico editorial;
- `APOSTILA_QA_0.1.0.md`: QA semântico/normativo de DIREITO-009;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Rastreabilidade de cobertura

Os IDs abaixo são backoffice e não aparecem como rótulos estudáveis.

| coverage_id | recorte | estado após DIREITO-009 |
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

## Resultado de DIREITO-009

| gate | resultado |
|---|---|
| cobertura DPP-01...DPP-25 | `pass_after_corrections` |
| revisão normativa integral | `pass_after_corrections` |
| didática/fluxos/contrastes | `pass` |
| prática autoral | `pass_60_of_60` |
| requisitos Q-LIT/Q-CMP/Q-CAS/Q-FLX/Q-VER/Q-FULL | `pass` |
| corpus Markdown | `pass_for_markdown` |
| coerência com banca sem overfitting | `pass` |
| ausência de IDs de backoffice em títulos | `pass` |
| `python tools/verify.py` | `not_executed_current_environment` por falha DNS ao obter checkout canônico, não tratado como PASS |
| PDF | `not_created_by_design` |
| NotebookLM | `not_started` |

## Próximo estágio

O pack está autorizado a avançar para preparação de release candidate em gate separado. A próxima etapa deve criar/sincronizar a configuração do tutor, identidade e QA estático do corpus antes do pipeline de PDF e do smoke real do NotebookLM.
