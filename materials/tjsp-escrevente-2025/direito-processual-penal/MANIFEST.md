# MANIFEST - SubjectPack Direito Processual Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-processual-penal`  
**Pack version:** `0.1.0-rc.1`  
**Status:** `release_candidate_incomplete`  
**RC date:** `2026-09-14`

## Objetivo

Este SubjectPack cobre Direito Processual Penal no recorte do Edital de Abertura n.º 02/2025 e segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DPP-01...DPP-25` de `DIREITO_B2_COVERAGE_MATRIX.md`.

`DIREITO-009` aprovou semanticamente o conteúdo em `0.1.0-draft.2`. `DIREITO-010` promove somente a identidade do conteúdo congelado para `0.1.0-rc.1`, cria a configuração do tutor e executa QA estático. Não houve reabertura semântica do conteúdo jurídico. O pack ainda não é release final e não presume PDF canônico nem smoke real do NotebookLM.

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

- `APOSTILA.md`: `0.1.0-rc.1`, conteúdo jurídico congelado do `0.1.0-draft.2`, 25 unidades, sem coverage IDs em títulos ou subtítulos, com 60 questões autorais A-E e gabarito comentado separado.
- `APOSTILA.pdf`: ainda não criado/versionado para este RC.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md`: `0.1.0-rc.1`, criada como configuração persistente do tutor; não integra o corpus estudável.

### BackofficeArtifact

- `MANIFEST.md`: identidade, escopo e estado dos gates;
- `SOURCES.md`: proveniência e controle de versão;
- `CHANGELOG.md`: histórico editorial;
- `APOSTILA_QA_0.1.0.md`: QA semântico/normativo de `DIREITO-009` e QA estático do RC em `DIREITO-010`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Rastreabilidade de cobertura

Os IDs abaixo são backoffice e não aparecem como rótulos estudáveis.

| coverage_id | recorte | estado semântico do conteúdo congelado |
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
| coerência com banca sem overfitting | `pass` |
| ausência de IDs de backoffice em títulos | `pass` |
| configuração do tutor | `pass_static` |
| corpus/tutor NotebookLM estático | `pass_static` |
| NotebookLM smoke real | `not_started` |
| `python tools/verify.py` | `not_executed_current_environment` por falha DNS ao obter checkout canônico, não tratado como PASS |
| `APOSTILA.pdf` canônico | `not_created` |

## QA estático de DIREITO-010

O release candidate foi revisado estaticamente sob a arquitetura de corpus limpo:

```text
fonte estudável -> APOSTILA.pdf, quando validado
configuração da conversa -> METODOLOGIA_NOTEBOOKLM.md
backoffice -> GitHub/ChatGPT
```

Foi confirmado que:

- a promoção de `draft.2` para `rc.1` altera identidade/status, sem mudança jurídica do corpo aprovado;
- `METODOLOGIA_NOTEBOOKLM.md` orienta uso exclusivo das fontes selecionadas como base factual/didática;
- a configuração distingue regra expressa, explicação didática e aplicação hipotética;
- jurisprudência, doutrina e atualização normativa ausentes do corpus não podem ser inventadas;
- ausência de informação é formulada como limite do corpus, não como negativa universal;
- treino interativo usa uma questão por vez e não antecipa gabarito;
- correção privilegia sujeito, etapa, prazo, competência, requisito, cabimento, efeito e exceção;
- a configuração não exige `MANIFEST`, `SOURCES`, QA, matriz ou análise de banca como fontes do NotebookLM;
- o StudentContent continua sem `DPP-*` em títulos ou subtítulos;
- perguntas e gabarito permanecem estruturalmente separados.

## Próximo estágio

O `0.1.0-rc.1` está preparado como release candidate incompleto. A etapa seguinte deve gerar `APOSTILA.pdf` exclusivamente a partir do Markdown congelado do RC e executar QA textual/visual antes de qualquer uso canônico no NotebookLM. Depois do PDF canônico validado, o smoke real do NotebookLM deve ser executado sem presumir resultados.
