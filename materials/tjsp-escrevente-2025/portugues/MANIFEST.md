# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `2.0.0`  
**Status:** `release-candidate`  
**Candidate date:** `2026-09-11`

## Objetivo

Este pack entrega uma apostila autocontida de Língua Portuguesa para aprendizado, revisão e uso como corpus limpo no NotebookLM. A reconstrução 2.0.0 aplica `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e mantém a separação entre conteúdo do estudante, configuração do tutor e backoffice.

## Arquivos canônicos do pack

### StudentContent

- `APOSTILA.md` — fonte autoral editável 2.0.0, reconstruída e editorialmente validada.
- `APOSTILA.pdf` — distribuição 2.0.0 pesquisável, publicada integralmente na branch e destinada ao estudante/NotebookLM.

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

A apostila foi reconstruída, não apenas ampliada. A nova versão:

- cobre os 13 itens de Português do syllabus com localização explícita na matriz;
- organiza o conteúdo por dependências pedagógicas;
- amplia leitura verbal, não verbal, multissemiótica, literária e não literária;
- separa literalidade, pressuposição, inferência e extrapolação;
- aprofunda coesão, relações lógico-semânticas e semântica contextual;
- ensina classes de palavras em funcionamento;
- aprofunda concordância, regência, pronomes, colocação, crase e pontuação;
- inclui reescrita integrada e fronteiras conceituais;
- contém 30 questões autorais A–E com gabarito comentado separado.

## APOSTILA.pdf — release candidate publicado

Artefato canônico da branch:

- páginas: `16`;
- formato: A4 (`595 x 842 pt`);
- tamanho: `20824 bytes`;
- SHA-256: `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`;
- Git blob: `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- texto pesquisável: sim;
- PDF: 1.4, não criptografado;
- extração textual: aproximadamente `54,5 mil` caracteres;
- QA visual: 16 páginas renderizadas e inspecionadas sem clipping/overlap observado;
- readback GitHub: `size=20824`, `sha=640efaed13dd43cc83f6904c62fdb86131b9124a`.

A versão compacta foi produzida especificamente para transporte íntegro pelo conector GitHub e preserva o conteúdo estudável da fonte autoral. Detalhes e incidentes de upload rejeitados estão em `APOSTILA_QA_2.0.0.md`.

## Instalação no NotebookLM

### Fontes

Carregar como fonte por padrão:

1. `APOSTILA.pdf` 2.0.0.

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

Princípio arquitetural:

```text
conteúdo estudável → APOSTILA.pdf
comportamento do tutor → configuração nativa da conversa
backoffice → GitHub/ChatGPT
```

## QA e status de release

Passaram:

- QA-1 cobertura;
- QA-2 exatidão/fonte;
- QA-3 didática;
- QA-4 distinções;
- QA-5 prática;
- QA-6 coerência com banca sem overfitting;
- QA-7 revisão estática de utilidade para NotebookLM;
- QA-8 redundância/coerência;
- QA-9 PDF textual/visual + publicação/readback no GitHub.

Pendente antes de promover para release final:

- QA-7 live: smoke real no NotebookLM usando o `APOSTILA.pdf` 2.0.0 como corpus limpo e `METODOLOGIA_NOTEBOOKLM.md` na configuração da conversa.

`python tools/verify.py` continua não executado neste runtime porque o ambiente local não resolve `github.com`; a impossibilidade está registrada em `APOSTILA_QA_2.0.0.md` e não é tratada como `pass`.

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
- a promoção para release final continua condicionada ao smoke real do NotebookLM.