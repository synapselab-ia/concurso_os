# NEXT_ACTION

## APOSTILA-002-FINAL — Validar Português 2.0.0 no NotebookLM e concluir o release

A reconstrução editorial de Português 2.0.0 está concluída na branch `content/apostila-portugues-2.0.0` como **release candidate**.

Já existem e foram revisados:

- `APOSTILA_AUDIT_1.0.0.md`;
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` com B1.1–B1.13 `covered`;
- `APOSTILA.md` reconstruída;
- 30 questões autorais A–E com gabarito comentado separado;
- `APOSTILA_QA_2.0.0.md`;
- novo `APOSTILA.pdf` pesquisável de 34 páginas;
- metadados do pack e continuidade atualizados.

Não reabrir a redação integral sem evidência concreta de problema. O próximo gate é **validação real do corpus no NotebookLM**.

## Recuperação obrigatória

Seguir `AGENTS.md` e ler pelo menos:

1. `00_SYSTEM/START_HERE.md`;
2. `PROJECT_CONTROL.md`;
3. `00_SYSTEM/CHECKPOINT.md`;
4. este `NEXT_ACTION.md`;
5. `00_SYSTEM/DECISION_LOG.md`, especialmente DEC-0009, DEC-0010, DEC-0016, DEC-0017 e DEC-0018;
6. `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7, QA-9 e QA-10;
7. `materials/tjsp-escrevente-2025/portugues/MANIFEST.md`;
8. `materials/tjsp-escrevente-2025/portugues/APOSTILA_QA_2.0.0.md`;
9. `materials/tjsp-escrevente-2025/portugues/METODOLOGIA_NOTEBOOKLM.md`.

Antes de alterar qualquer coisa, conferir `main`, a branch `content/apostila-portugues-2.0.0` e o PR aberto correspondente.

## Arquitetura que o smoke test deve preservar

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf

CONFIGURAÇÃO DA CONVERSA
→ Personalizado (ou equivalente)
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Não carregar `METODOLOGIA_NOTEBOOKLM.md`, análise de banca, manifest, sources, QA, edital ou provas históricas como fontes durante este smoke, pois o objetivo é testar a suficiência do corpus didático limpo.

## Smoke test obrigatório

Usar o `APOSTILA.pdf` 2.0.0 da branch e verificar, no mínimo:

### 1. Teste

Gerar um Teste nativo e confirmar que:

- pergunta sobre Língua Portuguesa, não sobre metodologia/backoffice;
- há questões de aplicação, não apenas reprodução literal de definições;
- o material permite distinguir interpretação, relações de sentido e norma-padrão.

### 2. Cartões

Gerar Cartões e confirmar que recuperam definições, regras, exceções e contrastes úteis, por exemplo:

- inferência x extrapolação;
- causa x explicação;
- condição x concessão;
- `se` apassivador x indeterminador;
- regência x crase;
- restritiva x explicativa.

### 3. Mapa mental

Gerar Mapa mental e confirmar que a hierarquia principal da apostila é recuperada de forma inteligível, sem tratar questões/gabaritos como única estrutura do material.

### 4. Chat configurado

Com o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md` na configuração da conversa, testar pelo menos:

- uma explicação conceitual (`qual a diferença entre causa e explicação?`);
- uma dúvida normativa (`por que há crase em "à qual"?`);
- um pedido de treino (`me testa em concordância`);
- uma correção após resposta errada ou hesitante.

Confirmar que o chat consegue explicar/treinar usando o corpus sem depender do backoffice.

## Critério de aprovação

Marcar QA-7 live como `pass` somente se o smoke real acima tiver sido executado e não revelar falha material do corpus.

Se houver falha:

1. registrar o caso concreto em `APOSTILA_QA_2.0.0.md`;
2. corrigir apenas a causa observada;
3. regenerar/validar o PDF se `APOSTILA.md` mudar;
4. repetir o smoke afetado.

Se passar:

1. atualizar `APOSTILA_QA_2.0.0.md` para `QA-7 live: PASS`;
2. atualizar `MANIFEST.md` de `release-candidate` para release final;
3. atualizar `CHANGELOG.md` removendo a pendência de smoke;
4. atualizar `PROJECT_CONTROL.md` e `CHECKPOINT.md` para Português 2.0.0 final;
5. executar `python tools/verify.py`; se o ambiente ainda impedir, manter justificativa explícita conforme DEC-0009;
6. revisar diff/readback do PR;
7. fazer merge quando couber sob DEC-0009;
8. após merge, definir a próxima ação canônica para o próximo SubjectPack.

## Definition of Done restante

`APOSTILA-002` termina quando o smoke real do NotebookLM estiver registrado como aprovado e o release/continuidade estiverem finalizados no GitHub.

Até lá, **não iniciar os SubjectPacks das outras matérias** salvo nova decisão canônica explícita.
