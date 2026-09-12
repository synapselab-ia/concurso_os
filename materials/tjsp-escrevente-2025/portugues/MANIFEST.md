# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `2.0.0`  
**Status:** `release`  
**Release date:** `2026-09-11`

## Objetivo

Este pack entrega uma apostila autocontida de Língua Portuguesa para aprendizado, revisão e uso como corpus limpo no NotebookLM. A reconstrução 2.0.0 aplica `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` e mantém a separação entre conteúdo do estudante, configuração do tutor e backoffice.

## Arquivos canônicos do pack

### StudentContent

- `APOSTILA.md` — fonte autoral editável 2.0.0.
- `APOSTILA.pdf` — distribuição 2.0.0 pesquisável destinada ao estudante e ao NotebookLM.

### ConversationInstruction

- `METODOLOGIA_NOTEBOOKLM.md` — configuração versionada do tutor; não é fonte de conteúdo.

### BackofficeArtifact

- `ANALISE_BANCA.md` — análise empírica do corpus histórico.
- `SOURCES.md` — proveniência e política de fontes.
- `APOSTILA_AUDIT_1.0.0.md` — auditoria da versão anterior.
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` — matriz de cobertura/autoria.
- `APOSTILA_QA_2.0.0.md` — registro dos gates editoriais e técnicos.
- `CHANGELOG.md` — histórico de versões.

## Escopo entregue

A versão 2.0.0 cobre os 13 itens de Português do syllabus, organiza o conteúdo por dependências pedagógicas, aprofunda leitura, interpretação, coesão, relações lógico-semânticas, semântica, classes de palavras, concordância, regência, pronomes, colocação, crase, pontuação e reescrita, e inclui 30 questões autorais A–E com gabarito comentado separado.

## APOSTILA.pdf — distribuição final

- páginas: `16`;
- formato: A4 (`595 x 842 pt`);
- tamanho: `20824 bytes`;
- SHA-256: `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`;
- Git blob: `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- PDF 1.4, não criptografado, texto pesquisável;
- aproximadamente `54,5 mil` caracteres extraídos;
- 16 páginas renderizadas e inspecionadas sem clipping/overlap observado;
- readback GitHub confirmou `size=20824` e o blob esperado.

## Instalação no NotebookLM

### Fontes

Carregar por padrão somente:

1. `APOSTILA.pdf` 2.0.0.

Não carregar como fonte `METODOLOGIA_NOTEBOOKLM.md`, análise de banca, manifest, sources, changelog, QA, edital ou provas históricas.

### Configuração da conversa

1. abrir `Configurar as conversas → Personalizado` ou equivalente;
2. copiar o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md`;
3. manter tamanho de resposta em `Padrão` inicialmente;
4. salvar.

Princípio arquitetural:

```text
conteúdo estudável → APOSTILA.pdf
comportamento do tutor → configuração nativa da conversa
backoffice → GitHub/ChatGPT
```

## QA de release

**PASS:** QA-1 cobertura; QA-2 exatidão/fonte; QA-3 didática; QA-4 distinções; QA-5 prática; QA-6 coerência com banca sem overfitting; QA-7 estático e live no NotebookLM; QA-8 redundância/coerência; QA-9 PDF textual/visual/publicação.

O smoke real do NotebookLM passou após ajuste da configuração do tutor: chat configurado, Teste nativo, Cartões e Mapa mental foram inspecionados e aprovados. O mapa recuperou a hierarquia principal da apostila sem ser dominado por questões/gabaritos.

`python tools/verify.py` não foi executado neste runtime porque o ambiente local não resolve `github.com`; a impossibilidade está registrada em `APOSTILA_QA_2.0.0.md` conforme DEC-0009 e não é tratada como `PASS`.

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
- não transforma backoffice ou instruções operacionais em conteúdo estudável.