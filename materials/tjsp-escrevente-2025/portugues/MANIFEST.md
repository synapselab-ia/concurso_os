# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `1.0.0`  
**Status:** ready-for-notebook  
**Release date:** `2026-09-11`

## Objetivo

Este pacote é a distribuição canônica de Língua Portuguesa para criação de um NotebookLM focado no TJSP/VUNESP. O GitHub mantém os arquivos autorais e o histórico de versão; os PDFs oficiais e históricos são adicionados manualmente pelo usuário no NotebookLM.

## Arquivos canônicos do pack

- `APOSTILA.md` — fonte autoral editável.
- `APOSTILA.pdf` — distribuição recomendada para o NotebookLM.
- `ANALISE_BANCA.md` — análise reproduzível das provas 2021/2023/2024/2025.
- `METODOLOGIA_NOTEBOOKLM.md` — comportamento pedagógico do notebook.
- `SOURCES.md` — registro e função das fontes.
- `CHANGELOG.md` — histórico de versões.

### Identidade da distribuição PDF 1.0.0

- páginas: `8`;
- tamanho: `13950 bytes`;
- SHA-256: `e203e62c6be1207dc5ca475e61460d9619be4bfeeeeb32bcf90990b485e8cc23`;
- Git blob: `2287be2ba025228cc311722effc794fc9edf476f`.

O hash permite conferir se o arquivo carregado no NotebookLM corresponde exatamente ao release canônico.

## Fontes que devem ser carregadas no NotebookLM

### Obrigatórias

1. `METODOLOGIA_NOTEBOOKLM.md`
2. `APOSTILA.pdf`
3. `ANALISE_BANCA.md`
4. Edital 2025 — arquivo original `TJSP2503_224_20250801114000.pdf.pdf`
5. Prova TJSP/VUNESP 2025 — `tjsp 2025.pdf`

### Recomendadas para análise histórica mais rica

6. `tjsp 2024.pdf`
7. `tjsp 2023.pdf`
8. `tjsp 2021.pdf`

Não é necessário carregar `APOSTILA.md` se `APOSTILA.pdf` já estiver no notebook; isso evita duplicação semântica.

## Configuração recomendada

Use **um notebook de Português por participante** quando houver interesse em preservar histórico individual de conversas, notas e artefatos. O mesmo SubjectPack pode alimentar notebooks diferentes.

Exemplo:

```text
SubjectPack Português 1.0.0
├── Notebook Português — p001
├── Notebook Português — p002
└── Notebook Português — p003
```

## Teste de instalação

Após carregar as fontes, faça estas perguntas ao NotebookLM:

1. `Qual é a versão do SubjectPack de Português?`
   - resposta esperada: `1.0.0`.
2. `Quantas questões de Língua Portuguesa o edital 2025 prevê?`
   - resposta esperada: `16`, com apoio do edital.
3. `Qual deve ser a diferença entre inferência válida e extrapolação no treino?`
   - deve responder a partir da apostila/metodologia.
4. `Comece uma sessão diagnóstica de Português no padrão deste pack.`
   - deve apresentar uma questão por vez e aguardar a tentativa antes de corrigir.

Se o notebook não reconhecer a versão ou ignorar a dinâmica de uma questão por vez, confirme se `METODOLOGIA_NOTEBOOKLM.md` e `APOSTILA.pdf` foram realmente carregados.

## Comando inicial recomendado

> Siga a `METODOLOGIA_NOTEBOOKLM` deste notebook. Comece uma sessão de Português para TJSP/VUNESP com questões inéditas, uma por vez. Exija resposta e confiança antes da correção. Use o edital para escopo, a apostila para teoria e a análise de banca para forma de cobrança.

## Regra de atualização

Quando este pack mudar:

1. incrementar a versão;
2. atualizar `CHANGELOG.md`;
3. regenerar `APOSTILA.pdf` se a apostila mudar;
4. substituir no NotebookLM somente os arquivos alterados;
5. repetir o teste de instalação.

## Limites

- Este pack não registra mastery questão a questão.
- Não mistura histórico de participantes.
- Não trata frequências históricas como garantia de cobrança futura.
- O edital prevalece sobre provas antigas quanto ao escopo vigente.
