# DIREITO B2 — Plano canônico de autoria

**Competition:** `tjsp-escrevente-2025`  
**Syllabus block:** `B2 — Conhecimentos em Direito`  
**Authority:** `SRC-TJSP-EDITAL-2025-02`  
**Status:** Gates 1–6 fechados para o primeiro pipeline; `direito-penal` autorizado a preparar release candidate  

## Objetivo

Transformar o bloco B2 do edital em unidades de autoria, fonte e QA que possam ser mantidas sem perder a unidade estatística da prova.

O edital continua tratando **Conhecimentos em Direito como um único bloco de 30 questões**. A divisão abaixo é exclusivamente editorial e pedagógica; não altera o blueprint do concurso nem autoriza inferir distribuição fixa de questões entre os subdomínios.

## Decisão de fronteira

B2 será entregue como **seis SubjectPacks**, um para cada domínio explicitamente separado no edital:

1. `direito-penal`;
2. `direito-processual-penal`;
3. `direito-processual-civil`;
4. `direito-constitucional`;
5. `direito-administrativo`;
6. `legislacao-interna`.

A decisão é registrada em `00_SYSTEM/DECISION_LOG.md` como DEC-0019.

## Escopo canônico por pack

### `direito-penal`

Código Penal: arts. 293 a 305; 307; 308; 311-A; 312 a 317; 319 a 333; 336 e 337; 339 a 347; 357 e 359.

### `direito-processual-penal`

Código de Processo Penal: arts. 251 a 258; 261 a 267; 274; 351 a 372; 394 a 497; 531 a 538; 541 a 548; 574 a 667.  
Lei n.º 9.099/1995: arts. 60 a 83; 88 e 89.

### `direito-processual-civil`

Código de Processo Civil: arts. 144 a 155; 188 a 275; 294 a 311; 318 a 538; 994 a 1026.  
Lei n.º 9.099/1995: arts. 3º a 19.  
Lei n.º 12.153/2009: integral.

### `direito-constitucional`

Constituição Federal: Título II, Capítulos I, II e III; Título III, Capítulo VII, Seções I e II; art. 92.

### `direito-administrativo`

Lei Estadual n.º 10.261/1968: arts. 1º a 86; 171 a 175; 239 a 323.  
Lei Federal n.º 8.429/1992: integral.

### `legislacao-interna`

- Resolução TJSP n.º 850/2021;
- Resolução TJSP n.º 963/2025;
- Lei Complementar Estadual n.º 1.111/2010;
- Regimento Interno do TJSP;
- Normas da Corregedoria Geral da Justiça, exatamente nos recortes impressos no edital:
  - Tomo I — Capítulo II — Seção I — subseções I e II;
  - Tomo I — Capítulo III — Seções I, II, V, VI e VII;
  - Tomo I — Capítulo III — Seção VIII — subseções I, II e III;
  - Tomo I — Capítulo III — Seções IX a XIX;
  - Tomo I — Capítulo XI — Seções I, IV e V;
  - Tomo I — Capítulo XI — Seções I a VII.

### Anomalia textual do edital

O último par de recortes das Normas da Corregedoria referencia o **Capítulo XI duas vezes**. O repositório preserva essa literalidade porque não foi localizada fonte oficial inequívoca que autorize corrigir o segundo apontamento. Para cobertura, a segunda linha literal (`Seções I a VII`) engloba as seções I, IV e V da primeira; essa relação de inclusão não altera a referência oficial.

## Gate 2 — versão normativa fechada

`competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` fecha a versão-base de todas as fontes em `2025-07-29` e separa drift posterior.

Pontos de manutenção que não podem ser perdidos na autoria:

- CPP: art. 584, § 4º sofreu alteração posterior pela Lei n.º 15.358/2026;
- CPC: alterações posteriores em arts. 196, 529-A e 998, com vigências distintas;
- Constituição: EC n.º 138/2025 alterou art. 37, XVI, `b` após o cutoff;
- Lei Estadual n.º 10.261/1968: Lei n.º 18.473/2026 atingiu o art. 78 dentro do recorte;
- LC Estadual n.º 1.111/2010: Lei n.º 18.373/2025 e LC n.º 1.441/2026 são posteriores ao cutoff;
- Regimento Interno: baseline inclui Assento n.º 591/2025 e exclui 592–596;
- NSCGJ: baseline dos recortes literais exclui alterações posteriores identificadas, incluindo Provimentos CG n.º 30/2025 e 04/2026 no Capítulo XI.

Para `direito-penal`, `SRC-B2-CP` está fechado como `cutoff_closed_no_scoped_drift`; o art. 338-A posterior não pertence ao recorte.

## Gate 3 — banca fechada

`competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md` classifica de forma reproduzível **150 questões de Direito** das provas de 2021, 2023, 2024 e 2025.

Sinais permitidos para engenharia da autoria:

- coexistência de literalidade normativa e aplicação curta;
- contraste de tipos/institutos próximos;
- troca de requisito, sujeito, prazo, competência, exceção e recurso como padrões de distractor;
- necessidade de fluxos procedimentais, tabelas regra/exceção e mini-casos;
- legislação interna exige tabelas operacionais e controle estrito de versão.

A distribuição histórica é descritiva, não preditiva, e não altera o syllabus vigente.

## Gate 4 — matriz fechada

`competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md` é o contrato de cobertura/autoria comum de B2.

O fechamento do Gate 4 confirma:

- seis matrizes independentes, uma por SubjectPack;
- 100% dos recortes do syllabus ligados a `coverage_id` verificável;
- todas as fontes do Gate 2 associadas às unidades pertinentes;
- riscos de confusão e sinais de banca convertidos em decisões pedagógicas;
- drift normativo preso às unidades afetadas;
- duplicidade oficial das NSCGJ preservada sem correção inferida;
- requisitos de prática e QA definidos por unidade.

Para `direito-penal`, o contrato de primeira autoria é `DP-01` a `DP-10`.

## Gate 5 — primeira implementação de `direito-penal`

A branch `content/direito-penal-v0.1-draft` estabeleceu o workspace `materials/tjsp-escrevente-2025/direito-penal/` com `APOSTILA.md`, `SOURCES.md`, `MANIFEST.md` e `CHANGELOG.md`. O `0.1.0-draft.1` cobriu DP-01…DP-10, incluiu contrastes, mini-casos e 30 questões autorais A–E, e foi mergeado através do PR 20.

## Gate 6 — QA do primeiro pack

A branch `qa/direito-penal-v0.1` executou a revisão semântica prevista em `DIREITO-006` e produziu `0.1.0-draft.3`.

Resultado registrado em `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md`:

- cobertura DP-01…DP-10: `pass`;
- revisão normativa completa contra `SRC-B2-CP`: `pass_after_corrections`;
- didática e contrastes: `pass`;
- 30 questões autorais: `pass` — 30/30;
- requisitos `Q-LIT`, `Q-CMP` e `Q-CAS`: `pass`;
- corpus Markdown: `pass_for_markdown`;
- coerência com banca sem overfitting: `pass`;
- gate determinístico: `not_executed_current_environment`, por falha de DNS para `github.com` — não tratado como PASS;
- PDF e NotebookLM: ainda não executados.

O QA corrigiu as duas pendências finais da prática: Q12 passou a isolar o art. 311-A, § 2º; Q29 passou a isolar o art. 359 por meio de atividade privada suspensa judicialmente, com contraste explícito `art. 324 x art. 359` no corpo.

O fechamento do Gate 6 autoriza **preparação de release candidate**. Não autoriza release final nem presume QA de PDF/NotebookLM.

## Ordem de produção

1. **concluído** — inventário e versão de todas as fontes de B2;
2. **concluído** — análise histórica reproduzível de 2021/2023/2024/2025;
3. **concluído** — matriz de cobertura/autoria dos seis packs;
4. **concluído como draft** — primeira implementação de `direito-penal`;
5. **concluído** — QA editorial/normativo do Markdown de `direito-penal`;
6. **próximo** — preparar release candidate, PDF e QA NotebookLM de `direito-penal`;
7. após validar o primeiro pipeline jurídico completo, seguir para `direito-processual-penal`;
8. `direito-processual-civil`;
9. `direito-constitucional`;
10. `direito-administrativo`;
11. `legislacao-interna`.

Cada pack deve usar a matriz como contrato e passar pelo fluxo de autoria/QA do `APOSTILA_AUTHORING_PROTOCOL.md` antes de release.

## Gates

| Gate | Estado | Critério |
|---|---|---|
| 1 — fronteira | `closed` | seis SubjectPacks definidos e decisão registrada |
| 2 — fontes/versões | `closed` | inventário oficial, cutoff, proveniência e drift normativo fechados em `DIREITO_SOURCES.md` |
| 3 — banca | `closed` | 150 questões de Direito classificadas em `DIREITO_B2_BANCA_ANALYSIS.md` |
| 4 — matriz | `closed` | todos os recortes do syllabus rastreados sem lacunas em `DIREITO_B2_COVERAGE_MATRIX.md` |
| 5 — primeira implementação | `closed_as_draft` | workspace e primeira passagem DP-01…DP-10 criados e mergeados |
| 6 — QA do primeiro pack | `closed` | conteúdo, norma, didática, prática e corpus Markdown aprovados; gate determinístico documentado como não executável neste runtime |
| 7 — release candidate | `pending` | metodologia/configuração do tutor, PDF e QA NotebookLM/PDF antes de release |

## Regra de autoridade

O edital vigente determina escopo e prevalece sobre provas históricas. Provas históricas servem apenas para calibrar profundidade, operação cognitiva, distinções, armadilhas e prática, conforme DEC-0010 e `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`.