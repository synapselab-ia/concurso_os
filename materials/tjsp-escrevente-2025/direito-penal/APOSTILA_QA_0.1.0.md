# APOSTILA_QA_0.1.0 — Direito Penal — TJSP Escrevente 2025

**QA date:** `2026-09-12`  
**Object reviewed:** `APOSTILA.md` `0.1.0-draft.1` → `0.1.0-draft.2` → `0.1.0-draft.3` → `0.1.0-rc.1`  
**Pack:** `direito-penal`  
**Overall semantic result:** `PASS`  
**Release candidate:** `created_incomplete`

## 1. Escopo e método

Este QA executou `DIREITO-006` e foi estendido em `DIREITO-007` sem reabrir o conteúdo aprovado. O edital e a matriz de cobertura controlam o escopo; `SRC-B2-CP`, Código Penal oficial no Planalto, controla as afirmações normativas; a análise histórica da banca calibra apenas contraste, forma e aplicação.

Recorte auditado artigo por artigo:

`293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Baseline autoral: `2025-07-29`. O Gate 2 classifica `SRC-B2-CP` como `cutoff_closed_no_scoped_drift`; o art. `338-A`, posterior e fora do recorte, permaneceu excluído.

A revisão semântica foi feita em duas passagens. A primeira promoveu `draft.1` a `draft.2`, aprofundando a cobertura literal e identificando duas pendências de prática, Q12 e Q29. A segunda reformulou esses itens, explicitou o contraste `art. 324 x art. 359` e produziu `draft.3`. O `rc.1` mantém o conteúdo aprovado e altera somente identidade/status, configuração do tutor e registros de QA do candidato.

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

Nenhum intervalo do edital desapareceu. Artigos fora do recorte, inclusive `338-A`, não foram absorvidos como conteúdo obrigatório.

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

Depois das correções de `draft.3`, não foi identificada incompatibilidade material entre as afirmações auditadas e a fonte normativa do recorte. O `rc.1` não modifica essas afirmações.

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

---

## 7. QA de banca e coerência interna

**Resultado:** `PASS`

Os formatos usados, literalidade controlada, distinção de requisito e mini-caso, são coerentes com os sinais empíricos do Gate 3, sem transformar frequência histórica em peso futuro. Não foi identificado overfitting às provas históricas.

A revisão final também não encontrou conflito interno material nas formulações dos contrastes que impeça a preparação do release candidate.

---

## 8. Gate determinístico de DIREITO-006

Tentativa em `2026-09-12`:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Consequência: `python tools/verify.py` não pôde ser executado em checkout canônico neste runtime. Resultado: `not_executed_current_environment`, **não** `PASS`, conforme DEC-0009.

---

## 9. DIREITO-007 — QA-7 NotebookLM estático

**Resultado:** `PASS_STATIC`

Arquitetura auditada:

```text
fonte estudável
→ APOSTILA.pdf

configuração da conversa
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Verificações estáticas:

- `METODOLOGIA_NOTEBOOKLM.md` foi criada como `ConversationInstruction`, não como matéria;
- a configuração orienta o tutor a usar somente as fontes selecionadas como base factual e didática;
- texto legal/regra da fonte, explicação didática e aplicação hipotética são distinguidos;
- jurisprudência e doutrina ausentes da fonte não podem ser inventadas para preencher lacunas;
- treino interativo mantém uma questão por vez e veda antecipação de gabarito;
- correção privilegia artigo, elemento textual decisivo e contraste entre tipos próximos;
- a apostila contém definições, regras, exceções, contrastes, mini-casos, sínteses e prática suficientes para Teste, Cartões, Mapa mental e chat;
- nenhum trecho estudável depende de `MANIFEST`, `SOURCES`, análise de banca ou outro documento de backoffice para fazer sentido.

**Smoke real:** `PENDING_USER_SMOKE`. A interface do NotebookLM não está disponível neste runtime. Nenhuma interação externa foi presumida como executada.

---

## 10. DIREITO-007 — QA-9 PDF candidato local

**Resultado:** `PASS_LOCAL_ONLY_CANONICAL_PENDING`

Um candidato local foi gerado a partir do `APOSTILA.md` congelado do `rc.1`. O candidato preferido, produzido em A4, apresentou:

- páginas: `18`;
- tamanho: `48.593 bytes`;
- SHA-256: `d190a2a73b6e6ad84d60d2a241ca8574ac4f34a75cfba1d8f643dbf95f9ea469`;
- PDF 1.4;
- texto pesquisável e extraível.

### Readback textual

Foram recuperados no arquivo, entre outros, os marcadores:

- `Direito Penal`;
- `Unidade 1` e `Unidade 10`;
- `Gabarito comentado`;
- `art. 359`;
- `§`;
- `Código Penal`;
- `Síntese final de recuperação`.

### Inspeção visual

As 18 páginas foram renderizadas a 150 dpi e inspecionadas integralmente. Não foram observados:

- clipping de texto;
- sobreposição de elementos;
- glifos quebrados;
- acentos ou símbolos jurídicos corrompidos;
- quebra visual impeditiva em tabelas;
- mistura acidental entre questões e gabarito.

O gabarito começa em página separada no candidato auditado.

### Limite canônico

`APOSTILA.pdf` **não está publicado no GitHub** nesta passagem. O conector disponível aceita gravação textual, mas não oferece caminho confiável para transferir o artefato binário local já auditado para o repositório. Por isso, o hash acima identifica somente o candidato local e **não fecha o gate do PDF canônico**. Quando o binário for efetivamente versionado, o QA textual/visual precisa ser confirmado sobre aquele arquivo exato ou sobre regeneração equivalente com novo hash registrado.

---

## 11. DIREITO-007 — gate determinístico

Nova checagem no runtime continua bloqueada por DNS:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Sem checkout canônico, executar `python tools/verify.py` em diretório parcial seria falsa validação. Resultado mantido: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, não `PASS`.

---

## 12. Decisão de saída atual

| Gate | Resultado |
|---|---|
| QA-1 cobertura | PASS |
| QA-2 normativo | PASS_AFTER_CORRECTIONS |
| QA-3 didática/contrastes | PASS |
| QA-4 30 questões | PASS — 30/30 |
| requisitos Q-LIT/Q-CMP/Q-CAS | PASS |
| QA-5 corpus Markdown | PASS_FOR_MARKDOWN |
| coerência com banca | PASS |
| configuração do tutor | PASS_STATIC |
| QA-7 NotebookLM estático | PASS_STATIC |
| QA-7 NotebookLM live | PENDING_USER_SMOKE |
| QA-9 PDF candidato local | PASS_LOCAL_ONLY_CANONICAL_PENDING |
| `APOSTILA.pdf` canônico | NOT_PUBLISHED |
| gate determinístico | NOT_EXECUTED_CURRENT_ENVIRONMENT |

**DIREITO-006: `closed`.**

**DIREITO-007: `open`.**

O `0.1.0-rc.1` existe como release candidate incompleto. O conteúdo jurídico permanece semanticamente aprovado, mas não pode ser promovido a release final enquanto o PDF canônico, o smoke real do NotebookLM e o gate determinístico aplicável não refletirem execução real.