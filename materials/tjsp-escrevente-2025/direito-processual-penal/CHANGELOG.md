# CHANGELOG - Direito Processual Penal - TJSP Escrevente 2025

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