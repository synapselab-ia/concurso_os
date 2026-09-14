# NEXT_ACTION

## DIREITO-008: Iniciar o SubjectPack `direito-processual-penal`

O primeiro pipeline jurídico foi validado em `direito-penal 0.1.0-rc.1`.

Estado fechado de Direito Penal:

- conteúdo semântico: `PASS`;
- 30/30 questões autorais: `PASS`;
- PDF canônico: `PASS_CANONICAL_BINARY_IDENTITY`;
- NotebookLM estático: `PASS_STATIC`;
- NotebookLM live smoke: `PASS_WITH_OBSERVATIONS`;
- `DIREITO-007`: `closed_with_observations`;
- `python tools/verify.py`: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, com impossibilidade DNS reavaliada em `2026-09-14` conforme DEC-0009 e sem falso PASS;
- não será criado `rc.2` apenas pelas observações do smoke;
- promoção formal de `direito-penal` para versão final sem sufixo fica separada e não bloqueia a continuação de B2.

O smoke real está documentado em:

`materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md`

## Entradas obrigatórias

Antes de escrever `direito-processual-penal`, ler conjuntamente:

- `AGENTS.md`;
- `00_SYSTEM/START_HERE.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `00_SYSTEM/SOURCE_POLICY.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`, seção `direito-processual-penal`;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- `materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md` como lição de processo, não como fonte jurídica;
- fontes primárias `SRC-B2-CPP` e `SRC-B2-L9099` na versão controlada do cutoff `2025-07-29`.

## 1. Contrato de cobertura

`direito-processual-penal` tem `25` coverage rows, `DPP-01` a `DPP-25`.

Recorte oficial:

- Código de Processo Penal: arts. `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`;
- Lei n.º 9.099/1995: arts. `60-83; 88-89`.

A matriz canônica é o contrato de cobertura, profundidade, contraste, forma e prática. Não omitir nenhuma row e não transformar a matriz em conteúdo visível do estudante.

## 2. Controle de versão obrigatório

Preservar o baseline `2025-07-29`.

Ponto de atenção já mapeado:

- CPP art. `584, § 4º`: usar o texto do cutoff; a alteração posterior pela Lei n.º `15.358/2026` deve permanecer separada e não pode contaminar a apostila do edital.

Reabrir a fonte oficial para qualquer ponto normativo sensível antes de fechar redação ou questão.

## 3. Lições obrigatórias do smoke de Direito Penal

Aplicar desde a primeira linha do novo StudentContent:

1. não colocar `DPP-01`, `DPP-02` etc. em títulos ou subtítulos visíveis da apostila;
2. coverage IDs, labels de gate e metadados de autoria ficam apenas no backoffice;
3. a rastreabilidade deve ser preservada em `MANIFEST`, matriz e QA, não no corpus estudável;
4. a futura configuração do tutor deve tratar informação ausente da fonte como limite do corpus, e não como prova de inexistência externa;
5. no smoke final, verificar explicitamente se Mapa mental, Teste e Cartões vazam metadados internos;
6. no smoke final, fazer ao menos uma pergunta sobre informação externa ao corpus para testar a disciplina epistemológica.

## 4. Primeira implementação

Criar workspace canônico:

`materials/tjsp-escrevente-2025/direito-processual-penal/`

Primeiros artefatos esperados:

- `MANIFEST.md`;
- `SOURCES.md`;
- `APOSTILA.md`;
- `CHANGELOG.md`.

A primeira passagem deve cobrir integralmente `DPP-01...DPP-25`, mas os identificadores `DPP-*` não devem aparecer no StudentContent visível.

A engenharia pedagógica deve privilegiar, conforme a matriz:

- fluxos procedimentais;
- tabelas regra/exceção quando genuinamente úteis;
- contrastes entre institutos e recursos próximos;
- prazos, sujeitos, legitimidade, competência, cabimento e efeitos;
- mini-casos autorais;
- prática de literalidade, fluxo, contraste e aplicação.

## 5. Regra de banca

Usar `DIREITO_B2_BANCA_ANALYSIS.md` apenas para engenharia silenciosa.

Não transformar frequência histórica em previsão de cobrança nem inserir metadiscurso como `a VUNESP cobra` no StudentContent sem valor pedagógico deliberado.

## 6. Gate desta etapa

A meta de `DIREITO-008` é produzir a primeira implementação completa de `direito-processual-penal` em estado `draft`, com:

- 100% de `DPP-01...DPP-25` coberto;
- fontes e baseline registrados;
- contrastes e fluxos implementados;
- prática autoral suficiente conforme a matriz;
- nenhum coverage ID exposto como título estudável;
- continuidade atualizada;
- revisão de diff/readback antes de merge.

Não gerar PDF nem promover a release candidate nesta etapa. Primeiro concluir o draft e então abrir o QA semântico/normativo específico do pack.
