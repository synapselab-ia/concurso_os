# CHANGELOG — Português — TJSP Escrevente 2025

## 2.0.0 — 2026-09-11 — release candidate

Reconstrução major da apostila de Língua Portuguesa sob `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`.

### Autoria e cobertura

- auditada a distribuição 1.0.0 em `APOSTILA_AUDIT_1.0.0.md`;
- criada e fechada a matriz `APOSTILA_AUTHORING_MATRIX_2.0.0.md`;
- os 13 itens do syllabus B1.1–B1.13 estão explicitamente localizados e marcados `covered`;
- o sumário foi reorganizado por dependências pedagógicas, em vez de repetir a ordem literal do edital;
- `APOSTILA.md` foi reconstruída para aprendizado do zero, revisão e recuperação semântica pelo NotebookLM.

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
- gabarito comentado mantido separado da bateria;
- comentários apontam o elemento decisivo de cada item.

### QA editorial

`APOSTILA_QA_2.0.0.md` registra:

- QA-1 cobertura: pass;
- QA-2 exatidão/fonte no escopo editorial: pass;
- QA-3 didática: pass;
- QA-4 distinções/casos-limite: pass;
- QA-5 prática: pass;
- QA-6 coerência com banca sem overfitting: pass;
- QA-7 utilidade estática para NotebookLM: pass; smoke real pendente;
- QA-8 redundância/coerência: pass;
- QA-9 PDF: pass;
- QA-10: parcial, pois o gate determinístico não pôde ser executado no runtime local.

### PDF 2.0.0 release candidate

- 34 páginas A4;
- 140496 bytes;
- SHA-256 `90052841384431f942f78234ce543fc5dbeb67f44793f40459632c6939dfbbc2`;
- pesquisável, com fontes Unicode incorporadas;
- 34 páginas renderizadas e inspecionadas sem clipping/overlap ou glyphs corrompidos;
- extração textual conferida, inclusive acentos e símbolos críticos.

### Arquitetura NotebookLM preservada

```text
FONTES
→ APOSTILA.pdf

CONFIGURAÇÃO DA CONVERSA
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

A metodologia foi versionada junto do pack sem mudança semântica relevante no bloco operacional.

### Pendências para release final

- executar smoke test real no NotebookLM usando somente o novo `APOSTILA.pdf` como corpus de conteúdo;
- verificar Teste, Cartões, Mapa mental e chat configurado;
- registrar o resultado e, se passar, concluir merge de APOSTILA-002.

### Gate determinístico

O runtime local não conseguiu resolver `github.com`, impedindo checkout canônico e execução válida de `python tools/verify.py`. A impossibilidade está registrada, sem ser tratada como `pass`.

---

## 1.0.3 — 2026-09-11

Patch de instalação após observar a configuração nativa de conversas do NotebookLM.

### Observado

- o NotebookLM oferece uma configuração própria de conversa em `Configurar as conversas → Personalizado`, destinada a definir meta, estilo ou papel do chat;
- essa camada é mais apropriada para instruções do tutor do que carregar `METODOLOGIA_NOTEBOOKLM.md` como fonte;
- a interface observada também oferece controle de tamanho de resposta, mantido em `Padrão` por default do projeto.

### Decisão

- `APOSTILA.pdf` permanece como fonte principal do notebook;
- `METODOLOGIA_NOTEBOOKLM.md` permanece versionada no GitHub, mas passa a ser **texto de configuração da conversa**, não fonte do NotebookLM;
- o usuário copia o bloco operacional da metodologia para a configuração `Personalizado` (ou equivalente);
- Estúdio e chat passam a usar o mesmo corpus didático limpo;
- deixa de existir a necessidade cotidiana de marcar/desmarcar a metodologia;
- `DEC-0017` refina `DEC-0016` nesse mecanismo de entrega das instruções.

### Conteúdo não alterado

- `APOSTILA.md` permanece igual ao release 1.0.0;
- `APOSTILA.pdf` permanece igual ao release 1.0.0;
- `ANALISE_BANCA.md` permanece igual ao release 1.0.0;
- `SOURCES.md` permanece igual ao release 1.0.0.

A próxima ação continua sendo reconstruir a apostila, com target recomendado `2.0.0`.

---

## 1.0.2 — 2026-09-11

Patch arquitetural após smoke tests reais do NotebookLM.

### Observado

- com `METODOLOGIA_NOTEBOOKLM.md` selecionada no `Teste`, o NotebookLM gerou pergunta sobre a própria metodologia;
- ao retirar a metodologia e manter a apostila, o `Teste` continuou funcionando como quiz sobre o conteúdo da fonte, inclusive com formulações do tipo “de acordo com a apostila”;
- no chat, a metodologia funcionou melhor como instrução operacional: uma questão por vez, alternativas A–E, espera da resposta, confiança e possibilidade de relatório de acertos/erros/dúvidas.

### Decisão

- `APOSTILA.pdf` passa a ser o principal conteúdo do estudante;
- `METODOLOGIA_NOTEBOOKLM.md` passa a ser instrução **exclusiva do chat**;
- para artefatos do Estúdio, usar a apostila e desmarcar a metodologia;
- para o chat, usar apostila + metodologia;
- `ANALISE_BANCA.md`, `SOURCES.md`, `MANIFEST.md`, `CHANGELOG.md`, edital e provas históricas deixam de ser fontes padrão do NotebookLM e permanecem no backoffice do GitHub/ChatGPT;
- `DEC-0015` é substituída por `DEC-0016`.

### Consequência editorial

A qualidade da apostila passa a ser o principal gargalo do sistema. O próximo trabalho é reconstruir `APOSTILA.md`/`APOSTILA.pdf` para que o material sustente sozinho Testes, Cartões, Mapas mentais, Relatórios e consulta no NotebookLM sem depender de documentação interna do projeto.

Target recomendado após a reconstrução: `2.0.0`.

### Artefatos de conteúdo não alterados neste patch

- `APOSTILA.md` permanece igual ao release 1.0.0;
- `APOSTILA.pdf` permanece igual ao release 1.0.0;
- `ANALISE_BANCA.md` permanece igual ao release 1.0.0;
- `SOURCES.md` permanece igual ao release 1.0.0.

---

## 1.0.1 — 2026-09-11

Patch de usabilidade para tornar o NotebookLM **Studio-first** e reduzir burocracia operacional.

### Alterado

- o Estúdio do NotebookLM passa a ser interface principal de estudo, não apenas o chat;
- `Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, resumos e outros artefatos podem ser usados naturalmente conforme a necessidade;
- removida a expectativa de selecionar subconjuntos de fontes para cada recurso por padrão;
- prompts longos deixaram de ser requisito operacional;
- `Teste` passa a usar inicialmente `Médio (padrão)` como posição neutra, com calibração de banca feita pelo corpus e por instrução curta;
- explicitado que `Fácil / Médio / Difícil` não equivalem automaticamente ao nível VUNESP;
- chat passa a ser camada de aprofundamento/correção, e não porta de entrada obrigatória de toda sessão;
- smoke test simplificado para poucos cliques e observação do resultado real antes de qualquer otimização.

### Smoke test recomendado

```text
Teste
→ Padrão
→ Médio (padrão)
→ "Teste de Português no padrão TJSP/VUNESP das provas carregadas."
→ responder algumas questões
→ trazer ao ChatGPT apenas desvios relevantes
```

### Artefatos não alterados

- `APOSTILA.md` permanece igual ao release 1.0.0;
- `APOSTILA.pdf` permanece igual ao release 1.0.0;
- `ANALISE_BANCA.md` permanece igual ao release 1.0.0;
- `SOURCES.md` permanece igual ao release 1.0.0.

---

## 1.0.0 — 2026-09-11

Primeira versão operacional do SubjectPack.

### Adicionado

- cobertura dos 13 itens de Língua Portuguesa do edital 2025;
- apostila autoral focada em interpretação, coesão, semântica e norma-padrão;
- `APOSTILA.pdf` pesquisável para distribuição no NotebookLM;
- análise de 88 questões de Português das provas 2021, 2023, 2024 e 2025;
- classificação reproduzível por categoria primária;
- metodologia específica para NotebookLM, derivada dos elementos úteis do protocolo legado;
- protocolo de confiança, correção rápida/profunda, diagnóstico de erro, reteste e relatório de sessão;
- manifesto de instalação e sincronização manual;
- registro de fontes e limites epistemológicos.

### QA do release

- `APOSTILA.md` revisada em UTF-8 e sem a corrupção de caracteres observada em uma tentativa intermediária de exportação;
- PDF final: 8 páginas, formato Letter, texto pesquisável;
- renderização das 8 páginas verificada sem clipping/overlap evidente;
- extração textual verificada para acentos e termos-chave de Português;
- corpus quantitativo conferido em 88 questões: 24 (2021) + 24 (2023) + 24 (2024) + 16 (2025);
- artefatos auxiliares usados durante a tentativa de upload binário foram removidos do pack final.

### Decisões de versão

- Provas históricas informam formato, não sobrescrevem o edital 2025.
- A classificação de questões é analítica do projeto, não oficial da VUNESP.
- Questões reais não são republicadas no pack; são referenciadas por ano/número e podem ser carregadas diretamente no NotebookLM pelos PDFs originais.
- A apostila evita ser enciclopédica e prioriza as operações exigidas no edital e observadas no corpus.
