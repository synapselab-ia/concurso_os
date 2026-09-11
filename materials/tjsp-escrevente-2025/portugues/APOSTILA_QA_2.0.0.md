# QA EDITORIAL — Apostila de Português 2.0.0

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Branch:** `content/apostila-portugues-2.0.0`  
**Protocolo:** `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`  
**Data:** 2026-09-11

## Resultado executivo

A reconstrução 2.0.0 passou pelos gates editoriais internos de cobertura, exatidão editorial, didática, distinções, prática, coerência com a análise empírica, organização para recuperação semântica e coerência interna. O PDF de release candidate foi validado textual e visualmente.

Há uma pendência deliberadamente não marcada como concluída: o **smoke test real no NotebookLM** com o novo `APOSTILA.pdf` como corpus limpo. O ambiente desta execução não dispõe de acesso operacional ao NotebookLM. Portanto, a release permanece `release-candidate` e o merge deve aguardar esse smoke test, conforme a Definition of Done de `APOSTILA-002`.

O gate determinístico `python tools/verify.py` também não pôde ser executado contra um checkout canônico porque o runtime local não resolve `github.com`; a impossibilidade está documentada abaixo, sem converter ausência de execução em `pass`.

---

## QA-1 — Cobertura

**Resultado: PASS.**

- O syllabus vigente contém 13 frentes de Língua Portuguesa em `competitions/tjsp-escrevente-2025/SYLLABUS.md`.
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` mapeia B1.1 a B1.13 e localiza a cobertura principal em `APOSTILA.md`.
- Todos os 13 itens estão marcados `covered`; nenhum foi silenciosamente omitido, remetido a backoffice ou declarado fora de escopo.
- A cobertura deixou de ser apenas nominal: tópicos que a auditoria 1.0.0 apontava como comprimidos foram expandidos em unidades ensináveis.

## QA-2 — Exatidão e fonte

**Resultado: PASS, dentro do escopo editorial desta matéria.**

- O escopo é controlado por `SRC-TJSP-EDITAL-2025-02`; a prova 2025 é a referência empírica mais próxima e as provas 2024/2023/2021 permanecem históricas, em conformidade com DEC-0010.
- A apostila não promove contagens históricas, previsões de incidência ou metadados internos como verdade didática.
- As questões históricas não foram copiadas para o produto; serviram à calibração editorial registrada em `ANALISE_BANCA.md`.
- Foi feito readback semântico integral de `APOSTILA.md`; não foi identificado erro central inequívoco nas regras ensinadas ou nos 30 gabaritos autorais.
- Formulações de norma-padrão foram apresentadas com qualificadores quando há variação relevante, evitando converter preferência escolar/tradicional em regra absoluta sem necessidade.

## QA-3 — Didática

**Resultado: PASS.**

A versão 2.0.0 passou de resumo comprimido para material de aprendizagem e revisão. Foram verificados:

- definição antes de aplicação;
- explicitação da ponte entre regra e exemplo;
- exemplos imediatamente próximos ao conceito;
- procedimentos de reconhecimento em contexto;
- reescritas que testam simultaneamente forma e sentido;
- sínteses de recuperação após blocos densos.

A organização por dependências pedagógicas começa em leitura/sentido, passa por coesão e semântica e só depois entra em morfologia, concordância, regência, pronomes, crase, pontuação e integração.

## QA-4 — Distinções e casos-limite

**Resultado: PASS.**

Foram conferidas fronteiras que a auditoria 1.0.0 identificou como críticas, entre elas:

- literalidade x inferência x extrapolação;
- tema x tese x argumento;
- voz citada x posição do autor;
- causa x explicação;
- consequência x conclusão;
- condição x concessão;
- finalidade x consequência;
- restrição x explicação em oração adjetiva;
- classe morfológica x função/valor contextual;
- oração sem sujeito x sujeito indeterminado;
- `se` apassivador x índice de indeterminação;
- objeto direto x objeto indireto;
- regência x crase;
- preposição `a` x artigo `a` x fusão crásica;
- frase gramatical x reescrita semanticamente equivalente.

## QA-5 — Prática

**Resultado: PASS.**

- Há 30 questões inéditas com cinco alternativas A–E.
- A prática está distribuída em interpretação/coesão/semântica, norma-padrão e integração.
- O gabarito fica estruturalmente separado da bateria.
- Cada resposta comentada aponta o elemento decisivo, em vez de apenas repetir a alternativa correta.
- A revisão confirmou alternativa única e plausibilidade suficiente dos distratores para o objetivo didático do material.

## QA-6 — Coerência com a banca sem overfitting

**Resultado: PASS.**

`ANALISE_BANCA.md` registra 88 questões históricas e mostra predominância de texto, sentido e coesão, seguida de norma-padrão/sintaxe. A 2.0.0 reflete isso na profundidade e na integração das unidades, mas:

- não transforma frequência passada em previsão;
- não informa ao aluno que determinado assunto é “garantido”;
- não reproduz questões reais;
- evita metadiscurso recorrente sobre VUNESP/TJSP dentro do corpus estudável.

## QA-7 — Utilidade para NotebookLM

**Resultado: STATIC PASS; LIVE SMOKE PENDING.**

A revisão estática confirma que o corpus:

- é autocontido e não depende de `ANALISE_BANCA.md`, `SOURCES.md`, manifest ou protocolo para fazer sentido;
- usa títulos semanticamente informativos;
- mantém conceitos próximos e contrastes na mesma região textual;
- contém definições, regras, exemplos, exceções e prática suficientes para Teste, Cartões e Mapa mental;
- separa conteúdo estudável de instrução operacional do tutor.

**Não executado:** geração real de Teste/Cartões/Mapa mental e conversa configurada no NotebookLM usando exclusivamente o novo PDF. Isso exige interação com o produto externo e permanece como último gate semântico de aceitação.

## QA-8 — Redundância e coerência interna

**Resultado: PASS.**

- Não foi encontrada formulação conflitante da mesma regra em seções diferentes.
- A terminologia central é consistente ao longo das unidades.
- Estratégias de prova aparecem apenas quando ajudam a recuperar o critério linguístico, sem substituir conteúdo.
- O metadiscurso de engenharia presente na 1.0.0 foi removido do corpus do estudante.

## QA-9 — PDF

**Resultado: PASS para o release candidate gerado em 2026-09-11.**

Artefato validado:

- formato: PDF pesquisável;
- páginas: **34**;
- tamanho: **140496 bytes**;
- SHA-256: `90052841384431f942f78234ce543fc5dbeb67f44793f40459632c6939dfbbc2`;
- formato de página: A4 (595 x 842 pt);
- fontes: incorporadas e Unicode;
- outline: 87 itens;
- campos de formulário: 0;
- anexos: 0.

QA textual:

- extração por `pdftotext`: aproximadamente 60,7 mil caracteres;
- caracteres de substituição Unicode: 0;
- NUL: 0;
- conferência positiva de termos com acentos e símbolos (`àquele`, `à qual`, `próclise`), títulos, Questão 30, gabarito e síntese final.

QA visual:

- as 34 páginas foram renderizadas a 150 dpi;
- contact sheet das 34 páginas inspecionada;
- páginas com tabelas e a página final verificadas em renderização individual;
- não foram observados clipping, sobreposição, tabelas quebradas ou glyphs corrompidos.

Observação cosmética não bloqueante: o sumário automático do gerador usa o rótulo `Contents`. Tentativas locais de forçar `Sumário` introduziram corrupção no próprio rótulo; preferiu-se preservar o PDF sem glyph quebrado. O conteúdo e os títulos internos permanecem em português.

## QA-10 — Repositório e gate determinístico

**Resultado: PARTIAL — continuidade/release candidate preparados; `verify.py` não executado por limitação do runtime.**

Estado verificado antes do fechamento:

- `main` base: `29f92f11d822b426d6af239afa31a09829881844`;
- branch: `content/apostila-portugues-2.0.0`;
- branch estava 4 commits à frente e 0 atrás antes dos commits de fechamento;
- nenhum PR aberto de Português existia;
- diff/readback feito pelo conector GitHub.

Tentativa do gate canônico no runtime local:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Sem checkout canônico do repositório, executar `python tools/verify.py` localmente produziria uma validação de diretório incompleto e seria epistemicamente inválido. A não execução é, portanto, registrada explicitamente conforme `AGENTS.md`, `QA_PROTOCOL.md` e DEC-0009.

---

## Parecer de release

**Português 2.0.0 está editorialmente apto como release candidate.**

Para concluir `APOSTILA-002` e autorizar merge, falta somente:

1. carregar o novo `APOSTILA.pdf` como fonte única de conteúdo no NotebookLM;
2. manter o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md` na configuração personalizada da conversa;
3. executar smoke test curto de Teste, Cartões, Mapa mental e chat;
4. registrar o resultado no repositório;
5. se o smoke passar, concluir o PR/merge sob DEC-0009.
