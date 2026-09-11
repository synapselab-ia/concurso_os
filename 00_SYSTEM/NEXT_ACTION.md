# NEXT_ACTION

## ENGINE-001 — Fechar pipeline de evidência antes de retomar baseline real

O adapter TJSP já existe, mas a coleta real foi pausada porque ainda faltam as camadas que transformam eventos em estado e prioridade sem misturar participantes.

Próxima execução de engenharia:

1. formalizar eventos de correção/anotação e regras de elegibilidade para projeção;
2. implementar projeção determinística por `participant_id + competition_id + enrollment_id`;
3. garantir isolamento entre participantes com fixtures sintéticas de `p001` e `p002`;
4. implementar o primeiro scheduler sobre estado derivado, sem dados reais;
5. testar reconstrução completa de estado a partir de eventos append-only;
6. validar que nenhum evento de um participante altera o estado de outro;
7. executar o gate canônico e só então reabrir `BASE-001`.

A resposta real já coletada de `p001` permanece no histórico como preflight, mas não deve influenciar domínio nem scheduler até revalidação.
