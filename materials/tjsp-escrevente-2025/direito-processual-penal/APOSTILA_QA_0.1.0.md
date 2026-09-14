# APOSTILA_QA_0.1.0 - Direito Processual Penal - TJSP Escrevente 2025

**QA date:** `2026-09-14`  
**Object reviewed:** `APOSTILA.md` `0.1.0-draft.1` -> `0.1.0-draft.2`  
**Pack:** `direito-processual-penal`  
**Gate:** `DIREITO-009`  
**Overall semantic result:** `PASS`  
**Normative result:** `PASS_AFTER_CORRECTIONS`  
**Release-candidate readiness:** `READY_FOR_RC_PREPARATION`

## 1. Escopo e método

O QA foi executado contra o syllabus canônico, a matriz `DPP-01...DPP-25`, o inventário de versões de B2 e as fontes normativas primárias `SRC-B2-CPP` e `SRC-B2-L9099`.

Recorte auditado:

- CPP: `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`;
- Lei n.º 9.099/1995: `60-83; 88-89`.

Baseline: `2025-07-29`.

A revisão não tratou provas históricas como fonte de direito. `DIREITO_B2_BANCA_ANALYSIS.md` foi usado apenas para calibrar contraste, fluxo, prazo e formato de prática, sem inferência de frequência futura.

O `draft.1` apresentava cobertura estrutural completa pelas 25 unidades, mas a revisão artigo por artigo encontrou pontos literais e de completude que precisavam ser explicitados antes de um PASS. O `draft.2` incorpora essas correções e continua sendo draft: nenhum PDF, release candidate ou smoke de NotebookLM foi produzido neste gate.

---

## 2. QA-1 - cobertura e rastreabilidade

**Resultado:** `PASS_AFTER_CORRECTIONS`

| coverage_id | recorte | conteúdo | prática/QA |
|---|---|---|---|
| DPP-01 | CPP 251-258 | PASS | PASS |
| DPP-02 | CPP 261-267 | PASS | PASS |
| DPP-03 | CPP 274 | PASS | PASS |
| DPP-04 | CPP 351-369 | PASS | PASS |
| DPP-05 | CPP 370-372 | PASS | PASS |
| DPP-06 | CPP 394-405 | PASS | PASS |
| DPP-07 | CPP 406-421 | PASS | PASS |
| DPP-08 | CPP 422-431 | PASS | PASS |
| DPP-09 | CPP 432-452 | PASS | PASS |
| DPP-10 | CPP 453-474 | PASS | PASS |
| DPP-11 | CPP 475-491 | PASS | PASS |
| DPP-12 | CPP 492-497 | PASS | PASS |
| DPP-13 | CPP 531-538 | PASS | PASS |
| DPP-14 | CPP 541-548 | PASS | PASS |
| DPP-15 | CPP 574-580 | PASS | PASS |
| DPP-16 | CPP 581-592 | PASS | PASS |
| DPP-17 | CPP 593-603 | PASS | PASS |
| DPP-18 | CPP 604-620 | PASS | PASS |
| DPP-19 | CPP 621-631 | PASS | PASS |
| DPP-20 | CPP 632-646 | PASS | PASS |
| DPP-21 | CPP 647-667 | PASS | PASS |
| DPP-22 | Lei 9.099, 60-68 | PASS | PASS |
| DPP-23 | Lei 9.099, 69-76 | PASS | PASS |
| DPP-24 | Lei 9.099, 77-83 | PASS | PASS |
| DPP-25 | Lei 9.099, 88-89 | PASS | PASS |

Os identificadores `DPP-*` permanecem no backoffice. O readback do `draft.2` não encontrou `DPP-` no StudentContent visível.

### Lacunas de completude corrigidas

A revisão integral levou às seguintes correções materiais ou de explicitação:

- art. 262: literalidade sobre curador do acusado menor registrada sem extrapolação jurisprudencial externa ao corpus;
- arts. 363-365: formação do processo, incisos revogados do art. 363, regra residual do art. 364 e elementos do edital explicitados;
- art. 394-A: prioridade de tramitação incorporada conforme o baseline;
- art. 398: identificado como revogado;
- art. 400-A: proteção da integridade e dignidade da vítima durante a audiência incorporada;
- arts. 531-538: art. 537 identificado como revogado e art. 538 explicitado;
- arts. 574-580: regras gerais ampliadas, incluindo erro de funcionário, desistência do MP, legitimidade, forma, fungibilidade e extensão a corréus;
- arts. 581-592: processamento do RESE, prazo especial da lista de jurados, instrumento, razões, contrarrazões, retratação e efeitos explicitados;
- arts. 593-603: revogação dos arts. 594-595, efeitos, legitimidade subsidiária, razões/contrarrazões e remessa explicitados;
- arts. 604-620: `604-608` e `611` tratados como revogados; `609-610` e `612-620` rastreados individualmente no texto;
- arts. 632-646: `632-636` tratados como revogados e `637-646` explicitados, inclusive prazos e ausência de efeito suspensivo da carta testemunhável;
- arts. 647-667: art. 647-A e sequência procedimental do habeas corpus incorporados;
- Lei 9.099, arts. 60-83: regras de competência, comunicação, audiência, acusação, prova, recursos e art. 81, § 1º-A, aprofundadas para cobertura literal do intervalo.

---

## 3. QA-2 - exatidão normativa e controle de versão

**Resultado:** `PASS_AFTER_CORRECTIONS`

As duas fontes primárias foram reabertas durante o gate e o conteúdo foi rechecado por intervalo. Foram conferidos sujeitos, legitimidade, prazos, hipóteses, cabimento, efeitos, sequência procedimental e dispositivos revogados.

### Controle do cutoff

O inventário canônico classifica `SRC-B2-CPP` como `cutoff_closed_drift_mapped`. O drift conhecido dentro do recorte é o art. `584, § 4º`, incluído pela Lei n.º `15.358/2026`.

O `draft.2` preserva:

```text
baseline estudável = 2025-07-29
art. 584 no baseline = §§ 1º a 3º
§ 4º de 2026 = registrado como drift, fora do conteúdo exigido
```

`SRC-B2-L9099` permanece `cutoff_closed_no_scoped_drift` no inventário canônico para os arts. `60-83; 88-89`.

Não foi promovido outro drift pós-cutoff a conteúdo estudável neste QA.

### Dispositivos revogados dentro do recorte

O `draft.2` passou a identificar explicitamente, onde necessário ao contrato de cobertura:

- CPP art. 398: revogado;
- CPP art. 537: revogado;
- CPP arts. 594-595: revogados;
- CPP arts. 604-608: revogados;
- CPP art. 611: revogado;
- CPP arts. 632-636: revogados.

Também registra os incisos revogados do art. 363 sem reconstruí-los por analogia.

Depois das correções, não foi identificada incompatibilidade material aberta entre o conteúdo auditado e as fontes controladas que impeça a preparação do próximo estágio.

---

## 4. QA-3 - didática, fluxos e contrastes

**Resultado:** `PASS`

A estrutura foi revisada segundo o protocolo jurídico:

```text
regra
-> sujeito/legitimidade
-> momento
-> requisito ou prazo
-> consequência/efeito
-> exceção
-> contraste
-> aplicação
```

Permanecem explícitos os contrastes de maior risco:

- impedimento x suspeição;
- citação por edital x hora certa;
- citação x intimação;
- rejeição x absolvição sumária;
- ordinário x sumário x sumaríssimo;
- pronúncia x impronúncia x absolvição sumária x desclassificação;
- RESE x apelação;
- apelação x revisão criminal;
- carta testemunhável x recurso destravado por ela;
- habeas corpus preventivo x liberatório e HC x revisão;
- composição civil x transação penal x suspensão condicional do processo;
- embargos de declaração do CPP x JECrim.

Fluxos de comunicação, procedimento comum, júri, recursos, carta testemunhável, habeas corpus e JECrim ficaram recuperáveis sem depender de documentação de backoffice.

---

## 5. QA-4 - prática autoral

**Resultado:** `PASS`

As `52` questões do `draft.1` foram revisadas individualmente quanto a:

- alinhamento ao syllabus e ao baseline;
- cinco alternativas;
- resposta única defensável;
- ausência de ambiguidade involuntária;
- coerência entre alternativa, gabarito e comentário;
- ausência de dependência de jurisprudência ou doutrina externa;
- ausência de contaminação pelo art. 584, § 4º, de 2026.

Resultado dos 52 itens originais:

- `PASS`: `52/52` após revisão e reescrita editorial do `draft.2`;
- `REVIEW_REQUIRED`: `0/52`;
- `FAIL`: `0/52`.

A revisão de cobertura mostrou que oito pontos mereciam prática literal própria. Foram adicionadas e revisadas Q53-Q60:

- Q53: art. 262;
- Q54: art. 394-A;
- Q55: art. 400-A;
- Q56: arts. 537-538;
- Q57: art. 611 revogado;
- Q58: art. 640, prazo de 48 horas da carta testemunhável;
- Q59: art. 647-A;
- Q60: Lei 9.099, art. 81, § 1º-A.

Contagem final do `draft.2`:

- `60/60` questões com resultado `PASS` neste gate.

### Requisitos de prática da matriz

Os requisitos `Q-LIT`, `Q-CMP`, `Q-CAS`, `Q-FLX`, `Q-VER` e `Q-FULL` aplicáveis às 25 rows foram rechecados contra a combinação de corpo didático, tabelas, fluxos, mini-casos e bateria objetiva.

- `Q-LIT`: atendido por regras e microitens literais;
- `Q-CMP`: atendido por quadros/contrastes e alternativas próximas;
- `Q-CAS`: atendido por mini-casos nas rows que o exigem;
- `Q-FLX`: atendido por fluxos e armadilhas de etapa, prazo e recurso;
- `Q-VER`: DPP-16 preserva explicitamente o cutoff do art. 584;
- `Q-FULL`: DPP-18 e DPP-20 passaram a tratar os dispositivos revogados e vigentes do intervalo sem preencher lacunas normativas.

---

## 6. QA-5 - utilidade como corpus Markdown

**Resultado:** `PASS_FOR_MARKDOWN`

- 25 unidades com títulos sem coverage IDs;
- terminologia processual consistente;
- regras, exceções, contrastes e exemplos ficam próximos;
- tabelas e blocos de fluxo preservam significado em texto simples;
- questões e gabarito estão separados;
- não há metadiscurso de frequência da banca;
- o corpus não depende de `MANIFEST`, matriz ou análise histórica para ser compreendido;
- ausência de informação externa não é apresentada como prova de inexistência no mundo externo.

A lição do smoke de Direito Penal foi aplicada: rastreabilidade fica no backoffice, não nos títulos do estudante.

---

## 7. Coerência com a banca

**Resultado:** `PASS`

O material usa os sinais empíricos do Gate 3 para privilegiar literalidade, sequência procedimental, competência, prazo, requisito e contraste. Não foi introduzida previsão de cobrança nem peso futuro por frequência histórica.

---

## 8. Gate determinístico

Em `2026-09-14`, foi reavaliada a possibilidade de executar o gate canônico a partir de checkout real:

```text
git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_verify
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

O clone terminou com exit code `128`. Sem checkout canônico local, `python tools/verify.py` não pode ser executado de forma válida neste runtime.

Resultado: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, **não** `PASS`, conforme DEC-0009.

---

## 9. Decisão de saída de DIREITO-009

| Gate | Resultado |
|---|---|
| QA-1 cobertura/rastreabilidade | PASS_AFTER_CORRECTIONS |
| QA-2 normativo/versão | PASS_AFTER_CORRECTIONS |
| QA-3 didática/contrastes | PASS |
| QA-4 prática | PASS, 60/60 |
| QA-5 corpus Markdown | PASS_FOR_MARKDOWN |
| coerência com banca | PASS |
| `python tools/verify.py` | NOT_EXECUTED_CURRENT_ENVIRONMENT |
| PDF | NOT_CREATED_BY_DESIGN |
| NotebookLM | NOT_STARTED |

`DIREITO-009` pode ser fechado. O `0.1.0-draft.2` está semanticamente aprovado para **preparação de release candidate**, mas ainda não é RC nem release.

A etapa seguinte deve criar a configuração do tutor jurídico, sincronizar identidade/versionamento e executar o QA estático necessário antes de gerar e auditar o PDF candidato e realizar smoke real do NotebookLM. Nenhum resultado futuro é presumido por este documento.
