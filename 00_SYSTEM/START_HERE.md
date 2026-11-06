# START_HERE

Este é o ponto de entrada canônico para qualquer humano ou agente sem contexto prévio.

## Leitura mínima

1. `../PROJECT_CONTROL.md`
2. `PROJECT_SPEC.md`
3. `ARCHITECTURE.md`
4. `DATA_MODEL.md`
5. `CHECKPOINT.md`
6. `NEXT_ACTION.md`

Leia protocolos específicos somente quando a tarefa exigir.

## Recuperação operacional

Antes de qualquer alteração, confirme no GitHub a branch real, PRs abertos e o conteúdo atual dos arquivos relevantes. A conversa nunca prevalece sobre o repositório.

## Mapa de protocolos

- continuidade entre chats/agentes: `CONTINUITY_PROTOCOL.md`
- autoria/reconstrução de apostilas: `APOSTILA_AUTHORING_PROTOCOL.md`
- prática semanal e separação aquisição/transferência: `PRACTICE_PROTOCOL.md`
- simulados autorais de alta fidelidade: `SIMULATION_PROTOCOL.md`
- estudo: `STUDY_PROTOCOL.md`
- avaliação: `ASSESSMENT_PROTOCOL.md`
- domínio: `MASTERY_PROTOCOL.md`
- priorização: `SCHEDULER_PROTOCOL.md`
- fontes: `SOURCE_POLICY.md`
- garantia de qualidade: `QA_PROTOCOL.md`
- decisões arquiteturais: `DECISION_LOG.md`

Ao criar ou reconstruir substancialmente uma `APOSTILA.md`/`APOSTILA.pdf`, ler `APOSTILA_AUTHORING_PROTOCOL.md` **antes de começar a redação**.

Ao criar microquestões em escala ou qualquer simulado que pretenda medir prontidão para a prova, ler `PRACTICE_PROTOCOL.md` e, para simulados, `SIMULATION_PROTOCOL.md` antes da autoria.

## Sessões de estudo simultâneas

Se dois ou mais chats atuarem sobre o mesmo enrollment, ler `PARALLEL_STUDY_PROTOCOL.md` antes de publicar feedback. A numeração de questões é local ao chat; cada chat usa `session_id` próprio e grava somente arquivos append-only exclusivos.

## Evolução do agendador de estudos (ainda não ativa)

Consultar `STUDY_SCHEDULER_ROLLOUT.md` ao planejar implementação de seleção de temas/cobertura. É proposta em implantação segura; não substituir automaticamente prompts nem filas de questões de sessões existentes. Seguir `PARALLEL_STUDY_PROTOCOL.md` para gravações.
