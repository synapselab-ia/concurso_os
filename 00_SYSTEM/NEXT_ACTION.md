# NEXT_ACTION

## DIREITO-004 — Construir as seis matrizes de cobertura/autoria de B2

Os Gates 1, 2 e 3 estão fechados. A fronteira editorial, o baseline normativo e a análise histórica reproduzível da banca já existem.

**Ainda não iniciar a redação substancial das apostilas.** O último gate comum antes da autoria é garantir que todo o syllabus vigente esteja mapeado, sem lacunas, para uma estratégia de ensino e QA em cada um dos seis SubjectPacks.

## Evidência obrigatória

Usar conjuntamente:

- `competitions/tjsp-escrevente-2025/SYLLABUS.md` — autoridade de escopo;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` — baseline, proveniência e drift;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md` — forma de cobrança e sinais editoriais;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md` — fronteiras dos seis packs;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` — contrato de autoria.

Histórico da banca calibra profundidade e apresentação, mas não pode eliminar ou adicionar conteúdo do edital.

## Artefato esperado

Criar:

`competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`

O arquivo deve conter uma matriz independente para cada SubjectPack:

1. `direito-penal`;
2. `direito-processual-penal`;
3. `direito-processual-civil`;
4. `direito-constitucional`;
5. `direito-administrativo`;
6. `legislacao-interna`.

## Campos mínimos por unidade de cobertura

Cada linha deve registrar, no mínimo:

- `coverage_id` estável;
- pack;
- fonte/source_id;
- recorte normativo exato;
- instituto/tema;
- objetivo de aprendizagem;
- forma pedagógica principal (`exposição`, `quadro comparativo`, `fluxo`, `tabela`, `mini-caso`, `linha do tempo`, combinação);
- contraste/risco de confusão;
- evidência de banca relevante, quando existir;
- risco de versão/drift, quando existir;
- requisito de prática/QA.

## Regras de granularidade

A matriz não precisa ter uma linha por artigo. Deve agrupar dispositivos apenas quando formarem uma unidade jurídica coerente e verificável.

É proibido usar grupos tão amplos que ocultem partes do edital. Todo artigo, intervalo, diploma integral ou recorte interno listado no syllabus deve poder ser rastreado a pelo menos um `coverage_id`.

Quando um intervalo contiver institutos muito diferentes, subdividi-lo. Quando vários artigos contíguos compuserem um único procedimento ou instituto, podem ficar juntos.

## Sinais editoriais obrigatórios do Gate 3

Sem alterar o conteúdo programático, incorporar na matriz:

- Penal: elementos típicos + tipos vizinhos + mini-casos;
- Processual Penal: fluxos, decisões, recursos, prazos e sujeitos;
- Processual Civil: regra/exceção, competência, efeitos, JEC/JEFaz e mini-casos;
- Constitucional: regra/exceção, pares conceituais, nacionalidade e servidores;
- Administrativo: hipótese→requisito→efeito, linhas do tempo disciplinares e modalidade→sanção;
- Legislação Interna: tabelas operacionais, sujeitos, condições, prazos e controle de versão.

## Controle de versão obrigatório

A matriz deve carregar explicitamente os pontos de drift já fechados no Gate 2, sem substituí-los por texto atual:

- CPP art. 584, § 4º;
- CPC arts. 196, 529-A e 998;
- CF art. 37, XVI, `b`;
- Lei SP 10.261/1968 art. 78;
- LC SP 1.111/2010 — alterações posteriores já mapeadas;
- RITJSP — baseline até Assento 591/2025;
- NSCGJ — baseline do cutoff e alterações posteriores mapeadas;
- duplicidade literal de `Capítulo XI` no edital continua sem correção inferida.

## Critério de fechamento do Gate 4

Marcar `closed` somente quando:

- os seis packs tiverem matriz própria;
- 100% dos recortes do syllabus estiverem cobertos;
- toda fonte estiver ligada a `coverage_id` verificável;
- não houver artigo/faixa/diploma interno órfão;
- riscos de confusão e sinais editoriais estiverem registrados;
- drift relevante estiver associado às unidades afetadas;
- a duplicidade oficial das NSCGJ estiver preservada sem falsa resolução;
- a matriz puder servir diretamente de contrato para a redação e para QA de cobertura.

## Depois do Gate 4 — DIREITO-005

Com Gates 1–4 fechados, autorizar a redação do primeiro SubjectPack: `direito-penal`.

A primeira implementação de autoria deverá usar a matriz como contrato: nenhuma unidade fora do syllabus, nenhuma unidade do syllabus omitida, e engenharia de banca aplicada silenciosamente.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

A tentativa de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` em `2026-09-12` continuou falhando com `Could not resolve host: github.com`. Se persistir, documentar a impossibilidade conforme DEC-0009; não tratar como `PASS`.
