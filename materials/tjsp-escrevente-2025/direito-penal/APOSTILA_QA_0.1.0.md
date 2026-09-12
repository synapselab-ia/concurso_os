# APOSTILA_QA_0.1.0 — Direito Penal — TJSP Escrevente 2025

**QA date:** `2026-09-12`  
**Object reviewed:** `APOSTILA.md` `0.1.0-draft.1` → corrected during QA to `0.1.0-draft.2`  
**Pack:** `direito-penal`  
**Overall result:** `FAIL_PRACTICE_REVIEW`  
**Release candidate:** `blocked`

## 1. Escopo e método

Este QA executa `DIREITO-006` conforme `00_SYSTEM/NEXT_ACTION.md`. O edital e a matriz de cobertura controlam o escopo; o Código Penal oficial controla as afirmações normativas; a análise histórica da banca serve apenas para calibrar contraste, forma e aplicação.

Recorte auditado artigo por artigo:

`293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Fonte primária: `SRC-B2-CP`, Decreto-Lei n.º 2.848/1940 — Código Penal, Planalto (`https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm`).

O Gate 2 já havia classificado o recorte como `cutoff_closed_no_scoped_drift` para o baseline `2025-07-29`. Durante este QA, a compilação oficial foi reaberta e todos os dispositivos do recorte foram confrontados com o draft. O art. `338-A`, posterior e fora do recorte, permaneceu excluído.

O QA separa conteúdo, prática e release. Uma falha em questão autoral impede o fechamento do gate mesmo quando a cobertura normativa foi corrigida.

---

## 2. QA-1 — cobertura e rastreabilidade

**Resultado:** `PASS`

| coverage_id | recorte | resultado | observação |
|---|---|---|---|
| DP-01 | 293–295 | PASS | caput, formas do art. 293, petrechos e majorante funcional explicitados |
| DP-02 | 296–305 | PASS | todos os artigos possuem bloco próprio; §§ previdenciários do 297 e penas dos arts. 300–301 foram explicitados |
| DP-03 | 307–308 | PASS | falsa identidade e uso/cessão de documento separados |
| DP-04 | 311-A | PASS | caput, facilitação, resultado danoso e majorante funcional cobertos |
| DP-05 | 312–317 | PASS | inclui 313-A e 313-B; formas e consequências centrais explicitadas |
| DP-06 | 319–327 | PASS | inclui 319-A; todos os artigos do intervalo aparecem individualmente |
| DP-07 | 328–333 | PASS | todos os artigos do intervalo aparecem; contraste 329/330 e 332/333 explícito |
| DP-08 | 336 e 337 | PASS | somente os dois artigos exigidos; `337-A` e seguintes não são absorvidos |
| DP-09 | 339–347 | PASS | todos os artigos do intervalo possuem ensino individual ou bloco inequivocamente identificado |
| DP-10 | 357 e 359 | PASS | ambos os artigos aparecem e o 358 permanece fora do recorte |

### Verificação de fronteira

- art. 306 não foi promovido ao syllabus;
- arts. 309–311 não foram promovidos ao syllabus;
- art. 318 não foi promovido ao syllabus;
- arts. 334–335 não foram promovidos ao syllabus;
- arts. `337-A` e seguintes não foram promovidos ao syllabus;
- art. `338-A` não foi promovido ao syllabus;
- arts. 348–356 e 358 não foram promovidos ao syllabus;
- art. 359-A e seguintes não foram promovidos ao syllabus.

A menção a artigo fora do recorte ocorre apenas quando necessária para explicar fronteira editorial, sem ensiná-lo como conteúdo obrigatório.

---

## 3. QA-2 — exatidão normativa

**Resultado:** `PASS_AFTER_CORRECTIONS`

A primeira passagem estava correta nos contrastes centrais, mas excessivamente compacta em diversos pontos de literalidade. O QA promoveu o draft para `0.1.0-draft.2` e executou as seguintes correções/expansões antes de atribuir PASS a este subgate.

### DP-01

- art. 293: explicitadas as três famílias do § 1º, a equiparação de atividade comercial do § 5º, as formas dos §§ 2º–4º e a pena específica do recebimento de boa-fé seguido de uso consciente;
- arts. 294–295: mantidos verbos, destinação especial do objeto e aumento de 1/6.

### DP-02

- art. 296: majorante funcional de 1/6 explicitada;
- art. 297: majorante, equiparações documentais e hipóteses previdenciárias dos §§ 3º–4º explicitadas;
- arts. 300–301: penas antes omitidas foram incorporadas;
- arts. 298–305: conferidos sujeito, objeto, verbo, finalidade, equiparações e penas.

### DP-03 / DP-04

- arts. 307–308: mantida a subsidiariedade textual e a diferença entre identidade declarada e documento de identidade;
- art. 311-A: conferidos certames abrangidos, finalidade, forma equiparada, resultado danoso e aumento de 1/3.

### DP-05

- art. 312: pena do peculato culposo explicitada, além dos efeitos temporais da reparação;
- arts. 313-A/313-B: separado `dados + finalidade específica` de `sistema/programa + falta de autorização`, com majorante de dano do 313-B;
- art. 316: penas do excesso de exação e do desvio do indevidamente recebido explicitadas;
- art. 317: pena do § 2º explicitada;
- arts. 313–315: conferidos integralmente no nível exigido pela matriz.

### DP-06

- art. 321: forma de interesse ilegítimo e pena explicitadas;
- arts. 322–324: penas antes compactadas foram incorporadas;
- art. 325: formas equiparadas de acesso e forma qualificada pelo dano explicitadas;
- art. 327: conceito, equiparação e aumento do § 2º conferidos.

### DP-07 / DP-08

- art. 329: pena-base, forma pelo insucesso do ato e cumulação com violência explicitadas;
- art. 332: aumento `da metade` conferido;
- arts. 328–333, 336–337: demais elementos e penas conferidos.

### DP-09 / DP-10

- art. 342: aumento de 1/6 a 1/3 e momento da retratação conferidos;
- art. 343: aumento de 1/6 a 1/3 explicitado;
- art. 344: aumento de 1/3 até metade quando o processo envolve crime contra a dignidade sexual conferido;
- arts. 339–347, 357 e 359: demais elementos, formas e penas conferidos.

### Resultado normativo

Não foi identificada afirmação materialmente incompatível com a fonte oficial após as correções. O draft `0.1.0-draft.2` está apto a servir de base normativa para a próxima iteração, sem que isso equivalha a release.

---

## 4. QA-3 — didática, contrastes e engenharia de banca

**Resultado:** `PASS`

O draft corrigido segue a estrutura jurídica prevista no protocolo:

`regra → elementos/requisitos → hipótese → consequência → contraste → mini-caso → síntese`.

Foram preservados/fortalecidos os contrastes empiricamente sustentados pelo Gate 3, entre eles:

- art. 293 x 294;
- falsidade material x ideológica;
- art. 304 x 305;
- art. 307 x 308;
- art. 313-A x 313-B;
- concussão x corrupção passiva;
- prevaricação x condescendência;
- resistência x desobediência;
- tráfico de influência x corrupção ativa;
- art. 336 x 337;
- denunciação caluniosa x comunicação falsa;
- falso testemunho x corrupção de sujeito da prova;
- tráfico de influência x exploração de prestígio.

Cada DP possui três mini-casos no corpo didático. A apostila não apresenta contagens históricas nem transforma frequência de prova em previsão.

### Risco didático ainda aberto

O contraste entre **art. 324** e **art. 359** precisa aparecer de forma mais explícita na prática. Ambos podem se aproximar quando o enunciado usa genericamente a ideia de “continuar função suspensa”. O critério seguro a enfatizar é:

- art. 324: exercício de **função pública** antes das exigências legais ou continuação sem autorização após ciência oficial de exoneração, remoção, substituição ou suspensão;
- art. 359: exercício de função, atividade, direito, autoridade ou múnus do qual houve suspensão/privação **por decisão judicial**.

Esse risco gera a falha registrada em QA-4, abaixo.

---

## 5. QA-4 — revisão semântica das 30 questões

**Resultado:** `FAIL`

### Critério

Cada item foi revisado contra a fonte e contra o próprio conteúdo. Para PASS, exige-se uma única resposta defensável sem depender de regra externa não ensinada.

| questão | unidade | resultado | elemento decisivo |
|---:|---|---|---|
| 1 | DP-01 | PASS | objeto especialmente destinado → art. 294 |
| 2 | DP-01 | PASS | boa-fé inicial + conhecimento posterior → art. 293 § 4º |
| 3 | DP-01 | PASS | prevalecimento do cargo → art. 295 |
| 4 | DP-02 | PASS | alteração física x conteúdo falso |
| 5 | DP-02 | PASS | médico no exercício profissional → art. 302 |
| 6 | DP-02 | PASS | documento verdadeiro destruído/suprimido → art. 305 |
| 7 | DP-03 | PASS | atribuição de identidade sem documento alheio → art. 307 |
| 8 | DP-03 | PASS | uso como próprio de documento alheio → art. 308 |
| 9 | DP-03 | PASS | cessão para uso de identidade → art. 308 |
| 10 | DP-04 | PASS | conteúdo sigiloso + certame + finalidade |
| 11 | DP-04 | PASS | facilitação de acesso não autorizado |
| 12 | DP-04 | REVIEW_REQUIRED | combina § 2º (resultado danoso) e § 3º (funcionário) e pressupõe cumulação sem explicitar no enunciado o nível de análise pretendido; deve ser reformulada para testar uma regra de cada vez |
| 13 | DP-05 | PASS | reparação antes da sentença irrecorrível no peculato culposo |
| 14 | DP-05 | PASS | dados + finalidade → art. 313-A |
| 15 | DP-05 | PASS | verbo exigir → concussão |
| 16 | DP-06 | PASS | interesse/sentimento pessoal → prevaricação |
| 17 | DP-06 | PASS | indulgência + subordinado → art. 320 |
| 18 | DP-06 | PASS | equiparação do art. 327 § 1º |
| 19 | DP-07 | PASS | violência/ameaça contra ato legal → resistência |
| 20 | DP-07 | PASS | vantagem a pretexto de influir → art. 332 |
| 21 | DP-07 | PASS | oferta/promessa ao funcionário → art. 333 |
| 22 | DP-08 | PASS | edital afixado → art. 336 |
| 23 | DP-08 | PASS | selo/sinal para identificar/cerrar → art. 336 |
| 24 | DP-08 | PASS | processo sob custódia → art. 337 |
| 25 | DP-09 | PASS | imputação contra pessoa sabidamente inocente |
| 26 | DP-09 | PASS | retratação antes da sentença do processo do ilícito |
| 27 | DP-09 | PASS | finalidade de produzir efeito em processo penal → dobro |
| 28 | DP-10 | PASS | juiz está expressamente no elenco do art. 357 |
| 29 | DP-10 | FAIL_AMBIGUOUS | “função suspensa por decisão judicial” também aproxima o art. 324; o enunciado deve usar atividade/direito fora da hipótese de função pública do art. 324 ou explicitar o contraste |
| 30 | DP-10 | PASS | elenco específico da Justiça x funcionário público em geral |

### Contagem

- `PASS`: 28/30;
- `REVIEW_REQUIRED`: 1/30 (Q12);
- `FAIL_AMBIGUOUS`: 1/30 (Q29).

Por isso, QA-4 **não fecha**. O pack continua `draft`.

### Correção mínima exigida

1. Q12: reformular para testar separadamente o resultado danoso ou a majorante de funcionário, evitando fazer a questão depender de combinação não explicada;
2. Q29: trocar o fato para exercício de atividade/direito judicialmente suspenso que não possa ser confundido com continuação de função pública do art. 324; acrescentar no corpo didático contraste expresso `324 x 359`.

Após as duas correções, revalidar Q12 e Q29 e conferir que gabarito/comentário acompanharam a mudança.

---

## 6. Requisitos Q-LIT / Q-CMP / Q-CAS da matriz

**Resultado:** `PASS_CONDICIONAL_ON_QA4`

A versão `draft.2` possui três mini-casos por DP no corpo didático e três questões A–E por DP. Quadros de contraste estão presentes nas linhas que exigem `Q-CMP`.

A quantidade, por si só, não fecha o requisito. O conteúdo das questões precisa ser semanticamente válido. Portanto o resultado só se torna PASS final depois da correção de Q12 e Q29.

---

## 7. QA-5 — utilidade como corpus

**Resultado:** `PASS_FOR_MARKDOWN_DRAFT`

- títulos descrevem conteúdo real;
- regra, contraste e caso aparecem próximos;
- terminologia foi mantida consistente;
- gabarito fica separado das questões;
- o texto é compreensível sem documentação interna do projeto;
- não há metadiscurso de frequência da banca no StudentContent;
- tabelas têm função comparativa/recuperável;
- o pack ainda não deve ser carregado como fonte canônica no NotebookLM porque QA-4 permanece aberto.

Nenhum smoke do NotebookLM foi executado neste gate, conforme o próprio NEXT_ACTION: primeiro estabilizar semanticamente o Markdown.

---

## 8. Gate determinístico

Tentativa em `2026-09-12`:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Consequência: `python tools/verify.py` não foi executado em checkout canônico neste runtime. Resultado: `not_executed_current_environment`, não `PASS`, conforme DEC-0009.

---

## 9. Decisão de saída

| Gate | Resultado |
|---|---|
| QA-1 cobertura | PASS |
| QA-2 normativo | PASS_AFTER_CORRECTIONS |
| QA-3 didática/contrastes | PASS |
| QA-4 30 questões | **FAIL** |
| QA-5 corpus Markdown | PASS_FOR_MARKDOWN_DRAFT |
| gate determinístico | NOT_EXECUTED_CURRENT_ENVIRONMENT |

**DIREITO-006: `not_closed`.**

O draft avançou materialmente e a camada normativa está revisada, mas duas questões ainda impedem o fechamento semântico. Não gerar PDF, não fazer smoke de NotebookLM e não promover release candidate.

Próxima ação: corrigir Q12 e Q29, explicitar `art. 324 x art. 359`, revalidar as duas questões e então atualizar este QA para o resultado final.