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
A V0.1 usa GitHub como memória canônica de análise e materiais, ChatGPT como camada de pesquisa/autoria/QA e NotebookLM como principal ambiente de estudo source-grounded. O objeto de entrega é um `SubjectPack` versionado por matéria. Rastreamento questão a questão, mastery projection e scheduler próprio ficam fora do caminho crítico até demonstrarem benefício real.

## DEC-0014 — Sincronização NotebookLM é manual e versionada
**Status:** accepted  
NotebookLM não é tratado como espelho do GitHub. Cada SubjectPack possui versão explícita; arquivos canônicos são exportados pelo projeto e carregados/substituídos manualmente no notebook. Feedback de sessão pode retornar ao ChatGPT em relatório resumido, sem exigir transcrição de todas as questões.

## DEC-0015 — Estúdio do NotebookLM primeiro; sem micro-orquestração por padrão
**Status:** superseded by DEC-0016  
A decisão reduziu corretamente prompts e micro-orquestração, mas o smoke test mostrou que um corpus misto ainda produz comportamento indesejado: o `Teste` nativo transforma documentos operacionais e didáticos em alvo de perguntas. A simplificação correta não é carregar tudo e esperar que o NotebookLM infira papéis; é separar explicitamente conteúdo do estudante de instrução operacional.

## DEC-0016 — Apostila como produto do estudante; metodologia isolada para o chat
**Status:** accepted, refined by DEC-0017  
A V0.1 separa os arquivos do SubjectPack por função.

- `APOSTILA.pdf` é o principal conteúdo do estudante e a fonte padrão para `Teste`, `Cartões`, `Mapa mental`, `Relatórios` e outros artefatos do Estúdio.
- `METODOLOGIA_NOTEBOOKLM.md` é **instrução do chat**, não matéria.
- `ANALISE_BANCA.md`, `SOURCES.md`, `MANIFEST.md`, `CHANGELOG.md`, provas históricas e documentação de QA são backoffice do GitHub/ChatGPT por padrão; servem para produzir e auditar a apostila, não para serem estudados diretamente.
- O chat do NotebookLM é o local para dúvidas, treino interativo, correção, confiança e `SESSION_REPORT` opcional.
- O Estúdio é usado para transformar **conteúdo da apostila** em ferramentas de revisão; não é presumido como simulador fiel de banca apenas por receber provas e instruções.

DEC-0017 refina apenas **como** a instrução do chat é entregue ao NotebookLM: ela deixa de ser uma fonte do notebook e passa a ser configuração nativa da conversa quando esse recurso estiver disponível.

## DEC-0017 — Instruções do tutor na configuração nativa da conversa
**Status:** accepted  
A interface observada do NotebookLM oferece `Configurar as conversas → Personalizado`, com campo próprio para definir meta/estilo/papel da conversa. Esse mecanismo é mais apropriado para comportamento do tutor do que carregar a metodologia como fonte.

Regra operacional da V0.1:

- o notebook recebe `APOSTILA.pdf` como **fonte de conteúdo**;
- o texto canônico de `METODOLOGIA_NOTEBOOKLM.md` é copiado para a configuração `Personalizado` da conversa;
- `METODOLOGIA_NOTEBOOKLM.md` permanece versionado no GitHub, mas **não é carregado como fonte** do NotebookLM;
- Estúdio e chat passam a consultar o mesmo corpus didático limpo, enquanto o chat recebe comportamento pela camada de configuração;
- por padrão, manter o tamanho de resposta nativo em `Padrão`, salvo necessidade concreta do usuário;
- a configuração é sincronizada manualmente quando o notebook é criado ou quando a metodologia muda.

Consequência:

```text
NotebookLM sources
└── APOSTILA.pdf

NotebookLM conversation configuration
└── conteúdo canônico de METODOLOGIA_NOTEBOOKLM.md
```

Isso elimina a necessidade cotidiana de marcar/desmarcar a metodologia e evita que instruções operacionais virem conteúdo de Teste, Cartões ou outros artefatos.

Como NotebookLM é produto externo, o nome e a forma desse controle de UI não são invariantes arquiteturais. Se a interface mudar, preservar o princípio: **instruções de comportamento ficam fora do corpus estudável sempre que houver uma camada nativa de configuração equivalente**.
