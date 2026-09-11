# NEXT_ACTION

## APOSTILA-002-FINAL — Retestar configuração rc2 no NotebookLM e concluir o release

A reconstrução editorial de Português 2.0.0 está concluída na branch `content/apostila-portugues-2.0.0` e o `APOSTILA.pdf` 2.0.0 já foi publicado de forma íntegra e confirmado por readback.

O primeiro smoke real no NotebookLM foi iniciado em 2026-09-11 e **não deve ser marcado como PASS ainda**. Ele recuperou o conteúdo central, mas revelou falhas concretas de comportamento/rotulagem no chat configurado. Essas falhas foram tratadas em `METODOLOGIA_NOTEBOOKLM.md` versão `2.0.0-rc2`.

O próximo gate é reinstalar a configuração rc2, repetir o chat crítico e concluir os artefatos nativos do Estúdio. Não reabrir a redação integral nem regenerar o PDF sem nova evidência de problema no corpus.

## Estado fechado antes do reteste

Já estão concluídos:

- `APOSTILA_AUDIT_1.0.0.md`;
- `APOSTILA_AUTHORING_MATRIX_2.0.0.md` com B1.1–B1.13 `covered`;
- `APOSTILA.md` 2.0.0 reconstruída;
- 30 questões autorais A–E com gabarito comentado separado;
- QA-1 a QA-6 `PASS`;
- QA-7 estático `PASS`;
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

## Evidência da primeira tentativa live

Foram observados:

- causa x explicação / inferência x extrapolação: conteúdo central correto, com uma formulação de inferência mais absoluta que a fonte;
- `à qual`: mecanismo de crase correto, mas um caso válido sem crase foi rotulado como “incorreto”;
- treino de concordância: questão válida, porém correção pouco específica para `Devem haver` → `Deve haver`;
- sugestão automática da interface exibindo `A resposta correta é a D.` antes da tentativa, possivelmente fora do controle das instruções persistentes.

`METODOLOGIA_NOTEBOOKLM.md` `2.0.0-rc2` corrige os comportamentos controláveis e registra o vazamento de sugestão de interface como risco a reavaliar, sem presumir controle sobre a camada externa do produto.

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

## Gate restante — Reteste real no NotebookLM

Preservar a arquitetura:

```text
FONTES DO NOTEBOOKLM
→ APOSTILA.pdf 2.0.0

CONFIGURAÇÃO DA CONVERSA
→ Personalizado (ou equivalente)
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md 2.0.0-rc2
```

Não carregar metodologia, análise de banca, manifest, sources, QA, edital ou provas históricas como fontes.

### 1. Reteste do chat configurado

Substituir a configuração anterior pelo bloco `2.0.0-rc2` e repetir:

- `qual a diferença entre causa e explicação?`;
- `por que há crase em "à qual"?`;
- `me testa em concordância`;
- responder uma questão errada ou pedir `por que a B está errada?`.

Aceitar o chat somente se:

- não houver contradição entre rótulo e explicação;
- o tutor não vazar o gabarito em sua própria resposta antes da tentativa;
- a correção explicar a construção específica do erro e mostrar a forma padrão corrigida;
- a resposta permanecer fiel à formulação da apostila sem absolutismos desnecessários.

Se a **interface externa** continuar exibindo sugestão automática com gabarito, registrar separadamente como limitação do produto e avaliar a usabilidade real; não atribuir automaticamente esse elemento ao prompt do tutor.

### 2. Teste nativo

Gerar um Teste e confirmar que pergunta sobre Língua Portuguesa, inclui aplicação e não vira teste sobre metodologia/backoffice.

### 3. Cartões

Confirmar recuperação útil de definições, regras, exceções e contrastes, incluindo alguns dos pares críticos da apostila.

### 4. Mapa mental

Confirmar que a hierarquia principal da apostila é inteligível e que questões/gabaritos não dominam a estrutura.

Marcar QA-7 live como `PASS` somente após esse reteste real completo.

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

`APOSTILA-002` termina somente quando o reteste real do NotebookLM estiver aprovado, o release estiver promovido a final e o PR #12 tiver sido concluído.

Até lá, **não iniciar os SubjectPacks das outras matérias** salvo nova decisão canônica explícita.
