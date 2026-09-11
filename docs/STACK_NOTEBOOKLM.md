# Stack de estudo — GitHub + ChatGPT + NotebookLM

## Princípio central

A V0.1 separa **engenharia editorial** de **material do estudante**.

```text
EDITAL + PROVAS + FONTES OFICIAIS
              ↓
          ChatGPT
   análise + autoria + QA
              ↓
           GitHub
  backoffice + SubjectPack
              ↓
        distribuição mínima
              ↓
         NotebookLM
```

O estudante não deve estudar a documentação interna do projeto. O NotebookLM não precisa entender por conta própria qual arquivo é metodologia, qual é análise de banca e qual é conteúdo.

## Papéis da stack

### GitHub

Guarda o que precisa sobreviver a qualquer chat:

- edital e blueprint;
- registro de fontes;
- provas e análises;
- `ANALISE_BANCA.md`;
- `APOSTILA.md` e `APOSTILA.pdf`;
- `METODOLOGIA_NOTEBOOKLM.md`;
- manifest/changelog;
- QA e continuidade.

### ChatGPT

É a camada de engenharia intelectual:

- lê edital, provas e fontes;
- verifica fatos;
- analisa a banca;
- decide cobertura e prioridades;
- escreve uma apostila realmente boa;
- produz exemplos/exercícios;
- revisa e versiona o material;
- integra feedback vindo do NotebookLM.

### NotebookLM

É o ambiente de estudo da matéria.

Na V0.1, ele recebe dois papéis de fonte claramente separados:

```text
APOSTILA.pdf
= conteúdo da matéria

METODOLOGIA_NOTEBOOKLM.md
= instrução do chat
```

## Regra operacional no NotebookLM

### Para o Estúdio

Ao criar `Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, resumo em áudio/vídeo, apresentação, infográfico ou artefato equivalente:

```text
selecionar APOSTILA.pdf
DESMARCAR METODOLOGIA_NOTEBOOKLM.md
```

O objetivo é fazer o Estúdio trabalhar sobre a matéria, não sobre instruções operacionais.

### Para o chat

Ao usar o chat para dúvida, explicação, treino interativo, correção ou relatório de sessão:

```text
selecionar APOSTILA.pdf
selecionar METODOLOGIA_NOTEBOOKLM.md
```

O chat deve tratar a metodologia como instrução, nunca como conteúdo que o aluno precisa memorizar.

## O que NÃO carregar no NotebookLM por padrão

Estes arquivos permanecem no GitHub/ChatGPT:

- `ANALISE_BANCA.md`;
- `SOURCES.md`;
- `MANIFEST.md`;
- `CHANGELOG.md`;
- documentação do sistema e QA;
- provas históricas e edital apenas para ensinar ao NotebookLM como o projeto funciona.

Uma fonte oficial adicional só deve entrar no notebook quando tiver valor direto de estudo, por exemplo lei seca em Direito ou documentação técnica em Informática. Isso é exceção pedagógica concreta, não regra administrativa.

## Por que essa separação existe

O smoke test de Português mostrou dois comportamentos:

1. com a metodologia selecionada no `Teste`, o NotebookLM gerou pergunta sobre a própria metodologia;
2. sem a metodologia, o `Teste` passou a perguntar conceitos da apostila — comportamento coerente com um quiz sobre a fonte selecionada, mas não prova de simulação automática da banca.

Já o chat respeitou bem instruções como:

- uma questão por vez;
- alternativas A–E;
- aguardar resposta;
- considerar confiança;
- corrigir de forma diagnóstica;
- gerar relatório de acertos/erros/dúvidas.

Portanto, a solução não é um superprompt nem um corpus maior. É **uma apostila melhor + papéis de fonte separados**.

## SubjectPack

Cada matéria mantém no GitHub:

```text
materials/<competition_id>/<subject_id>/
├── MANIFEST.md
├── APOSTILA.md
├── APOSTILA.pdf
├── ANALISE_BANCA.md
├── METODOLOGIA_NOTEBOOKLM.md
├── SOURCES.md
└── CHANGELOG.md
```

### APOSTILA.md / APOSTILA.pdf

É o produto principal do estudante.

A apostila deve ser suficientemente boa para o NotebookLM gerar artefatos úteis sem depender da documentação de bastidores. Deve priorizar:

- organização clara;
- explicações completas, mas sem enciclopedismo;
- definições precisas;
- distinções entre conceitos próximos;
- tabelas quando realmente ajudam;
- exemplos autorais;
- contraexemplos;
- casos-limite;
- exercícios e aplicações curtas;
- checklists e sínteses;
- terminologia consistente;
- estrutura semântica boa para recuperação pelo NotebookLM.

A influência do edital e da banca deve aparecer principalmente na **seleção, profundidade, exemplos e ênfases**, e não em frases repetitivas como “a VUNESP cobra...” ou “segundo o TJSP...”. A rastreabilidade dessas escolhas fica no backoffice.

### ANALISE_BANCA.md

Backoffice. Sustenta decisões editoriais e QA. Não é fonte de estudo padrão.

### METODOLOGIA_NOTEBOOKLM.md

Instrução exclusiva do chat.

Ela deve dizer ao chat como:

- responder dúvidas;
- conduzir treino interativo;
- esperar a tentativa antes da correção;
- usar confiança quando informada;
- comparar alternativas próximas;
- fazer reteste curto quando útil;
- acompanhar a sessão corrente;
- gerar `SESSION_REPORT` sob demanda.

Ela não deve conter conteúdo programático desnecessário nem tentar controlar os geradores do Estúdio.

### MANIFEST.md

Explica ao usuário/agente como montar o notebook e qual versão está vigente.

### SOURCES / CHANGELOG

Backoffice de proveniência e versão.

## Uso do Estúdio

O Estúdio é útil justamente porque a apostila deve ser boa o bastante para alimentá-lo.

### Teste

Usar como quiz/revisão sobre o conteúdo da apostila. Não assumir, sem validação empírica, que o botão reproduz exatamente uma banca específica.

### Cartões

Usar para definições, regras, distinções, exceções e pontos de recuperação rápida.

### Mapa mental

Usar para visualizar a estrutura da matéria.

### Relatórios / Áudio / Apresentações / Infográficos / Tabelas

Usar livremente quando agregarem valor. A fonte continua sendo a apostila, não os documentos de engenharia do projeto.

## Uso do chat

O chat é especialmente útil para:

- “não entendi este tópico”;
- “por que esta alternativa está errada?”;
- “compare B e D”;
- “me dê outro exemplo”;
- “me teste nisso”;
- “faça um reteste”;
- “resuma meus acertos, erros e dúvidas desta sessão”.

A metodologia pode manter contexto da sessão corrente, mas o sistema não presume banco de dados permanente dentro do NotebookLM.

## SESSION_REPORT opcional

Quando o usuário quiser preservar a sessão:

```text
SESSION_REPORT
participant: pNNN ou não informado
competition: <id>
subject: <id>
pack_version: <version>
date: YYYY-MM-DD

covered:
- tópicos trabalhados

performance:
- acertos firmes
- acertos com dúvida
- erros
- chutes, se observados

main_doubts:
- confusões relevantes

recommended_review:
- pontos a revisar

material_feedback:
- lacunas ou trechos insuficientes da apostila, se houver
END_REPORT
```

O relatório é opcional. Não registrar cada resposta no GitHub por padrão.

## Múltiplos participantes

O SubjectPack é compartilhável. Se Lucas, Duda ou outra pessoa quiserem preservar histórico pessoal no NotebookLM, usam notebooks separados baseados na mesma apostila/metodologia.

## Sincronização

NotebookLM não é espelho do GitHub.

Quando o pack mudar:

1. atualizar versão e changelog;
2. regenerar `APOSTILA.pdf` quando a apostila mudar;
3. substituir no notebook apenas os arquivos distribuídos que mudaram;
4. não reenviar documentos de backoffice.

## Definition of Done da matéria

Uma matéria está pronta para replicação quando:

1. a apostila é material de estudo forte por si só;
2. o Estúdio gera artefatos úteis usando apenas a apostila;
3. o chat usa apostila + metodologia sem perguntar sobre a metodologia;
4. dúvidas e sessões podem ser resumidas sem infraestrutura própria;
5. o backoffice permite auditar e atualizar o material em qualquer chat novo.
