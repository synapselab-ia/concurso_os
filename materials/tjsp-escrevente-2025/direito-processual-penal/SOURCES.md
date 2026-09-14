# SOURCES - Direito Processual Penal - TJSP Escrevente 2025

**Pack version:** `0.1.0-rc.1`  
**Full source review:** `2026-09-14`

## Regra de autoridade

```text
edital vigente -> define o escopo
CPP e Lei 9.099/1995 oficiais -> sustentam afirmações normativas
provas/análise histórica -> calibram forma, contraste e profundidade
matriz de cobertura -> contrato editorial e de QA
```

Provas históricas não substituem edital ou legislação e não criam previsão de cobrança.

## Escopo oficial

### `SRC-TJSP-EDITAL-2025-02`

- autoridade: TJSP, Edital de Abertura n.º 02/2025;
- publicação registrada: `2025-07-29`;
- arquivo original registrado: `TJSP2503_224_20250801114000.pdf.pdf`;
- SHA-256 canônico: `c87c402606c99c75cb0efef19716003b2dce0a728e58dab2800cbf5d099e7400`;
- recorte: CPP `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667` e Lei 9.099/1995 `60-83; 88-89`.

O `SYLLABUS.md` é resumo operacional. Em divergência, o edital prevalece.

## Fonte normativa principal 1

### `SRC-B2-CPP`

- diploma: Decreto-Lei n.º 3.689/1941, Código de Processo Penal;
- autoridade: Presidência da República / Planalto;
- URL oficial: `https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm`;
- recorte: `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`;
- baseline: `2025-07-29`;
- estado no Gate 2: `cutoff_closed_drift_mapped`.

A fonte oficial foi reaberta em `2026-09-14` durante `DIREITO-009` e o recorte foi rechecado integralmente por intervalo para sujeitos, prazos, legitimidade, competência, cabimento, efeitos, sequência e revogações.

### Drift pós-cutoff isolado

A compilação atual contém art. `584, § 4º`, incluído pela Lei n.º `15.358/2026`. O parágrafo é posterior ao cutoff e não integra o StudentContent.

```text
baseline da prova = 2025-07-29
art. 584 no baseline = §§ 1º a 3º
art. 584, § 4º de 2026 = drift de backoffice
```

Nenhum outro drift pós-cutoff foi promovido a conteúdo estudável no QA semântico.

### Pontos de completude corrigidos no QA

A revisão integral de `DIREITO-009` explicitou, entre outros:

- art. 262;
- arts. 363-365;
- art. 394-A;
- art. 398 revogado;
- art. 400-A;
- art. 537 revogado e art. 538;
- detalhamento de 574-580, 581-592 e 593-603;
- arts. 604-608 revogados, art. 611 revogado e conteúdo vigente de 609-620;
- arts. 632-636 revogados e conteúdo vigente de 637-646;
- art. 647-A e sequência de 647-667.

O tratamento de dispositivo revogado é declarativo: não se reconstrói regra por analogia.

## Fonte normativa principal 2

### `SRC-B2-L9099`

- diploma: Lei n.º 9.099/1995;
- autoridade: Presidência da República / Planalto;
- URL oficial: `https://www.planalto.gov.br/ccivil_03/leis/l9099.htm`;
- recorte: `60-83; 88-89`;
- baseline: `2025-07-29`;
- estado no Gate 2: `cutoff_closed_no_scoped_drift`.

A fonte oficial foi reaberta em `2026-09-14`. `DIREITO-009` rechecou todo o intervalo, com atenção especial a competência, atos de comunicação, termo circunstanciado, composição civil, representação, transação, acusação oral, audiência, sentença, apelação, embargos, art. 81, § 1º-A, e suspensão condicional do processo.

Não foi incorporada alteração pós-cutoff no recorte.

## Evidência empírica da banca

As provas históricas permanecem exclusivamente como backoffice de engenharia editorial:

- `SRC-TJSP-PROVA-2025`, SHA-256 `068cfd0fbc929d250e2703cbf90ff2a7efde3bf4fb86915eeb9088a2a78a8b87`, Processo Penal em `21-25`;
- `SRC-TJSP-PROVA-2024`, SHA-256 `05993d52b7cd955bb29ea14f175f60ecbde2f7f9b3b4c069143c249f1947836d`;
- `SRC-TJSP-PROVA-2023`, SHA-256 `ae203c145c68766c83aa4c4b35dbb2778854481f9d89fb752de28b649f3bfc4d`;
- `SRC-TJSP-PROVA-2021`, SHA-256 `4368240090841eab1de84d20cfbfd0d8a86579a081136308f2409051f4e12d90`.

O Gate 3 sustenta engenharia silenciosa de literalidade, fluxo, prazo, competência, recurso e distratores próximos. Não altera o syllabus.

## Artefatos canônicos de engenharia

- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`: análise empírica;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`: contrato `DPP-01...DPP-25`;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`: inventário de versão de B2;
- `APOSTILA_QA_0.1.0.md`: resultado de `DIREITO-009` e QA estático de `DIREITO-010`;
- `materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md`: lição de processo, não fonte jurídica.

## Política de redação

- texto autoral e explicativo, sem reprodução extensa da lei;
- prazos, requisitos, legitimidade, competência, cabimento e efeitos sustentados nas fontes oficiais;
- nenhuma jurisprudência ou doutrina é inventada para completar silêncio normativo;
- ausência no corpus é tratada como limite do corpus, não como negativa universal;
- questões e mini-casos são autorais;
- revogações no intervalo são identificadas explicitamente quando relevantes.

## Relação entre `draft.2` e `rc.1`

O `0.1.0-rc.1` não altera o conteúdo jurídico aprovado no `0.1.0-draft.2`. `DIREITO-010` promove a identidade do candidato, acrescenta `METODOLOGIA_NOTEBOOKLM.md` e registra QA estático. A revisão normativa permanece a executada em `DIREITO-009`.

## Política para NotebookLM

A arquitetura do release candidate é:

```text
fonte estudável -> APOSTILA.pdf validado e versionado
configuração do tutor -> METODOLOGIA_NOTEBOOKLM.md na camada nativa da conversa
backoffice -> GitHub/ChatGPT
```

`METODOLOGIA_NOTEBOOKLM.md` não deve ser carregado como fonte estudável. Enquanto o PDF canônico e o smoke real permanecerem pendentes, o pack continua `release_candidate_incomplete`.
