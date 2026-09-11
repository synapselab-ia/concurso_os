# NEXT_ACTION

## APOSTILA-002-FINAL — Validar Mapa mental no NotebookLM e concluir o release

A reconstrução editorial de Português 2.0.0 está concluída na branch `content/apostila-portugues-2.0.0` e o `APOSTILA.pdf` 2.0.0 já foi publicado de forma íntegra e confirmado por readback.

O smoke real no NotebookLM avançou: o reteste do chat configurado com `METODOLOGIA_NOTEBOOKLM.md` `2.0.0-rc2` passou, o Teste nativo passou e os Cartões passaram. Resta apenas o **Mapa mental** para fechar QA-7 live.

Não reabrir a redação integral nem regenerar o PDF sem nova evidência concreta de problema no corpus.

## Estado fechado

Já estão concluídos:

- `APOSTILA_AUDIT_1.0.0.md`;
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` com B1.1–B1.13 `covered`;
- `APOSTILA.md` 2.0.0 reconstruída;
- 30 questões autorais A–E com gabarito comentado separado;
- QA-1 a QA-6 `PASS`;
- QA-7 estático `PASS`;
- QA-7 live chat rc2 `PASS`;
- QA-7 Teste nativo `PASS`;
- QA-7 Cartões `PASS`;
- QA-8 `PASS`;
- QA-9 PDF `PASS`, incluindo publicação/readback no GitHub.

Distribuição canônica do PDF:

```text
path: materials/tjsp-escrevente-2025/portugues/APOSTILA.pdf
pages: 16
page_size: A4
bytes: 20824
sha256: b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931
git_blob: 640efaed13dd43cc83f6904c62fdb86131b9124a
```

## Evidência live já aceita

### Chat rc2

O reteste passou em treino de concordância e correção específica por construção. Foram explicitados corretamente `fazer` temporal impessoal, `menos` invariável, concordância de `anexo` e `dever + existir`. Não houve vazamento do gabarito produzido pela resposta controlada do tutor. Sugestões automáticas da interface permanecem um risco separado da camada do produto.

### Teste nativo

Amostras aceitas cobriram:

- concordância com expressão partitiva;
- sentido figurado;
- equivalência de conectivos adversativos.

As questões exigiram aplicação real do conteúdo e não desviaram para metodologia/backoffice.

### Cartões

Amostras aceitas cobriram:

- identificação de quem enuncia;
- inferência legítima;
- extrapolação;
- concordância de `cujo` com o termo possuído.

Os cartões mostrados foram curtos, recuperáveis e fiéis ao corpus.

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

Conferir `main`, a branch `content/apostila-portugues-2.0.0` e o PR #12 antes de qualquer mutação.

## Gate único restante — Mapa mental

No mesmo notebook, mantendo como fonte apenas `APOSTILA.pdf` 2.0.0, gerar/abrir o Mapa mental e confirmar visualmente que:

- a hierarquia principal da matéria é inteligível;
- os grandes blocos de leitura/interpretação, coesão/semântica e norma-padrão aparecem de modo coerente;
- regras e conceitos relevantes são recuperados em níveis subordinados;
- questões e gabaritos não dominam a árvore;
- não aparecem metodologia, QA, manifest ou outro backoffice como conteúdo estudável.

Uma evidência visual suficiente do mapa permite marcar QA-7 live como `PASS` integral se nenhum problema material aparecer.

## Fechamento após PASS do Mapa mental

1. atualizar `APOSTILA_QA_2.0.0.md` para QA-7 live `PASS`;
2. atualizar `MANIFEST.md` de `release-candidate` para release final;
3. fechar a pendência no `CHANGELOG.md`;
4. atualizar `PROJECT_CONTROL.md` e `CHECKPOINT.md` para Português 2.0.0 final;
5. executar `python tools/verify.py`; se o ambiente ainda impedir, manter justificativa explícita conforme DEC-0009;
6. revisar diff/readback do PR #12;
7. marcar o PR pronto para review e fazer merge quando couber sob DEC-0009;
8. depois do merge, definir a próxima ação canônica para o próximo SubjectPack.

## Definition of Done restante

`APOSTILA-002` termina somente quando o Mapa mental estiver aprovado, QA-7 live estiver fechado, o release estiver promovido a final e o PR #12 tiver sido concluído.

Até lá, **não iniciar os SubjectPacks das outras matérias** salvo nova decisão canônica explícita.
