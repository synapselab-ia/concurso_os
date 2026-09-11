# CHANGELOG — Português — TJSP Escrevente 2025

## 2.0.0 — 2026-09-11 — release candidate blocked

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
- QA-9 PDF: **pass local / publicação no GitHub bloqueada**;
- QA-10: parcial, porque o gate determinístico não pôde ser executado neste runtime.

### PDF 2.0.0 — artefato local validado

O artefato que substitui a distribuição anterior no release final, quando puder ser publicado de forma íntegra, possui:

- 29 páginas A4;
- 40928 bytes;
- SHA-256 `1a7a1cbe8a0597f94ea490da7eec8ff874f2430ef596ec5bb9c3a14ecb2f1d62`;
- Git blob esperado `b06f1150ac71cd9b87a3f8341be70a1c87355ccc`;
- texto pesquisável;
- `pdfinfo` e extração textual conferidos;
- 29 páginas renderizadas e inspecionadas sem clipping/overlap evidente;
- conferência de Questão 30, gabarito, acentuação e síntese final.

### Correção de estado após readback binário

Uma tentativa anterior de publicação foi documentada incorretamente como um PDF de 34 páginas / 140496 bytes. O readback real do GitHub demonstrou que o blob ligado à branch (`5bea23e3bd98b307496a086e98effc51853a0cd7`) continha apenas **7500 bytes** e terminava durante um stream compactado. Logo, não era uma distribuição 2.0.0 íntegra.

A branch foi corrigida para não manter um arquivo corrompido: `APOSTILA.pdf` foi restaurado temporariamente ao último binário íntegro conhecido da 1.0.0 (`2287be2ba025228cc311722effc794fc9edf476f`, 13950 bytes). O Markdown 2.0.0 e o backoffice permanecem na branch.

Esse fallback **não é o PDF 2.0.0** e não deve ser usado no smoke de aceitação.

### Arquitetura NotebookLM preservada

```text
FONTES
→ APOSTILA.pdf 2.0.0 íntegro

CONFIGURAÇÃO DA CONVERSA
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

### Pendências para release final

1. publicar o PDF 2.0.0 íntegro no GitHub e confirmar por readback o artefato correto;
2. executar smoke real no NotebookLM usando somente esse PDF como corpus de conteúdo;
3. verificar Teste, Cartões, Mapa mental e chat configurado;
4. registrar o resultado e, se passar, concluir release e merge do PR #12.

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
- deixa de existir necessidade cotidiana de marcar/desmarcar metodologia;
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
- no chat, a metodologia funcionou melhor como instrução operacional: uma questão por vez, alternativas A–E, espera da resposta, confiança e possibilidade de relatório.

### Decisão

- `APOSTILA.pdf` passa a ser o principal conteúdo do estudante;
- `METODOLOGIA_NOTEBOOKLM.md` passa a ser instrução exclusiva do chat;
- `ANALISE_BANCA.md`, `SOURCES.md`, `MANIFEST.md`, `CHANGELOG.md`, edital e provas históricas ficam no backoffice;
- DEC-0015 é substituída por DEC-0016.

### Consequência editorial

A qualidade da apostila passa a ser o principal gargalo do sistema. O próximo trabalho é reconstruir `APOSTILA.md`/`APOSTILA.pdf` para sustentar Testes, Cartões, Mapas mentais, Relatórios e consulta no NotebookLM sem depender do backoffice.

---

## 1.0.1 — 2026-09-11

Patch de usabilidade para tornar o NotebookLM Studio-first e reduzir burocracia operacional.

### Alterado

- o Estúdio passa a ser interface principal de estudo;
- Teste, Cartões, Mapa mental, Relatórios e outros artefatos podem ser usados conforme a necessidade;
- prompts longos e seleção constante de subconjuntos de fontes deixam de ser requisitos;
- chat passa a ser camada de aprofundamento/correção;
- smoke test foi simplificado para observar resultado real antes de otimizações.

### Artefatos não alterados

- `APOSTILA.md`, `APOSTILA.pdf`, `ANALISE_BANCA.md` e `SOURCES.md` permaneceram iguais à distribuição 1.0.0.

---

## 1.0.0 — 2026-09-11

Primeira versão operacional do SubjectPack.

### Adicionado

- cobertura dos 13 itens de Língua Portuguesa do edital 2025;
- apostila autoral focada em interpretação, coesão, semântica e norma-padrão;
- `APOSTILA.pdf` pesquisável para distribuição no NotebookLM;
- análise de 88 questões de Português das provas 2021, 2023, 2024 e 2025;
- classificação reproduzível por categoria primária;
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