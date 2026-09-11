# Stack de estudo — GitHub + ChatGPT + NotebookLM

## Objetivo

A V0.1 não transforma o GitHub em um aplicativo de treino nem exige que o ChatGPT registre cada resposta do estudante. O sistema separa três funções:

- **GitHub:** memória canônica de análise e fábrica de materiais.
- **ChatGPT:** pesquisador, autor, revisor, integrador e mantenedor dos materiais.
- **NotebookLM:** ambiente principal de estudo source-grounded, usando **Estúdio + chat**.

A regra de usabilidade é: **o estudante deve estudar, não administrar o sistema**.

Depois de montar um notebook de matéria, a rotina deve exigir poucos cliques, comandos curtos e o mínimo possível de seleção manual de fontes/configurações.

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
      Estúdio + chat
              ↓
     feedback opcional
              ↓
          ChatGPT
 melhoria do corpus / materiais
              ↓
           GitHub
```

## Princípio de usabilidade: Studio-first

O NotebookLM não deve ser tratado como apenas um chat com documentos. O Estúdio é parte central do produto de estudo.

Recursos como `Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, `Resumo em áudio/vídeo`, `Apresentações` e `Infográficos` podem ser usados diretamente quando forem pedagogicamente úteis.

O pack fornece **um corpus bom e uma metodologia curta**. Ele não deve obrigar o usuário a decorar uma receita diferente de fontes e prompts para cada botão.

### Padrão operacional

1. carregar o conjunto recomendado de fontes uma vez;
2. manter essas fontes disponíveis no notebook;
3. escolher o recurso do Estúdio que fizer sentido naquele momento;
4. usar controles padrão quando não houver motivo para alterá-los;
5. quando precisar direcionar a geração, escrever uma instrução curta e concreta;
6. só introduzir subseleção de fontes ou prompt detalhado se um resultado real estiver ruim e houver hipótese clara de correção.

**Não otimizar antes de observar problema.**

## Calibração de banca versus dificuldade genérica

Os controles nativos de dificuldade de ferramentas como Testes/Cartões são genéricos. Eles não devem ser interpretados como escala oficial de VUNESP, FCC, FGV etc.

Para calibrar uma banca:

```text
provas reais + análise reproduzível da banca + edital
                         ↓
               instrução curta de foco
```

Exemplo para o TJSP/VUNESP:

> `Teste de Português no padrão TJSP/VUNESP das provas carregadas.`

Por padrão, usar a configuração nativa neutra (`Médio/Padrão`) durante o smoke test. Só mudar o seletor se o usuário quiser deliberadamente uma versão mais fácil ou mais difícil para fins pedagógicos. Não usar `Difícil` como sinônimo de `nível VUNESP`.

## Pacote obrigatório por matéria

Cada matéria possui um `SubjectPack` reutilizável:

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

Diz o que carregar no notebook, versão do pack e smoke test mínimo. Deve ser suficiente para uma pessoa ou agente montar o notebook sem contexto de chat anterior.

### APOSTILA

Material didático autoral e versionado. Deve cobrir o edital de forma eficiente, com teoria essencial, distinções, exemplos, armadilhas, checklist e referências. Não substitui fonte oficial quando literalidade/versão normativa forem decisivas.

### ANALISE_BANCA.md

Registra padrões observados em provas reais, com método reproduzível e limites da amostra. Não transformar ocorrência histórica em previsão garantida.

### METODOLOGIA_NOTEBOOKLM.md

Define **como usar o notebook sem burocracia** e, quando o chat for usado, como corrigir/explicar. Não deve tentar controlar todas as ferramentas do Estúdio por um único superprompt.

## Organização dos notebooks

A unidade pedagógica é matéria, não bloco da prova. Para TJSP, a segmentação inicial é:

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

Quando o volume for pequeno, matérias próximas podem ser combinadas; quando o corpus ficar grande, podem ser subdivididas.

Para múltiplos participantes, o **SubjectPack é compartilhável**, mas notebooks podem ser separados por participante para evitar mistura de histórico e artefatos pessoais.

## O que carregar no NotebookLM

Por matéria, o conjunto normal contém:

```text
APOSTILA.pdf
ANALISE_BANCA.md
METODOLOGIA_NOTEBOOKLM.md
edital / recorte oficial relevante
prova mais recente da banca
provas históricas úteis (opcionais/recomendadas)
fontes normativas ou técnicas quando necessárias
```

Não exigir que o estudante alterne subconjuntos de fontes a cada ferramenta. O primeiro teste sempre usa o corpus completo recomendado. Seleção específica de fontes é uma **ferramenta de correção**, não uma obrigação diária.

## Papel dos recursos do Estúdio

Não existe uma sequência obrigatória universal. Cada matéria usa os recursos que agregam valor.

### Teste

Principal mecanismo nativo de prática quando a matéria se presta a questões objetivas.

- usar questões geradas a partir das fontes;
- para banca específica, dar instrução curta de calibração;
- revisar resultado usando os controles nativos;
- levar ao chat apenas erros, ambiguidades ou explicações que mereçam aprofundamento.

### Cartões

Úteis para recuperação de regras, definições, exceções, prazos, comandos e contrastes curtos. Evitar transformar texto longo em cartão.

### Mapa mental

Útil para estrutura e relações entre tópicos. Não é prova de domínio e não precisa preceder todo estudo.

### Relatórios / Apresentações / Áudio / Vídeo

Servem para visão geral, revisão e consolidação. São complementares à prática ativa.

### Tabela de dados

Boa para comparações estruturadas: regra × exceção, instituto × hipótese, conectivo × relação, comando × função etc.

### Infográfico

Opcional. Usar quando a informação realmente se beneficiar de visualização.

### Chat

Usar quando houver necessidade de:

- tirar dúvida;
- corrigir uma questão de forma profunda;
- comparar alternativas próximas;
- pedir exemplos/reteste;
- discutir lacuna ou contradição nas fontes;
- gerar um relatório curto da sessão.

O chat **não precisa** ser a porta de entrada de toda sessão.

## Metodologia por matéria

### Direito

Prioridade: fonte normativa → distinção → aplicação. Testes e cartões tendem a ser úteis; tabelas são especialmente valiosas para hipóteses, prazos, competências e exceções.

### Português

Prioridade: texto/regra → elemento linguístico decisivo → padrão de erro. Testes são centrais; chat entra para interpretação ambígua, análise A–E e correção gramatical. Tabelas/cartões servem bem para relações lógicas e regras curtas.

### Matemática

Prioridade: resolver → verificar → comparar método. Testes e chat predominam. Cartões têm papel secundário.

### Raciocínio Lógico

Prioridade: formalização → dedução → contraprova. Testes e chat predominam; mapas podem ajudar apenas em alguns tópicos.

### Informática

Prioridade: comportamento real da ferramenta → distinção entre comandos. Testes, cartões e tabelas têm alto valor.

### Atualidades

Prioridade: corpus atualizado e datado. Relatórios/áudio/mapas podem ajudar na construção de contexto; testes verificam retenção e relações.

### Redação

Prioridade: produzir → diagnosticar → reescrever. Chat e relatórios são mais importantes; Teste/Cartões são auxiliares.

## Correção aprofundada no chat

Quando o usuário levar uma questão/erro ao chat, preservar os elementos úteis do protocolo legado:

- resposta antes da explicação quando a questão ainda estiver aberta;
- confiança quando fizer sentido;
- diferença entre acerto firme e hesitante;
- diagnóstico do erro;
- comparação entre alternativas próximas;
- explicação localizada;
- reteste curto quando necessário.

Isso é uma **camada de aprofundamento**, não uma exigência para cada artefato do Estúdio.

## Feedback ao ChatGPT

Não é necessário exportar cada sessão.

Trazer ao ChatGPT somente quando houver valor:

```text
- questão gerada que parece fora do padrão da banca
- explicação duvidosa
- lacuna da apostila
- recurso do Estúdio que funcionou/mal funcionou
- resumo curto de dificuldades recorrentes
```

Se for útil, usar `SESSION_REPORT`, mas ele é opcional.

## Sincronização GitHub → NotebookLM

NotebookLM não é espelho automático do GitHub. O GitHub mantém o pack canônico; o usuário substitui/adiciona apenas os arquivos alterados quando sai nova versão.

Atualizações pequenas podem aguardar um release para evitar burocracia.

## Produto externo e deriva de UI

NotebookLM é um produto externo e seus controles podem mudar. Detalhes da interface observados não devem virar invariantes arquiteturais.

Ao continuar este projeto em outro chat:

- confiar nos princípios do repositório;
- se a UI do NotebookLM tiver mudado, verificar o comportamento atual antes de reescrever a metodologia;
- preferir sempre a solução de menor fricção que mantenha fidelidade às fontes e à banca.

## Definition of Done da V0.1

Uma matéria está aprovada quando o usuário consegue:

1. montar o notebook em poucos minutos;
2. abrir um recurso nativo do Estúdio sem precisar de receita complexa;
3. obter conteúdo coerente com edital e corpus da banca;
4. usar o chat somente quando realmente precisar de aprofundamento;
5. estudar sem depender do contexto de um chat anterior;
6. reportar um problema ao ChatGPT de forma simples quando algo não funcionar.

Depois disso, o padrão é replicado matéria por matéria.
