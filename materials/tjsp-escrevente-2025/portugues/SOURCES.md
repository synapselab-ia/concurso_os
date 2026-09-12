# SOURCES — Língua Portuguesa — TJSP Escrevente 2025

**Pack version:** `2.0.0-rc`

## Fonte de autoridade para escopo

### `SRC-TJSP-EDITAL-2025-02`

- Tipo: edital oficial.
- Título: Edital de Abertura n.º 02/2025 — Escrevente Técnico Judiciário.
- Autoridade: Tribunal de Justiça do Estado de São Paulo.
- Publicação registrada no projeto: 2025-07-29.
- Arquivo original: `TJSP2503_224_20250801114000.pdf.pdf`.
- SHA-256 registrado: `c87c402606c99c75cb0efef19716003b2dce0a728e58dab2800cbf5d099e7400`.
- Uso neste pack: escopo oficial de Língua Portuguesa, quantidade de 16 questões e regras gerais do certame.
- Política: em divergência quanto ao escopo, o edital prevalece.

## Corpus empírico de prova

### `SRC-TJSP-PROVA-2025`

- Fundação VUNESP.
- Arquivo original: `tjsp 2025.pdf`.
- SHA-256: `068cfd0fbc929d250e2703cbf90ff2a7efde3bf4fb86915eeb9088a2a78a8b87`.
- Português analisado: Q01–Q16.
- Papel: referência empírica mais próxima do edital vigente.

### `SRC-TJSP-PROVA-2024`

- Fundação VUNESP.
- Arquivo original: `tjsp 2024.pdf`.
- SHA-256: `05993d52b7cd955bb29ea14f175f60ecbde2f7f9b3b4c069143c249f1947836d`.
- Português analisado: Q01–Q24.
- Papel: histórico de formatos e operações de cobrança.

### `SRC-TJSP-PROVA-2023`

- Fundação VUNESP.
- Arquivo original: `tjsp 2023.pdf`.
- SHA-256: `ae203c145c68766c83aa4c4b35dbb2778854481f9d89fb752de28b649f3bfc4d`.
- Português analisado: Q01–Q24.
- Papel: histórico de formatos e operações de cobrança.

### `SRC-TJSP-PROVA-2021`

- Fundação VUNESP.
- Arquivo original: `tjsp 2021.pdf`.
- SHA-256: `4368240090841eab1de84d20cfbfd0d8a86579a081136308f2409051f4e12d90`.
- Português analisado: Q01–Q24.
- Papel: histórico de formatos e operações de cobrança.

## Fonte metodológica legada

### `SRC-LEGACY-STUDY-METHODOLOGY`

- Arquivo: `Metodologia-para-sessões-de-estudo.txt`.
- SHA-256: `45a37f1cee2e620880d850c620aacd20a66bf4c48ffc133628bfcf4415387c91`.
- Natureza: desenho pedagógico anterior; não é fonte factual sobre língua ou banca.
- Elementos migrados: questão por vez, declaração de confiança, acerto firme/instável, diagnóstico de erro, análise de alternativas, reteste e relatório periódico.

## Artefatos autorais e de engenharia do pack

### `APOSTILA.md`

Fonte autoral **2.0.0** reconstruída. O syllabus controla o que precisa ser coberto; provas e `ANALISE_BANCA.md` calibram silenciosamente profundidade, distinções e tipos de aplicação. Exemplos e as 30 questões são autorais.

### `APOSTILA.pdf`

A distribuição final 2.0.0 ainda está em gate de publicação binária. O candidato local validado possui 29 páginas A4, 40928 bytes e SHA-256 `1a7a1cbe8a0597f94ea490da7eec8ff874f2430ef596ec5bb9c3a14ecb2f1d62`.

**Estado real da branch:** o arquivo `APOSTILA.pdf` atualmente apontado no GitHub é deliberadamente o fallback íntegro da versão 1.0.0 (`2287be2ba025228cc311722effc794fc9edf476f`, 13950 bytes), restaurado depois que o readback demonstrou truncamento da tentativa de upload do PDF 2.0.0. Ele não deve ser confundido com a distribuição 2.0.0 nem usado no smoke de aceitação.

### `ANALISE_BANCA.md`

Análise do projeto a partir das 88 questões de Português do corpus. A classificação por categoria primária é taxonomia analítica própria e reproduzível pelo apêndice do arquivo.

### `APOSTILA_AUDIT_1.0.0.md`

Auditoria editorial da distribuição anterior, usada para identificar compressão, lacunas didáticas, distinções ausentes e insuficiência de prática.

### `APOSTILA_AUTHORING_MATRIX_2.0.0.md`

Matriz de cobertura/autoria que liga os 13 itens do syllabus aos objetivos, conceitos, contrastes, aplicações, fontes, sinal empírico, profundidade e localização final na apostila.

### `APOSTILA_QA_2.0.0.md`

Registro dos gates editoriais, do PDF e de repositório aplicados ao release candidate 2.0.0, incluindo a falha de publicação binária e as validações ainda pendentes.

### `METODOLOGIA_NOTEBOOKLM.md`

Configuração versionada do tutor. Não é fonte factual nem conteúdo estudável. Seu bloco operacional deve ficar na configuração nativa da conversa quando disponível.

## Política canônica de uso no NotebookLM

Conforme DEC-0016/DEC-0017:

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf 2.0.0 íntegro

CONFIGURAÇÃO DA CONVERSA
→ Personalizado (ou equivalente)
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Por padrão, não carregar como fontes:

- `METODOLOGIA_NOTEBOOKLM.md`;
- `ANALISE_BANCA.md`;
- `SOURCES.md`;
- `MANIFEST.md`;
- `CHANGELOG.md`;
- auditoria/matriz/QA;
- edital e provas históricas apenas para explicar o projeto.

Fontes adicionais só entram quando houver necessidade pedagógica concreta. Os PDFs de origem não são republicados no repositório público.

## Questões reais e direitos autorais

Questões reais ficam no backoffice para análise e calibração. A apostila usa questões autorais. Quando o usuário pedir questão real, preferir acesso ao PDF de origem e referência pontual, evitando republicação extensa de conteúdo protegido.