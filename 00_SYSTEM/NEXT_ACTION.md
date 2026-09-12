# NEXT_ACTION

## DIREITO-007 — Preparar release candidate do SubjectPack `direito-penal`

`DIREITO-006` fechou o QA editorial/normativo do Markdown. O estado aprovado para entrada neste gate é `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` `0.1.0-draft.3`.

O pack **ainda não é release**. Não marcar PDF, NotebookLM ou release como PASS antes da execução real dos respectivos gates.

## Entradas obrigatórias

Ler conjuntamente:

- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` — conteúdo semanticamente aprovado;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md` — evidência de fechamento do DIREITO-006;
- `materials/tjsp-escrevente-2025/direito-penal/MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md`;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7, QA-9 e QA-10;
- `00_SYSTEM/QA_PROTOCOL.md`;
- arquitetura NotebookLM em `00_SYSTEM/PROJECT_SPEC.md` e `00_SYSTEM/ARCHITECTURE.md`;
- `materials/tjsp-escrevente-2025/portugues/METODOLOGIA_NOTEBOOKLM.md` apenas como referência de arquitetura/comportamento, sem copiar regras específicas de Português.

## 1. Congelar o conteúdo-base do candidato

Usar `0.1.0-draft.3` como base sem reabrir escopo ou alterar silenciosamente a matriz DP-01…DP-10.

Se surgir erro material durante a preparação do candidato, voltar o estado para draft, corrigir e registrar nova passagem de QA. Não corrigir conteúdo silenciosamente dentro do PDF.

## 2. Criar a configuração do tutor

Criar:

`materials/tjsp-escrevente-2025/direito-penal/METODOLOGIA_NOTEBOOKLM.md`

O arquivo deve seguir DEC-0016/DEC-0017:

```text
fonte estudável → APOSTILA.pdf
comportamento do tutor → configuração nativa da conversa
backoffice → GitHub/ChatGPT
```

A metodologia deve orientar dúvidas, treino interativo, correção e relatório de sessão, sem virar conteúdo da matéria e sem depender de metadados internos do projeto.

## 3. Promover para release candidate

Depois de `METODOLOGIA_NOTEBOOKLM.md` e metadados coerentes, promover identidade de trabalho para `0.1.0-rc.1`.

Atualizar conjuntamente:

- `APOSTILA.md` — apenas metadados de versão/status se o conteúdo não mudar;
- `MANIFEST.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- documento de QA aplicável.

`rc.1` significa candidato em teste, não release.

## 4. Gerar `APOSTILA.pdf`

Somente a partir do Markdown aprovado/RC:

- gerar PDF pesquisável;
- preservar hierarquia de títulos, tabelas e separação pergunta/gabarito;
- registrar páginas, tamanho, SHA-256 e demais metadados úteis;
- fazer readback textual do arquivo produzido;
- renderizar e inspecionar visualmente todas as páginas para clipping, sobreposição, quebra inadequada de tabelas, acentos e símbolos.

Registrar o resultado como QA-9. Uma geração bem-sucedida não equivale a PASS visual.

## 5. QA do NotebookLM

Executar o que for possível sem inventar interação externa:

- QA estático de recuperabilidade do corpus;
- quando houver acesso real à interface, carregar **somente** `APOSTILA.pdf` como fonte;
- colocar `METODOLOGIA_NOTEBOOKLM.md` na configuração personalizada da conversa, não nas fontes;
- inspecionar chat e artefatos úteis, conforme o protocolo.

Se o smoke real depender de ação do usuário/interface indisponível no runtime, registrar `not_executed`/`pending_user_smoke`; não promover a release final como se o teste tivesse ocorrido.

## 6. Critério de saída

`DIREITO-007` só fecha quando existir um release candidate coerente com:

- `METODOLOGIA_NOTEBOOKLM.md` criada e auditada;
- versão/metadados sincronizados;
- `APOSTILA.pdf` íntegro, pesquisável e com QA textual/visual realizado;
- QA NotebookLM estático concluído e smoke real registrado quando executável;
- `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md` e QA refletindo exatamente o estado;
- nenhuma promoção a release final se algum gate obrigatório continuar pendente.

A decisão de release final deve ser explícita e sustentada pelos gates realizados. Só depois do primeiro pipeline jurídico completo os demais cinco SubjectPacks avançam na ordem canônica.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

Em `2026-09-12`, `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` continua falhando neste runtime com `Could not resolve host: github.com`. Enquanto essa condição persistir, registrar a impossibilidade conforme DEC-0009; não tratar como `PASS`.