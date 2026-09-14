# NEXT_ACTION

## DIREITO-010: Preparar o release candidate de `direito-processual-penal`

`DIREITO-009` aprovou semanticamente o Markdown de Direito Processual Penal após correções.

Estado de entrada esperado após merge do QA:

- pack: `direito-processual-penal`;
- versão de conteúdo: `0.1.0-draft.2`;
- cobertura `DPP-01...DPP-25`: `PASS_AFTER_CORRECTIONS`;
- revisão normativa: `PASS_AFTER_CORRECTIONS`;
- didática/fluxos/contrastes: `PASS`;
- prática: `60/60 PASS`;
- corpus Markdown: `PASS_FOR_MARKDOWN`;
- baseline: `2025-07-29`;
- CPP art. 584, § 4º, de 2026: fora do baseline estudável;
- PDF: ainda não criado;
- NotebookLM: ainda não iniciado;
- gate determinístico: `NOT_EXECUTED_CURRENT_ENVIRONMENT` no runtime de DIREITO-009 por impossibilidade DNS, sem falso PASS.

O QA detalhado está em:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`

## Entradas obrigatórias

Antes de preparar o RC, ler conjuntamente:

- `AGENTS.md`;
- `00_SYSTEM/START_HERE.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `00_SYSTEM/SOURCE_POLICY.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/MANIFEST.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/SOURCES.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/CHANGELOG.md`;
- `materials/tjsp-escrevente-2025/direito-penal/METODOLOGIA_NOTEBOOKLM.md` como referência de arquitetura de tutor, não como fonte jurídica;
- `materials/tjsp-escrevente-2025/direito-penal/NOTEBOOKLM_SMOKE_0.1.0.md` como lição de processo;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md`;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md`.

Antes de escrever, confirmar `main`, PRs abertas e estado real do GitHub.

## 1. Identidade do release candidate

Preparar o primeiro RC de Processo Penal sem reabrir silenciosamente o conteúdo aprovado.

Se nenhuma correção semântica nova for necessária:

```text
content base -> 0.1.0-draft.2
candidate identity -> 0.1.0-rc.1
```

Sincronizar `APOSTILA.md`, `MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md` para a identidade do candidato, registrando explicitamente que o conteúdo normativo deriva do `draft.2` aprovado.

Se surgir erro jurídico durante a preparação, interromper a promoção, corrigir como novo draft e reabrir o QA correspondente. Não esconder correção semântica dentro de mudança de versão.

## 2. Configuração do tutor

Criar:

`materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md`

O arquivo é `ConversationInstruction`, não StudentContent.

A configuração deve:

- usar somente a fonte selecionada como base factual/didática da conversa;
- distinguir texto legal, explicação didática e aplicação hipotética;
- não inventar jurisprudência, doutrina ou atualização normativa ausente do corpus;
- quando a informação não estiver na fonte, declarar o limite do corpus em vez de afirmar inexistência externa;
- permitir dúvida explicativa e treino A-E;
- no treino, apresentar uma questão por vez e não antecipar o gabarito;
- corrigir pela regra, requisito, prazo, competência, cabimento ou efeito decisivo;
- oferecer reteste depois da correção quando útil.

## 3. QA estático de corpus e tutor

Antes de gerar PDF, verificar:

- a apostila funciona isoladamente como fonte estudável;
- `DPP-*`, IDs de matriz, gate labels e outros metadados de backoffice continuam fora dos títulos estudáveis;
- o tutor não exige `MANIFEST`, `SOURCES`, QA ou análise da banca como fontes do NotebookLM;
- perguntas e gabarito permanecem separados;
- tabelas e fluxos preservam sentido fora do layout específico do Markdown;
- nenhuma formulação do tutor transforma ausência no corpus em negativa universal;
- o baseline `2025-07-29` e o isolamento do art. 584, § 4º, de 2026 permanecem explícitos no backoffice.

Registrar o resultado estático no artefato de QA existente ou em seção claramente identificada de continuidade.

## 4. Pipeline de PDF

Somente depois do RC e do QA estático, gerar `APOSTILA.pdf` a partir do Markdown congelado do candidato.

O PDF deve passar por:

- identidade entre fonte Markdown congelada e candidato gerado;
- readback textual;
- inspeção visual de todas as páginas;
- conferência de títulos, símbolos jurídicos, tabelas, questões e gabarito;
- registro de tamanho, páginas, SHA-256 e Git blob quando versionado.

Não declarar `PASS_CANONICAL_BINARY_IDENTITY` até o binário versionado no GitHub ser comprovadamente idêntico ao candidato auditado.

## 5. NotebookLM

Arquitetura operacional esperada:

```text
fonte estudável -> APOSTILA.pdf
configuração da conversa -> METODOLOGIA_NOTEBOOKLM.md na camada nativa
backoffice -> GitHub/ChatGPT, fora do notebook por padrão
```

Depois que o PDF canônico estiver validado, o smoke real deve testar:

- chat explicativo;
- treino interativo;
- Teste;
- Cartões;
- Mapa mental;
- ausência de vazamento de IDs internos;
- ao menos uma pergunta cuja resposta não esteja no corpus, para testar disciplina epistemológica.

Não presumir resultado de smoke não executado.

## Critério de saída

`DIREITO-010` deve deixar explicitamente registrado o que efetivamente foi concluído. O gate só pode marcar um RC como preparado quando:

- identidade do candidato estiver sincronizada;
- configuração do tutor existir e passar QA estático;
- conteúdo semântico aprovado do `draft.2` permanecer congelado ou qualquer reabertura estiver registrada;
- continuidade estiver atualizada;
- gate determinístico tiver sido executado ou sua impossibilidade atual tiver sido documentada conforme DEC-0009.

PDF e smoke real podem exigir etapas subsequentes se houver bloqueio de transporte ou interação externa. Não promover a release final apenas por criar `rc.1`.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

Se o runtime ainda não conseguir obter checkout canônico, reavaliar e documentar a impossibilidade. Nunca registrar impossibilidade como `PASS`.
