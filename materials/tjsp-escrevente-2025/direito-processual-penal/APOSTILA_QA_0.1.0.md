# APOSTILA_QA_0.1.0 - Direito Processual Penal - TJSP Escrevente 2025

**QA dates:** `2026-09-14` e `2026-09-15`  
**Pack:** `direito-processual-penal`  
**Version:** `0.1.0-rc.1`  
**Semantic gate:** `DIREITO-009`  
**RC preparation gate:** `DIREITO-010`  
**PDF gate:** `DIREITO-011`  
**Overall semantic result:** `PASS`  
**Normative result:** `PASS_AFTER_CORRECTIONS`  
**Static NotebookLM result:** `PASS_STATIC`  
**PDF candidate local QA:** `PASS_LOCAL_CANDIDATE`  
**Canonical PDF identity:** `BLOCKED_NOT_VERSIONED`

## 1. Escopo e estado semântico congelado

O QA semântico foi executado contra o syllabus canônico, a matriz `DPP-01...DPP-25`, o inventário de versões de B2 e as fontes normativas primárias `SRC-B2-CPP` e `SRC-B2-L9099`.

Recorte auditado:

- CPP: `251-258; 261-267; 274; 351-372; 394-497; 531-538; 541-548; 574-667`;
- Lei n.º 9.099/1995: `60-83; 88-89`.

Baseline: `2025-07-29`.

`DIREITO-009` fechou o conteúdo em `0.1.0-draft.2` como `PASS_AFTER_CORRECTIONS`. `DIREITO-010` promoveu somente a identidade/status para `0.1.0-rc.1`, sem mudança jurídica do corpo aprovado, e criou `METODOLOGIA_NOTEBOOKLM.md` como `ConversationInstruction`.

### Cobertura

| coverage_id | recorte | resultado |
|---|---|---|
| DPP-01 | CPP 251-258 | PASS |
| DPP-02 | CPP 261-267 | PASS |
| DPP-03 | CPP 274 | PASS |
| DPP-04 | CPP 351-369 | PASS |
| DPP-05 | CPP 370-372 | PASS |
| DPP-06 | CPP 394-405 | PASS_AFTER_CORRECTIONS |
| DPP-07 | CPP 406-421 | PASS |
| DPP-08 | CPP 422-431 | PASS |
| DPP-09 | CPP 432-452 | PASS |
| DPP-10 | CPP 453-474 | PASS |
| DPP-11 | CPP 475-491 | PASS |
| DPP-12 | CPP 492-497 | PASS |
| DPP-13 | CPP 531-538 | PASS_AFTER_CORRECTIONS |
| DPP-14 | CPP 541-548 | PASS |
| DPP-15 | CPP 574-580 | PASS_AFTER_CORRECTIONS |
| DPP-16 | CPP 581-592 | PASS_AFTER_CORRECTIONS |
| DPP-17 | CPP 593-603 | PASS_AFTER_CORRECTIONS |
| DPP-18 | CPP 604-620 | PASS_AFTER_CORRECTIONS |
| DPP-19 | CPP 621-631 | PASS |
| DPP-20 | CPP 632-646 | PASS_AFTER_CORRECTIONS |
| DPP-21 | CPP 647-667 | PASS_AFTER_CORRECTIONS |
| DPP-22 | Lei 9.099, 60-68 | PASS_AFTER_CORRECTIONS |
| DPP-23 | Lei 9.099, 69-76 | PASS |
| DPP-24 | Lei 9.099, 77-83 | PASS_AFTER_CORRECTIONS |
| DPP-25 | Lei 9.099, 88-89 | PASS |

Os identificadores `DPP-*` permanecem no backoffice e não aparecem como títulos/subtítulos estudáveis.

### Correções relevantes fechadas em DIREITO-009

A passagem normativa integral explicitou ou corrigiu, entre outros pontos:

- art. 262;
- arts. 363-365;
- art. 394-A;
- art. 398 revogado;
- art. 400-A;
- art. 537 revogado e art. 538;
- regras gerais de recursos, RESE e apelação nos intervalos 574-603;
- arts. 604-608 e 611 revogados, com 609-610 e 612-620 rastreados;
- arts. 632-636 revogados e 637-646 explicitados;
- art. 647-A e sequência de 647-667;
- Lei 9.099, arts. 60-83, inclusive art. 81, § 1º-A.

O art. `584, § 4º`, incluído pela Lei n.º `15.358/2026`, permanece fora do baseline estudável.

## 2. Prática e corpus Markdown

- questões originais revisadas: `52/52 PASS`;
- questões adicionadas para fechamento de lacunas: `Q53-Q60`;
- total final: `60/60 PASS`;
- requisitos `Q-LIT`, `Q-CMP`, `Q-CAS`, `Q-FLX`, `Q-VER` e `Q-FULL`: `PASS`;
- corpus Markdown: `PASS_FOR_MARKDOWN`;
- configuração do tutor: `PASS_STATIC`;
- NotebookLM live smoke: `NOT_STARTED`.

## 3. DIREITO-011 - congelamento da fonte do PDF

Em `2026-09-15`, o `main` canônico continuava em:

`947ea624d7abfa3b1db4481064aa4abf9743be19`

O arquivo congelado usado para a geração local foi conferido contra o GitHub:

- caminho: `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.md`;
- versão: `0.1.0-rc.1`;
- bytes locais da cópia usada: `69.109`;
- SHA-256 local: `da3f1b0c75e4300d22584d2393cab3a3ee4d88f0bd5199ec5a0761a2d2f62fa1`;
- Git blob calculado localmente: `11a41d18ff3a8b03150923ec68d44087bded7267`;
- Git blob retornado pelo GitHub para `APOSTILA.md`: `11a41d18ff3a8b03150923ec68d44087bded7267`.

**Resultado:** `PASS_SOURCE_MARKDOWN_IDENTITY`.

Nenhuma correção jurídica foi feita durante a diagramação.

## 4. DIREITO-011 - candidato local auditado

Foi gerado um candidato A4 pesquisável exclusivamente a partir do Markdown congelado. A versão preferida para transporte foi produzida em formato PDF 1.4 ASCII-safe, usando fontes básicas do PDF e streams comprimidos, sem incorporar conteúdo externo.

### Identidade do candidato preferido

- arquivo local: `APOSTILA_ascii_compact.pdf`;
- páginas: `28`;
- página: `A4`, `595.28 x 841.89 pt`;
- formato: `PDF 1.4`;
- tamanho: `37.894 bytes`;
- SHA-256: `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob esperado: `4eabdacec7858120792cf792ca227335e41730b6`;
- pesquisável: `sim`;
- criptografia: `não`;
- JavaScript: `não`;
- conteúdo externo: `não`.

A geração substitui apenas glifos de diagramação indisponíveis em WinAnsi por equivalentes textuais seguros quando necessário, como setas por `->`; o conteúdo jurídico não foi alterado.

## 5. Readback textual do mesmo candidato

`pdftotext -layout` foi executado sobre o candidato acima. Foram confirmados:

- `Direito Processual Penal`;
- `Unidade 1`;
- `Unidade 25`;
- `Gabarito comentado`;
- `art. 584`;
- `§`;
- `JECrim`;
- `habeas corpus`;
- `carta testemunhável`;
- questão `60`;
- gabarito `60. B.`;
- acentos e símbolos jurídicos no readback.

Trecho de controle da questão 60 recuperado do PDF:

```text
60.
Na audiência do JECrim, o art. 81, § 1º-A,
...
60. B. O § 1º-A do art. 81 protege a dignidade da vítima na audiência do JECrim.
```

**Resultado:** `PASS_TEXT_READBACK`.

## 6. Inspeção visual integral

As `28/28` páginas do mesmo candidato foram renderizadas a `150 dpi` e inspecionadas em quatro contact sheets cobrindo páginas `1-7`, `8-14`, `15-21` e `22-28`.

Não foram observados:

- clipping de texto;
- sobreposição de elementos;
- páginas vazias indevidas;
- glifos quebrados;
- corrupção de acentos ou `§`;
- quebra impeditiva de tabelas ou fluxos;
- mistura acidental entre bateria e gabarito.

A seção `Prática autoral` inicia em página própria na página `17`. O `Gabarito comentado` inicia em página própria na página `27` e continua na página `28` com o fechamento da apostila.

**Resultado:** `PASS_VISUAL_28_OF_28`.

## 7. Transporte e identidade canônica

O critério canônico exige que o binário auditado seja versionado em:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`

Neste runtime, o conector GitHub disponível não expõe uma operação de upload de arquivo binário por referência de arquivo local. As operações de conteúdo disponíveis recebem texto UTF-8; portanto não é seguro tratá-las como transporte do PDF auditado.

Uma tentativa anterior com outro candidato local (`56.319 bytes`, SHA-256 `946bac9ce3206ad97009e0f23c641945a61b345e754c89a1ce342194069d59e8`, Git blob esperado `97426cc526c542de6f07ed7e07698984a629ceb5`) produziu um blob remoto órfão com SHA `dd10a124a6226cf1bd63e7fa5104033c00d52788`, diferente do Git blob esperado. Esse blob nunca foi referenciado por tree, commit, branch ou PR e foi rejeitado como candidato canônico.

Para o candidato preferido atual, **nenhum upload remoto foi declarado como válido**. Não existe `APOSTILA.pdf` versionado no pack e não há prova de identidade binária remota.

**Resultado:** `CANONICAL_PDF_TRANSPORT_BLOCKED`.

Consequentemente:

- `PASS_CANONICAL_BINARY_IDENTITY`: **não**;
- `APOSTILA.pdf` canônico: **não versionado**;
- NotebookLM live smoke: continua bloqueado;
- o gate `DIREITO-011` permanece aberto.

## 8. Gate determinístico reavaliado em 2026-09-15

Nova tentativa:

```text
git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d011
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Exit code: `128`.

Sem checkout canônico, `python tools/verify.py` não foi executado. Resultado:

`NOT_EXECUTED_CURRENT_ENVIRONMENT`

Isso **não** é `PASS` e permanece documentado conforme DEC-0009.

## 9. Estado atual do release candidate

| Gate | Resultado |
|---|---|
| cobertura/normativo | PASS_AFTER_CORRECTIONS |
| prática | PASS, 60/60 |
| corpus Markdown | PASS_FOR_MARKDOWN |
| identidade `0.1.0-rc.1` | PASS |
| tutor/NotebookLM estático | PASS_STATIC |
| identidade da fonte Markdown usada no PDF | PASS_SOURCE_MARKDOWN_IDENTITY |
| PDF local - readback | PASS_TEXT_READBACK |
| PDF local - visual | PASS_VISUAL_28_OF_28 |
| PDF local - metadados | PASS_LOCAL_CANDIDATE |
| PDF canônico versionado | BLOCKED_NOT_VERSIONED |
| identidade binária GitHub | NOT_PROVEN |
| NotebookLM live smoke | NOT_STARTED |
| `python tools/verify.py` | NOT_EXECUTED_CURRENT_ENVIRONMENT |

`DIREITO-011` não está fechado como PDF validado. A próxima ação continua sendo transportar **exatamente** o candidato auditado para o caminho canônico e provar Git blob/identidade binária antes de avançar ao NotebookLM live smoke.