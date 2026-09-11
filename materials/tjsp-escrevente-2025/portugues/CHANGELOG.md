# CHANGELOG — Português — TJSP Escrevente 2025

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
