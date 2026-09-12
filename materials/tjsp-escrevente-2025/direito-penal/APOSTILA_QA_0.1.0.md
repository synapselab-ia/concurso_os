# APOSTILA_QA_0.1.0 — Direito Penal — TJSP Escrevente 2025

**QA date:** `2026-09-12`  
**Object reviewed:** `APOSTILA.md` `0.1.0-draft.1` → `0.1.0-draft.2` → `0.1.0-draft.3`  
**Pack:** `direito-penal`  
**Overall semantic result:** `PASS`  
**Release candidate:** `authorized_not_created`

## 1. Escopo e método

Este QA executa `DIREITO-006`. O edital e a matriz de cobertura controlam o escopo; `SRC-B2-CP`, Código Penal oficial no Planalto, controla as afirmações normativas; a análise histórica da banca calibra apenas contraste, forma e aplicação.

Recorte auditado artigo por artigo:

`293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Baseline autoral: `2025-07-29`. O Gate 2 classifica `SRC-B2-CP` como `cutoff_closed_no_scoped_drift`; o art. `338-A`, posterior e fora do recorte, permaneceu excluído.

A revisão foi feita em duas passagens. A primeira promoveu `draft.1` a `draft.2`, aprofundando a cobertura literal e identificando duas pendências de prática, Q12 e Q29. A segunda reformulou esses itens, explicitou o contraste `art. 324 x art. 359` e produziu `draft.3`.

---

## 2. QA-1 — cobertura e rastreabilidade

**Resultado:** `PASS`

| coverage_id | recorte | resultado |
|---|---|---|
| DP-01 | 293–295 | PASS |
| DP-02 | 296–305 | PASS |
| DP-03 | 307–308 | PASS |
| DP-04 | 311-A | PASS |
| DP-05 | 312–317, incluindo 313-A/313-B | PASS |
| DP-06 | 319–327, incluindo 319-A | PASS |
| DP-07 | 328–333 | PASS |
| DP-08 | 336–337 | PASS |
| DP-09 | 339–347 | PASS |
| DP-10 | 357 e 359 | PASS |

Nenhum intervalo do edital desapareceu. Artigos fora do recorte — inclusive `338-A` — não foram absorvidos como conteúdo obrigatório.

---

## 3. QA-2 — exatidão normativa

**Resultado:** `PASS_AFTER_CORRECTIONS`

A revisão completa contra `SRC-B2-CP` levou, entre outros, aos seguintes ajustes antes do PASS:

- formas do art. 293, inclusive recebimento de boa-fé seguido de uso consciente;
- equiparações e hipóteses previdenciárias do art. 297;
- penas e distinções dos arts. 300–301;
- pena do peculato culposo e efeitos temporais da reparação;
- contraste `313-A x 313-B` e majorante por dano do art. 313-B;
- excesso de exação e corrupção passiva do § 2º;
- penas e elementos dos arts. 321–325;
- formas da resistência e aumentos dos arts. 342–344.

A fonte oficial foi reaberta na passagem final para os pontos que haviam gerado bloqueio de prática. O art. 311-A, § 2º, prevê reclusão de 2 a 6 anos e multa quando da ação ou omissão resulta dano à Administração; o § 3º trata separadamente do aumento de 1/3 para funcionário público. O art. 324 trata de função pública e continuação sem autorização após ciência oficial de exoneração, remoção, substituição ou suspensão. O art. 359 alcança função, atividade, direito, autoridade ou múnus de que houve suspensão ou privação por decisão judicial.

Depois das correções de `draft.3`, não foi identificada incompatibilidade material entre as afirmações auditadas e a fonte normativa do recorte.

---

## 4. QA-3 — didática e distinções

**Resultado:** `PASS`

A estrutura segue a família jurídica do protocolo: `regra → elementos → hipótese → consequência → contraste → caso → síntese`.

Os contrastes de maior risco ficaram explícitos, entre eles: `293 x 294`, material x ideológica, `304 x 305`, `307 x 308`, `313-A x 313-B`, concussão x corrupção passiva, prevaricação x condescendência, `324 x 359`, resistência x desobediência, `332 x 333`, `336 x 337`, `339 x 340`, `342 x 343` e `332 x 357`.

Cada DP contém três mini-casos. A engenharia histórica da banca permanece silenciosa: não há contagem de frequência nem previsão de cobrança no StudentContent.

---

## 5. QA-4 — prática autoral

**Resultado:** `PASS`

As 30 questões foram revisadas individualmente para: uma resposta defensável, cinco alternativas, ausência de ambiguidade involuntária, alinhamento ao syllabus, coerência entre gabarito e comentário e explicitação do elemento decisivo.

### Histórico das duas falhas corrigidas

**Q12 — DP-04.** No `draft.2`, a questão combinava resultado danoso (§ 2º) e qualidade funcional (§ 3º), tornando o item desnecessariamente dependente da combinação das duas regras. Em `draft.3`, a questão passou a testar isoladamente a consequência expressa do § 2º: dano à Administração → `reclusão de 2 a 6 anos e multa`. Resultado final: `PASS`.

**Q29 — DP-10.** No `draft.2`, “função suspensa por decisão judicial” aproximava art. 324 e art. 359. Em `draft.3`, o enunciado usa `atividade privada` suspensa por decisão judicial, isolando a literalidade do art. 359. O corpo didático também ganhou contraste explícito `324 x 359`, sem inventar regra jurisprudencial de concurso de normas. Resultado final: `PASS`.

### Contagem final

- `PASS`: `30/30`;
- `REVIEW_REQUIRED`: `0/30`;
- `FAIL`: `0/30`.

Os requisitos de prática `Q-LIT`, `Q-CMP` e `Q-CAS` do contrato DP-01…DP-10 estão atendidos no conjunto após as correções.

---

## 6. QA-5 — utilidade como corpus Markdown

**Resultado:** `PASS_FOR_MARKDOWN`

- títulos descrevem conteúdo real;
- regra, contraste e caso aparecem próximos;
- terminologia é consistente;
- tabelas são comparativas e compreensíveis em texto;
- perguntas e gabarito permanecem separados;
- o material funciona sem documentação interna do projeto;
- não há metadiscurso de banca no corpo estudável.

O PASS desta etapa não substitui o smoke real do NotebookLM. Esse teste pertence ao próximo pipeline, depois da preparação do release candidate e do PDF.

---

## 7. QA de banca e coerência interna

**Resultado:** `PASS`

Os formatos usados — literalidade controlada, distinção de requisito e mini-caso — são coerentes com os sinais empíricos do Gate 3, sem transformar frequência histórica em peso futuro. Não foi identificado overfitting às provas históricas.

A revisão final também não encontrou conflito interno material nas formulações dos contrastes que impeça a preparação do release candidate.

---

## 8. Gate determinístico

Tentativa em `2026-09-12`:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Consequência: `python tools/verify.py` não pôde ser executado em checkout canônico neste runtime. Resultado: `not_executed_current_environment`, **não** `PASS`, conforme DEC-0009.

---

## 9. Decisão de saída

| Gate | Resultado |
|---|---|
| QA-1 cobertura | PASS |
| QA-2 normativo | PASS_AFTER_CORRECTIONS |
| QA-3 didática/contrastes | PASS |
| QA-4 30 questões | PASS — 30/30 |
| requisitos Q-LIT/Q-CMP/Q-CAS | PASS |
| QA-5 corpus Markdown | PASS_FOR_MARKDOWN |
| coerência com banca | PASS |
| gate determinístico | NOT_EXECUTED_CURRENT_ENVIRONMENT |
| PDF | NOT_CREATED |
| NotebookLM live | NOT_TESTED |

**DIREITO-006: `closed`.**

O conteúdo Markdown de `direito-penal` está semanticamente aprovado para avançar ao estágio de **release candidate**, mas ainda não é release. Os próximos gates devem criar a configuração do tutor, produzir e auditar o PDF pesquisável e executar o QA aplicável no NotebookLM. Nenhum desses gates posteriores é presumido como PASS.