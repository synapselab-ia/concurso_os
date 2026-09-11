# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `1.0.2`  
**Status:** `content-rebuild-pending`  
**Release date:** `2026-09-11`

## Objetivo

Este pack separa o que é **conteúdo do estudante** do que é **backoffice** e do que é **instrução do chat**.

A versão `1.0.2` corrige a arquitetura de uso do NotebookLM após os smoke tests reais. A apostila/PDF ainda é a mesma distribuição de `1.0.0`; sua reconstrução qualitativa é a próxima ação canônica.

## Arquivos canônicos do pack

- `APOSTILA.md` — fonte autoral editável do material do estudante.
- `APOSTILA.pdf` — distribuição atual para o NotebookLM.
- `METODOLOGIA_NOTEBOOKLM.md` — **instrução exclusiva do chat**, não conteúdo.
- `ANALISE_BANCA.md` — backoffice editorial.
- `SOURCES.md` — proveniência/backoffice.
- `CHANGELOG.md` — histórico de versão/backoffice.

## Apostila PDF atual

A versão `1.0.2` não altera o PDF. Ele continua sendo o artefato validado originalmente em `1.0.0`:

- páginas: `8`;
- tamanho: `13950 bytes`;
- SHA-256: `e203e62c6be1207dc5ca475e61460d9619be4bfeeeeb32bcf90990b485e8cc23`;
- Git blob: `2287be2ba025228cc311722effc794fc9edf476f`.

**Importante:** o PDF atual não é considerado qualidade final para replicação. `APOSTILA-002` deverá reconstruí-lo.

## O que carregar no NotebookLM

Carregue somente:

1. `APOSTILA.pdf`
2. `METODOLOGIA_NOTEBOOKLM.md`

Não carregar por padrão:

- `ANALISE_BANCA.md`;
- `MANIFEST.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- edital e provas históricas apenas para dar contexto de projeto.

Esses documentos permanecem no GitHub/ChatGPT para análise, autoria e QA.

## Como selecionar as fontes

### Estúdio

Para `Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, Áudio, Apresentação, Infográfico e equivalentes:

```text
[x] APOSTILA.pdf
[ ] METODOLOGIA_NOTEBOOKLM.md
```

A metodologia deve ficar **desmarcada** para que o NotebookLM não produza questões ou cartões sobre as próprias instruções.

### Chat

Para tirar dúvidas, pedir explicação, fazer treino interativo, corrigir uma questão ou pedir relatório da sessão:

```text
[x] APOSTILA.pdf
[x] METODOLOGIA_NOTEBOOKLM.md
```

O chat deve usar a metodologia como comportamento e a apostila como conteúdo.

## O que os smoke tests mostraram

- Com a metodologia incluída no `Teste`, o NotebookLM gerou pergunta sobre a própria metodologia.
- Sem a metodologia, o `Teste` gerou pergunta conceitual diretamente baseada na apostila, confirmando que o recurso funciona como quiz sobre a fonte selecionada.
- No chat, a metodologia funcionou melhor: questão por vez, alternativas A–E, resposta + confiança e possibilidade de relatório da sessão.

Por isso, a V0.1 não tenta mais fazer um corpus misto cumprir todos os papéis.

## Uso cotidiano

### Para estudar com Estúdio

Escolha um recurso e deixe apenas a apostila marcada. Não precisa citar TJSP/VUNESP nem administrar documentação interna do projeto.

### Para usar o chat

Deixe apostila + metodologia marcadas e fale normalmente, por exemplo:

- `não entendi este tópico`
- `me explica por que a B está errada`
- `me testa nisso`
- `faz mais uma questão`
- `resume meus acertos, erros e dúvidas desta sessão`

## Múltiplos participantes

O mesmo pack pode alimentar notebooks separados para `p001`, `p002`, `p003` etc. O material é compartilhado; histórico pessoal pode permanecer isolado no notebook de cada participante.

## Próxima versão de conteúdo

A próxima mudança substancial deve reconstruir `APOSTILA.md` e `APOSTILA.pdf` para que sejam materiais fortes por si só e alimentem bem os recursos do NotebookLM.

Target recomendado após reconstrução: `2.0.0`.

## Limites

- não implementa mastery questão a questão;
- não mistura participantes;
- não presume que `Teste` nativo simula automaticamente a banca;
- não transforma backoffice em conteúdo de estudo;
- detalhes da UI do NotebookLM podem mudar.
