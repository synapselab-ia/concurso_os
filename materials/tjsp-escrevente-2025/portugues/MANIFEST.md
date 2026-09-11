# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `2.0.0`  
**Status:** `release-candidate`  
**Candidate date:** `2026-09-11`

## Objetivo

Este pack entrega uma apostila autocontida de Língua Portuguesa para aprendizado, revisão e uso como corpus limpo no NotebookLM. A reconstrução 2.0.0 aplica `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e substitui a distribuição didática 1.0.0, mantendo a separação arquitetural entre conteúdo do estudante, configuração do tutor e backoffice.

## Arquivos canônicos do pack

### StudentContent

- `APOSTILA.md` — fonte autoral editável.
- `APOSTILA.pdf` — distribuição pesquisável para o estudante e fonte principal do NotebookLM.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` — configuração versionada do tutor; **não é fonte de conteúdo**.

### BackofficeArtifact

- `ANALISE_BANCA.md` — análise empírica do corpus histórico.
- `SOURCES.md` — proveniência e política de fontes.
- `APOSTILA_AUDIT_1.0.0.md` — auditoria da versão anterior.
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` — matriz de cobertura/autoria.
- `APOSTILA_QA_2.0.0.md` — registro dos gates editoriais e técnicos.
- `CHANGELOG.md` — histórico de versões.

## O que mudou em 2.0.0

A apostila foi reconstruída, não apenas ampliada. A versão nova:

- cobre os 13 itens de Português do syllabus com localização explícita na matriz;
- organiza o conteúdo por dependências pedagógicas, e não pela simples ordem do edital;
- amplia leitura de textos verbais, não verbais, multissemióticos, literários e não literários;
- separa literalidade, pressuposição, inferência e extrapolação;
- aprofunda coesão, pronomes relativos e relações lógico-semânticas;
- amplia semântica contextual, polissemia, sinonímia, antonímia e linguagem figurada;
- ensina classes de palavras em funcionamento;
- aprofunda concordância, regência, pronomes, colocação, crase e pontuação;
- inclui fronteiras conceituais e reescrita integrada;
- acrescenta 30 questões autorais A–E e gabarito comentado separado.

## APOSTILA.pdf — release candidate

Artefato produzido e validado em QA-9:

- páginas: `34`;
- formato: A4;
- tamanho: `140496 bytes`;
- SHA-256: `90052841384431f942f78234ce543fc5dbeb67f44793f40459632c6939dfbbc2`;
- Git blob preparado: `5bea23e3bd98b307496a086e98effc51853a0cd7`;
- texto pesquisável: sim;
- fontes incorporadas/Unicode: sim;
- outline: `87` itens;
- QA visual: 34 páginas renderizadas e inspecionadas sem clipping/overlap evidente.

Detalhes e limitações estão em `APOSTILA_QA_2.0.0.md`.

## Instalação no NotebookLM

### Fontes

Carregar como fonte por padrão:

1. `APOSTILA.pdf`

Não carregar como fonte:

- `METODOLOGIA_NOTEBOOKLM.md`;
- `ANALISE_BANCA.md`;
- `MANIFEST.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- auditoria, matriz e QA;
- edital e provas históricas apenas para explicar o projeto.

### Configuração da conversa

1. abrir a configuração persistente da conversa (`Personalizado` ou equivalente);
2. copiar o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md`;
3. manter o tamanho de resposta em `Padrão` inicialmente;
4. salvar.

O princípio arquitetural é estável mesmo que a UI do NotebookLM mude:

```text
conteúdo estudável → APOSTILA.pdf
comportamento do tutor → configuração nativa da conversa
backoffice → GitHub/ChatGPT
```

## QA e status de release

Passaram na revisão interna:

- QA-1 cobertura;
- QA-2 exatidão/fonte no escopo editorial;
- QA-3 didática;
- QA-4 distinções;
- QA-5 prática;
- QA-6 coerência com banca sem overfitting;
- QA-7 revisão estática de utilidade para NotebookLM;
- QA-8 redundância/coerência;
- QA-9 PDF textual/visual.

Pendente antes de promover `release-candidate` a release final:

- smoke test real no NotebookLM usando o novo `APOSTILA.pdf` como corpus limpo e `METODOLOGIA_NOTEBOOKLM.md` na configuração da conversa.

O gate determinístico `python tools/verify.py` não pôde ser executado no runtime desta sessão porque o ambiente local não resolve `github.com`; a impossibilidade está registrada em `APOSTILA_QA_2.0.0.md` e deve permanecer explícita, não ser tratada como `pass`.

## Múltiplos participantes

O mesmo SubjectPack pode alimentar notebooks separados de participantes diferentes. O material é compartilhado; históricos pessoais podem permanecer isolados em cada notebook.

## Atualização

- se `APOSTILA.pdf` mudar, substituir a fonte no NotebookLM;
- se `METODOLOGIA_NOTEBOOKLM.md` mudar, atualizar a configuração personalizada;
- se mudar apenas backoffice, nenhuma sincronização do notebook é necessária.

## Limites

- não implementa mastery questão a questão;
- não mistura participantes;
- não presume que o Teste nativo reproduza automaticamente a banca;
- não transforma backoffice em conteúdo estudável;
- não transforma instruções de chat em fonte estudável;
- o smoke test real do corpus 2.0.0 ainda precisa ser executado antes do merge final.
