# CONTINUITY_PROTOCOL

## Princípio

Chats são descartáveis. GitHub é memória durável.

## Ao iniciar em um chat novo

1. seguir `AGENTS.md` e `START_HERE.md`;
2. conferir o estado real do GitHub;
3. reconstruir fase, checkpoint e próxima ação;
4. carregar somente o contexto específico necessário para a tarefa.

## Antes de encerrar trabalho que mudou o projeto

Persistir no repositório:

- o que foi concluído;
- o que permanece em andamento;
- a próxima ação executável;
- blockers;
- decisões arquiteturais novas;
- resultado do gate de validação;
- branch e PR esperados.

## Regra contra memória fantasma

Não escrever "como discutido anteriormente" sem que a decisão correspondente exista em arquivo canônico. Se uma conversa produziu uma decisão válida, a decisão deve ser persistida antes de ser tratada como estado do projeto.
