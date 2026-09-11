# PROJECT_SPEC

## Missão

Construir um sistema de preparação para concursos assistido por IA em que o GitHub seja a memória canônica de análise e materiais, o ChatGPT seja a camada de pesquisa/autoria/QA e o NotebookLM seja o principal ambiente de estudo source-grounded por matéria.

## Objetivo da V0.1

Produzir e versionar `subject packs` reutilizáveis por matéria, contendo apostila, análise de banca, metodologia específica para NotebookLM, manifesto de fontes e changelog. Um agente novo deve conseguir recuperar o estado pelo GitHub e continuar a produção ou manutenção desses materiais sem depender de memória de chat.

A experiência de uso deve ser **simples**: depois de montar o notebook, o estudante usa naturalmente o Estúdio do NotebookLM (`Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, resumos etc.) e o chat quando houver necessidade de explicação ou correção aprofundada. O sistema não deve exigir microgerenciamento de fontes, prompts longos ou um ritual diferente para cada clique.

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
- inferência automática de verdade normativa sem fonte;
- substituir os recursos nativos do Estúdio por uma orquestração manual complexa;
- tratar os rótulos genéricos de dificuldade do NotebookLM como escala oficial da banca.

## Critério de sucesso

Uma matéria está operacional quando seu pacote pode ser carregado manualmente em um NotebookLM e permite estudo confiável, focado no edital e no padrão da banca, **com poucos cliques e instruções curtas**, sem depender de contexto de conversas anteriores.

O GitHub deve permitir reproduzir, revisar e atualizar esse pacote. O NotebookLM deve conseguir explorar o corpus com seus recursos nativos; quando a ferramenta oferecer um seletor genérico de dificuldade, a calibração da banca deve vir principalmente das provas e da análise carregadas, não da suposição de que `Difícil = VUNESP`.

## Stack canônica

Ver `docs/STACK_NOTEBOOKLM.md`.
