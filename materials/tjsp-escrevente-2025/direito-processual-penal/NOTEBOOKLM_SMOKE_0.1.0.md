# NOTEBOOKLM_SMOKE_0.1.0 - Direito Processual Penal - TJSP Escrevente 2025

**Gate:** `DIREITO-012`  
**Pack:** `direito-processual-penal 0.1.0-rc.1`  
**Initial attempt date:** `2026-09-15`  
**Real user evidence recorded:** `2026-09-18`  
**Result:** `PASS_BEHAVIORAL_ON_RC1_CORPUS_INVALIDATED`

## Estado canônico revalidado

Antes de tentar o smoke, o estado real do GitHub foi rechecado:

- `main`: `b63f9a8f4b51894bf37e070eee3feeb481781855`;
- PRs abertas no início da execução: `0`;
- `APOSTILA.pdf` existe no caminho canônico;
- Git blob remoto do PDF: `4eabdacec7858120792cf792ca227335e41730b6`;
- identidade binária do PDF: `PASS_CANONICAL_BINARY_IDENTITY`;
- `NEXT_ACTION`: `DIREITO-012`, smoke real do NotebookLM.

## Corpus e configuração exigidos pelo gate

Quando o smoke puder ser executado, usar exatamente:

```text
FONTES DO NOTEBOOKLM
-> somente materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf

CONFIGURAÇÃO DA CONVERSA
-> bloco entre INICIO_CONFIG e FIM_CONFIG de METODOLOGIA_NOTEBOOKLM.md
-> fora das fontes estudáveis
```

O smoke deve verificar chat explicativo, treino A-E uma questão por vez, ausência de gabarito antes da tentativa, correção source-grounded, pergunta fora do corpus, `Teste`, `Cartões`, `Mapa mental` e ausência de IDs `DPP-*` ou metadados de backoffice nos artefatos estudáveis.

## Execução externa

Nesta execução, o runtime disponível não forneceu uma sessão autenticada do NotebookLM nem um canal interativo já conectado capaz de operar a interface do produto em nome do usuário. Por isso nenhuma conversa, Teste, Cartão, Mapa mental ou outro artefato do NotebookLM foi criado ou inspecionado.

Resultado correto:

`EXTERNAL_SMOKE_NOT_EXECUTED`

Isso não é `PASS`, `PASS_WITH_OBSERVATIONS` nem `FAIL` do comportamento do NotebookLM. É somente registro de que o gate externo não foi executado neste ambiente.

## Gate determinístico do repositório

Foi feita nova tentativa de obter checkout canônico para executar:

```text
python tools/verify.py
```

A tentativa de clone falhou com:

```text
Could not resolve host: github.com
```

Exit code: `128`.

Resultado:

`NOT_EXECUTED_CURRENT_ENVIRONMENT`

A impossibilidade não é tratada como `PASS`, conforme `DEC-0009`.

## Estado de saída

Na tentativa inicial de `2026-09-15`, `DIREITO-012` permaneceu `blocked_external_access`. Esse estado foi superado pela execução manual do usuário registrada abaixo; não representa o estado atual do gate.


---

## Evidência real fornecida pelo usuário - registrada em 2026-09-18

Após o bloqueio de acesso do runtime, o usuário executou manualmente o smoke no NotebookLM com o PDF de `0.1.0-rc.1` e forneceu transcrições e capturas da interface.

### Chat explicativo

Consulta sobre citação por edital x hora certa: `PASS`. O tutor distinguiu não localização de ocultação deliberada, apontou arts. 361/362 e tratou os efeitos de modo coerente com o corpus.

### Treino interativo

Treino A-E sobre recursos: `PASS`.

- uma questão por vez;
- nenhuma dica ou gabarito antes da tentativa;
- correção somente após a resposta;
- correção distinguiu apelação de RESE e os prazos de CPP/JECrim;
- reteste curto ocorreu somente após a correção completa.

### Disciplina epistemológica

Pergunta sobre jurisprudência mais recente do STJ: `PASS`. O tutor respondeu que a fonte selecionada não trazia a informação e não fabricou jurisprudência.

### Estúdio

- Teste: `PASS_SAMPLE` em amostra visual de questões sobre impedimento, defesa técnica, hora certa e absolvição sumária;
- Cartões: `PASS_SAMPLE` em amostra visual;
- Mapa mental: `PASS_SAMPLE`, com hierarquia processual útil;
- vazamento de `DPP-*`, QA, gates ou metadados internos nas amostras: `NOT_OBSERVED`.

## Interrupção por defeito do corpus

Depois da coleta do smoke, a revisão semântica final identificou erro autoral no art. 371 da Unidade 5. Por isso, o comportamento observado é aceito como evidência de funcionamento do tutor/Estúdio sobre o RC antigo, mas o gate de release não fecha sobre esse corpus.

Estado de saída:

`PASS_BEHAVIORAL_ON_RC1_CORPUS_INVALIDATED`

Próxima verificação externa necessária: smoke curto de regressão sobre o novo PDF derivado do `0.1.0-draft.3` corrigido.


---

## Estado após DIREITO-015 - 2026-09-18

O PDF corrigido de `0.1.0-rc.2` foi publicado com `PASS_CANONICAL_BINARY_IDENTITY`, Git blob `6374969ba722451dd6740364e24c41f25e730b54`.

A evidência comportamental ampla anterior continua útil, mas foi executada sobre o rc.1 invalidado. Falta somente uma regressão curta, executada manualmente pelo usuário, sobre o PDF rc.2:

1. confirmar a resposta correta sobre arts. 371-372;
2. confirmar uma questão A-E sem gabarito antes da tentativa;
3. confirmar ausência de IDs `DPP-*` e metadados internos.

Estado: `PENDING_SHORT_REGRESSION_ON_RC2`.


---

## Correção de continuidade do repositório - 2026-09-24

A auditoria do `main` real mostrou que o tree mesclado da PR #35 não continha o caminho canônico `APOSTILA.pdf`, apesar do registro de `DIREITO-015`. O blob auditado `6374969ba722451dd6740364e24c41f25e730b54` permaneceu existente e foi relinkado ao caminho canônico em `DIREITO-015R`, sem regeneração ou alteração do PDF.

Esta correção é exclusivamente de vínculo no repositório. **Não constitui evidência de execução do NotebookLM** e não altera a classificação do gate externo.

Estado do smoke: `PENDING_SHORT_REGRESSION_ON_RC2`.
