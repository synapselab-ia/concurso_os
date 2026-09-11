# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `2.0.0`  
**Status:** `release-candidate-blocked`  
**Candidate date:** `2026-09-11`

## Objetivo

Este pack entrega uma apostila autocontida de Língua Portuguesa para aprendizado, revisão e uso como corpus limpo no NotebookLM. A reconstrução 2.0.0 aplica `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e mantém a separação entre conteúdo do estudante, configuração do tutor e backoffice.

## Arquivos canônicos do pack

### StudentContent

- `APOSTILA.md` — fonte autoral editável **2.0.0**, reconstruída e editorialmente validada.
- `APOSTILA.pdf` — distribuição para NotebookLM. **No estado atual da branch, este arquivo é temporariamente o fallback íntegro 1.0.0, não o PDF 2.0.0.**

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

A apostila foi reconstruída, não apenas ampliada. A nova fonte autoral:

- cobre os 13 itens de Português do syllabus com localização explícita na matriz;
- organiza o conteúdo por dependências pedagógicas;
- amplia leitura verbal, não verbal, multissemiótica, literária e não literária;
- separa literalidade, pressuposição, inferência e extrapolação;
- aprofunda coesão, relações lógico-semânticas e semântica contextual;
- ensina classes de palavras em funcionamento;
- aprofunda concordância, regência, pronomes, colocação, crase e pontuação;
- inclui reescrita integrada e fronteiras conceituais;
- contém 30 questões autorais A–E com gabarito comentado separado.

## Estado do PDF 2.0.0

### Artefato validado localmente

O candidato de distribuição 2.0.0 que passou no QA local possui:

- páginas: `29`;
- formato: A4;
- tamanho: `40928 bytes`;
- SHA-256: `1a7a1cbe8a0597f94ea490da7eec8ff874f2430ef596ec5bb9c3a14ecb2f1d62`;
- Git blob esperado: `b06f1150ac71cd9b87a3f8341be70a1c87355ccc`;
- texto pesquisável: sim;
- QA textual e visual: pass local.

Esse artefato **ainda não está publicado de forma íntegra no GitHub**.

### Fallback presente na branch

Após detectar que uma tentativa de upload binário foi truncada, a branch foi restaurada ao último `APOSTILA.pdf` íntegro conhecido para não deixar um arquivo corrompido como distribuição:

- versão material: `1.0.0` fallback;
- páginas: `8`;
- tamanho: `13950 bytes`;
- SHA-256: `e203e62c6be1207dc5ca475e61460d9619be4bfeeeeb32bcf90990b485e8cc23`;
- Git blob: `2287be2ba025228cc311722effc794fc9edf476f`.

**Não usar esse fallback no smoke de aceitação da 2.0.0.** O smoke só começa depois que o PDF 2.0.0 íntegro for publicado e confirmado por readback.

## Instalação no NotebookLM após publicação do PDF 2.0.0

### Fontes

Carregar como fonte por padrão:

1. `APOSTILA.pdf` **2.0.0 íntegro**.

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
- QA-9 textual/visual **do artefato local 2.0.0**.

Pendentes antes de promover para release final:

1. publicação íntegra do `APOSTILA.pdf` 2.0.0 no GitHub, com readback confirmando o artefato;
2. smoke real no NotebookLM com esse PDF como corpus limpo;
3. fechamento do QA/release e merge do PR #12.

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
- a 2.0.0 não pode ser mesclada enquanto o PDF final e o smoke real não estiverem validados.