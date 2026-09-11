# QA EDITORIAL — Apostila de Português 2.0.0

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Branch:** `content/apostila-portugues-2.0.0`  
**Protocolo:** `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`  
**Data:** 2026-09-11

## Resultado executivo

A reconstrução 2.0.0 passou pelos gates editoriais internos de cobertura, exatidão editorial, didática, distinções, prática, coerência com a análise empírica, organização para recuperação semântica e coerência interna.

O QA local do PDF 2.0.0 também passou em um artefato íntegro de **29 páginas A4**. Porém, o readback do GitHub revelou que a tentativa anterior de publicar o PDF pela API de blobs foi truncada. O blob que estava na branch (`5bea23e3bd98b307496a086e98effc51853a0cd7`) tinha apenas **7500 bytes**, embora a documentação anterior registrasse 140496 bytes. Esse binário não é um PDF 2.0.0 válido para release.

Para impedir que um arquivo corrompido permanecesse como distribuição canônica, `APOSTILA.pdf` foi restaurado temporariamente ao último binário íntegro conhecido, o PDF 1.0.0 (`2287be2ba025228cc311722effc794fc9edf476f`, 13950 bytes). Portanto, a branch contém **APOSTILA.md 2.0.0 + PDF fallback 1.0.0** até que o PDF 2.0.0 seja publicado por um caminho binário íntegro.

Além disso, o smoke test real no NotebookLM continua pendente e `python tools/verify.py` não pôde ser executado contra um checkout canônico porque o runtime local não resolve `github.com`.

---

## QA-1 — Cobertura

**Resultado: PASS.**

- O syllabus vigente contém 13 frentes de Língua Portuguesa em `competitions/tjsp-escrevente-2025/SYLLABUS.md`.
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` mapeia B1.1 a B1.13 e localiza a cobertura principal em `APOSTILA.md`.
- Todos os 13 itens estão `covered`; nenhum foi omitido, remetido silenciosamente ao backoffice ou declarado fora de escopo.
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

Foram verificados:

- definição antes de aplicação;
- ponte entre regra e exemplo;
- exemplos próximos ao conceito;
- procedimentos de reconhecimento em contexto;
- reescritas que testam forma e sentido;
- sínteses de recuperação após blocos densos.

A sequência parte de leitura/sentido, passa por coesão e semântica e depois avança para morfologia, concordância, regência, pronomes, crase, pontuação e integração.

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

A análise das 88 questões históricas orienta profundidade e integração, mas o produto:

- não transforma ocorrência passada em previsão;
- não declara assunto “garantido”;
- não reproduz questões reais;
- evita metadiscurso recorrente sobre VUNESP/TJSP.

## QA-7 — Utilidade para NotebookLM

**Resultado: STATIC PASS; LIVE SMOKE PENDING.**

A revisão estática confirma que `APOSTILA.md` 2.0.0:

- é autocontida e não depende de backoffice;
- usa títulos semanticamente informativos;
- mantém contrastes próximos;
- contém definições, regras, exemplos, exceções e prática suficientes para Teste, Cartões e Mapa mental;
- separa conteúdo estudável de instrução operacional do tutor.

**Não executado:** Teste/Cartões/Mapa mental e conversa configurada no NotebookLM usando exclusivamente o PDF 2.0.0. O smoke só deve ser feito depois que o binário 2.0.0 íntegro estiver publicado.

## QA-8 — Redundância e coerência interna

**Resultado: PASS.**

- Não foi encontrada formulação conflitante da mesma regra em seções diferentes.
- A terminologia central é consistente.
- Estratégias de prova aparecem apenas quando ajudam a recuperar o critério linguístico.
- O metadiscurso de engenharia da 1.0.0 foi removido do corpus do estudante.

## QA-9 — PDF

**Resultado: LOCAL PASS; PUBLICAÇÃO NO REPOSITÓRIO BLOQUEADA.**

### Artefato 2.0.0 validado localmente

- páginas: **29**;
- formato: A4 (595.276 x 841.89 pt);
- tamanho: **40928 bytes**;
- SHA-256: `1a7a1cbe8a0597f94ea490da7eec8ff874f2430ef596ec5bb9c3a14ecb2f1d62`;
- Git blob esperado para esses bytes: `b06f1150ac71cd9b87a3f8341be70a1c87355ccc`;
- PDF 1.4, não criptografado;
- texto pesquisável;
- extração textual: aproximadamente 56,4 mil caracteres;
- conferência positiva de `Questão 30`, `Gabarito comentado`, `próclise`, `à qual` e síntese final;
- as 29 páginas foram renderizadas e inspecionadas em contact sheet, sem clipping/overlap evidente.

Também foi produzida uma variante ASCII-safe de 29 páginas para investigação do problema de transporte; ela passou em `pdfinfo`, `pdftotext` e renderização das 29 páginas, mas não foi promovida a distribuição canônica.

### Falha detectada na publicação anterior

O readback do GitHub mostrou:

- documentação anterior: 34 páginas / 140496 bytes / SHA-256 `900528...`;
- blob efetivamente publicado: `5bea23e3bd98b307496a086e98effc51853a0cd7`;
- tamanho efetivo no GitHub: **7500 bytes**;
- conteúdo base64 termina durante stream compactado, sem fechamento estrutural confiável.

Logo, o gate de publicação do PDF não passou. A afirmação anterior de que o “PDF 34 páginas foi publicado” foi revogada por evidência de readback.

Um segundo blob órfão, `82046b5da25a7565fd84763763be33ebac2556fc`, também não é tratado como distribuição válida: o tamanho exposto pelo GitHub não corresponde ao artefato local pretendido. Ele não foi ligado à branch.

### Estado seguro atual da branch

`materials/tjsp-escrevente-2025/portugues/APOSTILA.pdf` foi restaurado ao último PDF íntegro conhecido:

- versão material: 1.0.0 fallback;
- páginas: 8;
- tamanho: 13950 bytes;
- Git blob: `2287be2ba025228cc311722effc794fc9edf476f`.

Esse fallback evita distribuir um PDF corrompido, mas **não satisfaz o release 2.0.0** e não deve ser usado no smoke do NotebookLM.

## QA-10 — Repositório e gate determinístico

**Resultado: PARTIAL.**

Estado:

- base `main`: `29f92f11d822b426d6af239afa31a09829881844`;
- branch: `content/apostila-portugues-2.0.0`;
- PR: #12, aberto;
- binário corrompido removido da branch por restauração do fallback íntegro;
- diff/readback realizado pelo conector GitHub.

Gate canônico tentado:

```text
git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Sem checkout canônico, executar `python tools/verify.py` sobre diretório parcial seria uma falsa validação. A não execução permanece registrada conforme `AGENTS.md`, `QA_PROTOCOL.md` e DEC-0009.

---

## Parecer de release

**Português 2.0.0 está editorialmente apto, mas não está liberado para merge.**

Restam dois gates materiais, nesta ordem:

1. publicar no GitHub o PDF 2.0.0 íntegro e confirmar por readback que os bytes/tamanho correspondem ao artefato validado;
2. executar o smoke real no NotebookLM com esse PDF 2.0.0 como única fonte de conteúdo e registrar QA-7 live como `PASS` somente se o comportamento for aprovado.

Depois disso, atualizar release/continuidade, executar `python tools/verify.py` se o ambiente permitir (ou manter a justificativa explícita), revisar o PR #12 e fazer merge sob DEC-0009.