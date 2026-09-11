# AGENTS.md

## Regra fundamental

Este repositório é a fonte canônica do projeto. Memória de chat NÃO é estado do projeto.

Nenhuma decisão, avanço, bloqueio ou próxima ação pode existir exclusivamente em uma conversa. Um agente sem contexto anterior deve conseguir recuperar o estado operacional apenas lendo o repositório.

## Ordem obrigatória de recuperação

1. Ler `00_SYSTEM/START_HERE.md`.
2. Ler `PROJECT_CONTROL.md`.
3. Ler `00_SYSTEM/CHECKPOINT.md`.
4. Ler `00_SYSTEM/NEXT_ACTION.md`.
5. Ler apenas as decisões relevantes em `00_SYSTEM/DECISION_LOG.md`.
6. Identificar participante e concurso envolvidos, quando houver.
7. Ler apenas o enrollment e os eventos necessários.
8. Verificar branch, PR, arquivos e estado real do GitHub antes de escrever.

## Regras de trabalho

- Não inferir estado a partir de conversa antiga quando o repositório disser algo diferente.
- Não inventar dados de participante, concurso, edital, desempenho ou fonte.
- Eventos de evidência são imutáveis e append-only. Corrigir um evento exige novo evento de correção, não reescrita silenciosa.
- Estado derivado pode ser recalculado; eventos brutos não.
- Não incluir dados sensíveis. Este repositório é público durante a produção.
- Não criar GitHub Actions nesta fase.
- Alterações estruturais exigem registro em `DECISION_LOG.md`.
- Antes de encerrar uma sessão de implementação, atualizar `CHECKPOINT.md` e `NEXT_ACTION.md` quando o estado tiver mudado.
- Nenhuma tarefa é concluída sem executar ou justificar explicitamente a não execução de `python tools/verify.py`.

## Definition of Done de continuidade

Ao abrir um chat novo e pedir "continue o projeto concurso_os a partir do estado canônico do GitHub", um agente deve conseguir determinar: fase atual, trabalho concluído, trabalho em andamento, próximo passo, branch/PR esperados, validação conhecida e decisões pendentes.
