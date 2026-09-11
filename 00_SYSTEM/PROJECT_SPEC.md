# PROJECT_SPEC

## Missão

Construir um sistema de preparação para concursos assistido por IA em que o GitHub seja a memória canônica de análise e materiais, o ChatGPT seja a camada de pesquisa/autoria/QA e o NotebookLM seja o principal ambiente de estudo source-grounded por matéria.

## Objetivo da V0.1

Produzir e versionar `subject packs` reutilizáveis por matéria, contendo apostila, análise de banca, metodologia específica para NotebookLM, manifesto de fontes e changelog. Um agente novo deve conseguir recuperar o estado pelo GitHub e continuar a produção ou manutenção desses materiais sem depender de memória de chat.

## Não objetivos da V0.1

- frontend;
- aplicativo móvel;
- banco de dados;
- autenticação;
- LMS próprio;
- motor próprio de quiz;
- rastreamento obrigatório questão a questão;
- CI remoto;
- geração massiva de banco de questões;
- inferência automática de verdade normativa sem fonte.

## Critério de sucesso

Uma matéria está operacional quando seu pacote pode ser carregado manualmente em um NotebookLM e permite estudo confiável, focado no edital e no padrão da banca, sem depender de contexto de conversas anteriores. O GitHub deve permitir reproduzir, revisar e atualizar esse pacote.

## Stack canônica

Ver `docs/STACK_NOTEBOOKLM.md`.
