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

## Evolução proposta (DEC-0022, não ativada)

O plano de migração está em `STUDY_SCHEDULER_ROLLOUT.md`. O microdrill poderá usar rodízio ponderado por blocos oficiais e três filas (exploração 60%, recuperação 30%, retenção 10%), com importância para a prova e dificuldade do estudante calculadas separadamente e revisão a cada 50 questões consolidadas. Enquanto não existir implementação e validação de reservas entre chats, essas proporções não são um scheduler executável nem eliminam colisões; sessões abertas seguem suas instruções atuais. Não alterar o modo de simulado fiel ao blueprint.


### Motor shadow disponível, não ativo

O protótipo determinístico read-only `tools/study_scheduler.py` e o catálogo `competitions/tjsp-escrevente-2025/STUDY_TOPIC_CATALOG.json` apenas emitem sugestões. Consultar `STUDY_SCHEDULER_ROLLOUT.md` para comando, limites e gates. Não usar uma sugestão como reserva de tema nem editar prompts de chats em andamento. O status de ativação continua `DISABLED`.
