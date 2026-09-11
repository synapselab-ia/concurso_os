# NEXT_ACTION

## APOSTILA-002-FINAL — Publicar PDF 2.0.0 íntegro, validar no NotebookLM e concluir o release

A reconstrução editorial de Português 2.0.0 está concluída na branch `content/apostila-portugues-2.0.0`, mas o release candidate **não pode ser mesclado ainda**.

O readback do GitHub corrigiu um estado anteriormente registrado de forma incorreta: a tentativa de publicar o PDF 2.0.0 via blob foi truncada. Para não manter um binário corrompido, `APOSTILA.pdf` foi restaurado temporariamente ao fallback íntegro da distribuição 1.0.0.

Portanto, o próximo gate não é reescrever a apostila. É **publicar o PDF 2.0.0 exato e validado**, confirmar o binário no GitHub e somente depois executar o smoke real no NotebookLM.

## Estado editorial já fechado

Existem e foram revisados:

- `APOSTILA_AUDIT_1.0.0.md`;
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` com B1.1–B1.13 `covered`;
- `APOSTILA.md` 2.0.0 reconstruída;
- 30 questões autorais A–E com gabarito comentado separado;
- `APOSTILA_QA_2.0.0.md`;
- QA-1 a QA-6 `PASS`;
- QA-7 estático `PASS`;
- QA-8 `PASS`;
- PDF 2.0.0 validado localmente em QA textual/visual.

Não reabrir a redação integral sem evidência concreta de problema.

## Recuperação obrigatória

Seguir `AGENTS.md` e ler pelo menos:

1. `00_SYSTEM/START_HERE.md`;
2. `PROJECT_CONTROL.md`;
3. `00_SYSTEM/CHECKPOINT.md`;
4. este `NEXT_ACTION.md`;
5. `00_SYSTEM/DECISION_LOG.md`, especialmente DEC-0009, DEC-0010, DEC-0016, DEC-0017 e DEC-0018;
6. `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7, QA-9 e QA-10;
7. `materials/tjsp-escrevente-2025/portugues/MANIFEST.md`;
8. `materials/tjsp-escrevente-2025/portugues/APOSTILA_QA_2.0.0.md`;
9. `materials/tjsp-escrevente-2025/portugues/METODOLOGIA_NOTEBOOKLM.md`.

Conferir também `main`, a branch `content/apostila-portugues-2.0.0` e o PR #12 antes de escrever.

## Gate 1 — Publicar o PDF 2.0.0 íntegro

O artefato aprovado localmente possui exatamente:

```text
pages: 29
page_size: A4
bytes: 40928
sha256: 1a7a1cbe8a0597f94ea490da7eec8ff874f2430ef596ec5bb9c3a14ecb2f1d62
expected_git_blob: b06f1150ac71cd9b87a3f8341be70a1c87355ccc
```

Destino:

```text
materials/tjsp-escrevente-2025/portugues/APOSTILA.pdf
```

Depois da publicação, fazer readback real e confirmar pelo menos:

- tamanho corresponde ao artefato pretendido;
- Git blob corresponde aos bytes esperados quando a publicação for byte-identical;
- download abre como PDF;
- `pdfinfo` identifica 29 páginas A4;
- `pdftotext` recupera conteúdo até Questão 30, gabarito e síntese final.

### Estado atual que não deve ser confundido com 2.0.0

O `APOSTILA.pdf` atualmente ligado à branch é um fallback seguro da 1.0.0:

```text
bytes: 13950
git_blob: 2287be2ba025228cc311722effc794fc9edf476f
material_version: 1.0.0
```

Ele foi restaurado apenas para remover o binário truncado. **Não usar esse arquivo no smoke de aceitação da 2.0.0.**

Também não promover os blobs rejeitados `5bea23e3...` ou `82046b5d...`.

## Gate 2 — Smoke real no NotebookLM

Somente depois do Gate 1 passar, preservar a arquitetura:

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf 2.0.0 íntegro

CONFIGURAÇÃO DA CONVERSA
→ Personalizado (ou equivalente)
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Não carregar metodologia, análise de banca, manifest, sources, QA, edital ou provas históricas como fontes durante o smoke.

### Teste

Gerar um Teste nativo e confirmar que:

- pergunta sobre Língua Portuguesa, não sobre metodologia/backoffice;
- inclui aplicação, não apenas reprodução literal;
- consegue distinguir interpretação, relações de sentido e norma-padrão.

### Cartões

Confirmar recuperação útil de definições, regras, exceções e contrastes, por exemplo:

- inferência x extrapolação;
- causa x explicação;
- condição x concessão;
- `se` apassivador x indeterminador;
- regência x crase;
- restritiva x explicativa.

### Mapa mental

Confirmar que a hierarquia principal da apostila é recuperada de forma inteligível e que questões/gabaritos não dominam a estrutura.

### Chat configurado

Testar pelo menos:

- `qual a diferença entre causa e explicação?`;
- `por que há crase em "à qual"?`;
- `me testa em concordância`;
- correção após uma resposta errada ou hesitante.

Marcar QA-7 live como `PASS` somente se esse smoke tiver sido realmente executado e não revelar falha material do corpus.

## Gate 3 — Fechamento do release

Se Gate 1 e Gate 2 passarem:

1. atualizar `APOSTILA_QA_2.0.0.md` para QA-7 live `PASS` e QA-9 publicação `PASS`;
2. atualizar `MANIFEST.md` para release final;
3. fechar a pendência no `CHANGELOG.md`;
4. atualizar `PROJECT_CONTROL.md` e `CHECKPOINT.md` para Português 2.0.0 final;
5. executar `python tools/verify.py`; se o ambiente ainda impedir, manter justificativa explícita conforme DEC-0009;
6. revisar diff/readback do PR #12;
7. fazer merge quando couber sob DEC-0009;
8. depois do merge, definir a próxima ação canônica para o próximo SubjectPack.

## Definition of Done restante

`APOSTILA-002` termina somente quando:

- o PDF 2.0.0 íntegro estiver no GitHub e validado por readback;
- o smoke real do NotebookLM estiver registrado como aprovado;
- release/continuidade estiverem finalizados;
- o PR #12 puder ser mesclado com segurança.

Até lá, **não iniciar os SubjectPacks das outras matérias** salvo nova decisão canônica explícita.
