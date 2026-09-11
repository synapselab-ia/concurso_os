# QA EDITORIAL — Apostila de Português 2.0.0

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Branch:** `content/apostila-portugues-2.0.0`  
**Protocolo:** `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`  
**Data:** 2026-09-11

## Resultado executivo

A reconstrução 2.0.0 passou pelos gates editoriais internos de cobertura, exatidão editorial, didática, distinções, prática, coerência com a análise empírica, organização para recuperação semântica e coerência interna.

O gate de publicação do PDF também está concluído. Após detectar e revogar uma tentativa anterior truncada, foi gerada uma distribuição compacta específica para transporte pelo conector GitHub. O arquivo foi validado localmente, publicado como blob byte-identical e confirmado por readback no repositório.

O smoke real no NotebookLM está em fase final. A primeira tentativa do chat revelou problemas concretos de formulação/rotulagem e correção insuficientemente específica; a configuração foi endurecida em `METODOLOGIA_NOTEBOOKLM.md` versão `2.0.0-rc2`. O reteste do chat com rc2 passou. O Teste nativo também passou em amostras de concordância, semântica figurada e relações lógico-semânticas. Os Cartões passaram em amostras de voz enunciadora, inferência, extrapolação e concordância de `cujo`. Resta somente validar o Mapa mental antes de marcar QA-7 live como `PASS` integral.

O gate determinístico `python tools/verify.py` também não pôde ser executado contra um checkout canônico porque o runtime local não resolve `github.com`; a impossibilidade permanece documentada sem ser convertida em `pass`.

---

## QA-1 — Cobertura

**Resultado: PASS.**

- O syllabus vigente contém 13 frentes de Língua Portuguesa em `competitions/tjsp-escrevente-2025/SYLLABUS.md`.
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` mapeia B1.1 a B1.13 e localiza a cobertura principal em `APOSTILA.md`.
- Todos os 13 itens estão `covered`; nenhum foi omitido ou remetido silenciosamente ao backoffice.
- A cobertura é ensinável, não apenas nominal.

## QA-2 — Exatidão e fonte

**Resultado: PASS, dentro do escopo editorial desta matéria.**

- O escopo é controlado por `SRC-TJSP-EDITAL-2025-02`; a prova 2025 é a referência empírica mais próxima e as provas 2024/2023/2021 permanecem históricas, conforme DEC-0010.
- A apostila não transforma frequência histórica em previsão.
- Questões históricas não foram copiadas para o produto; serviram à calibração editorial registrada em `ANALISE_BANCA.md`.
- O readback semântico de `APOSTILA.md` não identificou erro central inequívoco nas regras ensinadas nem nos 30 gabaritos autorais.
- Formulações de norma-padrão recebem qualificadores quando existe variação relevante.

## QA-3 — Didática

**Resultado: PASS.**

Foram verificados definição antes de aplicação, ponte entre regra e exemplo, procedimentos de reconhecimento em contexto, reescritas que testam forma e sentido e sínteses de recuperação. A sequência parte de leitura/sentido, passa por coesão e semântica e depois avança para morfologia, concordância, regência, pronomes, crase, pontuação e integração.

## QA-4 — Distinções e casos-limite

**Resultado: PASS.**

Foram conferidas, entre outras, as fronteiras:

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

- Há 30 questões inéditas A–E.
- A prática cobre interpretação/coesão/semântica, norma-padrão e integração.
- O gabarito fica separado da bateria.
- Cada comentário aponta o elemento decisivo.
- A revisão confirmou alternativa única para o objetivo didático de cada item.

## QA-6 — Coerência com a banca sem overfitting

**Resultado: PASS.**

A análise das 88 questões históricas orienta profundidade e integração, mas o produto não transforma ocorrência passada em previsão, não declara assunto “garantido”, não reproduz questões reais e evita metadiscurso recorrente sobre VUNESP/TJSP.

## QA-7 — Utilidade para NotebookLM

**Resultado: STATIC PASS; LIVE SMOKE PARTIAL PASS — MAPA MENTAL PENDENTE.**

A revisão estática confirma que o corpus é autocontido, mantém contrastes próximos, contém definições, regras, exemplos, exceções e prática suficientes e separa conteúdo estudável da instrução operacional do tutor.

### Primeira tentativa live — achados e correção

A primeira execução real encontrou:

- formulação de inferência mais absoluta que a fonte;
- um exemplo válido sem crase rotulado como “incorreto”;
- correção de concordância insuficientemente específica para `Devem haver` → `Deve haver`;
- sugestão automática da interface exibindo resposta correta antes da tentativa, aparentemente fora da resposta principal do tutor.

`METODOLOGIA_NOTEBOOKLM.md` foi atualizada para `2.0.0-rc2`, com proibição de absolutismos não sustentados, rotulagem correta de pares mínimos, questão por vez sem gabarito produzido pelo tutor e correção específica por construção/alternativa.

### Reteste do chat configurado — PASS

No reteste com rc2:

- questão de concordância foi válida;
- correção explicou separadamente `fazer` temporal impessoal, `menos` invariável, concordância de `anexo` e `dever + existir`;
- formas corrigidas foram explicitadas;
- reteste curto de consolidação foi pertinente;
- não foi observado vazamento de gabarito produzido pela resposta do tutor.

Sugestões automáticas da interface continuam tratadas como risco de camada externa do produto, não como comportamento garantidamente controlável pela configuração persistente.

### Teste nativo — PASS

Foram inspecionadas amostras reais do quiz nativo sobre:

- concordância com expressão partitiva (`a maioria dos processos`);
- sentido figurado de `chave`;
- equivalência adversativa entre `entretanto` e `contudo`.

As amostras exigiram aplicação do conteúdo, apresentaram distratores semanticamente plausíveis e não desviaram para metodologia/backoffice. A dica observada era opcional e foi aberta deliberadamente pelo usuário; não foi tratada como vazamento obrigatório.

### Cartões — PASS

Foram inspecionadas amostras reais de cartões sobre:

- identificação de quem enuncia;
- definição de inferência legítima;
- definição de extrapolação;
- concordância do pronome relativo `cujo` com o termo possuído.

As perguntas são curtas, as respostas são recuperáveis e fiéis ao corpus, e a amostra cobre conceito, contraste interpretativo e regra gramatical. Não houve metadiscurso nem conteúdo de backoffice nos cartões mostrados.

### Mapa mental — PENDENTE

Falta apenas confirmar que o Mapa mental recupera de forma inteligível a hierarquia principal da apostila e que questões/gabaritos não dominam a estrutura. QA-7 live só deve ser promovido a `PASS` integral após essa verificação visual real.

## QA-8 — Redundância e coerência interna

**Resultado: PASS.**

- Não foi encontrada formulação conflitante da mesma regra em seções diferentes.
- A terminologia central é consistente.
- Estratégias de prova aparecem apenas quando ajudam a recuperar o critério linguístico.
- O metadiscurso de engenharia da 1.0.0 foi removido do corpus do estudante.

## QA-9 — PDF

**Resultado: PASS — arquivo publicado e confirmado por readback.**

### Distribuição canônica 2.0.0 na branch

- páginas: **16**;
- formato: A4 (595 x 842 pt);
- tamanho: **20824 bytes**;
- SHA-256 local: `b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931`;
- Git blob esperado para os bytes locais: `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- Git blob publicado: `640efaed13dd43cc83f6904c62fdb86131b9124a`;
- PDF 1.4, não criptografado;
- texto pesquisável: **PASS**;
- extração textual: aproximadamente 54,5 mil caracteres;
- conferência positiva de `Questão 30`, `Gabarito comentado`, `próclise`, `à qual` e `Síntese final de alta recuperação`;
- 16 páginas renderizadas a 150 dpi e inspecionadas em contact sheet;
- clipping/overlap: nenhum observado;
- preflight: PDF abre em PyMuPDF, sem XFA, não escaneado.

A distribuição usa uma composição tipográfica compacta (Helvetica 9,2 pt) para permanecer abaixo do limite prático de transporte do conector sem sacrificar o conteúdo textual do `APOSTILA.md`. O Markdown continua sendo a fonte autoral editável; o PDF é a distribuição estudável e o corpus do NotebookLM.

### Incidentes revogados

- `5bea23e3bd98b307496a086e98effc51853a0cd7` — upload truncado de 7500 bytes, rejeitado;
- `82046b5da25a7565fd84763763be33ebac2556fc` — tentativa órfã/intermediária, não promovida;
- fallback 1.0.0 `2287be2ba025228cc311722effc794fc9edf476f` — usado temporariamente para remover corrupção e substituído pelo PDF 2.0.0 íntegro.

O readback do diretório da branch confirma `APOSTILA.pdf` com `size: 20824` e `sha: 640efaed13dd43cc83f6904c62fdb86131b9124a`.

## QA-10 — Repositório e gate determinístico

**Resultado: PARTIAL.**

Estado:

- base `main`: `29f92f11d822b426d6af239afa31a09829881844`;
- branch: `content/apostila-portugues-2.0.0`;
- PR: #12, aberto em draft enquanto QA-7 live estiver pendente;
- PDF 2.0.0 íntegro publicado e confirmado por readback;
- diff/readback realizado pelo conector GitHub.

Gate canônico tentado:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Sem checkout canônico, executar `python tools/verify.py` sobre diretório parcial seria uma falsa validação. A não execução permanece registrada conforme `AGENTS.md`, `QA_PROTOCOL.md` e DEC-0009.

---

## Parecer de release

**Português 2.0.0 está editorialmente apto, o PDF canônico está publicado e chat/Teste/Cartões passaram no smoke real.**

Resta apenas o Mapa mental para fechar QA-7 live. Se esse artefato preservar a hierarquia do conteúdo e não for dominado por questões/gabaritos, promover QA-7 live a `PASS`, concluir release e revisar/mesclar o PR #12 sob DEC-0009. Se `python tools/verify.py` continuar impossível no ambiente de execução, manter a justificativa explícita em vez de inventar um resultado.