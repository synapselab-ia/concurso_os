# MANIFEST — SubjectPack Direito Penal — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-penal`  
**Pack version:** `0.1.0-draft.1`  
**Status:** `draft`  
**Draft date:** `2026-09-12`

## Objetivo

Este SubjectPack inicia a primeira implementação jurídica de B2. O draft deve ser autocontido para aprendizado e revisão, manter rastreabilidade ao recorte oficial e servir como corpus potencial do NotebookLM depois dos gates editoriais, normativos, de PDF e de uso real.

A autoria segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DP-01`…`DP-10` de `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Escopo oficial

Código Penal: `arts. 293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fonte normativa principal: `SRC-B2-CP` — Decreto-Lei n.º 2.848/1940, Código Penal, Planalto.

Baseline autoral: texto vigente em `2025-07-29`. O Gate 2 classificou o recorte como `cutoff_closed_no_scoped_drift`; alterações posteriores identificadas no Código Penal não atingem diretamente os dispositivos deste pack. O art. 338-A é posterior e está fora do recorte.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md` — presente em `0.1.0-draft.1`; draft completo de primeira passagem cobrindo DP-01…DP-10.
- `APOSTILA.pdf` — **não criado**; publicação binária bloqueada até QA editorial/normativo e preparação de release candidate.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` — ainda não criado neste pack. Quando necessário, deve registrar apenas a configuração do tutor e não integrar o corpus estudável.

### BackofficeArtifact

- `SOURCES.md` — presente; proveniência e regra de versão.
- `CHANGELOG.md` — presente; histórico do draft.
- análise de banca — referenciada centralmente por `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`.
- matriz de autoria — referenciada centralmente por `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.
- documento de QA específico — ainda não criado; é o próximo gate depois da primeira implementação.

## Cobertura do draft

| coverage_id | recorte | estado |
|---|---|---|
| DP-01 | arts. 293–295 | `drafted` |
| DP-02 | arts. 296–305 | `drafted` |
| DP-03 | arts. 307–308 | `drafted` |
| DP-04 | art. 311-A | `drafted` |
| DP-05 | arts. 312–317, incluindo dispositivos intercalares dentro do intervalo | `drafted` |
| DP-06 | arts. 319–327, incluindo art. 319-A | `drafted` |
| DP-07 | arts. 328–333 | `drafted` |
| DP-08 | arts. 336 e 337 | `drafted` |
| DP-09 | arts. 339–347 | `drafted` |
| DP-10 | arts. 357 e 359 | `drafted` |

O estado `drafted` não equivale a `qa` nem a `covered` de release. A promoção depende de revisão semântica e normativa registrada.

## Engenharia pedagógica aplicada

O draft organiza cada bloco por regra, elementos, hipótese, consequência, contraste e caso aplicado. Falsidades, crimes funcionais e crimes contra a Administração/Justiça são apresentados por diferenças decisivas entre tipos próximos. A prática final usa questões autorais A–E, separadas do gabarito comentado.

A análise histórica da banca é usada apenas como engenharia silenciosa de profundidade e distractores. O material não apresenta contagens históricas nem afirma probabilidades futuras.

## Próximos gates

1. QA de cobertura DP-01…DP-10 e rastreabilidade artigo a artigo;
2. QA normativo contra `SRC-B2-CP` e baseline `2025-07-29`;
3. QA didático, contrastes, mini-casos e questões autorais;
4. QA de redundância, terminologia e recuperação semântica;
5. criação de release candidate e `APOSTILA.pdf` somente depois dos gates de conteúdo;
6. smoke/QA de NotebookLM e QA textual/visual do PDF antes de release.

## Regra de distribuição

Enquanto o status for `draft`, este pack não deve ser tratado como release final nem substituir material validado no NotebookLM.
