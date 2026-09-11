# SCHEDULER_PROTOCOL

## Objetivo

Escolher a próxima atividade que maximize valor esperado de aprendizagem e desempenho no concurso, sem confundir peso de prova com prioridade pedagógica pura.

## Sinais de prioridade

A fórmula futura deve considerar, entre outros:

- risco de eliminação por bloco;
- incidência/peso no concurso;
- deficiência demonstrada;
- importância como pré-requisito;
- esquecimento esperado;
- incerteza sobre o domínio;
- falso conhecimento;
- proximidade da prova;
- revisões vencidas.

## Restrições

Evitar que um único tópico fraco monopolize indefinidamente o plano. O scheduler recebe `participant_id` e `competition_id`; não codifica pessoas específicas.
