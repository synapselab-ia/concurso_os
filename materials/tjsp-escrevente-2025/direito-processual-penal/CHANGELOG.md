# CHANGELOG - Direito Processual Penal - TJSP Escrevente 2025

## `0.1.0-rc.2` - DIREITO-015R recuperação de vínculo do PDF - 2026-09-24

- auditoria do `main` real em `ad004ba538c0e34b2c3739f563d4f09230d1f6f5` encontrou o caminho canônico `APOSTILA.pdf` ausente do tree, apesar da documentação de fechamento da PR #35;
- o objeto Git auditado `6374969ba722451dd6740364e24c41f25e730b54` continuava existente e com `37.917` bytes;
- a recuperação apenas liga esse mesmo blob ao caminho `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`;
- não houve regeneração, alteração semântica ou mudança binária do PDF;
- verificação do tree da branch de recuperação confirmou exatamente o blob e o tamanho esperados;
- nova tentativa de `python tools/verify.py` não chegou a executar porque o clone falhou por DNS em `2026-09-24`, exit `128`; resultado `NOT_EXECUTED_CURRENT_ENVIRONMENT`.

Após o merge da recuperação, o próximo gate permanece `DIREITO-016`, smoke curto de regressão no NotebookLM.

---

## `0.1.0-rc.2` - DIREITO-015 PDF corrigido - 2026-09-18

- novo `APOSTILA.pdf` gerado exclusivamente do Markdown rc.2 congelado, Git blob de fonte `8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18`;
- 28 páginas A4, PDF 1.4, 37.917 bytes, pesquisável;
- SHA-256 `aeaa44ac6a275623d79098d0699c18899f83d6ade75be8661f71a3ad9dfc36fe`;
- Git blob do PDF `6374969ba722451dd6740364e24c41f25e730b54`;
- readback textual `PASS`, incluindo arts. 371-372 corrigidos;
- inspeção visual `PASS_VISUAL_28_OF_28`;
- identidade binária remota `PASS_CANONICAL_BINARY_IDENTITY`;
- PDF rc.1 permanece somente como histórico semanticamente invalidado;
- gate determinístico: `NOT_EXECUTED_CURRENT_ENVIRONMENT` por falha DNS no clone, exit `128`.

Próximo gate: smoke curto de regressão no NotebookLM sobre o PDF rc.2 corrigido.

---

## `0.1.0-rc.2` - 2026-09-18

Preparação do release candidate corrigido em `DIREITO-014`.

### Promoção de identidade

- `APOSTILA.md` promovida de `0.1.0-draft.3` para `0.1.0-rc.2`;
- nenhuma alteração jurídica no corpo da apostila, prática ou gabarito;
- correção dos arts. 371-372 permanece exatamente a aprovada em `DIREITO-013`;
- `SOURCES.md`, `MANIFEST.md` e `METODOLOGIA_NOTEBOOKLM.md` sincronizados para rc.2;
- tutor sem alteração comportamental;
- novo `APOSTILA.pdf` ainda não criado por design.

Próximo gate: gerar e auditar o PDF exclusivamente a partir do Markdown rc.2 congelado.

Gate determinístico: clone da branch rc.2 falhou por DNS em `2026-09-18`, exit `128`; `python tools/verify.py` permanece `NOT_EXECUTED_CURRENT_ENVIRONMENT`.

---

## `0.1.0-draft.3` - 2026-09-18

Reabertura semântica direcionada após identificação de erro normativo no `0.1.0-rc.1` durante o fechamento de `DIREITO-012`.

### Corrigido

- Unidade 5: removida a atribuição incorreta de que o art. 371 do CPP consideraria intimadas em audiência as pessoas presentes;
- art. 371 alinhado à fonte oficial: intimação por despacho na petição em que for requerida, observado o art. 357;
- art. 372 alinhado à literalidade oficial: adiamento da instrução criminal, marcação imediata de dia e hora para prosseguimento na presença de partes e testemunhas e lavratura de termo nos autos;
- QA direcionado de DPP-05 reaberto e reexecutado contra `SRC-B2-CPP`.

### Invalidado para uso corrente

- o `APOSTILA.pdf` de `0.1.0-rc.1` mantém verdadeiro o histórico `PASS_CANONICAL_BINARY_IDENTITY`, mas deixa de ser elegível como corpus/release por ter sido gerado de fonte Markdown semanticamente defeituosa;
- o binário foi removido do caminho canônico durante a correção para impedir uso acidental;
- `DIREITO-012` registrou evidência comportamental real do NotebookLM fornecida pelo usuário, mas não pode fechar o release sobre corpus invalidado.

Próximo passo: preparar novo RC a partir de `0.1.0-draft.3`, gerar novo PDF e executar smoke final curto sobre o corpus corrigido.

Gate determinístico: nova tentativa de clone da branch de correção em `2026-09-18` falhou por DNS (`Could not resolve host: github.com`, exit `128`); `python tools/verify.py` permanece `NOT_EXECUTED_CURRENT_ENVIRONMENT`, não `PASS`.

---

## `0.1.0-rc.1` - 2026-09-14

Preparação do primeiro release candidate sob `DIREITO-010`, sem promoção a release final.

### Adicionado em DIREITO-010

- `METODOLOGIA_NOTEBOOKLM.md` como `ConversationInstruction`, destinada à configuração nativa da conversa e não ao corpus estudável;
- regras de tutoria para fluxo processual, sujeito, legitimidade, prazo, competência, cabimento, efeito, contraste e correção;
- regra epistemológica explícita: ausência de informação na fonte deve ser tratada como limite do corpus, nunca como negativa universal;
- controle comportamental para não incorporar jurisprudência, doutrina ou atualização normativa ausente da fonte.

### Sincronizado em DIREITO-010

- `APOSTILA.md` promovida para identidade `0.1.0-rc.1`, mantendo congelado o conteúdo jurídico aprovado no `0.1.0-draft.2`;
- `MANIFEST.md` e `SOURCES.md` alinhados ao release candidate;
- `APOSTILA_QA_0.1.0.md` estendido para registrar o QA estático do RC.

### QA estático de DIREITO-010

- identidade do candidato: `pass`;
- mudança semântica do corpo jurídico no RC: `false`;
- configuração do tutor: `pass_static`;
- corpus/tutor NotebookLM estático: `pass_static`;
- ausência de `DPP-*` em títulos estudáveis: preservada;
- separação entre questões e gabarito: preservada;
- backoffice mantido fora das fontes do NotebookLM;
- baseline `2025-07-29` preservado;
- art. 584, § 4º, de 2026 permanece fora do baseline estudável.

### DIREITO-011 - 2026-09-15

O pipeline de PDF foi concluído sem alteração semântica da apostila.

#### Fonte e candidato auditado

- fonte Markdown confirmada contra o GitHub: Git blob `11a41d18ff3a8b03150923ec68d44087bded7267`;
- candidato final: 28 páginas A4, PDF 1.4, pesquisável;
- tamanho: `37.894 bytes`;
- SHA-256: `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob esperado: `4eabdacec7858120792cf792ca227335e41730b6`;
- readback textual: `PASS_TEXT_READBACK`;
- inspeção visual: `PASS_VISUAL_28_OF_28`;
- `Prática autoral` inicia na página 17;
- `Gabarito comentado` inicia na página 27.

#### Publicação canônica

O binário auditado foi transportado por Git Data API com conteúdo base64 e versionado exatamente em:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`

O GitHub criou o blob `4eabdacec7858120792cf792ca227335e41730b6`, idêntico ao Git blob esperado do candidato local. O readback do caminho remoto retornou o mesmo SHA.

Resultado final de DIREITO-011:

- `PASS_SOURCE_MARKDOWN_IDENTITY`;
- `PASS_TEXT_READBACK`;
- `PASS_VISUAL_28_OF_28`;
- `PASS_CANONICAL_BINARY_IDENTITY`;
- PDF canônico: `VERSIONED_EXACT_BINARY`;
- NotebookLM live smoke: `NOT_STARTED`.

A tentativa anterior com outro candidato, que produziu blob remoto divergente, permanece registrada apenas como histórico de QA; o blob foi rejeitado e nunca referenciado por tree, commit, branch ou PR canônico.

O gate determinístico foi reavaliado em `2026-09-15`; nova tentativa de clone falhou com `Could not resolve host: github.com`, exit `128`. `python tools/verify.py` permanece `NOT_EXECUTED_CURRENT_ENVIRONMENT`, não `PASS`.

Nenhuma correção semântica de Direito Processual Penal foi introduzida no `rc.1` durante `DIREITO-010` ou `DIREITO-011`.

### DIREITO-012 - tentativa de smoke externo - 2026-09-15

O estado canônico foi revalidado antes do smoke: `main` em `b63f9a8f4b51894bf37e070eee3feeb481781855`, zero PRs abertas e `APOSTILA.pdf` remoto com Git blob `4eabdacec7858120792cf792ca227335e41730b6`.

O runtime desta execução não forneceu sessão autenticada do NotebookLM nem canal interativo já conectado para operar a interface. Nenhuma conversa, Teste, Cartão, Mapa mental ou outro artefato externo foi criado ou inspecionado.

Resultado correto:

- NotebookLM live smoke: `EXTERNAL_SMOKE_NOT_EXECUTED`;
- `DIREITO-012`: permanece aberto como `blocked_external_access`;
- registro: `NOTEBOOKLM_SMOKE_0.1.0.md`.

O gate determinístico também foi reavaliado: o clone para `/tmp/concurso_os_d012` falhou com `Could not resolve host: github.com`, exit `128`. `python tools/verify.py` permanece `NOT_EXECUTED_CURRENT_ENVIRONMENT`, não `PASS`.

Nenhum resultado externo foi presumido e nenhuma alteração semântica foi feita no StudentContent.

---

## `0.1.0-draft.2` - 2026-09-14

Fechamento do QA semântico/normativo de `DIREITO-009`.

### Corrigido e aprofundado

- cobertura literal do art. 262;
- arts. 363-365, distinguindo regra atual de citação por edital das referências residuais a incisos revogados;
- art. 394-A e art. 400-A;
- identificação expressa do art. 398 como revogado;
- procedimento sumário com art. 537 revogado e art. 538 explicitado;
- regras gerais de recursos, RESE e apelação aprofundadas;
- intervalo `604-620` refeito para identificar `604-608` e `611` como revogados e rastrear `609-610` e `612-620`;
- intervalo `632-646` refeito para identificar `632-636` como revogados e explicitar `637-646`, inclusive prazos da carta testemunhável;
- art. 647-A e fluxo do habeas corpus incorporados;
- Lei n.º 9.099/1995, arts. 60-83, aprofundada em comunicação, fase preliminar, audiência, recursos e art. 81, § 1º-A.

### Controle de versão

- baseline mantido em `2025-07-29`;
- art. 584, § 4º, incluído em 2026, permanece excluído do StudentContent;
- `SRC-B2-L9099` permanece `cutoff_closed_no_scoped_drift` no inventário canônico.

### Prática

- as 52 questões do `draft.1` foram revisadas individualmente;
- foram adicionadas 8 questões para fechar pontos literais e de Q-FULL/Q-VER;
- total final: `60` questões A-E com gabarito comentado separado;
- QA final da prática: `60/60 PASS`.

### QA

- DPP-01...DPP-25: `pass_after_corrections`;
- normativo: `pass_after_corrections`;
- didática/fluxos/contrastes: `pass`;
- prática: `pass_60_of_60`;
- requisitos `Q-LIT`, `Q-CMP`, `Q-CAS`, `Q-FLX`, `Q-VER` e `Q-FULL`: `pass`;
- corpus Markdown: `pass_for_markdown`;
- IDs de backoffice em títulos estudáveis: `pass_absent`;
- PDF: `not_created_by_design`;
- NotebookLM: `not_started`.

### Gate determinístico

Nova tentativa de obter checkout canônico por `git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git` falhou com `Could not resolve host: github.com`, exit code `128`. `python tools/verify.py` permaneceu `not_executed_current_environment`, não `PASS`.

### Saída de DIREITO-009

O `0.1.0-draft.2` foi semanticamente aprovado para preparação de release candidate em etapa separada.

---

## `0.1.0-draft.1` - 2026-09-14

Primeira implementação completa do SubjectPack `direito-processual-penal` sob `DIREITO-008`.

### Adicionado

- workspace canônico em `materials/tjsp-escrevente-2025/direito-processual-penal/`;
- `MANIFEST.md` com status de draft, recorte oficial e rastreabilidade `DPP-01...DPP-25` mantida no backoffice;
- `SOURCES.md` com edital, `SRC-B2-CPP`, `SRC-B2-L9099`, baseline `2025-07-29` e controle explícito do drift posterior do CPP art. 584, § 4º;
- `APOSTILA.md` em primeira passagem completa;
- fluxos de citação, intimação, procedimento comum, Tribunal do Júri, procedimento sumário, recursos, habeas corpus e JECrim;
- quadros de contraste entre institutos próximos;
- mini-casos autorais;
- prática objetiva A-E com gabarito comentado separado.

### Engenharia de corpus

- nenhum `DPP-*` foi usado em título ou subtítulo estudável;
- coverage IDs e rótulos de gate ficaram no backoffice;
- a redação evitou transformar ausência de conteúdo externo na lei em negativa universal.

### Versão normativa

- baseline: `2025-07-29`;
- CPP e Lei n.º 9.099/1995 oficiais reabertos durante a autoria;
- art. 584, § 4º, de 2026 mantido fora da apostila.

### Estado de QA no draft.1

- implementação das 25 coverage rows: `complete_first_pass_pending_semantic_qa`;
- QA semântico/normativo específico: `not_started`;
- PDF: `not_created_by_design`;
- NotebookLM: `not_started`.
