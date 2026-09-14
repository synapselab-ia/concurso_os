# NEXT_ACTION

## DIREITO-007: Concluir release candidate do SubjectPack `direito-penal`

O conteúdo jurídico de `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` foi aprovado em `0.1.0-draft.3` e congelado no release candidate `0.1.0-rc.1`.

Estado já comprovado:

- `METODOLOGIA_NOTEBOOKLM.md` criada e auditada estaticamente;
- `APOSTILA.md`, `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md` e QA sincronizados para `0.1.0-rc.1`;
- QA estático do corpus para NotebookLM concluído;
- `APOSTILA.md` canônico possui Git blob `008c3ac439d8b7d4038fd0114e486c1daaf755b1`;
- o candidato preferido de PDF foi gerado a partir de cópia local com esse mesmo Git blob do Markdown congelado;
- PDF preferido: `17` páginas A4, `30.167` bytes, PDF 1.4, SHA-256 `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`, Git blob `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`;
- o candidato preferido passou readback textual e inspeção visual de `17/17` páginas a 150 dpi, sem clipping, sobreposição, glifos quebrados, quebra impeditiva de tabela ou mistura entre questões e gabarito;
- PR `#23` e PR `#24` registraram as tentativas anteriores de transporte binário sem aceitar blobs divergentes;
- em `2026-09-14`, o arquivo foi enviado manualmente para `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf` na branch `upload/direito-penal-apostila-pdf`;
- GitHub retornou para esse arquivo exatamente o Git blob `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`, provando identidade binária com o candidato integralmente auditado;
- o commit de upload/rename observado foi `fd7f0f78b16f85d06979ab1e6cc86762c1bd1d00`;
- em `2026-09-14`, readback textual e renderização/inspeção de `17/17` páginas foram executados novamente sobre o binário local de identidade idêntica e permaneceram `PASS`;
- QA-9 do PDF está fechado como `PASS_CANONICAL_BINARY_IDENTITY` para o artefato que será incorporado a `main` por esta branch;
- nova tentativa de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` em `2026-09-14` continua falhando com `Could not resolve host: github.com`, portanto `python tools/verify.py` permanece `not_executed_current_environment`, não `PASS`.

O pack ainda não é release. O PDF deixou de ser bloqueio técnico. Restam o smoke real do NotebookLM, a reavaliação do gate determinístico e a sincronização final de continuidade/release.

## Entradas obrigatórias

Ler conjuntamente:

- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md`;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf`;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-penal/METODOLOGIA_NOTEBOOKLM.md`;
- `materials/tjsp-escrevente-2025/direito-penal/MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md`;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7, QA-9 e QA-10;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `00_SYSTEM/PROJECT_SPEC.md` e `00_SYSTEM/ARCHITECTURE.md`.

## 1. Preservar o conteúdo congelado

Não reabrir escopo nem alterar silenciosamente DP-01 a DP-10 ou as 30 questões.

Se surgir erro material no conteúdo jurídico, voltar o estado para draft, corrigir e registrar nova passagem semântica antes de qualquer release final.

## 2. Preservar a identidade do PDF canônico

O PDF aprovado é:

- caminho: `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf`;
- páginas: `17`;
- bytes: `30.167`;
- PDF: `1.4`;
- SHA-256: `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`;
- Git blob: `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`.

Não substituir silenciosamente esse binário. Qualquer regeneração ou alteração do PDF exige novo registro de páginas, bytes, SHA-256, Git blob e nova execução de QA-9.

## 3. Executar smoke real do NotebookLM

Próxima ação funcional após o merge do PDF:

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

Enquanto a interface estiver indisponível ou o usuário ainda não executar o smoke, manter `pending_user_smoke`.

## 4. Gate canônico do repositório

Antes de encerrar `DIREITO-007`:

```bash
python tools/verify.py
```

O runtime local continua sem resolução DNS para `github.com`, impedindo checkout canônico. A última rechecagem ocorreu em `2026-09-14`. Enquanto isso persistir, registrar `not_executed_current_environment`; não tratar como `PASS`.

## 5. Critério de saída

`DIREITO-007` só fecha quando houver evidência real de:

- configuração de tutor auditada;
- metadados coerentes do `0.1.0-rc.1`;
- `APOSTILA.pdf` versionado com Git blob exato `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e` e QA-9 fechado;
- QA NotebookLM estático concluído e smoke real registrado;
- `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md`, QA e continuidade refletindo exatamente o estado;
- `python tools/verify.py` executado ou impossibilidade atual explicitamente reavaliada conforme DEC-0009.

Somente depois disso decidir explicitamente se o candidato pode ser promovido a release final. Os outros cinco SubjectPacks de B2 permanecem aguardando a validação completa deste primeiro pipeline jurídico.