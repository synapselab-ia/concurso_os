# DATA_MODEL

A V0.1 organiza **materiais, fontes e configuração de estudo**, não um LMS próprio. O modelo principal reflete a stack GitHub + ChatGPT + NotebookLM e separa material do estudante, instrução do tutor e documentação de engenharia editorial.

## Competition

Define o concurso-alvo, edital/versão, banca, estrutura da prova, regras eliminatórias e referências de fonte. Não contém histórico individual de estudo.

## Subject

Unidade pedagógica usada para organizar notebooks e materiais (`portugues`, `direito-penal`, `matematica` etc.).

## SubjectPack

Unidade canônica de entrega da V0.1, identificada por `competition_id + subject_id + pack_version`.

Arquivos mínimos:

- `MANIFEST.md`;
- `APOSTILA.md`;
- `APOSTILA.pdf`;
- `ANALISE_BANCA.md`;
- `METODOLOGIA_NOTEBOOKLM.md`;
- `SOURCES.md`;
- `CHANGELOG.md`.

Esses arquivos não têm o mesmo papel. Cada pack possui três classes lógicas.

### StudentContent

Material que pode ser estudado diretamente e usado pelo Estúdio do NotebookLM.

Na V0.1, o principal `StudentContent` é:

- `APOSTILA.pdf`.

`APOSTILA.md` é a fonte autoral editável correspondente.

### ConversationInstruction

Configuração versionada do comportamento do tutor no chat do NotebookLM.

- arquivo canônico: `METODOLOGIA_NOTEBOOKLM.md`;
- destino operacional preferido: configuração nativa da conversa (`Personalizado` ou equivalente);
- **não é fonte de conteúdo** e não deve ser carregada como documento estudável quando houver uma camada nativa de configuração do chat.

Uso esperado:

```text
NotebookLM sources = APOSTILA.pdf
Conversation config = conteúdo operacional de METODOLOGIA_NOTEBOOKLM.md
```

A sincronização dessa configuração é manual e acontece na criação do notebook ou quando a metodologia muda.

### BackofficeArtifact

Arquivos usados por ChatGPT/GitHub para pesquisa, autoria, proveniência e QA. Não são carregados no NotebookLM por padrão:

- `ANALISE_BANCA.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- `MANIFEST.md`;
- documentação de arquitetura/QA;
- registros de provas/fontes que sustentam a autoria.

O backoffice pode influenciar a apostila sem aparecer como conteúdo explícito para o aluno.

## SourceRecord

Registro de uma fonte usada para sustentar escopo, conteúdo ou análise. Deve preservar identidade e proveniência suficientes para revisão: `source_id`, tipo, autoridade quando aplicável, título/arquivo, versão ou data relevante e, quando disponível, hash.

Binários-fonte de terceiros não precisam ser republicados no repositório público.

## BancaAnalysis

Análise empírica separada do conteúdo didático. Frequências, categorias e padrões só podem ser promovidos a material canônico quando houver método reproduzível e limites da amostra explícitos.

Sua função é orientar autoria/QA. Não é, por padrão, fonte de estudo no NotebookLM.

## Participant

Perfil público mínimo (`p001`, `p002`, ...), usado apenas quando a organização por participante for útil. O mesmo SubjectPack pode alimentar notebooks separados sem duplicar o material compartilhado.

## SessionFeedback

Resumo opcional vindo do chat do NotebookLM quando houver utilidade longitudinal ou editorial. Pode conter tópicos trabalhados, acertos, erros, dúvidas, padrões de confusão e lacunas do material.

Não exige persistência questão a questão.

## Telemetria experimental

`Enrollment`, `Competency`, `EvidenceEvent` e `DerivedState` continuam compatíveis com experimentos futuros, mas **não fazem parte do caminho crítico da V0.1**.

## Separações obrigatórias

```text
fonte de verdade
!= análise da banca
!= material didático
!= instrução do tutor
!= feedback individual
```

Também:

```text
arquivo existente no SubjectPack
!= arquivo que deve ser carregado como fonte no NotebookLM
```

E:

```text
instrução versionada no GitHub
!= fonte estudável
```

## IDs e versões

- concursos usam slug versionado;
- matérias usam slug estável;
- participantes usam `pNNN`;
- fontes usam `source_id` estável;
- SubjectPacks usam versão explícita e changelog.
