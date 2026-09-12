# PRACTICE_PROTOCOL

## Finalidade

Este protocolo define a rotina de prática da preparação. O sistema separa deliberadamente dois tipos de treino porque eles otimizam capacidades diferentes:

```text
microdrill
→ aquisição, recuperação e discriminação rápida

simulation
→ transferência para a prova, gestão de tempo e robustez sob formato real
```

Uma questão curta não é considerada pior por não imitar integralmente a banca. Ela só é inadequada quando é usada para medir uma capacidade que exige transferência para o formato real.

## Ciclo semanal padrão

Durante a fase regular de preparação:

- **segunda a sábado:** microquestões (`microdrill`) como padrão de prática;
- **domingo:** um simulado objetivo completo (`simulation`) com o blueprint vigente da competição;
- os erros, hesitações e falsos conhecimentos observados no domingo alimentam a priorização dos microdrills da semana seguinte.

O último mês antes da prova pode receber uma política específica de reta final. Este protocolo não inventa essa política: ela deve ser definida por decisão canônica quando a fase for iniciada. Até lá, o ciclo semanal acima é o padrão.

## Lane 1 — Microdrill

### Objetivo

Maximizar conhecimento recuperado e decisões úteis por unidade de tempo.

### Características preferidas

- uma habilidade ou distinção principal por item;
- enunciado proporcional ao objetivo;
- feedback imediato;
- correção específica da construção ou raciocínio decisivo;
- reteste curto após erro ou hesitação quando útil;
- alta variação superficial para testar transferência local;
- possibilidade de formato aberto, verdadeiro/falso, múltipla escolha curta ou interação pelo chat.

Microdrill **não precisa** reproduzir fielmente comprimento, distribuição, densidade textual ou ritmo da banca.

### Fontes operacionais

Microdrills podem ser gerados a partir do `StudentContent` validado e das fontes canônicas aplicáveis. Para conteúdo normativo, técnico ou temporalmente sensível, a versão/fonte precisa estar controlada.

## Lane 2 — Simulation

### Objetivo

Medir se o conhecimento adquirido sobrevive ao formato, à mistura de matérias, aos distratores, à leitura, ao tempo e à fadiga da prova-alvo.

Todo simulado semanal deve seguir `SIMULATION_PROTOCOL.md` e o `SIMULATION_BLUEPRINT.json` da competição quando existir.

## Loop domingo → semana seguinte

Depois do simulado:

1. registrar acerto/erro por bloco e matéria;
2. separar erro de conteúdo, erro de leitura, erro de processo e chute;
3. destacar erros com alta confiança;
4. identificar padrões repetidos e competências frágeis;
5. aumentar a prioridade dos microdrills correspondentes durante a semana seguinte;
6. manter alguma prática de manutenção nos demais tópicos para evitar esquecimento;
7. retestar o ponto fraco com item diferente, não apenas repetir a mesma pergunta.

O simulado serve para **medir e redirecionar o estudo**, não apenas para produzir uma nota.

## Relação com NotebookLM

NotebookLM permanece adequado para:

- microquestões;
- Teste nativo;
- Cartões;
- chat interativo;
- revisão e correção.

Esses recursos pertencem majoritariamente à lane de aquisição/recuperação. O `Teste` nativo não é presumido como simulador fiel da banca.

O simulado integral é um artefato separado, montado e auditado pelo pipeline do projeto.

## Regra de evidência

Um acerto em microdrill mostra recuperação local. Um acerto em simulation fornece evidência mais forte de transferência para a prova, mas nenhum dos dois, isoladamente, prova domínio permanente.

A avaliação longitudinal deve considerar repetição, variedade, confiança e desempenho posterior.
