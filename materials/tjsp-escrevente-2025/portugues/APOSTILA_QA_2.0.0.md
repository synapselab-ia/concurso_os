# QA EDITORIAL — Apostila de Português 2.0.0

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Branch:** `content/apostila-portugues-2.0.0`  
**Protocolo:** `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`  
**Data:** 2026-09-11

## Resultado executivo

**Português 2.0.0 está aprovado para release.** A reconstrução passou nos gates editoriais, no QA textual/visual e de publicação do PDF e no smoke real do NotebookLM. O primeiro smoke do chat encontrou problemas de formulação e correção; eles foram tratados na configuração `METODOLOGIA_NOTEBOOKLM.md` `2.0.0-rc2`, e o reteste subsequente passou.

O único gate não executado é `python tools/verify.py`: o runtime local não resolve `github.com`, impedindo checkout canônico. A impossibilidade permanece explícita e não é tratada como `PASS`, conforme DEC-0009.

## QA-1 — Cobertura

**PASS.** Os 13 itens B1.1–B1.13 de Língua Portuguesa estão mapeados em `APOSTILA_AUTHORING_MATRIX_2.0.0.md` e cobertos de forma ensinável em `APOSTILA.md`.

## QA-2 — Exatidão e fonte

**PASS.** O edital vigente controla o escopo; provas 2021/2023/2024/2025 servem à calibração histórica sem sobrescrever o edital. Não há reprodução de questões reais nem transformação de frequência histórica em previsão.

## QA-3 — Didática

**PASS.** A sequência apresenta definição, regra, aplicação, exemplos, contrastes, casos-limite, prática e sínteses de recuperação.

## QA-4 — Distinções e casos-limite

**PASS.** Foram verificadas, entre outras, literalidade/inferência/extrapolação, causa/explicação, consequência/conclusão, condição/concessão, restritiva/explicativa, oração sem sujeito/sujeito indeterminado, `se` apassivador/índice de indeterminação, regência/crase e preposição `a`/artigo `a`/fusão crásica.

## QA-5 — Prática

**PASS.** Há 30 questões autorais A–E com gabarito comentado separado e alternativa única para o objetivo didático de cada item.

## QA-6 — Coerência com a banca sem overfitting

**PASS.** A análise de 88 questões históricas orienta profundidade e integração sem produzir previsão, garantia de incidência ou metadiscurso excessivo de banca.

## QA-7 — Utilidade para NotebookLM

**STATIC PASS; LIVE PASS.**

Arquitetura testada:

```text
FONTES
→ APOSTILA.pdf 2.0.0

CONFIGURAÇÃO DA CONVERSA
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

### Primeira tentativa do chat

Foram observados quatro pontos: formulação de inferência mais absoluta que a fonte; rótulo incorreto em um exemplo válido sem crase; correção pouco específica de `Devem haver` → `Deve haver`; e sugestão automática da interface exibindo gabarito antes da tentativa. A configuração foi endurecida para `2.0.0-rc2`, tratando os comportamentos controláveis. Sugestões automáticas da interface são registradas como risco da camada do produto, não como comportamento garantidamente controlável pelo tutor.

### Reteste do chat configurado — PASS

O reteste com rc2 apresentou questão válida de concordância e correção específica por construção, explicitando corretamente `fazer` temporal impessoal, `menos` invariável, concordância de `anexo` e `dever + existir`. Não houve vazamento de gabarito produzido pela resposta controlada do tutor.

### Teste nativo — PASS

Amostras reais inspecionadas cobriram:

- concordância com expressão partitiva (`a maioria dos processos`);
- sentido figurado de `chave`;
- equivalência adversativa entre `entretanto` e `contudo`.

As questões exigiram aplicação do conteúdo e não desviaram para metodologia/backoffice. A dica observada era opcional e foi aberta deliberadamente pelo usuário.

### Cartões — PASS

Amostras reais cobriram:

- identificação de quem enuncia;
- inferência legítima;
- extrapolação;
- concordância do relativo `cujo` com o termo possuído.

As perguntas e respostas foram curtas, recuperáveis e fiéis ao corpus.

### Mapa mental — PASS

O mapa real recuperou uma hierarquia ampla e inteligível da apostila, com ramos principais para:

- sentido em textos;
- arquitetura textual e coesão;
- semântica e léxico;
- classes de palavras;
- concordância;
- regência e crase;
- pontuação e reescrita.

Os subramos recuperaram tópicos como situação comunicativa, tipos de texto, inferência/extrapolação, progressão, coesão referencial, pronomes relativos, relações lógico-semânticas, sentido figurado, modos/tempos verbais, `haver`/`fazer` impessoais, partícula `se`, regência verbal, colocação pronominal, casos de crase e filtros de reescrita. Questões e gabaritos não dominaram a estrutura. **Mapa mental aprovado.**

## QA-8 — Redundância e coerência interna

**PASS.** Terminologia central consistente, sem conflito material identificado entre regras em seções diferentes.

## QA-9 — PDF

**PASS — publicado e confirmado por readback.**

Distribuição canônica 2.0.0:

- páginas: `16`;
- formato: A4 (`595 x 842 pt`);
- tamanho: `20824 bytes`;
- SHA-256: `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`;
- Git blob: `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- PDF 1.4, não criptografado e pesquisável;
- aproximadamente 54,5 mil caracteres extraídos;
- `Questão 30`, `Gabarito comentado`, `próclise`, `à qual` e síntese final recuperados;
- 16 páginas renderizadas e inspecionadas sem clipping/overlap observado.

Incidentes anteriores `5bea23e3...` e `82046b5d...` permanecem rejeitados; o fallback 1.0.0 `2287be2b...` foi apenas temporário e não é a distribuição atual.

## QA-10 — Repositório e gate determinístico

**PARTIAL por limitação de ambiente; suficiente para merge sob DEC-0009.**

Estado antes do merge:

- base: `main`;
- branch: `content/apostila-portugues-2.0.0`;
- PR: #12;
- PDF publicado e confirmado por readback;
- diff GitHub revisado sem mudança destrutiva não prevista.

Gate canônico não executado:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Sem checkout canônico, executar `python tools/verify.py` sobre diretório parcial seria falsa validação. A impossibilidade está documentada conforme DEC-0009.

## Parecer de release

**PASS PARA RELEASE E MERGE.** Todos os gates materiais de conteúdo, PDF e uso real no NotebookLM passaram. O gate determinístico permanece não executado por impossibilidade técnica explicitamente registrada, condição permitida pela política de merge autônomo DEC-0009.