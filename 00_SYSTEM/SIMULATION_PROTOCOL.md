# SIMULATION_PROTOCOL

## Finalidade

Este protocolo define como produzir, auditar, aplicar e analisar simulados autorais de alta fidelidade à prova-alvo.

Para TJSP Escrevente 2025, o simulado dominical padrão representa a **prova objetiva de 70 questões**. A redação permanece uma dimensão eliminatória separada e só entra no mesmo treino quando uma sessão de `full dress rehearsal` for explicitamente planejada.

## Princípio central

```text
verdade e escopo
→ edital + fontes vigentes/controladas

forma de cobrança
→ prova mais recente + corpus histórico + análise de banca

questão final
→ autoria original + QA semântico + QA de conjunto
```

Provas históricas calibram estilo, operação cognitiva, densidade e distratores. Elas não criam conteúdo fora do edital e não devem ser copiadas extensamente.

## Tipos de simulado

### weekly_full_objective

Padrão dos domingos durante a fase regular.

- reproduz a distribuição objetiva vigente;
- usa cinco alternativas quando o blueprint assim exigir;
- não libera gabarito antes do encerramento;
- mistura matérias conforme a estrutura real;
- busca fidelidade de linguagem, operação e distratores, sem copiar questões históricas.

### partial_pilot

Usado para validar um bloco ainda em desenvolvimento.

- não é tratado como nota global de prontidão;
- pode cobrir apenas uma matéria ou bloco;
- deve ser identificado explicitamente como parcial.

### full_dress_rehearsal

Pode incluir prova objetiva, redação, tempo integral e demais condições relevantes. Não é o padrão semanal e exige planejamento explícito.

## Elegibilidade de conteúdo

Uma matéria ou domínio só pode fornecer questões novas para um simulado de alta fidelidade quando houver base suficiente para autoria segura:

- escopo oficial conhecido;
- fontes aplicáveis identificadas e versionadas quando necessário;
- material ou matriz suficiente para não inventar conteúdo;
- análise de banca disponível quando a fidelidade de estilo depender dela.

Quando a base não estiver pronta, o sistema deve reduzir o escopo do piloto ou declarar a lacuna. Não preencher silenciosamente com conhecimento não auditado.

## Pipeline de autoria

### 1. Planejamento do conjunto

Antes de redigir questões, fechar:

- contagem por bloco/matéria;
- tópicos elegíveis;
- operações cognitivas desejadas;
- nível de dificuldade relativo;
- estímulos compartilhados quando o estilo da banca os utiliza;
- limites de tempo/comprimento;
- itens ou estruturas já usados que não devem ser repetidos.

### 2. Autoria em lotes

Não gerar o simulado inteiro de 70 questões como uma única unidade de autoria.

O conjunto final deve ser composto por lotes menores, preferencialmente por matéria, domínio ou estímulo compartilhado. O limite inicial recomendado é de **até 24 questões por lote de geração**, porque 24 corresponde ao maior tamanho observado das seções históricas de Português de 2021–2024 usadas no projeto. Esse número é um **teto operacional provisório de qualidade, não uma afirmação sobre o limite do modelo**.

Aumentar esse teto exige benchmark interno mostrando que a taxa de aprovação sem correção, a variedade e a consistência não pioraram.

### 3. QA semântico por item

Cada questão `simulation` deve passar por uma revisão separada da autoria verificando:

- aderência ao syllabus;
- sustentação por fonte quando aplicável;
- apenas uma alternativa defensavelmente correta;
- enunciado sem ambiguidade involuntária;
- distratores plausíveis e relacionados a erros reais;
- gabarito compatível com a justificativa;
- justificativa do elemento decisivo;
- ausência de informação não ensinada/não autorizada;
- ausência de cópia extensa de questão histórica;
- fidelidade ao perfil da banca sem caricatura.

Questões de Direito exigem conferência de versão normativa e dispositivo aplicável.

### 4. QA de conjunto

Depois dos itens individualmente aprovados, revisar o simulado como prova única:

- total e distribuição por bloco/matéria;
- cinco alternativas quando exigidas;
- duplicação de assunto, frase, número, estrutura ou pegadinha;
- excesso de uma letra no gabarito ou padrão detectável;
- equilíbrio de dificuldade;
- comprimento e carga de leitura;
- dependência indevida entre questões;
- estímulos compartilhados coerentes;
- mistura de operações cognitivas;
- ausência de spoilers;
- tempo plausível para a sessão;
- preservação das regras eliminatórias no relatório de resultado.

A distribuição de letras deve parecer natural, não matematicamente artificial. O objetivo é impedir padrões óbvios, não forçar 14 respostas de cada letra.

### 5. Lock

Depois do QA de conjunto:

- congelar o enunciado do simulado;
- gerar `SIMULADO.md`;
- manter `GABARITO.md` separado;
- registrar `QA.md`;
- não corrigir silenciosamente uma questão após a aplicação; qualquer correção deve ficar documentada.

## Calibração de estilo

A fidelidade não significa copiar a superfície de uma prova.

Avaliar pelo menos:

- tamanho e estrutura dos enunciados;
- uso de texto-base/estímulo compartilhado;
- operação cognitiva;
- proximidade entre alternativas;
- tipo de erro explorado pelo distrator;
- grau de literalidade/aplicação;
- integração entre regras quando observada na banca;
- nível de leitura e atenção exigido.

A prova mais recente compatível com o edital vigente recebe maior peso qualitativo. Provas anteriores ampliam a amostra, mas não sobrescrevem mudanças do blueprint atual.

## Aplicação

Durante o simulado:

- sem gabarito;
- sem dicas produzidas pelo sistema;
- sem correção item a item antes do encerramento;
- registrar tempo total e, quando viável, tempo por bloco;
- confiança pode ser registrada sem interromper o ritmo, caso a interface permita.

## Correção e relatório

O relatório deve separar:

- total de acertos;
- desempenho por bloco/matéria;
- risco eliminatório, quando aplicável;
- erro de conteúdo;
- erro de leitura/interpretação do comando;
- erro de processo;
- chute;
- erro com alta confiança;
- tópicos que exigem microdrill na semana seguinte;
- itens possivelmente defeituosos, que devem voltar ao QA em vez de serem usados como evidência contra o estudante.

Não transformar uma única prova em `mastery` definitivo.

## Armazenamento

Convenção preferida:

```text
question_banks/<competition_id>/<subject_id>/batches/<batch_id>.json
simulations/<competition_id>/<simulation_id>/
├── MANIFEST.json
├── SIMULADO.md
├── GABARITO.md
└── QA.md
```

Resultados individuais não devem ser publicados automaticamente no repositório público. Persistência de desempenho é opcional e deve seguir as regras de privacidade e telemetria do projeto.

## Validação determinística

`SIMULATION_BLUEPRINT.json` deve permanecer coerente com `BLUEPRINT.json`. Testes de repositório devem verificar pelo menos total de questões e distribuição estrutural declarada.

A automação não substitui QA semântico dos itens.
