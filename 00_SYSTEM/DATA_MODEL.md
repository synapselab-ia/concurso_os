# DATA_MODEL

A V0.1 organiza **materiais, fontes, configuração de estudo e artefatos de prática**, não um LMS próprio. O modelo principal reflete a stack GitHub + ChatGPT + NotebookLM e separa material do estudante, instrução do tutor, documentação de engenharia editorial e avaliação de transferência.

## Competition

Define o concurso-alvo, edital/versão, banca, estrutura da prova, regras eliminatórias e referências de fonte. Não contém histórico individual de estudo.

## Subject

Unidade pedagógica usada para organizar notebooks e materiais (`portugues`, `direito-penal`, `matematica` etc.).

## SubjectPack

Unidade canônica de entrega de conteúdo da V0.1, identificada por `competition_id + subject_id + pack_version`.

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

O backoffice pode influenciar a apostila e as questões autorais sem aparecer como conteúdo explícito para o aluno.

## SourceRecord

Registro de uma fonte usada para sustentar escopo, conteúdo ou análise. Deve preservar identidade e proveniência suficientes para revisão: `source_id`, tipo, autoridade quando aplicável, título/arquivo, versão ou data relevante e, quando disponível, hash.

Binários-fonte de terceiros não precisam ser republicados no repositório público.

## BancaAnalysis

Análise empírica separada do conteúdo didático. Frequências, categorias e padrões só podem ser promovidos a material canônico quando houver método reproduzível e limites da amostra explícitos.

Sua função é orientar autoria/QA de apostilas **e** calibrar simulados. Não é, por padrão, fonte de estudo no NotebookLM.

## QuestionItem

Questão autoral reutilizável. O schema canônico é `schemas/question_item.schema.json`.

Cada item declara `mode`:

### `microdrill`

Questão para aquisição, recuperação e aplicação curta.

Pode usar formato curto e não precisa reproduzir a estrutura integral da banca. Deve continuar correta, source-grounded quando aplicável e pedagogicamente útil.

### `simulation`

Questão destinada a simulado de transferência.

Exige formato coerente com o blueprint da prova, fidelidade maior ao estilo da banca e QA semântico específico. Para TJSP Escrevente 2025, questão objetiva de simulation usa cinco alternativas.

Itens podem ser armazenados em lotes:

```text
question_banks/<competition_id>/<subject_id>/batches/<batch_id>.json
```

O banco é incremental. Não existe obrigação de pré-gerar grande volume antes de existir uso concreto.

## Simulation

Artefato composto que representa uma aplicação de prova. O schema do manifest é `schemas/simulation.schema.json`.

Tipos previstos:

- `weekly_full_objective` — simulado dominical integral da parte objetiva;
- `partial_pilot` — piloto parcial usado em desenvolvimento/calibração;
- `full_dress_rehearsal` — ensaio mais completo, podendo incluir redação e demais condições.

Convenção:

```text
simulations/<competition_id>/<simulation_id>/
├── MANIFEST.json
├── SIMULADO.md
├── GABARITO.md
└── QA.md
```

`SIMULADO.md` e `GABARITO.md` ficam separados para evitar vazamento durante a aplicação.

## SimulationBlueprint

Configuração específica da competição que traduz `BLUEPRINT.json` para a rotina de simulado sem alterar o edital.

Para TJSP Escrevente 2025:

- arquivo: `competitions/tjsp-escrevente-2025/SIMULATION_BLUEPRINT.json`;
- total objetivo: 70;
- distribuição deve permanecer coerente com `BLUEPRINT.json`;
- autoria é original e calibrada pelas provas/análises históricas;
- redação não faz parte automaticamente do simulado objetivo semanal;
- o ciclo semanal ali definido é um default da competição, não uma regra rígida por participante.

## PracticeCycle

Configuração operacional de cadência.

A competição pode declarar um padrão, e cada `Enrollment` pode herdá-lo ou sobrescrevê-lo declarativamente em `CONFIG.json`. Comportamento específico não deve ser implementado por condicionais de identidade.

Para TJSP Escrevente 2025, o default regular é:

```text
segunda–sábado → microdrill
domingo → weekly_full_objective
resultado do domingo → prioridade da semana seguinte
```

O ciclo está definido em `PRACTICE_PROTOCOL.md` e no `SIMULATION_BLUEPRINT.json` da competição.

## Participant

Perfil público mínimo (`p001`, `p002`, ...), usado apenas quando a organização por participante for útil. O mesmo SubjectPack pode alimentar notebooks separados sem duplicar o material compartilhado.

## Enrollment

Vínculo entre participante e competição. Pode carregar configuração declarativa de estudo, inclusive `practice_cycle` quando houver necessidade de sobrescrever o default da competição.

A ausência de override significa herança do padrão da competição. Isso preserva o kernel sem condicionais por pessoa estabelecido em DEC-0008.

## SessionFeedback

Resumo opcional vindo do chat do NotebookLM quando houver utilidade longitudinal ou editorial. Pode conter tópicos trabalhados, acertos, erros, dúvidas, padrões de confusão e lacunas do material.

Não exige persistência questão a questão.

## SimulationResult

Resultado individual opcional de uma aplicação.

Pode conter totais, desempenho por bloco, tempo, categorias de erro e prioridades para a semana seguinte. **Não deve ser publicado automaticamente** no repositório público.

A persistência individual continua opcional; o sistema pode usar o resultado apenas na conversa/sessão para orientar o próximo ciclo.

## Telemetria experimental

`Competency`, `EvidenceEvent` e `DerivedState` continuam compatíveis com experimentos futuros, mas **não fazem parte do caminho crítico da V0.1**.

## Separações obrigatórias

```text
fonte de verdade
!= análise da banca
!= material didático
!= instrução do tutor
!= questão autoral
!= simulado
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

Além disso:

```text
microdrill
!= simulation
```

porque medem e treinam capacidades diferentes.

## IDs e versões

- concursos usam slug versionado;
- matérias usam slug estável;
- participantes usam `pNNN`;
- fontes usam `source_id` estável;
- SubjectPacks usam versão explícita e changelog;
- questões usam `question_id` estável dentro do contexto de autoria;
- simulados usam `simulation_id` estável e data/aplicação quando necessário.
