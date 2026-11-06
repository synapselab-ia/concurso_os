# STUDY_SCHEDULER_ROLLOUT | contrato de implantação segura

## Problema e hipótese

A auditoria dos reviews p001 Q01-Q60 encontrou repetição de CPP 252/254, CPP 366/367, CPC 334/335, CP 312, concordância verbal e lógicas condicionais, ao mesmo tempo em que vários ramos do edital permanecem sem avaliação. Acertos imediatos em questões estruturalmente semelhantes não equivalem a retenção nem transferência. A proposta combina **Weighted Round Robin por bloco oficial** com prioridade pedagógica individual. Este documento é um PLANO; não declara motor de distribuição ativo.

## Política proposta para microdrills

Meta inicial por dez questões principais válidas: **seis de exploração**, **três de recuperação de dificuldade**, **uma de retenção espaçada** (60/30/10). Ajustar se alguma fila estiver vazia; não criar questões artificialmente nem forçar reteste sem intervalo. Esse é o balanço didático dos microdrills, **não** a distribuição oficial dos simulados.

- **Exploração:** subtema ainda não avaliado nos registros, distribuído de modo a cobrir o programa.
- **Recuperação:** erro, acerto com dúvida, chute, regra não compreendida e, sobretudo, erro com confiança alta.
- **Retenção:** tema aparentemente bem respondido, reavaliado depois de intervalo e com aplicação diferente.

Usar duas variáveis independentes:
1. **Importância para a prova:** peso oficial da disciplina, mínimos eliminatórios, escopo expresso no edital e, apenas quando fundamentada, incidência empírica histórica. A frequência histórica de um subtema não pode ser inventada ou tratada como previsão.
2. **Dificuldade individual:** evidências de erro, confiança, dúvidas, eliminação, reaplicação e tempo desde a última avaliação. Ausência de questões não é prova de domínio nem de desconhecimento.

A cada **50 questões principais válidas e persistidas** de um enrollment, gerar revisão de prioridades com classificação dos subtemas, importância, dificuldade observada, lacunas de cobertura, retestes vencidos e alteração desde o checkpoint anterior. Reforços e revisões não contam novamente; não criar registros históricos inexistentes. As Q01-Q60 atuais são baseline, não devem ser reclassificadas como novas tentativas; próximo checkpoint regular de 50 ao atingir Q100 **se os eventos pertencerem a uma mesma série válida**. Com chats paralelos, o checkpoint global precisa usar consolidação confirmada, nunca a numeração local.

### Weighted Round Robin hierárquico

Primeiro respeitar a proporção por disciplina/bloco do **BLUEPRINT.json**: 16 Português, 30 Direito, 4 Atualidades/PCD, 4 Matemática, 9 Informática, 7 Lógica por 70. Distribuir Direito entre os seis ramos por rodízio e déficits de cobertura, **sem fingir conhecer o peso oficial de cada ramo**. Dentro de cada ramo, alternar subtemas aptos e filas pedagógicas. A seleção considera histórico recente e evita o mesmo subtema duas vezes no mesmo bloco planejado. Ao exaurir a fila, informar que não há candidato em vez de usar sempre o primeiro da lista.

### Evitar falsa sensação de mastery

Após dois acertos firmes em variações independentes, rebaixar a prioridade de repetição imediata. Não marcar MASTERED: deixar pendente a validação por questão diferente, intercalada e após espaçamento real. Um critério inicial para testar, **não definitivo**, é esperar pelo menos 7 dias e 20 outras questões principais para o reteste de retenção. Falta de timestamp confiável significa que o espaçamento não está comprovado; o algoritmo não deve inferir sequência temporal entre chats simultâneos.

## Implantação sem interromper os dois blocos em curso

**Fase A | SHADOW, sem efeitos**: criar catálogo de cobertura e protótipo determinístico que somente lê JSONs persistidos e produz recomendações/diagnósticos; não altera registros, CONFIG dos participantes, prompts ativos, PDFs, questões apresentadas ou NEXT_ACTION editorial. Validar contra histórico e fixtures sintéticas.

**Fase B | CONFERÊNCIA**: testar equivalência entre o edital e catálogo, classificação dos reviews Q01-Q60, divisão 60/30/10, déficits entre disciplinas, retestes espaçados, ids de sessão, duplicação, retificação, questões defeituosas e simulado. Executar `python tools/verify.py` no checkout completo. Sem teste real ou justificativa registrada, não afirmar PASS.

**Fase C | NOVAS SESSÕES/ BLOCOS, opt-in controlado**: somente ativar após a conclusão dos blocos atuais e quando a nova sessão recuperar sua política no GitHub. Não alterar automaticamente sessões já abertas. Requer coordenação **efetiva** de reservas de tópico por sessão (operações condicionais, expiração e readback) para evitar duas sugestões simultâneas idênticas; o protocolo append-only sozinho não distribui temas. Sem reserva confirmada, admitir que pode haver repetição entre chats.

**Fase D | REVIEW 50**: comparar cobertura, dificuldade e retenção dos 50 itens seguintes com o baseline anterior; validar se a mudança melhorou transferência sem mascarar erros. Calibrar percentuais, intervalos e pesos mediante evidência; permitir rollback para a política anterior sem reescrever eventos.

## Critérios de não interferência e evidência

- Não atualizar `participants/p001/**` ou `participants/p002/**` durante a implantação em shadow.
- Não editar nenhum `session_feedback` existente, seja bloco completo ou parcialmente em andamento.
- Não substituir a metodologia de uma questão por vez, painel, radio, confiança e correção das sessões correntes.
- Não utilizar resultado de um chat ainda não persistido como evidência global.
- Não deixar um tema fraco dominar indefinidamente, mesmo com score alto de dificuldade.
- A numeração local não cria sequência global. Registrar commit de origem em qualquer snapshot agregado.
- A edição do protocolo não faz o ChatGPT de um chat já aberto atualizar seu comportamento de forma automática.
- Sem novas GitHub Actions, sem alteração de SubjectPacks, sem interferência no gate editorial `DIREITO-016`.

## Estado de entrega nesta fase

Esta especificação é apenas a **porta de segurança e os critérios de aceitação**. A implementação computacional, testes de integração e ativação serão tarefas separadas, não presumidas concluídas pelo merge documental.