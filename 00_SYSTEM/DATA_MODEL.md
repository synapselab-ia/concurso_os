# DATA_MODEL

A V0.1 organiza **materiais e fontes para estudo**, não um LMS próprio. O modelo principal deve refletir a stack GitHub + ChatGPT + NotebookLM.

## Competition

Define o concurso-alvo, edital/versão, banca, estrutura da prova, regras eliminatórias e referências de fonte. Não contém histórico individual de estudo.

## Subject

Unidade pedagógica usada para organizar os notebooks e materiais (`portugues`, `direito-penal`, `matematica` etc.). Um concurso referencia as matérias exigidas no edital.

## SubjectPack

Unidade canônica de entrega da V0.1. É identificado por `competition_id + subject_id + pack_version` e contém, no mínimo:

- `MANIFEST.md`;
- `APOSTILA.md`;
- `APOSTILA.pdf`;
- `ANALISE_BANCA.md`;
- `METODOLOGIA_NOTEBOOKLM.md`;
- `SOURCES.md`;
- `CHANGELOG.md`.

O GitHub guarda a versão canônica; o NotebookLM recebe uma distribuição manual versionada.

## SourceRecord

Registro de uma fonte usada para sustentar escopo, conteúdo ou análise. Deve preservar identidade e proveniência suficientes para revisão: `source_id`, tipo, autoridade quando aplicável, título/arquivo, versão ou data relevante e, quando disponível, hash. Binários-fonte de terceiros não precisam ser republicados no repositório público.

## BancaAnalysis

Análise empírica separada do conteúdo normativo/didático. Frequências, categorias e padrões só podem ser promovidos a material canônico quando houver método reproduzível e limites da amostra explícitos.

## Participant

Perfil público mínimo (`p001`, `p002`, ...), usado apenas quando a organização por participante for útil. O mesmo SubjectPack pode alimentar notebooks separados sem duplicar o material compartilhado. Não armazenar dados sensíveis ou desnecessários.

## SessionFeedback

Resumo opcional trazido do NotebookLM para o ChatGPT quando houver utilidade longitudinal ou editorial. Pode registrar tópicos trabalhados, padrões de erro, lacunas de fonte e feedback sobre material. Não exige persistência de cada questão respondida.

## Telemetria experimental

`Enrollment`, `Competency`, `EvidenceEvent` e `DerivedState` permanecem compatíveis com experimentos futuros, mas **não fazem parte do caminho crítico da V0.1**. Nenhuma dessas entidades deve bloquear produção, distribuição ou uso de SubjectPacks.

## Separações obrigatórias

```text
fonte de verdade
!= análise da banca
!= material didático
!= feedback individual
```

Dificuldade de um participante não altera automaticamente verdade curricular nem análise da banca.

## IDs e versões

- concursos usam slug versionado;
- matérias usam slug estável;
- participantes usam `pNNN`;
- fontes usam `source_id` estável;
- SubjectPacks usam versionamento explícito e changelog.
