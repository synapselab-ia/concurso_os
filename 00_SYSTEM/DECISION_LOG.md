# DECISION_LOG

## DEC-0001 — GitHub como fonte canônica
**Status:** accepted  
Chats não carregam estado autoritativo do projeto.

## DEC-0002 — Arquitetura multi-participante e multi-concurso
**Status:** accepted  
Participant, Enrollment e Competition são entidades distintas.

## DEC-0003 — Eventos append-only
**Status:** accepted, experimental for study telemetry  
Evidência histórica é imutável; métricas são projeções reconstruíveis. O uso de eventos questão a questão deixou de ser requisito da V0.1 por DEC-0013.

## DEC-0004 — Competência é uma unidade pedagógica útil
**Status:** accepted  
Questões são instrumentos de observação, não a fonte principal do conhecimento. Competências podem apoiar análise e materiais sem exigir um motor próprio de mastery.

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
Comportamento específico deve vir de configuração/material/feedback, nunca de `if participant == ...`.

## DEC-0009 — Merge autônomo após validação
**Status:** accepted  
Durante a fase de desenvolvimento, PRs podem ser mescladas sem aprovação manual a cada merge quando o agente responsável tiver revisado o diff, confirmado ausência de mudança destrutiva não prevista e executado o gate canônico ou documentado por que ele não pôde ser executado. Mudanças com impacto externo irreversível continuam exigindo autorização específica quando aplicável.

## DEC-0010 — Edital vigente prevalece sobre provas históricas
**Status:** accepted  
No adapter `tjsp-escrevente-2025`, o Edital de Abertura n.º 02/2025 controla estrutura, distribuição, escopo e regras eliminatórias. A prova de 2025 é a referência empírica mais próxima para forma e estilo. Provas de 2024, 2023 e 2021 são históricas e não podem sobrescrever o blueprint atual.

## DEC-0011 — Binários-fonte não são copiados para o repositório público
**Status:** accepted  
Durante a fase pública de produção, PDFs e outros binários de fonte não são republicados no GitHub. A rastreabilidade é mantida por `source_id`, nome original, autoridade/URL quando disponível, hash SHA-256 e tamanho. Materiais autorais produzidos pelo projeto podem ser publicados normalmente.

## DEC-0012 — Baseline real pausado durante a fase de engenharia
**Status:** superseded by DEC-0013  
A decisão interrompeu corretamente a coleta real iniciada cedo demais. A V0.1 agora não depende de baseline nem de pipeline de projeção questão a questão.

## DEC-0013 — Stack pedagógica canônica: GitHub + ChatGPT + NotebookLM
**Status:** accepted  
A V0.1 usa GitHub como memória canônica de análise e materiais, ChatGPT como camada de pesquisa/autoria/QA e NotebookLM como principal ambiente de estudo source-grounded. O objeto de entrega passa a ser um `SubjectPack` versionado por matéria (apostila, análise de banca, metodologia NotebookLM, manifesto de fontes e changelog). Rastreamento questão a questão, mastery projection e scheduler próprio ficam fora do caminho crítico até demonstrarem benefício real.

## DEC-0014 — Sincronização NotebookLM é manual e versionada
**Status:** accepted  
NotebookLM não é tratado como espelho do GitHub. Cada subject pack possui versão explícita; arquivos canônicos são exportados pelo projeto e carregados/substituídos manualmente no notebook. Feedback de sessão pode retornar ao ChatGPT em relatório resumido, sem exigir transcrição de todas as questões.

## DEC-0015 — Estúdio do NotebookLM primeiro; sem micro-orquestração por padrão
**Status:** accepted  
A experiência de estudo da V0.1 deve aproveitar os recursos nativos do Estúdio do NotebookLM (testes, cartões, mapas mentais, relatórios, tabelas, resumos e outros artefatos) em vez de transformar o chat em única interface ou exigir um prompt complexo para cada ação. O corpus recomendado é carregado uma vez e permanece disponível. Subseleção de fontes, prompts longos e configurações especiais só entram quando um teste real demonstrar necessidade. Rótulos nativos de dificuldade (`Fácil`, `Médio`, `Difícil`) são genéricos e não equivalem automaticamente ao nível de uma banca; a calibração de estilo deve vir das provas e da análise de banca carregadas. O objetivo operacional é `poucos cliques + instruções curtas + corpus forte`.
