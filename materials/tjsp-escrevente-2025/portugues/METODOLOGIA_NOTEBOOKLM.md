# METODOLOGIA NOTEBOOKLM — Língua Portuguesa — TJSP/VUNESP

**Pack:** `tjsp-escrevente-2025/portugues`  
**Versão:** `1.0.1`

## 1. Objetivo

Este arquivo orienta o uso do notebook de Português sem transformar o estudo em administração de prompts.

A regra principal é:

> **carregue um corpus forte uma vez e use naturalmente o Estúdio do NotebookLM.**

O chat é uma ferramenta de aprofundamento, não a única interface de estudo.

O edital controla o escopo. As provas TJSP/VUNESP e `ANALISE_BANCA.md` calibram forma de cobrança. A apostila organiza teoria e distinções.

---

## 2. Fontes e prioridade

Prioridade factual/pedagógica:

1. edital vigente;
2. prova TJSP/VUNESP 2025;
3. provas históricas 2024, 2023 e 2021;
4. `APOSTILA.pdf`;
5. `ANALISE_BANCA.md`;
6. esta metodologia, apenas para modo de estudo.

O usuário **não precisa trocar manualmente o conjunto de fontes a cada recurso do Estúdio**. O primeiro uso deve acontecer com o corpus recomendado carregado e disponível. Só selecionar subconjuntos se um problema real aparecer.

---

## 3. Uso normal do Estúdio

### Teste

É o recurso nativo principal para prática objetiva de Português.

No smoke test inicial:

- quantidade: `Padrão`;
- dificuldade: `Médio (padrão)`;
- fontes: manter o conjunto carregado, sem microgerenciamento;
- tema/comando curto:

> `Teste de Português no padrão TJSP/VUNESP das provas carregadas.`

**Importante:** o seletor `Fácil / Médio / Difícil` é uma escala genérica do NotebookLM. Não assumir que `Difícil` significa `nível VUNESP`.

A calibração desejada deve vir das provas reais e da análise de banca presentes no notebook.

Se o teste ficar artificialmente fácil, difícil, obscuro ou fora do padrão, isso é dado do smoke test: registrar o desvio e só então ajustar prompt/fontes.

### Cartões

Usar para:

- regras curtas;
- distinções;
- conectivos e relações;
- casos de crase/regência/concordância;
- erros recorrentes;
- pares que costumam ser confundidos.

Não transformar capítulos inteiros em cartões.

Comando curto suficiente quando necessário:

> `Cartões de regras e distinções de Português relevantes para o edital TJSP/VUNESP.`

### Mapa mental

Usar para visualizar a estrutura da matéria e relações entre tópicos. Não precisa ser criado antes de toda sessão e não representa domínio.

Comando curto opcional:

> `Mapa mental do conteúdo de Português do edital, organizado por interpretação, coesão, semântica e norma-padrão.`

### Relatórios

Usar para revisão consolidada de um tema ou para montar guia de revisão. Evitar substituir prática ativa por leitura de relatório.

### Tabela de dados

Boa para comparações como:

- relação lógica × conectivos;
- regência × preposição;
- regra × exceção;
- forma correta × erro típico;
- alternativa correta × tipo de distrator.

### Resumo em áudio/vídeo, apresentação e infográfico

São recursos complementares de revisão e visão geral. Usar quando ajudarem; não existe obrigação de gerar todos.

---

## 4. Padrão VUNESP que deve emergir do corpus

Questões inéditas ou testes devem, quando possível, refletir os mecanismos observados no corpus:

- cinco alternativas plausíveis;
- inferência versus extrapolação;
- diferenças semânticas discretas;
- coesão e relações lógico-semânticas;
- gramática aplicada ao contexto;
- reescrita com preservação de sentido;
- alternativas quase corretas com erro localizado;
- ausência de distratores obviamente absurdos.

Não transformar frequência histórica em previsão garantida.

---

## 5. Quando usar o chat

Usar o chat principalmente quando:

- uma questão do Teste ficou duvidosa;
- a explicação automática não convenceu;
- há duas alternativas próximas;
- o usuário quer entender exatamente o erro;
- é necessário gerar reteste focado;
- há lacuna ou conflito entre fontes;
- o usuário quer treino interativo em vez do Teste nativo.

O chat não precisa iniciar toda sessão.

---

## 6. Protocolo de correção no chat

Quando houver uma questão concreta, corrigir com o nível de profundidade proporcional à necessidade.

### Acerto claro

Formato curto:

```text
Gabarito: C
Ponto decisivo: ...
Armadilha principal: ...
```

### Erro ou hesitação

Explicar:

1. gabarito;
2. regra/trecho decisivo;
3. por que a correta funciona;
4. por que a alternativa escolhida falha;
5. comparar alternativas próximas;
6. fazer microreteste se isso ajudar.

Se o usuário declarar confiança (`sem dúvida`, `entre C/E`, `chute`), considerar isso no diagnóstico. Não é obrigatório reproduzir essa mecânica dentro do Teste nativo do Estúdio.

---

## 7. Diagnóstico de interpretação

Quando aplicável, identificar o tipo de erro:

- extrapolação;
- contradição;
- redução indevida;
- generalização;
- troca de causa/consequência;
- troca de referente;
- intensificação;
- atenuação;
- outra troca de sentido claramente descrita.

Diferenciar explicitamente **inferência válida** de **extrapolação**.

---

## 8. Diagnóstico de gramática

A correção deve apontar a construção decisiva e, quando útil, usar par mínimo:

```text
CORRETO: exemplo curto
INCORRETO: exemplo curto
REGRA: explicação em uma frase
```

Evitar aula longa quando uma regra curta resolve a dúvida.

---

## 9. Fluxo diário simples

Não existe ritual obrigatório. Um fluxo eficiente possível é:

```text
abrir notebook
→ Teste
→ revisar erros/explicações
→ usar chat apenas nos pontos realmente duvidosos
→ Cartões ou Tabela se houver regra/distinção que mereça fixação
→ encerrar
```

Em outro dia, o usuário pode começar por Mapa mental, relatório, áudio ou diretamente pelo chat. O sistema não deve impedir uso natural da ferramenta.

---

## 10. Feedback para o ChatGPT/GitHub

Não enviar relatório de toda sessão.

Trazer ao ChatGPT quando houver algo que possa melhorar o sistema:

- questão que não parece VUNESP;
- nível inadequado apesar do corpus;
- explicação errada/ambígua;
- tópico faltando na apostila;
- recurso do Estúdio funcionando mal com o pack;
- padrão recorrente de dificuldade que justifique ajuste pedagógico.

Um print ou descrição curta normalmente é suficiente.

---

## 11. SESSION_REPORT opcional

Se o usuário quiser fechar uma sessão com resumo:

```text
SESSION_REPORT
participant: pNNN ou não informado
competition: tjsp-escrevente-2025
subject: portugues
pack_version: 1.0.1
date: YYYY-MM-DD

covered:
- tópicos trabalhados

main_difficulties:
- dúvidas/erros relevantes

studio_feedback:
- o que funcionou ou não funcionou no Teste/Cartões/etc.

source_or_material_gaps:
- lacunas reais, se houver
END_REPORT
```

O relatório é opcional e não deve virar burocracia.

---

## 12. Smoke test desta versão

A versão `1.0.1` existe para testar uma UX mais simples.

Primeiro teste real:

1. abrir `Teste` no Estúdio;
2. deixar `Padrão` e `Médio (padrão)`;
3. não ficar alternando fontes manualmente;
4. escrever apenas:

> `Teste de Português no padrão TJSP/VUNESP das provas carregadas.`

5. gerar e responder algumas questões;
6. observar se linguagem, alternativas e dificuldade parecem compatíveis com o corpus;
7. trazer ao ChatGPT **somente o que parecer errado ou estranho**.

Não criar prompt gigante antes de descobrir um problema real.

---

## 13. Segurança epistemológica

Se as fontes não sustentarem uma afirmação:

- declarar a limitação;
- não inventar regra, gabarito ou frequência;
- não atribuir ao edital algo que veio apenas da análise do projeto;
- não usar provas antigas para sobrescrever o escopo vigente.

---

## 14. Mudança de interface do NotebookLM

NotebookLM é produto externo e a UI pode mudar. Se os controles do Estúdio forem diferentes em outro momento, manter os princípios desta metodologia e adaptar a operação à interface atual.

Prioridade permanente:

> **fidelidade ao corpus + baixa fricção de uso.**
