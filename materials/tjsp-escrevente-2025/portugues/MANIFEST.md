# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `1.0.1`  
**Status:** studio-smoke-test  
**Release date:** `2026-09-11`

## Objetivo

Este pacote é a distribuição canônica de Língua Portuguesa para criação de um NotebookLM focado no TJSP/VUNESP.

A versão `1.0.1` simplifica a usabilidade: o notebook deve ser montado uma vez e usado naturalmente pelo **Estúdio + chat**, sem exigir que o estudante escolha manualmente um conjunto diferente de fontes ou cole prompts longos para cada ferramenta.

## Arquivos canônicos do pack

- `APOSTILA.md` — fonte autoral editável.
- `APOSTILA.pdf` — distribuição recomendada para o NotebookLM.
- `ANALISE_BANCA.md` — análise reproduzível das provas 2021/2023/2024/2025.
- `METODOLOGIA_NOTEBOOKLM.md` — regras de uso simples do Estúdio e do chat.
- `SOURCES.md` — registro e função das fontes.
- `CHANGELOG.md` — histórico de versões.

## Apostila PDF

A apostila não mudou na versão `1.0.1`; portanto o mesmo PDF validado do release `1.0.0` é reutilizado.

- páginas: `8`;
- tamanho: `13950 bytes`;
- SHA-256: `e203e62c6be1207dc5ca475e61460d9619be4bfeeeeb32bcf90990b485e8cc23`;
- Git blob: `2287be2ba025228cc311722effc794fc9edf476f`.

## O que carregar no NotebookLM

### Núcleo recomendado

1. `METODOLOGIA_NOTEBOOKLM.md`
2. `APOSTILA.pdf`
3. `ANALISE_BANCA.md`
4. Edital 2025 — `TJSP2503_224_20250801114000.pdf.pdf`
5. Prova TJSP/VUNESP 2025 — `tjsp 2025.pdf`

### Histórico recomendado

6. `tjsp 2024.pdf`
7. `tjsp 2023.pdf`
8. `tjsp 2021.pdf`

Não é necessário carregar `APOSTILA.md` junto com `APOSTILA.pdf`.

## Regra de uso sem burocracia

Depois de carregar as fontes:

- **não** fique trocando fontes a cada botão do Estúdio por padrão;
- use `Teste`, `Cartões`, `Mapa mental`, `Relatórios`, `Tabela de dados`, resumos e outros recursos conforme forem úteis;
- use comandos curtos;
- só ajuste fontes/configurações de forma mais detalhada se um resultado real mostrar problema;
- use o chat para dúvida, correção profunda ou análise de uma questão específica.

A metodologia completa está em `METODOLOGIA_NOTEBOOKLM.md`.

## Primeiro smoke test — Teste do Estúdio

Este é o teste que deve ser feito agora.

1. abrir **Teste**;
2. deixar **Número de questões = Padrão**;
3. deixar **Nível de dificuldade = Médio (padrão)**;
4. manter as fontes carregadas sem microgerenciamento;
5. no campo de tema, escrever somente:

> `Teste de Português no padrão TJSP/VUNESP das provas carregadas.`

6. gerar o teste;
7. responder algumas questões normalmente;
8. observar:
   - se o conteúdo está dentro do edital;
   - se as alternativas são plausíveis;
   - se a linguagem lembra a forma de cobrança das provas carregadas;
   - se a dificuldade parece compatível, sem obscuridade artificial;
   - se as explicações são úteis.

**Não usar `Difícil` como sinônimo de nível VUNESP.** O seletor é genérico; o padrão da banca deve vir do corpus carregado.

## O que trazer de volta ao ChatGPT

Não precisa produzir relatório formal agora.

Se algo der errado, basta trazer:

- print da questão;
- enunciado/alternativas;
- explicação estranha;
- ou uma frase dizendo o que pareceu inadequado.

Se tudo parecer bom após algumas questões, informar apenas que o smoke test passou.

## Critério de aprovação do pack

O SubjectPack está aprovado para replicação quando o usuário consegue estudar no Estúdio em poucos cliques, sem receita complexa, e os artefatos gerados permanecem coerentes com edital + corpus TJSP/VUNESP.

## Múltiplos participantes

O mesmo SubjectPack pode alimentar notebooks separados de `p001`, `p002`, `p003` etc. O material é compartilhado; histórico e artefatos pessoais podem permanecer separados em cada notebook.

## Atualização

Quando o pack mudar:

1. incrementar a versão;
2. atualizar `CHANGELOG.md`;
3. regenerar `APOSTILA.pdf` apenas se a apostila mudar;
4. substituir no NotebookLM somente os arquivos alterados;
5. repetir apenas o smoke test necessário à mudança.

## Limites

- não implementa mastery questão a questão;
- não mistura participantes;
- não trata frequência histórica como garantia futura;
- o edital prevalece sobre provas antigas quanto ao escopo;
- detalhes da interface do NotebookLM podem mudar e não são invariantes do projeto.
