# MANIFEST - SubjectPack Direito Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-penal`  
**Pack version:** `0.1.0-rc.1`  
**Status:** `release_candidate_incomplete`  
**RC date:** `2026-09-12`

## Objetivo

Este SubjectPack é a primeira implementação jurídica de B2. O conteúdo Markdown foi aprovado no QA editorial/normativo em `0.1.0-draft.3` e congelado para o release candidate. A identidade `0.1.0-rc.1` não representa release final: o PDF canônico já foi publicado e auditado, mas o smoke real no NotebookLM e a reavaliação do gate determinístico continuam bloqueantes.

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
- `APOSTILA_QA_0.1.0.md` - QA semântico fechado; QA-9 do PDF canônico fechado; NotebookLM estático concluído; smoke real e gate determinístico ainda pendentes.
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
| NotebookLM smoke real | `pending_user_smoke` |
| `python tools/verify.py` | `not_executed_current_environment` - DNS do runtime não resolve github.com |
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

## Próximo estágio

`DIREITO-007` permanece aberto. Para fechá-lo:

1. executar o smoke real no NotebookLM com somente `APOSTILA.pdf` como fonte e `METODOLOGIA_NOTEBOOKLM.md` na configuração nativa da conversa;
2. executar `python tools/verify.py` em ambiente com checkout/rede funcional ou reavaliar formalmente a impossibilidade conforme DEC-0009;
3. sincronizar os registros finais de QA e continuidade;
4. somente depois decidir promoção a release final.

## Regra de distribuição

Enquanto o status for `release_candidate_incomplete`, este pack não deve ser tratado como release final nem substituir material validado no NotebookLM.