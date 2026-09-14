# MANIFEST - SubjectPack Direito Processual Penal - TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `direito-processual-penal`  
**Pack version:** `0.1.0-draft.1`  
**Status:** `draft_pending_semantic_normative_qa`  
**Draft date:** `2026-09-14`

## Objetivo

Este SubjectPack implementa a primeira passagem completa de Direito Processual Penal para o concurso de Escrevente Técnico Judiciário do TJSP 2025. A autoria segue `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e o contrato `DPP-01` a `DPP-25` de `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

A etapa `DIREITO-008` produz somente o draft em Markdown e seus artefatos de proveniência. Não há `APOSTILA.pdf`, release candidate nem configuração final de NotebookLM nesta etapa.

## Escopo oficial

Código de Processo Penal:

`arts. 251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`.

Lei n.º 9.099/1995:

`arts. 60-83; 88-89`.

Autoridade de escopo: `SRC-TJSP-EDITAL-2025-02`.

Fontes normativas principais:

- `SRC-B2-CPP` - Decreto-Lei n.º 3.689/1941, Código de Processo Penal, Planalto;
- `SRC-B2-L9099` - Lei n.º 9.099/1995, Planalto.

Baseline autoral: texto vigente em `2025-07-29`.

Ponto de versão obrigatório: o art. 584, § 4º, do CPP foi incluído posteriormente pela Lei n.º 15.358/2026 e não integra o baseline desta apostila. O texto estudável trata o art. 584 conforme o cutoff do edital e mantém a alteração posterior apenas no backoffice.

## Estado dos arquivos

### StudentContent

- `APOSTILA.md` - `0.1.0-draft.1`; primeira implementação completa em Markdown, sem coverage IDs em títulos ou subtítulos visíveis.

### BackofficeArtifact

- `MANIFEST.md` - identidade, escopo, rastreabilidade e estado de gates;
- `SOURCES.md` - proveniência, autoridade e controle de versão;
- `CHANGELOG.md` - histórico do draft;
- análise de banca compartilhada - `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md`;
- matriz de autoria compartilhada - `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`.

## Rastreabilidade de cobertura

Os identificadores abaixo pertencem exclusivamente ao backoffice. Eles não aparecem como rótulos estudáveis na apostila.

| coverage_id | recorte | localização pedagógica principal | estado no draft |
|---|---|---|---|
| DPP-01 | CPP 251-258 | juiz e Ministério Público | implemented_pending_qa |
| DPP-02 | CPP 261-267 | acusado e defensor | implemented_pending_qa |
| DPP-03 | CPP 274 | serventuários e funcionários da justiça | implemented_pending_qa |
| DPP-04 | CPP 351-369 | citações | implemented_pending_qa |
| DPP-05 | CPP 370-372 | intimações | implemented_pending_qa |
| DPP-06 | CPP 394-405 | procedimento comum | implemented_pending_qa |
| DPP-07 | CPP 406-421 | júri: acusação, instrução preliminar e decisões | implemented_pending_qa |
| DPP-08 | CPP 422-431 | júri: preparação, desaforamento e pauta | implemented_pending_qa |
| DPP-09 | CPP 432-452 | júri: jurados e Conselho de Sentença | implemented_pending_qa |
| DPP-10 | CPP 453-474 | júri: reunião, sessão e instrução em plenário | implemented_pending_qa |
| DPP-11 | CPP 475-491 | júri: debates, quesitação e votação | implemented_pending_qa |
| DPP-12 | CPP 492-497 | júri: sentença, ata e atribuições do presidente | implemented_pending_qa |
| DPP-13 | CPP 531-538 | procedimento sumário | implemented_pending_qa |
| DPP-14 | CPP 541-548 | restauração de autos | implemented_pending_qa |
| DPP-15 | CPP 574-580 | recursos em geral | implemented_pending_qa |
| DPP-16 | CPP 581-592 | recurso em sentido estrito | implemented_pending_qa |
| DPP-17 | CPP 593-603 | apelação | implemented_pending_qa |
| DPP-18 | CPP 604-620 | tramitação e julgamento recursal no intervalo legal | implemented_pending_qa |
| DPP-19 | CPP 621-631 | revisão criminal | implemented_pending_qa |
| DPP-20 | CPP 632-646 | dispositivos revogados, RE/REsp e carta testemunhável | implemented_pending_qa |
| DPP-21 | CPP 647-667 | habeas corpus | implemented_pending_qa |
| DPP-22 | Lei 9.099, 60-68 | competência, princípios e comunicação no JECrim | implemented_pending_qa |
| DPP-23 | Lei 9.099, 69-76 | fase preliminar, composição civil e transação penal | implemented_pending_qa |
| DPP-24 | Lei 9.099, 77-83 | procedimento sumaríssimo e recursos | implemented_pending_qa |
| DPP-25 | Lei 9.099, 88-89 | representação e suspensão condicional do processo | implemented_pending_qa |

## Engenharia pedagógica implementada

A primeira passagem organiza o conteúdo por fluxos e decisões, com:

- distinção entre impedimento, suspeição e regras de extensão;
- fluxos de citação e intimação;
- sequência do procedimento comum e do procedimento do júri;
- contrastes entre pronúncia, impronúncia, absolvição sumária e desclassificação;
- composição, impedimentos e formação do Conselho de Sentença;
- sequência de plenário, debates, quesitos, votação, sentença e ata;
- contraste entre ordinário, sumário e sumaríssimo;
- fluxos recursais e distinção entre RESE, apelação, revisão criminal, carta testemunhável e habeas corpus;
- sequência própria do JECrim, com composição civil, transação penal, procedimento sumaríssimo, apelação, embargos de declaração e suspensão condicional do processo;
- mini-casos e prática autoral A-E com gabarito comentado separado.

A análise histórica da VUNESP é usada como engenharia silenciosa. O StudentContent não contém previsão de frequência, metadiscurso de banca nem questões reais reproduzidas.

## Lições herdadas do primeiro pipeline jurídico

Desde o `draft.1`:

1. coverage IDs e rótulos internos ficam fora dos títulos e subtítulos estudáveis;
2. a apostila não transforma ausência de jurisprudência ou doutrina na fonte legal em afirmação de inexistência externa;
3. a futura configuração do tutor deverá declarar explicitamente os limites do corpus;
4. o futuro smoke deverá inspecionar Teste, Cartões e Mapa mental para vazamento de metadados internos.

## Estado dos gates

| gate | resultado atual |
|---|---|
| implementação DPP-01...DPP-25 | complete_first_pass_pending_semantic_qa |
| fontes e baseline | recorded |
| contraste/fluxo | implemented_pending_qa |
| prática autoral | implemented_pending_qa |
| ausência de coverage IDs em títulos estudáveis | selfcheck_pass |
| QA semântico/normativo específico do pack | not_started |
| PDF | not_created_by_design |
| NotebookLM | not_started |
| `python tools/verify.py` | not_executed_current_environment - runtime continua sem resolução DNS para checkout canônico; não tratado como PASS |

## Próximo estágio

Após merge de `DIREITO-008`, a continuidade deve avançar para o QA semântico/normativo específico do `0.1.0-draft.1`, com revisão integral das duas fontes primárias, checagem de cobertura DPP-01...DPP-25, revisão de questões e correção de qualquer ambiguidade antes de gerar PDF ou preparar release candidate.
