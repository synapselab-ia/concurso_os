# MANIFEST — SubjectPack Direito Penal — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-penal`  
**Pack version:** `0.1.0-rc.1`  
**Status:** `release_candidate_incomplete`  
**RC date:** `2026-09-12`

## Objetivo

Este SubjectPack é a primeira implementação jurídica de B2. O conteúdo Markdown foi aprovado no QA editorial/normativo em `0.1.0-draft.3` e congelado para o release candidate. A identidade `0.1.0-rc.1` não representa release final: os gates que dependem do PDF canônico e do smoke real no NotebookLM continuam bloqueantes.

A autoria segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DP-01`…`DP-10` de `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Escopo oficial

Código Penal: `arts. 293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fonte normativa principal: `SRC-B2-CP` — Decreto-Lei n.º 2.848/1940, Código Penal, Planalto.

Baseline autoral: texto vigente em `2025-07-29`. O Gate 2 classificou o recorte como `cutoff_closed_no_scoped_drift`; alterações posteriores identificadas no Código Penal não atingem diretamente os dispositivos deste pack. O art. 338-A é posterior e está fora do recorte.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md` — `0.1.0-rc.1`; conteúdo editorial/normativo idêntico ao `0.1.0-draft.3`, salvo metadados de RC e nota de estado final.
- `APOSTILA.pdf` — **ainda não presente no repositório**. Um candidato local foi gerado a partir do `APOSTILA.md` congelado e passou por QA textual e visual, mas o runtime atual não dispõe de caminho confiável para publicar binário via conector GitHub. Esse candidato local tem `18` páginas A4, `48.593` bytes e SHA-256 `d190a2a73b6e6ad84d60d2a241ca8574ac4f34a75cfba1d8f643dbf95f9ea469`. Como o binário não é canônico no GitHub, o gate de PDF permanece aberto.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` — criado em `0.1.0-rc.1`; contém a configuração nativa do tutor jurídico e não integra o corpus estudável.

### BackofficeArtifact

- `SOURCES.md` — proveniência e regra de versão.
- `CHANGELOG.md` — histórico do draft e do RC.
- `APOSTILA_QA_0.1.0.md` — QA semântico fechado; QA estático de NotebookLM e QA do candidato local de PDF registrados; gates externos/canônicos ainda pendentes.
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
| configuração do tutor `METODOLOGIA_NOTEBOOKLM.md` | `pass_static` |
| NotebookLM corpus QA estático | `pass_static` |
| NotebookLM smoke real | `pending_user_smoke` |
| `python tools/verify.py` | `not_executed_current_environment` — DNS do runtime não resolve github.com |
| PDF local candidato | `pass_textual_visual_local_only` |
| `APOSTILA.pdf` canônico no GitHub | `not_published` |

## Cobertura do release candidate

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

O `rc.1` não reabriu o conteúdo aprovado. Criou a configuração do tutor jurídico, sincronizou a identidade do pack e executou os QAs estáticos possíveis no runtime. O candidato local de PDF foi pesquisável, teve leitura de texto confirmada e todas as 18 páginas renderizadas e inspecionadas sem clipping, sobreposição, glifos quebrados ou mistura acidental entre questões e gabarito. A ausência do binário no GitHub impede tratar essa verificação local como fechamento do gate canônico.

## Próximo estágio

`DIREITO-007` permanece aberto. Para fechá-lo:

1. publicar `APOSTILA.pdf` canônico a partir do conteúdo congelado, preferencialmente reproduzindo o candidato já auditado ou regenerando-o de forma equivalente;
2. repetir/confirmar QA textual e visual sobre o binário efetivamente versionado;
3. executar o smoke real no NotebookLM com somente `APOSTILA.pdf` como fonte e `METODOLOGIA_NOTEBOOKLM.md` na configuração nativa da conversa;
4. executar `python tools/verify.py` em ambiente com checkout/rede funcional;
5. somente depois decidir promoção a release final.

## Regra de distribuição

Enquanto o status for `release_candidate_incomplete`, este pack não deve ser tratado como release final nem substituir material validado no NotebookLM.