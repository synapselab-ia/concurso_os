# MANIFEST — SubjectPack Direito Penal — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-penal`  
**Pack version:** `0.1.0-draft.3`  
**Status:** `draft`  
**Draft date:** `2026-09-12`

## Objetivo

Este SubjectPack é a primeira implementação jurídica de B2. O Markdown é autocontido para aprendizado e revisão, mantém rastreabilidade ao recorte oficial e foi aprovado no QA editorial/normativo de conteúdo. Ele só se torna material de distribuição depois dos gates de release candidate, PDF e NotebookLM.

A autoria segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DP-01`…`DP-10` de `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Escopo oficial

Código Penal: `arts. 293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fonte normativa principal: `SRC-B2-CP` — Decreto-Lei n.º 2.848/1940, Código Penal, Planalto.

Baseline autoral: texto vigente em `2025-07-29`. O Gate 2 classificou o recorte como `cutoff_closed_no_scoped_drift`; alterações posteriores identificadas no Código Penal não atingem diretamente os dispositivos deste pack. O art. 338-A é posterior e está fora do recorte.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md` — `0.1.0-draft.3`; DP-01…DP-10 revisados normativamente, didaticamente e na prática autoral.
- `APOSTILA.pdf` — **não criado**; publicação binária pertence ao próximo pipeline.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` — ainda não criado. Deve registrar a configuração do tutor e não integrar o corpus estudável.

### BackofficeArtifact

- `SOURCES.md` — proveniência e regra de versão.
- `CHANGELOG.md` — histórico do draft.
- `APOSTILA_QA_0.1.0.md` — `DIREITO-006` fechado; conteúdo Markdown aprovado para avançar a release candidate.
- análise de banca — `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`.
- matriz de autoria — `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Estado dos gates do pack

| gate | resultado |
|---|---|
| cobertura/rastreabilidade DP-01…DP-10 | `pass` |
| revisão normativa completa contra `SRC-B2-CP` | `pass_after_corrections` |
| didática/contrastes | `pass` |
| 30 questões autorais | `pass` — 30/30 |
| requisitos Q-LIT/Q-CMP/Q-CAS | `pass` |
| estrutura do corpus Markdown | `pass_for_markdown` |
| coerência com banca sem overfitting | `pass` |
| `python tools/verify.py` | `not_executed_current_environment` — DNS do runtime não resolve github.com |
| PDF | `not_created` |
| NotebookLM | `not_tested` |

## Cobertura do draft

| coverage_id | recorte | conteúdo | prática |
|---|---|---|---|
| DP-01 | arts. 293–295 | `qa_pass` | `qa_pass` |
| DP-02 | arts. 296–305 | `qa_pass` | `qa_pass` |
| DP-03 | arts. 307–308 | `qa_pass` | `qa_pass` |
| DP-04 | art. 311-A | `qa_pass` | `qa_pass` |
| DP-05 | arts. 312–317, incluindo dispositivos intercalares | `qa_pass` | `qa_pass` |
| DP-06 | arts. 319–327, incluindo art. 319-A | `qa_pass` | `qa_pass` |
| DP-07 | arts. 328–333 | `qa_pass` | `qa_pass` |
| DP-08 | arts. 336 e 337 | `qa_pass` | `qa_pass` |
| DP-09 | arts. 339–347 | `qa_pass` | `qa_pass` |
| DP-10 | arts. 357 e 359 | `qa_pass` | `qa_pass` |

## Histórico da revisão

O `draft.2` resultou da revisão normativa integral e aprofundou formas do art. 293, §§ previdenciários do art. 297, penas dos arts. 300–301, peculato culposo, excesso de exação, art. 317, § 2º, arts. 321–325, resistência e aumentos dos arts. 342–344.

O `draft.3` resolveu as duas pendências semânticas restantes: Q12 passou a testar isoladamente o art. 311-A, § 2º; Q29 passou a usar atividade privada suspensa por decisão judicial e o corpo ganhou contraste explícito `art. 324 x art. 359`.

## Próximo estágio

O conteúdo está autorizado a entrar em **preparação de release candidate**, sem promoção automática de versão final. O próximo pipeline deve:

1. criar `METODOLOGIA_NOTEBOOKLM.md` conforme a arquitetura canônica;
2. estabilizar identidade/versionamento do release candidate;
3. gerar `APOSTILA.pdf` pesquisável;
4. executar QA textual e visual do PDF;
5. executar o QA aplicável no NotebookLM;
6. somente depois decidir promoção a release.

## Regra de distribuição

Enquanto o status for `draft`, este pack não deve ser tratado como release final nem substituir material validado no NotebookLM.