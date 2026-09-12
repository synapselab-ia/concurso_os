# PROJECT_SPEC

## Missão

Construir um sistema de preparação para concursos assistido por IA em que o GitHub seja a memória canônica de análise e materiais, o ChatGPT seja a camada de pesquisa/autoria/QA e o NotebookLM seja o ambiente de estudo por matéria.

## Objetivo da V0.1

Produzir e versionar `SubjectPacks` reutilizáveis por matéria. O produto principal para o estudante é uma **apostila forte, autocontida e adequada aos recursos do NotebookLM**. Edital, provas, análise de banca, fontes, QA e decisões editoriais permanecem no GitHub como backoffice do projeto.

A criação e reconstrução substancial de apostilas segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, que padroniza cobertura, processo editorial e QA sem impor o mesmo formato didático a matérias diferentes.

Cada pack também contém `METODOLOGIA_NOTEBOOKLM.md`, mas esse arquivo tem função restrita: registrar a configuração de comportamento do **chat** do NotebookLM para dúvidas, treino interativo, correção e relatórios de sessão. Ele não é conteúdo da matéria nem deve ser carregado como fonte quando houver configuração nativa da conversa.

Um agente novo deve conseguir recuperar pelo GitHub tanto o estado da produção quanto a próxima ação sem depender de memória de chat.

## UX canônica no NotebookLM

A separação operacional é deliberadamente simples:

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf

CONFIGURAÇÃO DA CONVERSA
→ Configurar as conversas / Personalizado (ou equivalente)
→ colar as instruções canônicas de METODOLOGIA_NOTEBOOKLM.md
→ tamanho de resposta: Padrão por default
```

Assim:

- `Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, áudio, apresentação e demais recursos trabalham sobre o corpus didático limpo;
- o chat recebe comportamento de tutor pela camada nativa de configuração;
- não é necessário marcar/desmarcar a metodologia como fonte a cada uso.

Arquivos de engenharia editorial (`ANALISE_BANCA.md`, `SOURCES.md`, `CHANGELOG.md`, `MANIFEST.md`, provas históricas, protocolo de autoria e registros de QA) não entram no notebook por padrão. Eles existem para o ChatGPT produzir uma apostila melhor, não para virar matéria de quiz.

## Ciclo de prática

A V0.1 passa a distinguir explicitamente **aquisição** de **transferência**.

Para TJSP Escrevente 2025, o default da competição é:

```text
segunda–sábado
→ microdrills
→ muitas recuperações/aplicações curtas por hora
→ feedback imediato

domingo
→ simulado objetivo integral
→ distribuição e estilo da prova-alvo
→ correção após encerramento
→ erros alimentam a semana seguinte
```

Esse ciclo é configuração herdável: um `Enrollment` pode sobrescrevê-lo declarativamente sem condicional por identidade. Na ausência de override, vale o default da competição.

Para TJSP Escrevente 2025, o simulado dominical padrão contém as **70 questões objetivas** do blueprint vigente. O `Teste` nativo do NotebookLM continua sendo ferramenta de aquisição/revisão e não é tratado como simulador fiel da VUNESP.

Questões autorais reutilizáveis e simulados podem ser persistidos no GitHub quando isso melhorar rastreabilidade e QA. Isso **não** implica pré-gerar um banco gigantesco: a geração pode ser incremental e orientada por necessidade, com autoria em lotes e revisão antes da aplicação.

Ver `00_SYSTEM/PRACTICE_PROTOCOL.md` e `00_SYSTEM/SIMULATION_PROTOCOL.md`.

## Processo canônico de autoria

Para uma apostila major, o fluxo esperado é:

```text
edital/syllabus + fontes + provas + análise da banca
                    ↓
       matriz de cobertura/autoria
                    ↓
           sumário pedagógico
                    ↓
        redação adequada ao domínio
                    ↓
       QA editorial + QA NotebookLM
                    ↓
           PDF + QA visual/textual
                    ↓
                release
```

A análise de banca orienta silenciosamente profundidade, distinções, exemplos e tipos de aplicação. O estudante recebe o resultado didático, não a documentação de engenharia editorial.

Para um simulado:

```text
blueprint + syllabus + fontes controladas + análise de banca
                         ↓
                 plano do conjunto
                         ↓
                 autoria em lotes
                         ↓
                 QA item a item
                         ↓
                  QA de conjunto
                         ↓
                      lock
                         ↓
                 aplicação/correção
                         ↓
            prioridade da semana seguinte
```

## Não objetivos da V0.1

- frontend ou aplicativo próprio;
- banco de dados ou autenticação;
- LMS próprio;
- motor próprio de quiz;
- rastreamento obrigatório questão a questão;
- CI remoto durante produção;
- pré-gerar indiscriminadamente um banco massivo de questões sem uso/QA definido;
- obrigar o estudante a administrar o backoffice do projeto;
- fazer o NotebookLM inferir sozinho o papel de documentos misturados;
- usar `Teste` nativo como simulador exato de banca quando ele se comporta como quiz sobre as fontes selecionadas;
- transformar metodologia, análise de banca, protocolo de autoria ou manifest em conteúdo estudável;
- depender do nome exato de um controle de UI do NotebookLM.

## Critério de sucesso

Uma matéria está operacional quando:

1. sua `APOSTILA.pdf` é boa o suficiente para sustentar estudo, Testes, Cartões, Mapas mentais e demais artefatos sem depender de documentação interna do projeto;
2. a apostila passou pelos gates aplicáveis de `APOSTILA_AUTHORING_PROTOCOL.md`;
3. o chat funciona com a apostila como corpus e com as instruções do tutor na configuração nativa da conversa;
4. o estudante não recebe questões sobre a própria metodologia, manifest ou análise interna;
5. o GitHub mantém rastreabilidade de por que o material foi escrito daquela forma;
6. outro chat consegue continuar a autoria/QA pelo estado canônico;
7. a rotina cotidiana não exige alternar fontes operacionais;
8. quando uma matéria entra em simulado de alta fidelidade, suas questões autorais passam pelo QA aplicável e respeitam o blueprint vigente.

## Stack canônica

Ver `docs/STACK_NOTEBOOKLM.md`.
