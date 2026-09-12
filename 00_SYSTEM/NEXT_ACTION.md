# NEXT_ACTION

## DIREITO-001 — Definir o próximo SubjectPack de Conhecimentos em Direito e fechar sua base de autoria

Português 2.0.0 está concluído e validado. O próximo domínio canônico é **B2 — Conhecimentos em Direito**, porque o syllabus vigente atribui **30 questões** a esse bloco, a maior parcela ainda sem SubjectPack.

Não começar redigindo a apostila. O primeiro objetivo é transformar B2 em um escopo autorável, versionado e verificável.

## Evidência canônica

`competitions/tjsp-escrevente-2025/SYLLABUS.md` define B2 com:

- Direito Penal;
- Direito Processual Penal;
- Direito Processual Civil;
- Direito Constitucional;
- Direito Administrativo;
- Legislação Interna;
- total de 30 questões no bloco.

O edital vigente prevalece sobre provas históricas conforme DEC-0010. Legislação deve respeitar a versão/data relevante e o recorte expresso no edital.

## Recuperação obrigatória

Antes de mutar o repositório, ler:

1. `AGENTS.md`;
2. `00_SYSTEM/START_HERE.md`;
3. `PROJECT_CONTROL.md`;
4. `00_SYSTEM/CHECKPOINT.md`;
5. este `NEXT_ACTION.md`;
6. `00_SYSTEM/DECISION_LOG.md`, especialmente DEC-0009, DEC-0010, DEC-0011, DEC-0013, DEC-0016, DEC-0017 e DEC-0018;
7. `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`;
8. `00_SYSTEM/SOURCE_POLICY.md`;
9. `00_SYSTEM/QA_PROTOCOL.md`;
10. `competitions/tjsp-escrevente-2025/SYLLABUS.md`;
11. o source registry/edital map do adapter TJSP 2025.

Conferir o estado real de `main` antes de criar branch.

## Gate 1 — Definir a fronteira do SubjectPack

Antes de criar material, decidir com evidência se B2 deve ser:

- um SubjectPack único `direito`, com seis unidades/domínios; ou
- mais de um SubjectPack, caso volume, fonte ou recuperação pedagógica tornem a divisão necessária.

A decisão deve considerar:

- os 30 itens do bloco como unidade de prova;
- quantidade e extensão dos recortes normativos;
- risco de um PDF excessivamente grande para NotebookLM/uso humano;
- coerência pedagógica e de revisão;
- manutenção/versionamento de legislação.

Registrar a decisão canônica antes de redigir conteúdo substancial. Não inferir a divisão apenas por conveniência de diretório.

## Gate 2 — Fechar fontes e versões

Construir inventário verificável de todas as fontes normativas exigidas pelo B2, incluindo no mínimo:

- Código Penal nos artigos indicados pelo syllabus;
- Código de Processo Penal nos artigos indicados;
- Lei 9.099/1995 nos recortes penal e cível;
- Código de Processo Civil nos artigos indicados;
- Lei 12.153/2009;
- Constituição Federal nos títulos/capítulos/seções e art. 92 indicados;
- Lei Estadual 10.261/1968 nos artigos indicados;
- Lei 8.429/1992;
- Resolução TJSP 850/2021;
- Resolução TJSP 963/2025;
- LC Estadual 1.111/2010;
- Regimento Interno do TJSP;
- Normas da Corregedoria nos recortes exatos do edital.

Para cada fonte, registrar autoridade, identificação, recorte, versão/data relevante, proveniência e hash/tamanho quando aplicável. Não publicar binários-fonte no repositório público, conforme DEC-0011.

## Gate 3 — Análise silenciosa da banca

Usar as provas históricas já registradas para classificar as questões de Direito de 2021, 2023, 2024 e 2025 de forma reproduzível, sem deixar frequência histórica sobrescrever o edital.

Produzir análise suficiente para orientar:

- profundidade por domínio;
- tipos de cobrança;
- distinções e armadilhas recorrentes;
- necessidade de literalidade legal versus compreensão sistemática;
- desenho da prática autoral.

Essa análise é backoffice, não texto do estudante.

## Gate 4 — Matriz de cobertura/autoria

Somente após fechar fronteira e fontes, criar a matriz exigida por `APOSTILA_AUTHORING_PROTOCOL.md` com, para cada recorte:

- item do syllabus;
- fonte normativa;
- objetivo de aprendizagem;
- conceitos/regras;
- distinções e casos-limite;
- aplicações/exemplos;
- prática necessária;
- status de cobertura.

Nenhum artigo ou diploma listado no edital pode desaparecer silenciosamente.

## Gate 5 — Autorizar redação

A redação da nova apostila só começa quando:

- a fronteira do SubjectPack estiver decidida;
- fontes e versões estiverem fechadas;
- análise histórica estiver suficiente;
- matriz de cobertura/autoria estiver criada e sem lacunas estruturais.

Depois disso, seguir o protocolo de autoria, gerar PDF pesquisável, fazer QA textual/visual, publicar por readback e repetir smoke real no NotebookLM.

## Estado anterior fechado

Português 2.0.0 foi concluído com:

- QA editorial: PASS;
- PDF: 16 páginas A4, 20824 bytes, SHA-256 `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`, Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- chat NotebookLM configurado: PASS após rc2;
- Teste nativo: PASS;
- Cartões: PASS;
- Mapa mental: PASS;
- `python tools/verify.py`: não executado por impossibilidade de resolução de `github.com`, explicitamente documentada sob DEC-0009.

Não reabrir Português 2.0.0 sem evidência concreta de regressão ou nova decisão canônica.