# NEXT_ACTION

## DIREITO-007: Concluir release candidate do SubjectPack `direito-penal`

O conteúdo jurídico de `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` foi aprovado em `0.1.0-draft.3` e congelado no release candidate `0.1.0-rc.1`.

Estado já comprovado:

- `METODOLOGIA_NOTEBOOKLM.md` criada e auditada estaticamente;
- `APOSTILA.md`, `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md` e QA sincronizados para `0.1.0-rc.1`;
- QA estático do corpus para NotebookLM concluído;
- `APOSTILA.md` canônico possui Git blob `008c3ac439d8b7d4038fd0114e486c1daaf755b1`;
- a cópia local usada para a geração do PDF foi verificada e possui o mesmo Git blob do Markdown canônico;
- candidato local preferido para publicação: `17` páginas A4, `30.167` bytes, PDF 1.4, SHA-256 `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`, Git blob local esperado `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`;
- o candidato preferido passou readback textual e inspeção visual de `17/17` páginas a 150 dpi, sem clipping, sobreposição, glifos quebrados, quebra impeditiva de tabela ou mistura entre questões e gabarito;
- PR `#23` registrou a primeira tentativa de publicação e foi mergeada em `main` no commit `737dc881f3eb91fed461d918bd026b86ce6bb210`;
- em `2026-09-13`, a integridade do candidato preferido foi revalidada localmente e permaneceu idêntica;
- em `2026-09-13`, o write surface GitHub disponível foi rechecado: `create_blob` recebe conteúdo textual/base64, mas não aceita referência direta ao arquivo binário local;
- um teste de transporte base64 em chunk alinhado também falhou em preservar os bytes: Git blob local esperado `f7b4c7b3256a3a93dcbb473062214c6007c4c398`, blob remoto retornado `d4d6c172421ca81eb40c825c44018e9ec4f421fd`;
- nenhum blob divergente foi anexado a árvore ou branch;
- `APOSTILA.pdf` continua `not_published`;
- o probe de rede local em `2026-09-13` continua falhando em resolver `github.com`, portanto `python tools/verify.py` permanece `not_executed_current_environment`, não `PASS`.

O pack ainda não é release. O PDF auditado continua local, o smoke real do NotebookLM não foi executado e o gate determinístico continua pendente.

## Entradas obrigatórias

Ler conjuntamente:

- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md`;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-penal/METODOLOGIA_NOTEBOOKLM.md`;
- `materials/tjsp-escrevente-2025/direito-penal/MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md`;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7, QA-9 e QA-10;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `00_SYSTEM/PROJECT_SPEC.md` e `00_SYSTEM/ARCHITECTURE.md`.

## 1. Preservar o conteúdo congelado

Não reabrir escopo nem alterar silenciosamente DP-01 a DP-10 ou as 30 questões.

Se surgir erro material no conteúdo jurídico, voltar o estado para draft, corrigir e registrar nova passagem semântica antes de qualquer PDF final.

## 2. Publicar `APOSTILA.pdf` somente por caminho binário confiável

O estado canônico permanece em `main`. A branch de implementação desta tentativa é `release/direito-penal-0.1.0-rc.1-pdf-publish`.

O repositório ainda não contém `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf`.

Prioridade técnica:

1. usar um write path que aceite os bytes exatos do arquivo local, referência de arquivo equivalente ou outro mecanismo cuja identidade binária possa ser verificada antes de anexar o objeto à árvore;
2. não repetir transporte manual de base64 pelo canal atual como se fosse confiável: o teste alinhado já demonstrou alteração de bytes;
3. para o candidato preferido atual, aceitar publicação somente se o Git blob remoto for exatamente `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`;
4. se for gerado outro binário válido, registrar novamente páginas, bytes, SHA-256, Git blob e executar QA-9 sobre esse arquivo exato;
5. somente depois versionar o caminho canônico `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf`.

Não usar SHA-256 ou Git blob local como se fossem identificadores do repositório antes de existir correspondência real no GitHub. Não anexar blob cuja identidade divergir da origem auditada.

## 3. Fechar QA-9 somente sobre o binário versionado

Sobre o `APOSTILA.pdf` efetivamente publicado:

- confirmar pesquisa e extração de texto;
- fazer readback textual;
- conferir acentos e símbolos jurídicos;
- renderizar e inspecionar todas as páginas ou confirmar identidade binária exata com um candidato já integralmente auditado;
- verificar clipping, sobreposição, tabelas, hierarquia e legibilidade;
- verificar separação entre perguntas e gabarito;
- registrar páginas, bytes, SHA-256 e Git blob.

Somente essa verificação fecha o gate canônico de PDF.

## 4. Executar smoke real do NotebookLM

Quando houver acesso efetivo à interface:

```text
FONTES
-> somente APOSTILA.pdf canônico

CONFIGURAÇÃO DA CONVERSA
-> bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Inspecionar no mínimo:

- chat configurado para dúvida jurídica e correção;
- Teste ou artefato de recuperação equivalente;
- Cartões;
- Mapa mental ou artefato hierárquico equivalente.

Confirmar que metodologia e backoffice não viram conteúdo estudável e que o tutor não inventa jurisprudência ou doutrina ausente da fonte.

Enquanto a interface estiver indisponível, manter `pending_user_smoke`.

## 5. Gate canônico do repositório

Antes de encerrar `DIREITO-007`:

```bash
python tools/verify.py
```

O runtime local continua sem resolução DNS para `github.com`, impedindo checkout canônico. Enquanto isso persistir, registrar `not_executed_current_environment`; não tratar como `PASS`.

## 6. Critério de saída

`DIREITO-007` só fecha quando houver evidência real de:

- configuração de tutor auditada;
- metadados coerentes do `0.1.0-rc.1`;
- `APOSTILA.pdf` versionado e QA textual/visual confirmado sobre o binário canônico;
- QA NotebookLM estático concluído e smoke real registrado;
- `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md`, QA e continuidade refletindo exatamente o estado;
- `python tools/verify.py` executado ou impossibilidade atual explicitamente reavaliada conforme DEC-0009.

Somente depois disso decidir explicitamente se o candidato pode ser promovido a release final. Os outros cinco SubjectPacks de B2 permanecem aguardando a validação completa deste primeiro pipeline jurídico.
