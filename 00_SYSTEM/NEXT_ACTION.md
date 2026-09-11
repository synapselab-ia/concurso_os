# NEXT_ACTION

## APOSTILA-002 — Reconstruir Português aplicando o protocolo canônico de autoria

A arquitetura NotebookLM está definida por `DEC-0016`/`DEC-0017` e o processo editorial por `DEC-0018` + `APOSTILA_AUTHORING_PROTOCOL.md`.

O próximo trabalho é **refazer a apostila de Português**, porque ela é o produto principal do estudante e o corpus que alimenta o NotebookLM.

Target recomendado do release: `portugues 2.0.0`.

## Recuperação obrigatória no próximo chat

Antes de escrever, seguir `AGENTS.md` e ler pelo menos:

1. `00_SYSTEM/START_HERE.md`;
2. `PROJECT_CONTROL.md`;
3. `00_SYSTEM/PROJECT_SPEC.md`;
4. `00_SYSTEM/ARCHITECTURE.md`;
5. `00_SYSTEM/DATA_MODEL.md`;
6. `00_SYSTEM/CHECKPOINT.md`;
7. este `NEXT_ACTION.md`;
8. `00_SYSTEM/DECISION_LOG.md`, especialmente DEC-0010, DEC-0013, DEC-0014, DEC-0016, DEC-0017 e DEC-0018;
9. `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` **integralmente**;
10. `00_SYSTEM/SOURCE_POLICY.md` e `00_SYSTEM/QA_PROTOCOL.md`;
11. `competitions/tjsp-escrevente-2025/SYLLABUS.md`;
12. `materials/tjsp-escrevente-2025/portugues/ANALISE_BANCA.md`;
13. `materials/tjsp-escrevente-2025/portugues/SOURCES.md`;
14. `materials/tjsp-escrevente-2025/portugues/APOSTILA.md` atual, somente como objeto de auditoria/reaproveitamento seletivo;
15. `materials/tjsp-escrevente-2025/portugues/METODOLOGIA_NOTEBOOKLM.md`, somente para garantir compatibilidade do corpus com o tutor configurado.

Verificar também o estado real da `main` e PRs abertos antes de escrever.

## Arquitetura NotebookLM a preservar

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf

CONFIGURAÇÃO DA CONVERSA
→ Personalizado (ou equivalente)
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

A apostila deve funcionar como **corpus didático limpo**. `ANALISE_BANCA.md`, `SOURCES.md`, protocolo de autoria, manifest, changelog e documentação de QA permanecem no backoffice.

## Execução obrigatória pelo protocolo

### Etapa 1 — Auditoria

Auditar a apostila atual e registrar lacunas concretas de:

- cobertura;
- profundidade;
- precisão;
- exemplos;
- distinções;
- exercícios;
- sequência pedagógica;
- utilidade para NotebookLM;
- redundância/metadiscurso.

### Etapa 2 — Matriz de cobertura/autoria

Antes da reescrita completa, mapear cada item do syllabus para:

```text
learning_goal
concepts
contrasts
applications
source_refs
banca_signal
depth
status
```

Nenhum item do edital pode desaparecer silenciosamente.

### Etapa 3 — Sumário pedagógico

Desenhar o novo sumário a partir de dependências de aprendizado e da matriz, não apenas copiando a ordem do edital ou da apostila antiga.

### Etapa 4 — Reconstrução

Reescrever `APOSTILA.md` segundo o perfil de Língua Portuguesa do protocolo:

```text
conceito linguístico
→ efeito/regra
→ como reconhecer no contexto
→ contraste
→ exemplos/pares mínimos
→ reescrita
→ aplicação
→ síntese/prática
```

A banca deve influenciar silenciosamente profundidade, distinções, tipos de erro e prática. Evitar transformar o material em relatório sobre TJSP/VUNESP.

### Etapa 5 — QA editorial

Executar e registrar os gates aplicáveis de `APOSTILA_AUTHORING_PROTOCOL.md`:

1. cobertura;
2. exatidão/fonte;
3. didática;
4. distinções/casos-limite;
5. prática;
6. coerência com banca sem overfitting;
7. utilidade para NotebookLM;
8. redundância/coerência.

### Etapa 6 — PDF

Gerar novo `APOSTILA.pdf` pesquisável e executar QA textual/visual:

- extração de texto;
- acentos/símbolos;
- clipping/overlap;
- tabelas;
- hierarquia;
- legibilidade;
- separação de perguntas/gabaritos.

### Etapa 7 — Release e continuidade

Atualizar:

- `MANIFEST.md`;
- `CHANGELOG.md`;
- `PROJECT_CONTROL.md`;
- `CHECKPOINT.md`;
- `NEXT_ACTION.md`.

Executar `python tools/verify.py` ou justificar explicitamente a impossibilidade. Revisar diff/readback, abrir PR e fazer merge quando couber sob `DEC-0009`.

## Definition of Done

`APOSTILA-002` só termina quando:

- todos os itens de Português do syllabus estão cobertos de modo ensinável;
- a apostila funciona para aprender do zero e revisar;
- conceitos confundíveis estão explicitamente separados;
- exemplos, contraexemplos e prática autoral são suficientes;
- fatos/regras sensíveis estão source-grounded;
- a apostila funciona como corpus do NotebookLM sem depender do backoffice;
- o chat configurado consegue explicar/treinar usando esse corpus;
- todos os gates aplicáveis do protocolo estão registrados como executados;
- o novo PDF foi validado;
- versão, continuidade e release foram atualizados no GitHub.

Não iniciar os SubjectPacks das outras matérias antes de fechar e testar este padrão com Português, salvo nova decisão canônica explícita.
