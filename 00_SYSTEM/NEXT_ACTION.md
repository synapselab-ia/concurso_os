# NEXT_ACTION

## DIREITO-003 — Classificar de forma reproduzível as questões históricas de Direito

Os Gates 1 e 2 de B2 estão fechados. A fronteira editorial está definida em seis SubjectPacks e todas as fontes normativas possuem baseline reconciliado com o cutoff do edital de `2025-07-29`, com drift posterior separado em `DIREITO_SOURCES.md`.

**Não iniciar a redação de nenhuma apostila.** O próximo gate é empírico: analisar as questões reais de Direito das provas TJSP/VUNESP de 2021, 2023, 2024 e 2025 antes de construir as matrizes de autoria.

## Autoridade e limite

- o edital vigente continua definindo escopo e prevalece sobre as provas históricas, conforme DEC-0010;
- a prova de 2025 é a referência empírica mais próxima para forma e nível;
- 2024, 2023 e 2021 são histórico útil para identificar operações cognitivas, distinções e distractores;
- frequências históricas **não** criam conteúdo programático novo nem autorizam excluir item do syllabus;
- a análise é backoffice e não deve ser copiada como metadiscurso para a futura apostila.

## Fontes canônicas do Gate 3

Usar os registros existentes em `competitions/tjsp-escrevente-2025/SOURCES.json`:

- `SRC-TJSP-PROVA-2025`;
- `SRC-TJSP-PROVA-2024`;
- `SRC-TJSP-PROVA-2023`;
- `SRC-TJSP-PROVA-2021`.

Os binários permanecem fora do repositório público conforme DEC-0011.

## Artefato esperado

Criar:

`competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`

O arquivo deve conter método, classificação por questão, síntese por domínio e implicações editoriais limitadas pela amostra.

## Unidade de análise

Classificar **cada questão de Direito** das quatro provas. Não inferir o gabarito ou o dispositivo sem evidência suficiente; quando a identificação for incerta, registrar a incerteza.

Campos mínimos por questão:

| Campo | Conteúdo |
|---|---|
| `year_question` | ano + número da questão |
| `domain` | Penal, Processual Penal, Processual Civil, Constitucional, Administrativo ou Legislação Interna |
| `source_or_institute` | diploma, dispositivo ou instituto principal |
| `task_form` | assertiva direta, caso hipotético, escolha da alternativa correta/incorreta, comparação etc. |
| `cognitive_operation` | recordar literalidade, distinguir requisitos, aplicar norma ao caso, identificar exceção, combinar dispositivos etc. |
| `literalness` | alta, média ou baixa, com critério explícito |
| `distractor_pattern` | troca de sujeito, prazo, requisito, modalidade, consequência, competência, exceção, generalização, instituto próximo etc. |
| `legal_contrast` | distinção jurídica decisiva, quando houver |
| `editorial_signal` | o que a futura apostila precisa tornar explícito por causa desse tipo de cobrança |

## Taxonomia mínima reproduzível

### Literalidade

- `alta` — a solução depende predominantemente de reconhecer texto/requisito legal específico;
- `média` — exige texto legal + distinção ou pequena aplicação;
- `baixa` — exige aplicação sistemática, encadeamento procedimental ou comparação mais ampla.

### Operação cognitiva

Usar uma ou mais categorias controladas:

- `literal_recall`;
- `requirement_discrimination`;
- `exception_identification`;
- `case_application`;
- `procedure_sequence`;
- `competence_or_deadline`;
- `institute_comparison`;
- `legal_consequence`.

### Distractor

Usar categorias controladas sempre que aplicáveis:

- `subject_swap`;
- `object_swap`;
- `requirement_swap`;
- `deadline_swap`;
- `competence_swap`;
- `action_or_remedy_swap`;
- `culpability_or_modality_swap`;
- `damage_or_result_requirement`;
- `exception_inversion`;
- `overgeneralization`;
- `neighboring_institute`;
- `partial_truth`.

Novas categorias só devem ser criadas se a amostra exigir, com definição no próprio artefato.

## Síntese obrigatória

Depois da tabela por questão, consolidar sem overfitting:

1. quantidade observada por domínio e por ano;
2. operações cognitivas recorrentes;
3. grau de literalidade observado;
4. padrões de distractor;
5. pares de institutos/regras que a banca aproxima;
6. sinais editoriais para profundidade, exemplos, tabelas comparativas e casos-limite;
7. limites da amostra e mudanças de blueprint entre os anos.

Não transformar contagem observada em probabilidade futura.

## Critério de fechamento do Gate 3

Marcar Gate 3 como `closed` somente quando:

- todas as questões jurídicas das quatro provas estiverem classificadas;
- a taxonomia usada estiver definida no arquivo;
- cada classificação puder ser rastreada até questão/ano;
- a síntese distinguir dado observado de interpretação editorial;
- nenhum resultado histórico tiver sobrescrito o syllabus vigente;
- inconsistências ou dúvidas de classificação estiverem explicitadas.

## Depois do Gate 3 — DIREITO-004

Construir uma matriz de cobertura/autoria para cada um dos seis SubjectPacks, conforme `APOSTILA_AUTHORING_PROTOCOL.md`, usando conjuntamente:

```text
syllabus vigente
+ DIREITO_SOURCES.md
+ DIREITO_B2_BANCA_ANALYSIS.md
+ complexidade e risco de confusão
```

Só depois das seis matrizes sem lacunas o Gate 5 poderá autorizar redação substancial.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

Neste runtime, a tentativa de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` em `2026-09-11` falhou com `Could not resolve host: github.com`. Se a condição persistir, registrar a impossibilidade; não tratá-la como `PASS`, conforme DEC-0009.
