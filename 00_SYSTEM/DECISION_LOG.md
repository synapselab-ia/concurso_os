# DECISION_LOG

## DEC-0001 — GitHub como fonte canônica
**Status:** accepted  
Chats não carregam estado autoritativo do projeto.

## DEC-0002 — Arquitetura multi-participante e multi-concurso
**Status:** accepted  
Participant, Enrollment e Competition são entidades distintas.

## DEC-0003 — Eventos append-only
**Status:** accepted  
Evidência histórica é imutável; métricas são projeções reconstruíveis.

## DEC-0004 — Competência é a unidade pedagógica principal
**Status:** accepted  
Questões são instrumentos de observação, não a fonte principal do estado de domínio.

## DEC-0005 — Repositório público durante produção
**Status:** accepted  
Perfis públicos mínimos e ausência de dados sensíveis são requisitos arquiteturais.

## DEC-0006 — Sem GitHub Actions na fase de produção
**Status:** accepted  
O gate canônico é local e deverá poder ser reutilizado por CI no futuro sem duplicar lógica.

## DEC-0007 — Continuidade independente de chat/modelo
**Status:** accepted  
Um agente novo deve recuperar o projeto somente pelo repositório.

## DEC-0008 — Kernel sem condicionais por pessoa
**Status:** accepted  
Comportamento específico deve vir de configuração/evidência, nunca de `if participant == ...`.

## DEC-0009 — Merge autônomo após validação
**Status:** accepted  
Durante a fase de desenvolvimento, PRs podem ser mescladas sem aprovação manual a cada merge quando o agente responsável tiver revisado o diff, confirmado ausência de mudança destrutiva não prevista e executado o gate canônico ou documentado por que ele não pôde ser executado. Mudanças com impacto externo irreversível continuam exigindo autorização específica quando aplicável.
