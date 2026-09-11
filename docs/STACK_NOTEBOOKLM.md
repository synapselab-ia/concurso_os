# Stack de estudo — GitHub + ChatGPT + NotebookLM

## Objetivo

A V0.1 não transforma o GitHub em um aplicativo de treino nem exige que o ChatGPT registre cada resposta do estudante. O sistema separa três funções:

- **GitHub:** memória canônica de análise e fábrica de materiais.
- **ChatGPT:** pesquisador, autor, revisor, integrador e mantenedor dos materiais.
- **NotebookLM:** ambiente de estudo source-grounded, com um notebook por matéria e por participante quando houver necessidade de histórico individual.

A regra de usabilidade é simples: o estudante deve passar a maior parte do tempo estudando no NotebookLM; o ChatGPT deve passar a maior parte do tempo melhorando o corpus e analisando o concurso; o GitHub deve guardar o que precisa sobreviver a qualquer chat.

## Fluxo principal

```text
EDITAL + PROVAS + FONTES OFICIAIS
              ↓
          ChatGPT
     análise + síntese + QA
              ↓
           GitHub
   materiais versionados por matéria
              ↓
       sincronização manual
              ↓
         NotebookLM
      estudo source-grounded
              ↓
     relatório de sessão opcional
              ↓
          ChatGPT
 análise agregada / melhoria do material
              ↓
           GitHub
```

## Pacote obrigatório por matéria

Cada matéria deve possuir um `subject pack` reutilizável por qualquer participante. O pacote canônico é produzido no GitHub e exportado para uso no NotebookLM.

```text
materials/<competition_id>/<subject_id>/
├── MANIFEST.md
├── APOSTILA.md
├── APOSTILA.pdf
├── ANALISE_BANCA.md
├── METODOLOGIA_NOTEBOOKLM.md
├── SOURCES.md
└── CHANGELOG.md
```

### MANIFEST.md

Identifica concurso, matéria, versão do pacote, data de atualização, arquivos que devem estar no notebook e fontes externas que o usuário precisa adicionar manualmente.

O notebook deve conseguir responder à pergunta `qual versão do seu pacote?` com a mesma versão do manifesto.

### APOSTILA

Material didático autoral e versionado. Deve ser suficiente para orientar o estudo, mas não substituir fontes oficiais quando literalidade, versão normativa ou precisão técnica forem relevantes.

Estrutura mínima:

```text
escopo do edital
→ mapa da matéria
→ teoria essencial
→ distinções e tabelas comparativas
→ exemplos de aplicação
→ armadilhas da banca
→ pontos de alta literalidade
→ checklist de revisão
→ resumo de alta retenção
→ referências
```

A apostila não deve ser uma enciclopédia. Prioriza o que está no edital e o que a análise reproduzível das provas demonstra ser pedagogicamente importante.

### ANALISE_BANCA.md

É produzida pelo ChatGPT a partir das provas disponíveis e separada da apostila para que padrões empíricos não sejam confundidos com conteúdo normativo.

Deve registrar, quando houver evidência suficiente:

```text
tipos de comando
formas de alternativa errada
nível de literalidade
subtemas observados
fronteiras entre alternativas próximas
pegadinhas recorrentes
perfil de cálculo/aplicação/interpretação
exemplos referenciados por prova/questão
limites da amostra
```

Não inventar frequências nem tendências sem contagem reproduzível.

### METODOLOGIA_NOTEBOOKLM.md

É a instrução operacional da matéria. Ela transforma o NotebookLM de simples ferramenta de consulta em tutor ativo. O arquivo deve ser carregado como fonte do notebook e sua versão deve acompanhar o manifesto.

A metodologia geral preserva os componentes úteis do protocolo legado: uma questão por vez, registro explícito de confiança, distinção entre acerto firme/instável, análise profunda de erro, comparação entre alternativas próximas, revisão ativa e relatórios periódicos.

## Organização dos notebooks

A unidade pedagógica é matéria, não bloco de prova. Para TJSP, a segmentação recomendada é:

```text
Português
Direito Penal
Processo Penal
Processo Civil
Direito Constitucional
Direito Administrativo
Legislação Interna TJSP
LBI / legislação especial
Atualidades
Matemática
Informática
Raciocínio Lógico
Redação
```

Quando o volume for pequeno, matérias próximas podem ser combinadas; quando o corpus ficar grande demais, podem ser subdivididas. A divisão existe para reduzir ruído de recuperação e manter cada notebook semanticamente focado.

Para múltiplos participantes, o **pacote de fontes é compartilhável**, mas o notebook de estudo pode ser separado por participante para evitar que histórico de conversa, notas e artefatos pessoais se misturem.

## O que carregar em cada NotebookLM

O notebook deve receber quatro camadas de fonte:

```text
1. METODOLOGIA_NOTEBOOKLM da matéria
2. APOSTILA da matéria
3. ANALISE_BANCA da matéria
4. fontes primárias relevantes
```

Fontes primárias incluem, conforme a matéria, edital, lei seca, normativos, provas históricas, documentação técnica oficial e materiais autorizados. Provas e PDFs de terceiros podem ser usados diretamente no NotebookLM sem necessidade de republicá-los no GitHub público.

## Ciclo de estudo no NotebookLM

A sessão usa cinco fases.

### 1. Recuperação

Antes de explicar conteúdo, testar conhecimento prévio com perguntas curtas, distinções ou uma questão de prova inédita baseada nas fontes selecionadas.

### 2. Correção diagnóstica

A resposta do estudante deve incluir grau de confiança. Classificações principais:

```text
acerto firme
acerto instável
acerto por eliminação
erro de conteúdo
erro de leitura
erro por pegadinha
falso conhecimento
chute
```

A correção deve identificar a fronteira técnica que decidiu a questão, e não apenas fornecer o gabarito.

### 3. Estudo direcionado

Explicar somente o necessário para corrigir a lacuna detectada, usando citações das fontes do notebook. Não transformar cada erro em aula longa.

### 4. Reteste

Erro ou hesitação exige nova recuperação em formato diferente: microquestão, comparação, variação numérica, caso hipotético ou pergunta de explicação curta.

### 5. Fechamento

Ao final, gerar revisão ativa e um relatório curto de sessão. O relatório pode ser trazido ao ChatGPT quando o usuário quiser análise longitudinal ou atualização de materiais.

## Metodologia específica por matéria

### Direito

Prioridade: fonte normativa → decomposição da regra → aplicação → distinção.

Toda correção relevante deve indicar diploma e dispositivo, trecho essencial quando necessário, requisito que decide a questão e por que as alternativas próximas falham. Diferenciar letra de lei, interpretação, aplicação em caso hipotético, exceção e eventual conhecimento jurisprudencial. Se a fonte carregada não sustenta uma afirmação, o NotebookLM deve declarar a limitação em vez de completar com memória geral.

### Português

Prioridade: texto/regra → elemento linguístico decisivo → padrão de erro.

Em interpretação, classificar erros como extrapolação, contradição, redução indevida, troca de sentido ou generalização. Em gramática, apontar a construção que decide o gabarito, dar exemplo contrastivo curto e mostrar a forma típica de cobrança da banca.

### Matemática

Prioridade: resolução independente → caminho mais rápido de prova → verificação.

A correção deve preservar passos essenciais, mostrar atalho apenas depois da compreensão e gerar variação numérica curta após erro. O foco é método transferível, não decorar uma resolução.

### Raciocínio Lógico

Prioridade: formalização → restrições → dedução → contraprova.

Quando útil, converter linguagem natural em estrutura simbólica/diagrama. Após erro, retestar mudando entidades e valores para verificar transferência.

### Informática

Prioridade: comportamento real da ferramenta → caminho operacional → distinção entre comandos parecidos.

Usar documentação/versão relevante quando disponível. Distinguir conceito de interface e evitar afirmar comportamento de software sem fonte adequada.

### Atualidades

Prioridade: corpus atualizado e datado. Esta matéria exige pacote com validade temporal curta. O manifesto deve registrar a janela temporal e a última atualização. Fatos novos entram por atualização do source pack, não por memória solta do modelo.

### Redação

Prioridade: produzir → diagnosticar por dimensão → reescrever.

A avaliação separa aderência ao tema/gênero, tese e desenvolvimento, coerência, coesão, norma-padrão e riscos eliminatórios do edital. Usar textos motivadores e rubrica; evitar modelos prontos memorizados.

## Artefatos do NotebookLM

Flashcards, testes, mapas mentais, relatórios e resumos em áudio/vídeo são complementares. Não substituem recuperação ativa. A ordem recomendada é primeiro tentar lembrar/aplicar; depois usar o artefato para consolidar ou revisar.

O ChatGPT não deve tentar reconstruir todos esses artefatos no GitHub. O repositório guarda os insumos e os outputs que agregam valor longitudinal.

## Relatório de sessão para retorno ao ChatGPT

Quando for útil manter acompanhamento entre notebooks ou melhorar materiais, pedir ao NotebookLM um relatório neste formato:

```text
SESSION_REPORT
participant: pNNN
competition: <id>
subject: <id>
pack_version: <version>
date: YYYY-MM-DD

covered:
- tópicos realmente trabalhados

performance:
- acertos firmes
- acertos instáveis
- erros
- chutes

error_patterns:
- padrões recorrentes e confusões específicas

source_gaps:
- ponto em que as fontes não foram suficientes, se houver

recommended_review:
- conteúdos e tipo de recuperação sugeridos

material_feedback:
- trechos da apostila/metodologia que pareceram insuficientes ou ambíguos
END_REPORT
```

O relatório é **resumo de sessão**, não transcrição questão a questão. Só deve ser persistido no GitHub quando houver utilidade real para continuidade/análise.

## Feedback loop ChatGPT → GitHub

Quando receber relatórios ou quando novas provas/fontes aparecerem, o ChatGPT decide entre três ações:

```text
problema do estudante → atualização apenas de acompanhamento
problema recorrente de vários estudantes → melhoria da apostila/metodologia
nova evidência de banca/fonte → atualização da análise e, se necessário, da apostila
```

Assim o material melhora sem misturar dificuldade individual com verdade curricular.

## Sincronização manual GitHub → NotebookLM

NotebookLM não é tratado como espelho automático do repositório. O GitHub mantém o pacote canônico; a cópia no NotebookLM é uma distribuição manual versionada.

Quando um subject pack mudar:

```text
1. ChatGPT incrementa a versão do MANIFEST.
2. Atualiza CHANGELOG.
3. Gera novamente o PDF da apostila/metodologia quando necessário.
4. O usuário substitui/adiciona os arquivos no NotebookLM.
5. Confere a versão perguntando ao notebook ou lendo o manifesto carregado.
```

Atualizações pequenas que não afetam o estudo podem aguardar um release de pacote para evitar sincronização excessiva.

## Papel do GitHub

Guardar de forma auditável:

```text
análise do edital
análise de provas e banca
mapas de conteúdo
apostilas
metodologias por matéria
manifests e changelogs
prompts/protocolos de geração
índices de fontes
relatórios de QA
opcionalmente, resumos de progresso por participante
```

Não é objetivo da V0.1 transformar o GitHub em banco de respostas, LMS ou motor de quiz.

## Papel do ChatGPT

O ChatGPT é a camada de engenharia intelectual:

```text
pesquisar/verificar
analisar provas
criar e atualizar apostilas
criar metodologia específica por matéria
fazer QA contra edital e fontes
comparar versões
integrar feedback dos notebooks
manter o repositório recuperável por qualquer chat
```

Ele também pode estudar diretamente com o usuário quando isso for conveniente, mas esse não é o requisito central do sistema.

## Definition of Done da V0.1

A V0.1 está realmente utilizável quando uma matéria completa possuir um subject pack aprovado, o usuário conseguir criar um NotebookLM a partir dele em poucos minutos, estudar sem depender de contexto de chat anterior e retornar feedback suficiente para o ChatGPT melhorar o pacote.

Depois disso, o padrão é replicado matéria por matéria.
