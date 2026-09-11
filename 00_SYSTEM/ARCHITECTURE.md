# ARCHITECTURE

## Visão

A arquitetura da V0.1 é uma cadeia editorial e pedagógica, não um LMS próprio.

```text
fontes oficiais + provas + análise empírica
                  ↓
               ChatGPT
        pesquisa / autoria / QA
                  ↓
                GitHub
        backoffice + SubjectPack
                  ↓
       distribuição manual mínima
                  ↓
              NotebookLM
       APOSTILA + instrução de chat
```

## Papéis

### GitHub

Fonte canônica de:

- edital e mapa do concurso;
- registro de fontes;
- provas e análise de banca referenciadas;
- apostilas editáveis e PDFs de distribuição;
- metodologia/instruções de chat do NotebookLM;
- manifests/changelogs;
- QA;
- continuidade entre chats.

GitHub é o **backoffice intelectual** do sistema. Nem tudo que existe no repositório deve ser carregado no NotebookLM.

### ChatGPT

Responsável por:

- pesquisar e verificar;
- analisar edital, provas e banca;
- decidir prioridades editoriais;
- escrever e reescrever apostilas;
- produzir exemplos e exercícios;
- fazer QA source-grounded;
- manter a continuidade canônica no GitHub.

A análise de banca deve melhorar silenciosamente o material do estudante. Não é necessário transformar o aluno em leitor da análise da análise.

### NotebookLM

Ambiente principal de estudo por matéria.

A unidade recomendada é um notebook por matéria e, quando houver interesse em histórico individual, por participante.

O NotebookLM recebe dois tipos diferentes de fonte:

#### 1. Conteúdo do estudante

`APOSTILA.pdf` é a fonte principal. Ela deve ser escrita para suportar leitura, consulta, Testes, Cartões, Mapas mentais, Relatórios, Áudio, Apresentações e demais artefatos nativos.

#### 2. Instrução operacional do chat

`METODOLOGIA_NOTEBOOKLM.md` existe apenas para orientar o **chat**: dúvidas, treino interativo, correção, confiança, reteste local e relatório de sessão.

Ela não é conteúdo da matéria.

## Regra de seleção de fontes

A V0.1 aceita uma única distinção operacional simples porque os smoke tests mostraram utilidade real:

```text
ESTÚDIO
→ selecionar APOSTILA.pdf
→ desmarcar METODOLOGIA_NOTEBOOKLM.md

CHAT
→ selecionar APOSTILA.pdf + METODOLOGIA_NOTEBOOKLM.md
```

Não carregar por padrão no notebook:

- `ANALISE_BANCA.md`;
- `MANIFEST.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- documentação de arquitetura/QA;
- provas históricas e edital apenas para ensinar ao NotebookLM como o projeto funciona.

Fontes oficiais adicionais podem ser carregadas quando uma matéria realmente exigir consulta literal, normativa ou técnica; isso deve ser uma necessidade pedagógica concreta, não rotina administrativa.

## O que aprendemos com o smoke test

O `Teste` nativo do NotebookLM tratou documentos selecionados como **conteúdo a ser perguntado**. Com metodologia selecionada, gerou questão sobre a própria metodologia; sem ela, gerou questão explicitamente sobre conceitos da apostila. Isso é comportamento útil para revisão do conteúdo, mas não prova que o recurso simula automaticamente o estilo de uma banca.

Já o chat, quando recebeu a metodologia, respeitou bem instruções como uma questão por vez, alternativas A–E, resposta + confiança e possibilidade de relatório da sessão.

Por isso, a arquitetura deixa de tentar fazer um corpus misto cumprir todos os papéis ao mesmo tempo.

## Unidade canônica de entrega

O objeto principal continua sendo o `SubjectPack`:

```text
Competition + Subject
        ↓
MANIFEST
APOSTILA.md / APOSTILA.pdf      # produto do estudante
METODOLOGIA_NOTEBOOKLM.md       # instrução de chat
ANALISE_BANCA.md                # backoffice
SOURCES.md                      # backoffice
CHANGELOG.md                    # backoffice
```

## Participantes

O material é compartilhável. Histórico de conversa, artefatos e relatórios pessoais podem permanecer em notebooks separados de `p001`, `p002`, etc.

## Evidência e scheduler

`EvidenceEvent`, mastery projection e scheduler próprio continuam fora do caminho crítico da V0.1. Se o chat do NotebookLM produzir um resumo útil de acertos, erros e dúvidas, o usuário pode exportá-lo ou trazê-lo ao ChatGPT sem registrar cada resposta no GitHub.

## Continuidade

Chats são descartáveis. Decisões, versões de pacote, estado de produção e próxima ação devem permanecer no repositório.

## Especificação detalhada

Ver `docs/STACK_NOTEBOOKLM.md`.
