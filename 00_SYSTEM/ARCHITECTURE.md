# ARCHITECTURE

## Visão

A arquitetura da V0.1 é uma cadeia editorial e pedagógica, não um LMS próprio.

```text
fontes oficiais + provas + análise empírica
                  ↓
               ChatGPT
        pesquisa / autoria / QA
                  ↓
     APOSTILA_AUTHORING_PROTOCOL
                  ↓
                GitHub
        backoffice + SubjectPack
                  ↓
       distribuição manual mínima
                  ↓
              NotebookLM
      APOSTILA como fonte de estudo
      + configuração nativa do chat

                +
       PRACTICE_PROTOCOL
                  ↓
microdrill durante a semana
                  +
simulado autoral dominical
                  ↓
erros/prioridades da semana seguinte
```

## Papéis

### GitHub

Fonte canônica de:

- edital e mapa do concurso;
- registro de fontes;
- provas e análise de banca referenciadas;
- protocolo de autoria das apostilas;
- apostilas editáveis e PDFs de distribuição;
- instruções versionadas para o chat do NotebookLM;
- manifests/changelogs;
- protocolos e blueprints de prática/simulado;
- lotes de questões autorais e simulados quando persistidos;
- QA;
- continuidade entre chats.

GitHub é o **backoffice intelectual** do sistema. Nem tudo que existe no repositório deve ser carregado no NotebookLM.

### ChatGPT

Responsável por:

- pesquisar e verificar;
- analisar edital, provas e banca;
- decidir prioridades editoriais;
- aplicar `APOSTILA_AUTHORING_PROTOCOL.md`;
- escrever e reescrever apostilas;
- produzir exemplos e exercícios;
- produzir microdrills e lotes autorais de simulado quando solicitado;
- fazer QA source-grounded item a item e de conjunto;
- montar simulados coerentes com o blueprint;
- manter a continuidade canônica no GitHub.

A análise de banca deve melhorar silenciosamente o material e as questões. Não é necessário transformar o aluno em leitor da análise da análise.

### Protocolo de autoria

`00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` é a camada canônica entre pesquisa/análise e release de uma apostila.

Ele exige:

```text
escopo e fontes
→ matriz de cobertura/autoria
→ sumário pedagógico
→ redação adaptada ao domínio
→ QA editorial
→ QA NotebookLM
→ PDF + QA textual/visual
→ release
```

O protocolo padroniza o processo de qualidade, não o formato de todas as matérias. Direito, Português, Matemática, RLM, Informática, Atualidades e Redação têm perfis didáticos próprios dentro do mesmo sistema de gates.

### Prática em duas lanes

`00_SYSTEM/PRACTICE_PROTOCOL.md` separa:

```text
microdrill
→ aquisição / recuperação / discriminação rápida

simulation
→ transferência / formato real / gestão de prova
```

O simulado não é uma versão “maior” do microdrill. Ele mede outra camada de competência.

`00_SYSTEM/SIMULATION_PROTOCOL.md` define autoria em lotes, QA item a item, QA de conjunto, lock, aplicação e feedback.

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
- `APOSTILA_AUTHORING_PROTOCOL.md`;
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

Os smoke tests de Português 2.0.0 também mostraram que o Teste nativo é útil para recuperação/aplicação curta, mas não precisa reproduzir a prova TJSP/VUNESP. Por isso a fidelidade de banca passa a ser responsabilidade do pipeline de `simulation`, não do NotebookLM nativo.

A arquitetura final da V0.1 separa:

```text
conteúdo estudável → fontes
comportamento do tutor → configuração da conversa
aquisição rápida → microdrills / NotebookLM
transferência para a prova → simulados autorais auditados
engenharia editorial → GitHub/ChatGPT + protocolos
```

## Unidade canônica de entrega

O objeto principal de conteúdo continua sendo o `SubjectPack`:

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

Questões e simulados são artefatos de prática separados do SubjectPack para permitir reutilização e composição entre matérias sem poluir o corpus do NotebookLM.

## Participantes

O material é compartilhável. Histórico de conversa, artefatos e relatórios pessoais podem permanecer em notebooks separados de `p001`, `p002`, etc.

Resultados individuais de simulados não são publicados automaticamente no repositório público.

## Evidência e scheduler

`EvidenceEvent`, mastery projection e scheduler próprio continuam fora do caminho crítico da V0.1. O loop mínimo necessário é mais simples: desempenho de simulado pode gerar prioridades de microdrill para a semana seguinte sem exigir telemetria questão a questão permanente.

Se o chat do NotebookLM produzir um resumo útil de acertos, erros e dúvidas, o usuário pode exportá-lo ou trazê-lo ao ChatGPT.

## Deriva de produto externo

NotebookLM é produto externo. Nomes, limites e posição dos controles de personalização podem mudar.

A arquitetura não depende do texto exato do botão. O princípio permanente é:

> sempre que houver uma camada nativa de configuração do chat, instruções de comportamento devem ficar fora do corpus estudável sempre que possível.

## Continuidade

Chats são descartáveis. Decisões, versões de pacote, estado de produção, etapa do protocolo de autoria, blueprints de simulado e próxima ação devem permanecer no repositório.

## Especificação detalhada

Ver `docs/STACK_NOTEBOOKLM.md`.
