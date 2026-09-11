# Stack de estudo — GitHub + ChatGPT + NotebookLM

## Princípio central

A V0.1 separa **engenharia editorial**, **conteúdo estudável** e **configuração do tutor**.

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

O estudante não deve estudar a documentação interna do projeto. O NotebookLM também não precisa inferir por conta própria qual arquivo é metodologia, qual é análise de banca e qual é conteúdo.

## Papéis da stack

### GitHub

Guarda o que precisa sobreviver a qualquer chat:

- edital e blueprint;
- registro de fontes;
- provas e análises;
- `ANALISE_BANCA.md`;
- `APOSTILA.md` e `APOSTILA.pdf`;
- `METODOLOGIA_NOTEBOOKLM.md` como configuração versionada do tutor;
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

Na V0.1, o NotebookLM recebe **conteúdo** e **comportamento do tutor** por canais diferentes:

```text
FONTES
APOSTILA.pdf
= conteúdo da matéria

CONFIGURAÇÃO DA CONVERSA
conteúdo operacional de METODOLOGIA_NOTEBOOKLM.md
= comportamento do tutor
```

## Instalação recomendada

### 1. Fontes

Carregar como fonte, por padrão:

```text
APOSTILA.pdf
```

Não carregar `METODOLOGIA_NOTEBOOKLM.md` como fonte quando houver configuração nativa da conversa.

### 2. Configurar as conversas

Na interface observada do NotebookLM existe uma configuração equivalente a:

```text
Configurar as conversas
→ Personalizado
→ definir meta, estilo ou papel na conversa
```

Colar ali o texto operacional mantido em `METODOLOGIA_NOTEBOOKLM.md`.

No estado observado, a interface também oferece escolha de tamanho da resposta. O default do projeto é:

```text
Tamanho da resposta = Padrão
```

Só alterar se houver necessidade concreta.

### 3. Uso cotidiano

Depois da instalação:

- não marcar/desmarcar metodologia;
- não administrar backoffice dentro do notebook;
- Estúdio e chat usam a mesma apostila;
- o chat recebe suas regras pela configuração da conversa.

## O que NÃO carregar no NotebookLM por padrão

Estes arquivos permanecem no GitHub/ChatGPT:

- `METODOLOGIA_NOTEBOOKLM.md` como fonte;
- `ANALISE_BANCA.md`;
- `SOURCES.md`;
- `MANIFEST.md`;
- `CHANGELOG.md`;
- documentação do sistema e QA;
- provas históricas e edital apenas para ensinar ao NotebookLM como o projeto funciona.

Uma fonte oficial adicional só deve entrar no notebook quando tiver valor direto de estudo, por exemplo lei seca em Direito ou documentação técnica em Informática. Isso é exceção pedagógica concreta, não regra administrativa.

## Por que essa separação existe

Os smoke tests de Português mostraram três fatos úteis:

1. com a metodologia selecionada no `Teste`, o NotebookLM gerou pergunta sobre a própria metodologia;
2. sem a metodologia, o `Teste` passou a perguntar conceitos da apostila — comportamento coerente com um quiz sobre a fonte selecionada;
3. no chat, instruções operacionais funcionaram bem para questão por vez, alternativas A–E, confiança, correção e relatório de sessão.

Depois foi observada uma camada própria de `Configurar as conversas → Personalizado`. Essa camada resolve melhor o problema: **comportamento do chat não precisa ocupar um slot de fonte**.

Portanto, a solução não é um superprompt nem um corpus maior. É:

```text
apostila melhor
+
corpus limpo
+
configuração nativa do tutor
```

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

É a **configuração versionada do tutor**.

O arquivo deve conter instruções para:

- responder dúvidas;
- conduzir treino interativo;
- esperar a tentativa antes da correção;
- usar confiança quando informada;
- comparar alternativas próximas;
- fazer reteste curto quando útil;
- acompanhar a sessão corrente;
- gerar `SESSION_REPORT` sob demanda.

O destino operacional preferido é a configuração `Personalizado` da conversa, não a lista de fontes.

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

A configuração do tutor pode manter contexto da sessão corrente, mas o sistema não presume banco de dados permanente dentro do NotebookLM.

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

O SubjectPack é compartilhável. Se participantes diferentes quiserem preservar histórico pessoal no NotebookLM, usam notebooks separados baseados na mesma apostila e na mesma configuração canônica do tutor.

## Sincronização

NotebookLM não é espelho do GitHub.

Quando o pack mudar:

1. atualizar versão e changelog;
2. regenerar `APOSTILA.pdf` quando a apostila mudar;
3. substituir a apostila no notebook apenas quando o PDF mudar;
4. atualizar a configuração `Personalizado` somente quando `METODOLOGIA_NOTEBOOKLM.md` mudar;
5. não reenviar documentos de backoffice.

## Deriva de UI

NotebookLM é produto externo. O nome `Configurar as conversas`, a opção `Personalizado`, o limite de caracteres e os controles de tamanho podem mudar.

O princípio arquitetural é mais estável que a UI:

> comportamento do tutor deve usar uma camada de configuração separada do corpus estudável sempre que a ferramenta oferecer essa possibilidade.

## Definition of Done da matéria

Uma matéria está pronta para replicação quando:

1. a apostila é material de estudo forte por si só;
2. o Estúdio gera artefatos úteis usando apenas a apostila;
3. o chat usa a apostila como corpus e a configuração nativa como comportamento, sem transformar metodologia em matéria;
4. dúvidas e sessões podem ser resumidas sem infraestrutura própria;
5. o backoffice permite auditar e atualizar o material em qualquer chat novo;
6. o uso cotidiano não exige alternar fontes operacionais.
