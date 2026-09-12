# SOURCES — Direito Penal — TJSP Escrevente 2025

**Pack version:** `0.1.0-draft.1`  
**Source verification for this draft:** `2026-09-12`

## Regra de autoridade

Escopo, verdade normativa e evidência empírica têm papéis distintos:

```text
edital vigente → define o que entra
Código Penal oficial → sustenta o conteúdo jurídico
provas/análise histórica → calibram forma, contraste e profundidade
matriz de cobertura → contrato editorial/QA
```

Provas históricas não substituem o edital nem criam conteúdo programático. Explicações editoriais não substituem a fonte normativa.

## Escopo oficial

### `SRC-TJSP-EDITAL-2025-02`

- Tipo: edital oficial.
- Autoridade: Tribunal de Justiça do Estado de São Paulo.
- Título: Edital de Abertura n.º 02/2025 — Escrevente Técnico Judiciário.
- Publicação registrada: `2025-07-29`.
- Arquivo original registrado: `TJSP2503_224_20250801114000.pdf.pdf`.
- SHA-256: `c87c402606c99c75cb0efef19716003b2dce0a728e58dab2800cbf5d099e7400`.
- Binário no repositório público: `false`.
- Uso: delimita Direito Penal aos arts. `293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359` do Código Penal.

## Fonte normativa principal

### `SRC-B2-CP`

- Diploma: Decreto-Lei n.º 2.848/1940 — Código Penal.
- Autoridade: Presidência da República / Planalto.
- URL oficial: `https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm`.
- Recorte: arts. `293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.
- Baseline autoral: `2025-07-29`.
- Estado de versão no Gate 2: `cutoff_closed_no_scoped_drift`.
- Verificação do Gate 2: atos posteriores que alteraram o Código Penal foram auditados contra este recorte e não foi identificada alteração textual direta nos dispositivos exigidos.
- Observação de fronteira: o art. `338-A`, incluído posteriormente pela Lei n.º 15.280/2025, está fora do recorte do edital e não é absorvido por proximidade numérica.
- Uso neste pack: única fonte primária para afirmações normativas específicas do conteúdo penal, sem introdução de jurisprudência não prevista na fonte.

A página oficial compilada foi reaberta em `2026-09-12` para a primeira redação. Como o inventário canônico registra ausência de drift pós-cutoff dentro do recorte, o texto atual desses dispositivos pode ser usado para confirmar o baseline sem promover artigos posteriores fora do syllabus.

## Evidência empírica da banca

### `SRC-TJSP-PROVA-2025`

- Fundação VUNESP.
- Arquivo original: `tjsp 2025.pdf`.
- SHA-256: `068cfd0fbc929d250e2703cbf90ff2a7efde3bf4fb86915eeb9088a2a78a8b87`.
- Questões de Direito Penal classificadas no Gate 3: `17–20`.
- Papel: referência empírica mais próxima para forma e nível; não altera o syllabus.

### `SRC-TJSP-PROVA-2024`

- Fundação VUNESP.
- Arquivo original: `tjsp 2024.pdf`.
- SHA-256: `05993d52b7cd955bb29ea14f175f60ecbde2f7f9b3b4c069143c249f1947836d`.
- Questões de Direito Penal classificadas: `25–30`.
- Papel: histórico de operações cognitivas, tipos vizinhos e distractores.

### `SRC-TJSP-PROVA-2023`

- Fundação VUNESP.
- Arquivo original: `tjsp 2023.pdf`.
- SHA-256: `ae203c145c68766c83aa4c4b35dbb2778854481f9d89fb752de28b649f3bfc4d`.
- Questões de Direito Penal classificadas: `25–30`.
- Papel: histórico de operações cognitivas, tipos vizinhos e distractores.

### `SRC-TJSP-PROVA-2021`

- Fundação VUNESP.
- Arquivo original: `tjsp 2021.pdf`.
- SHA-256: `4368240090841eab1de84d20cfbfd0d8a86579a081136308f2409051f4e12d90`.
- Questões de Direito Penal classificadas: `25–30`.
- Papel: histórico de operações cognitivas, tipos vizinhos e distractores.

## Artefatos canônicos de engenharia

### `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`

Gate 3 fechado. Para Penal, registra coexistência de literalidade e casos curtos, comparação de tipos vizinhos, discriminação de requisitos e distractores que trocam objeto, sujeito, modalidade ou finalidade. O draft converte esses sinais em quadros comparativos e mini-casos, sem expor metadiscurso de banca ao estudante.

### `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`

Gate 4 fechado. `DP-01`…`DP-10` formam o contrato de cobertura, profundidade, contraste e prática deste pack.

### `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`

Inventário de versão que fecha `SRC-B2-CP` no cutoff e separa alterações posteriores do restante de B2.

## Política de redação

- O texto da apostila é autoral e explicativo; não reproduz extensamente a lei.
- Dispositivos, requisitos, efeitos e penas são sintetizados a partir do Código Penal oficial.
- Não é introduzida jurisprudência como se fosse parte do recorte legal.
- Quando uma distinção depende apenas da letra da lei, o critério decisivo é explicitado no mesmo bloco.
- Questões reais ficam no backoffice; a prática do draft é autoral.

## Política para NotebookLM

Enquanto o pack estiver em `draft`, não há distribuição canônica no NotebookLM. Em release, a arquitetura prevista continua:

```text
fonte estudável → APOSTILA.pdf validado
configuração do tutor → METODOLOGIA_NOTEBOOKLM.md na camada nativa da conversa
backoffice → GitHub/ChatGPT
```
