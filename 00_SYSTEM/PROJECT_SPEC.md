# PROJECT_SPEC

## Missão

Construir um sistema de preparação para concursos assistido por IA em que o GitHub seja a memória canônica de análise e materiais, o ChatGPT seja a camada de pesquisa/autoria/QA e o NotebookLM seja o ambiente de estudo por matéria.

## Objetivo da V0.1

Produzir e versionar `SubjectPacks` reutilizáveis por matéria. O produto principal para o estudante é uma **apostila forte, autocontida e adequada aos recursos do NotebookLM**. Edital, provas, análise de banca, fontes, QA e decisões editoriais permanecem no GitHub como backoffice do projeto.

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

Arquivos de engenharia editorial (`ANALISE_BANCA.md`, `SOURCES.md`, `CHANGELOG.md`, `MANIFEST.md`, provas históricas e registros de QA) não entram no notebook por padrão. Eles existem para o ChatGPT produzir uma apostila melhor, não para virar matéria de quiz.

## Não objetivos da V0.1

- frontend ou aplicativo próprio;
- banco de dados ou autenticação;
- LMS próprio;
- motor próprio de quiz;
- rastreamento obrigatório questão a questão;
- CI remoto durante produção;
- geração massiva de banco de questões;
- obrigar o estudante a administrar o backoffice do projeto;
- fazer o NotebookLM inferir sozinho o papel de documentos misturados;
- usar `Teste` nativo como simulador exato de banca quando ele se comporta como quiz sobre as fontes selecionadas;
- transformar metodologia, análise de banca ou manifest em conteúdo estudável;
- depender do nome exato de um controle de UI do NotebookLM.

## Critério de sucesso

Uma matéria está operacional quando:

1. sua `APOSTILA.pdf` é boa o suficiente para sustentar estudo, Testes, Cartões, Mapas mentais e demais artefatos sem depender de documentação interna do projeto;
2. o chat funciona com a apostila como corpus e com as instruções do tutor na configuração nativa da conversa;
3. o estudante não recebe questões sobre a própria metodologia, manifest ou análise interna;
4. o GitHub mantém rastreabilidade de por que o material foi escrito daquela forma;
5. outro chat consegue continuar a autoria/QA pelo estado canônico;
6. a rotina cotidiana não exige alternar fontes operacionais.

## Stack canônica

Ver `docs/STACK_NOTEBOOKLM.md`.
