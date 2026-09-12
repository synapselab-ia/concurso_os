# MANIFEST — SubjectPack Direito Penal — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-penal`  
**Pack version:** `0.1.0-draft.2`  
**Status:** `draft`  
**Draft date:** `2026-09-12`

## Objetivo

Este SubjectPack é a primeira implementação jurídica de B2. O Markdown deve ser autocontido para aprendizado e revisão, manter rastreabilidade ao recorte oficial e tornar-se corpus potencial do NotebookLM somente depois dos gates editoriais, normativos, de PDF e de uso real.

A autoria segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DP-01`…`DP-10` de `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Escopo oficial

Código Penal: `arts. 293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fonte normativa principal: `SRC-B2-CP` — Decreto-Lei n.º 2.848/1940, Código Penal, Planalto.

Baseline autoral: texto vigente em `2025-07-29`. O Gate 2 classificou o recorte como `cutoff_closed_no_scoped_drift`; alterações posteriores identificadas no Código Penal não atingem diretamente os dispositivos deste pack. O art. 338-A é posterior e está fora do recorte.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md` — `0.1.0-draft.2`; cobertura DP-01…DP-10 revisada normativamente e didaticamente; prática ainda contém duas pendências de QA.
- `APOSTILA.pdf` — **não criado**; publicação binária bloqueada enquanto o QA semântico não fechar.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` — ainda não criado. Quando necessário, deve registrar apenas a configuração do tutor e não integrar o corpus estudável.

### BackofficeArtifact

- `SOURCES.md` — proveniência e regra de versão.
- `CHANGELOG.md` — histórico do draft.
- `APOSTILA_QA_0.1.0.md` — QA semântico em andamento; QA-1/2/3/5 passaram, QA-4 falhou por Q12 e Q29.
- análise de banca — `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`.
- matriz de autoria — `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Estado dos gates do pack

| gate | resultado |
|---|---|
| cobertura/rastreabilidade DP-01…DP-10 | `pass` |
| revisão normativa completa contra `SRC-B2-CP` | `pass_after_corrections` |
| didática/contrastes | `pass` |
| 30 questões autorais | `fail` — Q12 `review_required`, Q29 `ambiguous` |
| estrutura do corpus Markdown | `pass_for_markdown_draft` |
| `python tools/verify.py` | `not_executed_current_environment` — DNS do runtime não resolve github.com |
| PDF | `not_created` |
| NotebookLM | `not_tested` |

## Cobertura do draft

| coverage_id | recorte | cobertura normativa | prática |
|---|---|---|---|
| DP-01 | arts. 293–295 | `qa_pass` | `qa_pass` |
| DP-02 | arts. 296–305 | `qa_pass` | `qa_pass` |
| DP-03 | arts. 307–308 | `qa_pass` | `qa_pass` |
| DP-04 | art. 311-A | `qa_pass` | `qa_blocked_q12` |
| DP-05 | arts. 312–317, incluindo dispositivos intercalares | `qa_pass` | `qa_pass` |
| DP-06 | arts. 319–327, incluindo art. 319-A | `qa_pass` | `qa_pass` |
| DP-07 | arts. 328–333 | `qa_pass` | `qa_pass` |
| DP-08 | arts. 336 e 337 | `qa_pass` | `qa_pass` |
| DP-09 | arts. 339–347 | `qa_pass` | `qa_pass` |
| DP-10 | arts. 357 e 359 | `qa_pass` | `qa_blocked_q29` |

O estado normativo `qa_pass` não autoriza release enquanto a prática do pack não estiver integralmente validada.

## Correções do `draft.2`

A revisão integral do recorte aprofundou pontos que estavam compactos no `draft.1`, incluindo formas do art. 293, §§ previdenciários do art. 297, penas dos arts. 300–301, peculato culposo, excesso de exação, corrupção passiva privilegiada, penas dos arts. 321–324, formas do art. 325, pena da resistência e aumentos dos arts. 342–344.

O corpo didático passou a conter três mini-casos por DP e manteve quadros comparativos nos blocos que exigem Q-CMP.

## Pendências reais

1. reformular Q12 para não depender de combinação não explicada entre art. 311-A §§ 2º e 3º;
2. reformular Q29 para evitar ambiguidade entre art. 324 e art. 359 e acrescentar contraste explícito `324 x 359` no corpo;
3. revalidar as duas questões, gabaritos e comentários;
4. somente depois disso encerrar o QA semântico e decidir sobre release candidate.

## Regra de distribuição

Enquanto o status for `draft`, este pack não deve ser tratado como release final nem substituir material validado no NotebookLM. PDF e smoke do NotebookLM permanecem bloqueados.