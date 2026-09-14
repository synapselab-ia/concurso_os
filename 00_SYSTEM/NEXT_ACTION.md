# NEXT_ACTION

## DIREITO-009: Executar QA semântico e normativo do draft `direito-processual-penal`

A primeira implementação de `direito-processual-penal` foi criada em:

`materials/tjsp-escrevente-2025/direito-processual-penal/`

Estado de entrada:

- versão: `0.1.0-draft.1`;
- `DIREITO-008`: `closed_as_draft`;
- 25 coverage rows `DPP-01...DPP-25` implementadas em primeira passagem;
- `APOSTILA.md`: 25 unidades estudáveis, sem coverage IDs em títulos/subtítulos;
- prática autoral: 52 questões A-E com gabarito comentado separado;
- fontes e cutoff registrados em `SOURCES.md`;
- PDF: não criado, por desenho desta etapa;
- NotebookLM: não iniciado;
- gate determinístico: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, porque o runtime local continua sem resolução DNS de `github.com`; a impossibilidade foi reavaliada em `2026-09-14` e não é tratada como PASS.

**O pack continua draft. Não gerar `APOSTILA.pdf`, não preparar release candidate e não iniciar smoke do NotebookLM antes de fechar este QA.**

## Entradas obrigatórias

Antes de revisar, ler conjuntamente:

- `AGENTS.md`;
- `00_SYSTEM/START_HERE.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `00_SYSTEM/SOURCE_POLICY.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/SOURCES.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/MANIFEST.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/CHANGELOG.md`;
- `competitions/tjsp-escrevente-2025/SYLLABUS.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`, seção `direito-processual-penal`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- `materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md` somente como lição de processo.

Fontes normativas primárias:

- `SRC-B2-CPP` - Código de Processo Penal oficial;
- `SRC-B2-L9099` - Lei n.º 9.099/1995 oficial.

Baseline obrigatório: `2025-07-29`.

## QA-1: cobertura e rastreabilidade

Revisar integralmente o recorte:

- CPP arts. `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`;
- Lei n.º 9.099/1995 arts. `60-83; 88-89`.

Para cada `DPP-01...DPP-25`, confirmar:

- todos os artigos e dispositivos relevantes do intervalo estão ensinados ou remetidos de forma inequívoca;
- nenhum coverage row foi apenas nominalmente mencionado;
- dispositivos revogados dentro do intervalo foram identificados corretamente, sem reconstrução por analogia;
- coverage IDs permanecem apenas no backoffice;
- títulos e subtítulos do StudentContent continuam livres de `DPP-*`, labels de gate e outros metadados internos.

Pontos de completude que devem ser verificados explicitamente:

- CPP arts. `604-608`: revogados;
- CPP art. `611`: revogado pelo Decreto-Lei n.º 552/1969;
- CPP arts. `632-636`: revogados;
- demais artigos vigentes entre `609-620` e `637-646`: conferir um a um;
- Lei n.º 9.099/1995 arts. `60-83`: conferir todos os dispositivos, inclusive regras literais de citação, intimação, acusação oral, audiência, apelação e embargos.

Não promover a cobertura para `pass` por amostragem.

## QA-2: exatidão normativa e controle de versão

Fazer revisão completa contra as duas fontes oficiais, conferindo especialmente:

- impedimento e suspeição do juiz;
- extensão das regras a Ministério Público, defensor, serventuários e funcionários;
- citação por mandado, precatória, edital, hora certa e rogatória;
- situações especiais de militar, funcionário público e acusado preso;
- efeitos da citação por edital e da ausência do acusado;
- intimações pessoais e por publicação;
- rito ordinário, sumário e sumaríssimo;
- rejeição da denúncia/queixa e absolvição sumária;
- ordem da audiência, limites de testemunhas, diligências e alegações finais;
- todas as etapas do Tribunal do Júri, da primeira fase à sentença e ata;
- hipóteses, prazos e efeitos do RESE e da apelação;
- revisão criminal;
- carta testemunhável;
- habeas corpus;
- competência, princípios, fase preliminar, composição civil, transação penal, procedimento sumaríssimo e recursos do JECrim;
- representação e suspensão condicional do processo.

### Controle de versão obrigatório

O CPP atual contém art. `584, § 4º` posterior ao cutoff, incluído pela Lei n.º `15.358/2026`. Esse parágrafo não pode entrar como regra da prova.

Reabrir a fonte oficial e confirmar que o StudentContent mantém:

```text
baseline da prova = 2025-07-29
art. 584 no baseline = sem o § 4º posterior
alteração de 2026 = backoffice/version drift, não conteúdo exigido
```

Se qualquer outro drift posterior ao cutoff for encontrado dentro do recorte, não o incorporar silenciosamente. Registrar e reconciliar no inventário canônico antes de alterar o conteúdo.

## QA-3: didática, fluxos e contrastes

Para cada unidade, verificar se a explicação entrega de modo suficiente:

```text
regra
-> sujeito/legitimidade
-> momento
-> requisito ou prazo
-> consequência/efeito
-> exceção
-> contraste com instituto próximo
-> aplicação curta
-> síntese ou fluxo quando útil
```

Dar prioridade aos contrastes que realmente resolvem alternativas próximas:

- impedimento x suspeição;
- citação por edital x hora certa;
- rejeição x absolvição sumária;
- ordinário x sumário x sumaríssimo;
- pronúncia x impronúncia x absolvição sumária x desclassificação;
- RESE x apelação;
- apelação x revisão criminal;
- carta testemunhável x recurso destravado por ela;
- habeas corpus x revisão criminal;
- composição civil x transação penal x suspensão condicional do processo;
- embargos de declaração do CPP x JECrim.

Remover generalizações que pareçam regra universal quando a lei traz hipótese específica.

## QA-4: prática autoral

Revisar as **52 questões** uma a uma.

Cada item deve ter:

- cinco alternativas plausíveis;
- exatamente uma resposta defensável dentro do recorte e do baseline;
- comando sem ambiguidade involuntária;
- gabarito coerente com o comentário;
- comentário que exponha o elemento decisivo;
- nenhum requisito dependente de jurisprudência ou doutrina não fornecida pelo corpus;
- nenhuma contaminação do texto legal por alteração pós-cutoff.

Conferir também os requisitos `Q-LIT`, `Q-CMP`, `Q-CAS`, `Q-FLX`, `Q-VER` e `Q-FULL` definidos na matriz. Se uma row estiver subtestada, substituir ou adicionar prática somente na medida necessária.

## QA-5: utilidade como corpus

Verificar:

- hierarquia de títulos;
- consistência de termos;
- proximidade entre regra, contraste e exemplo;
- legibilidade de tabelas e fluxos;
- ausência de metadiscurso de banca no StudentContent;
- ausência de coverage IDs e labels internos em títulos estudáveis;
- capacidade de a apostila funcionar isoladamente como fonte de estudo.

Aplicar a lição do smoke de Direito Penal: quando a fonte não sustentar informação externa ao corpus, não converter silêncio da fonte em negativa universal.

## Artefato esperado

Criar:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`

O arquivo deve registrar:

- resultado separado de QA-1 a QA-5;
- artigo/dispositivo revisado quando houver correção material;
- correções executadas e motivação;
- pendências reais;
- estado final das 52 questões;
- estado dos requisitos de prática por coverage row;
- decisão explícita sobre prontidão ou não para preparar release candidate.

Se houver falha semântica, manter o pack como `draft`, corrigir `APOSTILA.md` e não mascarar a falha como PASS.

## Critério de saída

`DIREITO-009` somente fecha quando:

- DPP-01...DPP-25 estiverem integralmente rastreados;
- todo o recorte do CPP e da Lei n.º 9.099/1995 tiver sido rechecado contra fonte oficial;
- o cutoff `2025-07-29` estiver preservado;
- o drift do art. 584, § 4º, permanecer isolado;
- dispositivos revogados do intervalo estiverem corretamente tratados;
- fluxos e contrastes essenciais estiverem corretos;
- as 52 questões tiverem revisão semântica individual;
- `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md`, `PROJECT_CONTROL.md`, `CHECKPOINT.md` e este arquivo refletirem o estado real;
- não houver PDF nem promoção a RC antes da decisão do QA.

Se o draft ficar aprovado, a etapa seguinte será preparar o release candidate de `direito-processual-penal`, incluindo configuração do tutor e depois o pipeline de PDF/NotebookLM. Isso não equivale automaticamente a release final.

## Gate canônico

Antes de encerrar a implementação, executar:

```bash
python tools/verify.py
```

No runtime atual, a tentativa de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` em `2026-09-14` retornou:

`Could not resolve host: github.com`

Enquanto essa condição persistir, documentar a impossibilidade conforme DEC-0009 e não tratá-la como `PASS`.
