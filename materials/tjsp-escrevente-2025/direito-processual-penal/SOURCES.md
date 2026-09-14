# SOURCES - Direito Processual Penal - TJSP Escrevente 2025

**Pack version:** `0.1.0-draft.1`  
**Source review for first draft:** `2026-09-14`

## Regra de autoridade

O material separa escopo, verdade normativa e evidência empírica:

```text
edital vigente -> define o que entra
CPP e Lei 9.099/1995 oficiais -> sustentam o conteúdo jurídico
provas/análise histórica -> calibram forma, contraste e profundidade
matriz de cobertura -> contrato editorial e de QA
```

Provas históricas não substituem o edital nem criam conteúdo programático. A apostila não usa inferência de frequência histórica como previsão de cobrança.

## Escopo oficial

### `SRC-TJSP-EDITAL-2025-02`

- Tipo: edital oficial.
- Autoridade: Tribunal de Justiça do Estado de São Paulo.
- Título: Edital de Abertura n.º 02/2025 - Escrevente Técnico Judiciário.
- Publicação registrada: `2025-07-29`.
- Arquivo original registrado: `TJSP2503_224_20250801114000.pdf.pdf`.
- SHA-256 registrado no inventário canônico: `c87c402606c99c75cb0efef19716003b2dce0a728e58dab2800cbf5d099e7400`.
- Uso: delimita Direito Processual Penal aos arts. `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667` do CPP e aos arts. `60-83; 88-89` da Lei n.º 9.099/1995.

O resumo operacional do syllabus está em `competitions/tjsp-escrevente-2025/SYLLABUS.md`. Em caso de divergência, o edital prevalece.

## Fonte normativa principal 1

### `SRC-B2-CPP`

- Diploma: Decreto-Lei n.º 3.689/1941 - Código de Processo Penal.
- Autoridade: Presidência da República / Planalto.
- URL oficial: `https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm`.
- Recorte: arts. `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`.
- Baseline autoral: `2025-07-29`.
- Estado de versão no Gate 2: `cutoff_closed_drift_mapped`.
- Verificação do primeiro draft: fonte oficial reaberta em `2026-09-14` para conferência de dispositivos, prazos, sujeitos, cabimento, efeitos e sequências procedimentais.

### Drift pós-cutoff que não entra na apostila

A compilação oficial atual contém o art. `584, § 4º`, incluído pela Lei n.º `15.358/2026`. Esse parágrafo é posterior ao cutoff do edital e fica excluído do StudentContent. Para o baseline `2025-07-29`, o art. 584 é tratado sem esse § 4º.

A existência dessa alteração posterior não autoriza atualizar silenciosamente o conteúdo estudável. O backoffice mantém as duas camadas separadas:

```text
baseline da prova: 2025-07-29
texto posterior observado: Lei 15.358/2026 no art. 584, § 4º
regra do pack: estudar o baseline, registrar o drift fora do corpus
```

## Fonte normativa principal 2

### `SRC-B2-L9099`

- Diploma: Lei n.º 9.099/1995 - Juizados Especiais Cíveis e Criminais.
- Autoridade: Presidência da República / Planalto.
- URL oficial: `https://www.planalto.gov.br/ccivil_03/leis/l9099.htm`.
- Recorte: arts. `60-83; 88-89`.
- Baseline autoral: `2025-07-29`.
- Estado de versão no Gate 2: `cutoff_closed_no_scoped_drift`.
- Verificação do primeiro draft: fonte oficial reaberta em `2026-09-14`; não foi incorporada alteração posterior ao cutoff no recorte estudável.

## Pontos normativos sensíveis conferidos na primeira autoria

A primeira passagem reabriu a fonte primária para os pontos mais propensos a troca de requisito, prazo ou efeito, entre eles:

- CPP arts. 252-258: impedimento, suspeição e extensão das regras;
- CPP arts. 261-267 e 274: defesa técnica e extensão da suspeição aos serventuários;
- CPP arts. 351-372: mandado, precatória, hora certa, edital, acusado preso, estrangeiro e intimações;
- CPP arts. 394-405: espécies do procedimento comum, resposta, absolvição sumária, audiência, testemunhas, diligências e alegações finais;
- CPP arts. 406-421: primeira fase do júri, prazos e decisões possíveis;
- CPP arts. 422-497: preparação, jurados, Conselho, plenário, debates, quesitação, votação, sentença e ata;
- CPP arts. 531-538: procedimento sumário;
- CPP arts. 541-548: restauração de autos;
- CPP arts. 574-620: regras gerais, RESE, apelação e tramitação recursal;
- CPP arts. 621-646: revisão criminal, dispositivos revogados, recurso extraordinário/especial e carta testemunhável;
- CPP arts. 647-667: habeas corpus;
- Lei 9.099, arts. 60-83: competência, fase preliminar, transação penal, procedimento sumaríssimo e recursos;
- Lei 9.099, arts. 88-89: representação e suspensão condicional do processo.

Esta lista é registro de revisão, não substitui o QA normativo integral do próximo gate.

## Evidência empírica da banca

As provas históricas ficam no backoffice e não são reproduzidas no StudentContent.

### `SRC-TJSP-PROVA-2025`

- Fundação VUNESP.
- Arquivo original: `tjsp 2025.pdf`.
- SHA-256 registrado: `068cfd0fbc929d250e2703cbf90ff2a7efde3bf4fb86915eeb9088a2a78a8b87`.
- Questões de Processo Penal classificadas no Gate 3: `21-25`.
- Papel: referência empírica mais próxima de forma e operação cognitiva.

### `SRC-TJSP-PROVA-2024`

- Fundação VUNESP.
- Arquivo original: `tjsp 2024.pdf`.
- SHA-256 registrado: `05993d52b7cd955bb29ea14f175f60ecbde2f7f9b3b4c069143c249f1947836d`.
- Questões processuais penais classificadas historicamente no artefato de banca.
- Papel: contraste de institutos, fluxos, requisitos e prazos.

### `SRC-TJSP-PROVA-2023`

- Fundação VUNESP.
- Arquivo original: `tjsp 2023.pdf`.
- SHA-256 registrado: `ae203c145c68766c83aa4c4b35dbb2778854481f9d89fb752de28b649f3bfc4d`.
- Questões processuais penais classificadas historicamente no artefato de banca.
- Papel: fluxo procedimental, comunicação de atos e recursos.

### `SRC-TJSP-PROVA-2021`

- Fundação VUNESP.
- Arquivo original: `tjsp 2021.pdf`.
- SHA-256 registrado: `4368240090841eab1de84d20cfbfd0d8a86579a081136308f2409051f4e12d90`.
- Questões processuais penais classificadas historicamente no artefato de banca.
- Papel: literalidade, comparação e aplicação em casos curtos.

## Artefatos canônicos de engenharia

### `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`

Gate 3 fechado. Para Processo Penal, registra recorrência histórica de literalidade combinada com fluxo procedimental, prazos, comunicação dos atos, competência, cabimento de recursos e alternativas quase corretas que trocam sujeito, requisito ou efeito. Esses sinais orientam a engenharia silenciosa do draft.

### `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`

Gate 4 fechado. `DPP-01` a `DPP-25` formam o contrato de cobertura, profundidade, contraste, fluxo e prática. Os IDs permanecem no backoffice e não aparecem como rótulos de estudo na apostila.

### `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`

Inventário canônico que fecha o baseline, registra o drift do CPP art. 584, § 4º, e mantém a Lei n.º 9.099/1995 estável no recorte auditado.

### `materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md`

Lição de processo, não fonte jurídica. Determina que identificadores de backoffice não contaminem títulos estudáveis e que limites do corpus sejam declarados como limites, não como negativas universais.

## Política de redação

- O texto é autoral e explicativo, sem reprodução extensa da legislação.
- Requisitos, prazos, legitimidade, competência, cabimento e efeitos são sintetizados a partir das fontes oficiais.
- Não é introduzida jurisprudência como se estivesse contida na lei seca.
- Quando a lei não resolve questão externa ao corpus, a apostila não transforma silêncio normativo em conclusão universal.
- Exemplos e questões são autorais.
- Dispositivos revogados dentro dos intervalos do edital são identificados como revogados quando relevantes para a leitura integral do recorte.

## Estado desta revisão

`0.1.0-draft.1` é primeira implementação completa, ainda pendente de QA semântico/normativo específico. A fonte foi reaberta durante a autoria, mas o próximo gate deve revisar novamente todo o recorte antes de qualquer PDF ou release candidate.
