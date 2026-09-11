# CHANGELOG — Português — TJSP Escrevente 2025

## 2.0.0 — 2026-09-11 — release candidate

Reconstrução major da apostila de Língua Portuguesa sob `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`.

### Autoria e cobertura

- auditada a distribuição 1.0.0 em `APOSTILA_AUDIT_1.0.0.md`;
- criada e fechada a matriz `APOSTILA_AUTHORING_MATRIX_2.0.0.md`;
- os 13 itens do syllabus B1.1–B1.13 estão explicitamente localizados e `covered`;
- o sumário foi reorganizado por dependências pedagógicas;
- `APOSTILA.md` foi reconstruída para aprendizado, revisão e recuperação semântica pelo NotebookLM.

### Conteúdo reconstruído

- leitura de textos verbais, não verbais, multissemióticos, literários e não literários;
- literalidade, pressuposição, inferência, extrapolação, tema, tese, argumento e ponto de vista;
- progressão, coesão referencial, pronomes relativos e relações lógico-semânticas;
- pares críticos como causa/explicação, consequência/conclusão, condição/concessão e finalidade/consequência;
- semântica contextual, polissemia, sinonímia, antonímia, linguagem figurada, ambiguidade e modalização;
- classes de palavras em funcionamento;
- concordância verbal/nominal, inclusive impessoais e `se`;
- regência verbal/nominal, pronomes oblíquos, colocação pronominal e crase;
- pontuação e reescrita integrada;
- unidade de estratégias integradas de análise.

### Prática

- adicionadas 30 questões autorais A–E;
- prática dividida entre interpretação/coesão/semântica, norma-padrão e integração;
- gabarito comentado separado da bateria;
- comentários apontam o elemento decisivo de cada item.

### QA editorial

`APOSTILA_QA_2.0.0.md` registra:

- QA-1 cobertura: pass;
- QA-2 exatidão/fonte: pass;
- QA-3 didática: pass;
- QA-4 distinções/casos-limite: pass;
- QA-5 prática: pass;
- QA-6 coerência com banca sem overfitting: pass;
- QA-7 utilidade estática para NotebookLM: pass; smoke real pendente;
- QA-8 redundância/coerência: pass;
- QA-9 PDF textual/visual + publicação/readback: pass;
- QA-10: parcial, porque o gate determinístico não pôde ser executado neste runtime.

### PDF 2.0.0 — distribuição publicada

A distribuição canônica da branch foi regenerada em formato compacto para caber integralmente no transporte do conector GitHub sem perder o conteúdo textual estudável:

- 16 páginas A4;
- 20824 bytes;
- SHA-256 `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`;
- Git blob `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- PDF 1.4 pesquisável, não criptografado;
- extração textual de aproximadamente 54,5 mil caracteres;
- Questão 30, gabarito, acentuação crítica e síntese final recuperados por `pdftotext`;
- 16 páginas renderizadas a 150 dpi e inspecionadas sem clipping/overlap observado;
- readback GitHub confirmou `size=20824` e o blob esperado.

### Incidente de transporte corrigido

Uma tentativa anterior havia sido documentada incorretamente como um PDF de 34 páginas / 140496 bytes. O readback mostrou que o blob ligado à branch continha somente 7500 bytes e estava truncado. Esse estado foi revogado, o fallback 1.0.0 foi usado temporariamente para remover a corrupção e, nesta revisão, substituído pela distribuição 2.0.0 íntegra acima.

Os blobs intermediários/rejeitados não são distribuição:

- `5bea23e3bd98b307496a086e98effc51853a0cd7` — truncado;
- `82046b5da25a7565fd84763763be33ebac2556fc` — órfão/intermediário;
- `2287be2ba025228cc311722effc794fc9edf476f` — fallback 1.0.0 temporário.

### Arquitetura NotebookLM preservada

```text
FONTES
→ APOSTILA.pdf 2.0.0

CONFIGURAÇÃO DA CONVERSA
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

### Pendência para release final

Resta o smoke real no NotebookLM usando somente o `APOSTILA.pdf` 2.0.0 como corpus de conteúdo, verificando Teste, Cartões, Mapa mental e chat configurado. O resultado só deve ser marcado `PASS` se realmente executado.

### Gate determinístico

O runtime local não conseguiu resolver `github.com`, impedindo checkout canônico e execução válida de `python tools/verify.py`. A impossibilidade permanece registrada sem ser tratada como `pass`.

---

## 1.0.3 — 2026-09-11

Patch de instalação após observar a configuração nativa de conversas do NotebookLM.

### Observado

- o NotebookLM oferece configuração própria de conversa em `Configurar as conversas → Personalizado`;
- essa camada é mais apropriada para instruções do tutor do que carregar `METODOLOGIA_NOTEBOOKLM.md` como fonte;
- o controle de tamanho de resposta foi mantido em `Padrão` por default do projeto.

### Decisão

- `APOSTILA.pdf` permanece como fonte principal do notebook;
- `METODOLOGIA_NOTEBOOKLM.md` permanece versionada no GitHub, mas como texto de configuração da conversa, não fonte;
- o usuário copia o bloco operacional da metodologia para `Personalizado` (ou equivalente);
- Estúdio e chat usam o mesmo corpus didático limpo;
- DEC-0017 refina DEC-0016.

### Conteúdo não alterado

- `APOSTILA.md`, `APOSTILA.pdf`, `ANALISE_BANCA.md` e `SOURCES.md` permaneceram iguais à distribuição 1.0.0.

A próxima ação passou a ser reconstruir a apostila com target recomendado 2.0.0.

---

## 1.0.2 — 2026-09-11

Patch arquitetural após smoke tests reais do NotebookLM.

### Observado

- com `METODOLOGIA_NOTEBOOKLM.md` selecionada no Teste, o NotebookLM gerou pergunta sobre a própria metodologia;
- sem a metodologia, o Teste gerou pergunta conceitual baseada na apostila;
- no chat, a metodologia funcionou melhor como instrução operacional.

### Decisão

- `APOSTILA.pdf` passa a ser o principal conteúdo do estudante;
- `METODOLOGIA_NOTEBOOKLM.md` passa a ser instrução exclusiva do chat;
- `ANALISE_BANCA.md`, `SOURCES.md`, `MANIFEST.md`, `CHANGELOG.md`, edital e provas históricas ficam no backoffice;
- DEC-0015 é substituída por DEC-0016.

---

## 1.0.1 — 2026-09-11

Patch de usabilidade para tornar o NotebookLM Studio-first e reduzir burocracia operacional.

### Alterado

- o Estúdio passa a ser interface principal de estudo;
- Teste, Cartões, Mapa mental, Relatórios e outros artefatos podem ser usados conforme a necessidade;
- prompts longos e seleção constante de subconjuntos de fontes deixam de ser requisitos;
- chat passa a ser camada de aprofundamento/correção.

---

## 1.0.0 — 2026-09-11

Primeira versão operacional do SubjectPack.

### Adicionado

- cobertura dos 13 itens de Língua Portuguesa do edital 2025;
- apostila autoral focada em interpretação, coesão, semântica e norma-padrão;
- `APOSTILA.pdf` pesquisável para distribuição no NotebookLM;
- análise de 88 questões de Português das provas 2021, 2023, 2024 e 2025;
- metodologia específica para NotebookLM;
- manifesto, fontes e limites epistemológicos.

### QA do release

- `APOSTILA.md` revisada em UTF-8;
- PDF final: 8 páginas, formato Letter, texto pesquisável;
- renderização das 8 páginas verificada sem clipping/overlap evidente;
- extração textual verificada para acentos e termos-chave;
- corpus quantitativo conferido em 88 questões: 24 (2021) + 24 (2023) + 24 (2024) + 16 (2025).

### Decisões de versão

- provas históricas informam formato, não sobrescrevem o edital 2025;
- a classificação de questões é analítica do projeto, não oficial da VUNESP;
- questões reais não são republicadas no pack;
- a apostila prioriza as operações exigidas no edital e observadas no corpus.