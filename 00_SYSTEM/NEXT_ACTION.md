# NEXT_ACTION

## APOSTILA-002-FINAL — Validar Português 2.0.0 no NotebookLM e concluir o release

A reconstrução editorial de Português 2.0.0 está concluída na branch `content/apostila-portugues-2.0.0` e o `APOSTILA.pdf` 2.0.0 já foi publicado de forma íntegra e confirmado por readback.

O próximo e último gate material de `APOSTILA-002` é o **smoke test real no NotebookLM**. Não reabrir a redação integral nem regenerar o PDF sem evidência concreta de problema observada nesse smoke.

## Estado fechado antes do smoke

Já existem e foram revisados:

- `APOSTILA_AUDIT_1.0.0.md`;
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` com B1.1–B1.13 `covered`;
- `APOSTILA.md` 2.0.0 reconstruída;
- 30 questões autorais A–E com gabarito comentado separado;
- `APOSTILA_QA_2.0.0.md`;
- QA-1 a QA-6 `PASS`;
- QA-7 estático `PASS`;
- QA-8 `PASS`;
- QA-9 PDF `PASS`, incluindo publicação/readback no GitHub.

Distribuição canônica do PDF na branch:

```text
path: materials/tjsp-escrevente-2025/portugues/APOSTILA.pdf
pages: 16
page_size: A4
bytes: 20824
sha256: b4d9035d0bcfacc88f8bc44100edadca8bf49a5eca47609e633d620dbabb9931
git_blob: 640efaed13dd43cc83f6904c62fdb86131b9124a
```

O readback do diretório confirmou exatamente `size=20824` e `sha=640efaed13dd43cc83f6904c62fdb86131b9124a`.

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

## Gate único restante — Smoke real no NotebookLM

Preservar a arquitetura:

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf 2.0.0

CONFIGURAÇÃO DA CONVERSA
→ Personalizado (ou equivalente)
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Não carregar metodologia, análise de banca, manifest, sources, QA, edital ou provas históricas como fontes durante o smoke.

### 1. Teste

Gerar um Teste nativo e confirmar que:

- pergunta sobre Língua Portuguesa, não sobre metodologia/backoffice;
- inclui aplicação, não apenas reprodução literal;
- consegue distinguir interpretação, relações de sentido e norma-padrão.

### 2. Cartões

Confirmar recuperação útil de definições, regras, exceções e contrastes, por exemplo:

- inferência x extrapolação;
- causa x explicação;
- condição x concessão;
- `se` apassivador x indeterminador;
- regência x crase;
- restritiva x explicativa.

### 3. Mapa mental

Confirmar que a hierarquia principal da apostila é recuperada de forma inteligível e que questões/gabaritos não dominam a estrutura.

### 4. Chat configurado

Testar pelo menos:

- `qual a diferença entre causa e explicação?`;
- `por que há crase em "à qual"?`;
- `me testa em concordância`;
- correção após uma resposta errada ou hesitante.

Marcar QA-7 live como `PASS` somente se esse smoke tiver sido realmente executado e não revelar falha material do corpus.

## Fechamento após PASS

Se o smoke passar:

1. atualizar `APOSTILA_QA_2.0.0.md` para QA-7 live `PASS`;
2. atualizar `MANIFEST.md` de `release-candidate` para release final;
3. fechar a pendência no `CHANGELOG.md`;
4. atualizar `PROJECT_CONTROL.md` e `CHECKPOINT.md` para Português 2.0.0 final;
5. executar `python tools/verify.py`; se o ambiente ainda impedir, manter justificativa explícita conforme DEC-0009;
6. revisar diff/readback do PR #12;
7. marcar o PR pronto para review e fazer merge quando couber sob DEC-0009;
8. depois do merge, definir a próxima ação canônica para o próximo SubjectPack.

## Definition of Done restante

`APOSTILA-002` termina somente quando o smoke real do NotebookLM estiver registrado como aprovado, o release estiver promovido a final e o PR #12 tiver sido concluído.

Até lá, **não iniciar os SubjectPacks das outras matérias** salvo nova decisão canônica explícita.
