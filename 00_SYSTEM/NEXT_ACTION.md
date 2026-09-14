# NEXT_ACTION

## DIREITO-011: Gerar e validar o PDF canônico de `direito-processual-penal`

`DIREITO-010` preparou o release candidate `0.1.0-rc.1` de Direito Processual Penal sem alterar semanticamente o conteúdo jurídico aprovado no `0.1.0-draft.2`.

Estado de entrada esperado após merge do RC:

- pack: `direito-processual-penal`;
- versão: `0.1.0-rc.1`;
- conteúdo-base: `0.1.0-draft.2` semanticamente congelado;
- cobertura `DPP-01...DPP-25`: `PASS_AFTER_CORRECTIONS`;
- revisão normativa: `PASS_AFTER_CORRECTIONS`;
- prática: `60/60 PASS`;
- corpus Markdown: `PASS_FOR_MARKDOWN`;
- configuração do tutor: `PASS_STATIC`;
- NotebookLM corpus/tutor estático: `PASS_STATIC`;
- baseline: `2025-07-29`;
- CPP art. 584, § 4º, de 2026: fora do baseline estudável;
- `APOSTILA.pdf`: ainda não criado/versionado;
- NotebookLM live smoke: ainda não executado;
- gate determinístico: `NOT_EXECUTED_CURRENT_ENVIRONMENT` no runtime de `DIREITO-010`, porque o checkout canônico falhou por DNS; não é PASS.

O QA acumulado está em:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`

## Entradas obrigatórias

Antes de gerar o PDF, ler conjuntamente:

- `AGENTS.md`;
- `00_SYSTEM/START_HERE.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente o gate de PDF;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/MANIFEST.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/SOURCES.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/CHANGELOG.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md` somente para compatibilidade de corpus;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md` somente como referência do procedimento de identidade binária, não como fonte jurídica.

Antes de escrever, confirmar `main`, PRs abertas e estado real do GitHub.

## 1. Congelar a fonte do PDF

O PDF deve derivar exclusivamente do `APOSTILA.md` do `0.1.0-rc.1`.

Antes da geração:

- registrar o Git blob do Markdown congelado;
- confirmar que a versão é `0.1.0-rc.1`;
- confirmar que a promoção do RC não alterou o corpo jurídico do `draft.2`;
- não fazer correção jurídica durante a diagramação.

Se for encontrado erro semântico ou normativo, interromper o pipeline de PDF, retornar o pack a draft e reabrir o QA. Não corrigir silenciosamente o conteúdo apenas no PDF.

## 2. Gerar o candidato de PDF

Produzir `APOSTILA.pdf` pesquisável, preferencialmente A4, preservando:

- hierarquia de títulos;
- tabelas e fluxos;
- acentos e símbolos jurídicos;
- distinção visual entre corpo didático e prática;
- separação estrutural entre bateria de questões e gabarito comentado;
- legibilidade sem depender de elementos gráficos frágeis.

Registrar no candidato local:

- número de páginas;
- tamanho em bytes;
- versão/formato do PDF quando disponível;
- SHA-256;
- pesquisabilidade.

## 3. Readback textual

Extrair texto do candidato e confirmar, no mínimo:

- título `Direito Processual Penal`;
- `Unidade 1` e `Unidade 25`;
- `Gabarito comentado`;
- referências críticas como `art. 584`, `§`, `JECrim`, `habeas corpus` e `carta testemunhável`;
- presença da questão `60` e do respectivo gabarito;
- ausência de corrupção de caracteres jurídicos.

A geração do arquivo, sozinha, não é PASS.

## 4. Inspeção visual integral

Renderizar e inspecionar todas as páginas do mesmo candidato auditado.

Verificar:

- clipping;
- sobreposição;
- páginas vazias indevidas;
- cabeçalhos ou títulos órfãos em posição impeditiva;
- tabelas quebradas de forma que altere significado;
- fluxos ilegíveis;
- acentos, `§`, números de artigos e caracteres especiais;
- separação clara entre questões e gabarito;
- continuidade visual da numeração de questões 1-60.

Registrar quantidade de páginas efetivamente inspecionadas e resultado.

## 5. Publicar o binário exato no GitHub

Versionar em:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`

A publicação precisa preservar a identidade do candidato auditado. Depois do upload/versionamento:

- ler o Git blob do arquivo remoto;
- calcular ou registrar o Git blob esperado do candidato local quando possível;
- confirmar identidade binária entre remoto e candidato auditado;
- registrar SHA-256, páginas e tamanho do arquivo canônico.

Não declarar `PASS_CANONICAL_BINARY_IDENTITY` se o binário versionado não puder ser provado como o mesmo candidato auditado.

Se o ambiente não oferecer transporte binário confiável, registrar `canonical_pdf_transport_blocked` e manter o gate aberto. Não usar hash de arquivo local como se fosse hash do repositório.

## 6. Atualizar QA e continuidade

Atualizar, conforme o estado real:

- `APOSTILA_QA_0.1.0.md`;
- `MANIFEST.md`;
- `CHANGELOG.md`;
- `PROJECT_CONTROL.md`;
- `CHECKPOINT.md`;
- este arquivo.

O PDF não altera a versão semântica do pack. `0.1.0-rc.1` permanece release candidate.

## 7. Próximo estágio após PDF canônico

Somente depois de `PASS_CANONICAL_BINARY_IDENTITY`, avançar para o smoke real do NotebookLM usando:

```text
FONTES
-> somente APOSTILA.pdf canônico

CONFIGURAÇÃO DA CONVERSA
-> bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

O smoke deverá testar chat explicativo, treino interativo, Teste, Cartões, Mapa mental, ausência de IDs internos e ao menos uma pergunta fora do corpus para verificar disciplina epistemológica.

Não presumir resultado de interação externa não executada.

## Critério de saída

`DIREITO-011` só fecha como PDF validado quando:

- o candidato derivar do Markdown congelado do RC;
- readback textual passar;
- todas as páginas forem inspecionadas visualmente;
- o binário auditado estiver versionado no GitHub;
- a identidade binária do artefato canônico estiver comprovada;
- QA e continuidade refletirem os metadados exatos;
- `python tools/verify.py` tiver sido executado ou a impossibilidade atual tiver sido explicitamente reavaliada conforme DEC-0009.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

Se o runtime ainda não conseguir obter checkout canônico, reavaliar e documentar a impossibilidade. Nunca registrar impossibilidade como `PASS`.
