# APOSTILA_QA_0.1.0 - Direito Penal - TJSP Escrevente 2025

**QA date:** `2026-09-14`  
**Object reviewed:** `APOSTILA.md` `0.1.0-draft.1` -> `0.1.0-draft.2` -> `0.1.0-draft.3` -> `0.1.0-rc.1`  
**Pack:** `direito-penal`  
**Overall semantic result:** `PASS`  
**Release candidate:** `validated_with_observations`

## 1. Escopo e método

Este QA executou `DIREITO-006` e foi estendido em `DIREITO-007` sem reabrir o conteúdo aprovado. O edital e a matriz de cobertura controlam o escopo; `SRC-B2-CP`, Código Penal oficial no Planalto, controla as afirmações normativas; a análise histórica da banca calibra apenas contraste, forma e aplicação.

Recorte auditado artigo por artigo:

`293-305; 307; 308; 311-A; 312-317; 319-333; 336; 337; 339-347; 357; 359`.

Baseline autoral: `2025-07-29`. O Gate 2 classifica `SRC-B2-CP` como `cutoff_closed_no_scoped_drift`; o art. `338-A`, posterior e fora do recorte, permaneceu excluído.

A revisão semântica foi feita em duas passagens. A primeira promoveu `draft.1` a `draft.2`, aprofundando a cobertura literal e identificando duas pendências de prática, Q12 e Q29. A segunda reformulou esses itens, explicitou o contraste `art. 324 x art. 359` e produziu `draft.3`. O `rc.1` mantém o conteúdo aprovado e altera somente identidade/status, configuração do tutor e registros de QA do candidato.

---

## 2. QA-1 - cobertura e rastreabilidade

**Resultado:** `PASS`

| coverage_id | recorte | resultado |
|---|---|---|
| DP-01 | 293-295 | PASS |
| DP-02 | 296-305 | PASS |
| DP-03 | 307-308 | PASS |
| DP-04 | 311-A | PASS |
| DP-05 | 312-317, incluindo 313-A/313-B | PASS |
| DP-06 | 319-327, incluindo 319-A | PASS |
| DP-07 | 328-333 | PASS |
| DP-08 | 336-337 | PASS |
| DP-09 | 339-347 | PASS |
| DP-10 | 357 e 359 | PASS |

Nenhum intervalo do edital desapareceu. Artigos fora do recorte, inclusive `338-A`, não foram absorvidos como conteúdo obrigatório.

---

## 3. QA-2 - exatidão normativa

**Resultado:** `PASS_AFTER_CORRECTIONS`

A revisão completa contra `SRC-B2-CP` levou, entre outros, aos seguintes ajustes antes do PASS:

- formas do art. 293, inclusive recebimento de boa-fé seguido de uso consciente;
- equiparações e hipóteses previdenciárias do art. 297;
- penas e distinções dos arts. 300-301;
- pena do peculato culposo e efeitos temporais da reparação;
- contraste `313-A x 313-B` e majorante por dano do art. 313-B;
- excesso de exação e corrupção passiva do § 2º;
- penas e elementos dos arts. 321-325;
- formas da resistência e aumentos dos arts. 342-344.

A fonte oficial foi reaberta na passagem final para os pontos que haviam gerado bloqueio de prática. O art. 311-A, § 2º, prevê reclusão de 2 a 6 anos e multa quando da ação ou omissão resulta dano à Administração; o § 3º trata separadamente do aumento de 1/3 para funcionário público. O art. 324 trata de função pública e continuação sem autorização após ciência oficial de exoneração, remoção, substituição ou suspensão. O art. 359 alcança função, atividade, direito, autoridade ou múnus de que houve suspensão ou privação por decisão judicial.

Depois das correções de `draft.3`, não foi identificada incompatibilidade material entre as afirmações auditadas e a fonte normativa do recorte. O `rc.1` não modifica essas afirmações.

---

## 4. QA-3 - didática e distinções

**Resultado:** `PASS`

A estrutura segue a família jurídica do protocolo: `regra -> elementos -> hipótese -> consequência -> contraste -> caso -> síntese`.

Os contrastes de maior risco ficaram explícitos, entre eles: `293 x 294`, material x ideológica, `304 x 305`, `307 x 308`, `313-A x 313-B`, concussão x corrupção passiva, prevaricação x condescendência, `324 x 359`, resistência x desobediência, `332 x 333`, `336 x 337`, `339 x 340`, `342 x 343` e `332 x 357`.

Cada DP contém três mini-casos. A engenharia histórica da banca permanece silenciosa: não há contagem de frequência nem previsão de cobrança no StudentContent.

---

## 5. QA-4 - prática autoral

**Resultado:** `PASS`

As 30 questões foram revisadas individualmente para: uma resposta defensável, cinco alternativas, ausência de ambiguidade involuntária, alinhamento ao syllabus, coerência entre gabarito e comentário e explicitação do elemento decisivo.

### Histórico das duas falhas corrigidas

**Q12 - DP-04.** No `draft.2`, a questão combinava resultado danoso (§ 2º) e qualidade funcional (§ 3º), tornando o item desnecessariamente dependente da combinação das duas regras. Em `draft.3`, a questão passou a testar isoladamente a consequência expressa do § 2º: dano à Administração -> `reclusão de 2 a 6 anos e multa`. Resultado final: `PASS`.

**Q29 - DP-10.** No `draft.2`, "função suspensa por decisão judicial" aproximava art. 324 e art. 359. Em `draft.3`, o enunciado usa `atividade privada` suspensa por decisão judicial, isolando a literalidade do art. 359. O corpo didático também ganhou contraste explícito `324 x 359`, sem inventar regra jurisprudencial de concurso de normas. Resultado final: `PASS`.

### Contagem final

- `PASS`: `30/30`;
- `REVIEW_REQUIRED`: `0/30`;
- `FAIL`: `0/30`.

Os requisitos de prática `Q-LIT`, `Q-CMP` e `Q-CAS` do contrato DP-01...DP-10 estão atendidos no conjunto após as correções.

---

## 6. QA-5 - utilidade como corpus Markdown

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

Tentativa original em `2026-09-12`:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Consequência: `python tools/verify.py` não pôde ser executado em checkout canônico neste runtime. Resultado: `not_executed_current_environment`, **não** `PASS`, conforme DEC-0009.

---

## 9. DIREITO-007 - QA-7 NotebookLM

### QA estático

**Resultado:** `PASS_STATIC`

Arquitetura auditada:

```text
fonte estudável
-> APOSTILA.pdf

configuração da conversa
-> bloco operacional de METODOLOGIA_NOTEBOOKLM.md
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

### Smoke real

**Resultado:** `PASS_WITH_OBSERVATIONS`

O usuário executou o smoke real em `2026-09-14` com somente o `APOSTILA.pdf` canônico como fonte e o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md` na configuração personalizada da conversa.

Foram observados:

- chat explicativo sobre concussão x corrupção passiva: `PASS`;
- treino interativo A-E, uma questão por vez e sem antecipação de gabarito: `PASS`;
- Teste do Estúdio: `PASS` na amostra inspecionada;
- Cartões: `PASS` na amostra inspecionada;
- Mapa mental: `PASS_WITH_OBSERVATION`;
- pergunta de limite epistemológico sobre jurisprudência: `PASS_WITH_OBSERVATION`.

As duas observações não foram classificadas como bloqueantes:

1. o Mapa mental exibiu `DP-01`, `DP-02` etc. porque esses IDs internos aparecem nos títulos do próprio StudentContent. A hierarquia jurídica e o conteúdo permaneceram corretos. Para os próximos SubjectPacks, coverage IDs e outros identificadores de backoffice não devem aparecer em títulos visíveis do StudentContent;
2. diante de pergunta sobre jurisprudência externa, o tutor não inventou precedentes, mas iniciou com uma negativa categórica antes de esclarecer que a fonte não traz jurisprudência. Para os próximos packs/configurações, ausência no corpus deve ser formulada como limite da fonte, não como afirmação universal sobre inexistência externa.

A decisão detalhada está em `NOTEBOOKLM_SMOKE_0.1.0.md`. Não será criado `rc.2` apenas para esses dois pontos.

---

## 10. DIREITO-007 - QA-9 PDF versionado

**Resultado:** `PASS_CANONICAL_BINARY_IDENTITY`

O candidato preferido foi gerado exclusivamente a partir da cópia local cujo Git blob coincide com o `APOSTILA.md` congelado do `rc.1` (`008c3ac439d8b7d4038fd0114e486c1daaf755b1`). O arquivo publicado manualmente na branch `upload/direito-penal-apostila-pdf` foi lido pelo GitHub com Git blob:

`5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`

Esse valor coincide exatamente com o Git blob calculado sobre o candidato local integralmente auditado. A identidade binária entre o arquivo versionado e o candidato auditado está, portanto, comprovada.

### Identidade do binário

- caminho: `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf`;
- páginas: `17`;
- tamanho: `30.167 bytes`;
- formato: `PDF 1.4`;
- página: `A4`;
- SHA-256: `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`;
- Git blob: `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`;
- commit de upload/rename observado na branch: `fd7f0f78b16f85d06979ab1e6cc86762c1bd1d00`.

### Readback textual

Em `2026-09-14`, o arquivo local de identidade binária idêntica ao versionado foi novamente extraído com `pdftotext -layout`. Foram confirmados:

- `Direito Penal`;
- `Unidade 1`;
- `Unidade 10`;
- `Gabarito comentado`;
- `art. 359`;
- `§`;
- `Código Penal`;
- `Síntese final de recuperação`.

Resultado: `PASS`.

### Inspeção visual

Em `2026-09-14`, as `17/17` páginas do mesmo binário foram novamente renderizadas a 150 dpi e inspecionadas. Não foram observados:

- clipping de texto;
- sobreposição de elementos;
- glifos quebrados;
- acentos ou símbolos jurídicos corrompidos;
- quebra visual impeditiva em tabelas;
- mistura acidental entre questões e gabarito.

As questões ocupam páginas anteriores ao gabarito, e o `Gabarito comentado` inicia em página própria na página 17. Resultado visual: `PASS`.

### Conclusão do QA-9

A publicação manual resolveu o bloqueio de transporte binário registrado nas PRs 23 e 24. Como o Git blob remoto é exatamente o Git blob do candidato local integralmente auditado, o QA-9 do PDF versionado está fechado como `PASS_CANONICAL_BINARY_IDENTITY`.

---

## 11. DIREITO-007 - gate determinístico

Nova checagem em `2026-09-14` continua bloqueada por DNS:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Sem checkout canônico, executar `python tools/verify.py` em diretório parcial seria falsa validação. Resultado mantido: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, não `PASS`. A impossibilidade foi reavaliada e permanece documentada conforme DEC-0009.

---

## 12. Decisão de saída atual

| Gate | Resultado |
|---|---|
| QA-1 cobertura | PASS |
| QA-2 normativo | PASS_AFTER_CORRECTIONS |
| QA-3 didática/contrastes | PASS |
| QA-4 30 questões | PASS - 30/30 |
| requisitos Q-LIT/Q-CMP/Q-CAS | PASS |
| QA-5 corpus Markdown | PASS_FOR_MARKDOWN |
| coerência com banca | PASS |
| configuração do tutor | PASS_STATIC |
| QA-7 NotebookLM estático | PASS_STATIC |
| QA-7 NotebookLM live | PASS_WITH_OBSERVATIONS |
| QA-9 PDF versionado | PASS_CANONICAL_BINARY_IDENTITY |
| `APOSTILA.pdf` | VERSIONED_EXACT_BINARY |
| gate determinístico | NOT_EXECUTED_CURRENT_ENVIRONMENT - IMPOSSIBILITY_REEVALUATED |

**DIREITO-006: `closed`.**

**DIREITO-007: `closed_with_observations`.**

O `0.1.0-rc.1` é aceito como release candidate validado do primeiro pipeline jurídico. As duas observações do smoke são melhorias de processo para os próximos SubjectPacks e não justificam um `rc.2`. A impossibilidade atual do gate determinístico permanece registrada e não é tratada como `PASS`.
