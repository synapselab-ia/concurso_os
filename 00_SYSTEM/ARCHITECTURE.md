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
      APOSTILA como fonte de estudo
      + configuração nativa do chat
```

## Papéis

### GitHub

Fonte canônica de:

- edital e mapa do concurso;
- registro de fontes;
- provas e análise de banca referenciadas;
- apostilas editáveis e PDFs de distribuição;
- instruções versionadas para o chat do NotebookLM;
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

O notebook separa duas camadas:

#### 1. Corpus estudável

`APOSTILA.pdf` é a fonte principal. Ela deve ser escrita para suportar leitura, consulta, Testes, Cartões, Mapas mentais, Relatórios, Áudio, Apresentações e demais artefatos nativos.

#### 2. Configuração do tutor

`METODOLOGIA_NOTEBOOKLM.md` é o registro canônico, no GitHub, das instruções de comportamento do chat: dúvidas, treino interativo, correção, confiança, reteste local e relatório de sessão.

Quando a interface do NotebookLM oferecer uma configuração nativa equivalente a `Configurar as conversas → Personalizado`, o conteúdo operacional da metodologia deve ser colocado **nessa configuração**, e não carregado como fonte.

A metodologia continua versionada no SubjectPack, mas não faz parte do corpus estudável.

## Regra operacional de instalação

Padrão V0.1 observado e preferido:

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf

CONFIGURAÇÃO DA CONVERSA
→ Personalizado
→ colar as instruções canônicas de METODOLOGIA_NOTEBOOKLM.md
→ tamanho de resposta: Padrão, salvo necessidade concreta
```

Não carregar por padrão no notebook:

- `METODOLOGIA_NOTEBOOKLM.md` como fonte;
- `ANALISE_BANCA.md`;
- `MANIFEST.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- documentação de arquitetura/QA;
- provas históricas e edital apenas para ensinar ao NotebookLM como o projeto funciona.

Fontes oficiais adicionais podem ser carregadas quando uma matéria realmente exigir consulta literal, normativa ou técnica; isso deve ser uma necessidade pedagógica concreta, não rotina administrativa.

## O que aprendemos com os smoke tests

O `Teste` nativo do NotebookLM tratou documentos selecionados como **conteúdo a ser perguntado**. Com metodologia selecionada, gerou questão sobre a própria metodologia; sem ela, gerou questão explicitamente sobre conceitos da apostila.

Já o chat respeitou bem instruções operacionais como uma questão por vez, alternativas A–E, resposta + confiança e possibilidade de relatório da sessão.

Depois, a interface mostrou uma camada própria de personalização da conversa. Isso elimina a necessidade de usar a metodologia como fonte apenas para controlar o chat.

Por isso, a arquitetura final da V0.1 separa:

```text
conteúdo estudável → fontes
comportamento do tutor → configuração da conversa
engenharia editorial → GitHub/ChatGPT
```

## Unidade canônica de entrega

O objeto principal continua sendo o `SubjectPack`:

```text
Competition + Subject
        ↓
MANIFEST
APOSTILA.md / APOSTILA.pdf      # produto do estudante
METODOLOGIA_NOTEBOOKLM.md       # configuração versionada do chat
ANALISE_BANCA.md                # backoffice
SOURCES.md                      # backoffice
CHANGELOG.md                    # backoffice
```

## Participantes

O material é compartilhável. Histórico de conversa, artefatos e relatórios pessoais podem permanecer em notebooks separados de `p001`, `p002`, etc.

## Evidência e scheduler

`EvidenceEvent`, mastery projection e scheduler próprio continuam fora do caminho crítico da V0.1. Se o chat do NotebookLM produzir um resumo útil de acertos, erros e dúvidas, o usuário pode exportá-lo ou trazê-lo ao ChatGPT sem registrar cada resposta no GitHub.

## Deriva de produto externo

NotebookLM é produto externo. Nomes, limites e posição dos controles de personalização podem mudar.

A arquitetura não depende do texto exato do botão. O princípio permanente é:

> sempre que houver uma camada nativa de configuração do chat, instruções de comportamento devem ficar fora do corpus estudável.

## Continuidade

Chats são descartáveis. Decisões, versões de pacote, estado de produção e próxima ação devem permanecer no repositório.

## Especificação detalhada

Ver `docs/STACK_NOTEBOOKLM.md`.
