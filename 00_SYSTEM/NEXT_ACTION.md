# NEXT_ACTION

## DIREITO-011: Publicar o PDF auditado de `direito-processual-penal` e provar a identidade canônica

O release candidate `0.1.0-rc.1` de Direito Processual Penal permanece semanticamente congelado a partir do `0.1.0-draft.2`.

Em `2026-09-15`, o pipeline local de PDF avançou até o QA completo do candidato, mas **não** até a publicação canônica. O gate continua aberto por bloqueio de transporte binário.

## Estado de entrada canônico

- pack: `direito-processual-penal`;
- versão: `0.1.0-rc.1`;
- conteúdo-base: `0.1.0-draft.2` semanticamente congelado;
- cobertura `DPP-01...DPP-25`: `PASS_AFTER_CORRECTIONS`;
- revisão normativa: `PASS_AFTER_CORRECTIONS`;
- prática: `60/60 PASS`;
- corpus Markdown: `PASS_FOR_MARKDOWN`;
- configuração do tutor: `PASS_STATIC`;
- NotebookLM corpus/tutor estático: `PASS_STATIC`;
- baseline: `2025-07-29`;
- CPP art. 584, § 4º, de 2026: fora do baseline estudável;
- Git blob do Markdown congelado: `11a41d18ff3a8b03150923ec68d44087bded7267`;
- identidade entre a cópia local usada na geração e o Markdown do GitHub: `PASS_SOURCE_MARKDOWN_IDENTITY`;
- NotebookLM live smoke: `NOT_STARTED`;
- gate determinístico: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, por falha DNS ao obter checkout canônico; não é PASS.

## Candidato local já auditado

O candidato preferido gerado exclusivamente do Markdown congelado possui:

- páginas: `28`;
- página: `A4`;
- formato: `PDF 1.4`;
- tamanho: `37.894 bytes`;
- SHA-256: `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob esperado: `4eabdacec7858120792cf792ca227335e41730b6`;
- pesquisabilidade: `PASS`;
- readback textual: `PASS`;
- inspeção visual: `28/28 PASS`;
- `Prática autoral`: inicia em página própria na página `17`;
- `Gabarito comentado`: inicia em página própria na página `27`.

O QA detalhado está em:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`

Esses metadados descrevem um **candidato local auditado**. Eles não provam que existe um PDF canônico no GitHub.

## Bloqueio atual

O caminho canônico continua sem um binário validado:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`

O runtime atual não expõe no conector GitHub um transporte binário que aceite a referência do arquivo local auditado. Uma tentativa anterior com outro candidato produziu um blob remoto diferente do Git blob esperado e foi rejeitada. O blob divergente não foi ligado a tree, commit, branch ou PR.

Estado do gate:

```text
local candidate QA -> PASS
canonical PDF versioned -> NO
remote Git blob identity -> NOT_PROVEN
PASS_CANONICAL_BINARY_IDENTITY -> NO
NotebookLM live smoke -> BLOCKED
```

## Entradas obrigatórias ao retomar

Ler conjuntamente:

- `AGENTS.md`;
- `00_SYSTEM/START_HERE.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-9/QA-10;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/MANIFEST.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/CHANGELOG.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md` somente para o estágio posterior de smoke.

Antes de escrever, confirmar novamente `main`, PRs abertas e o estado real do caminho do PDF.

## 1. Transportar exatamente o binário auditado

Usar mecanismo que preserve bytes binários, como upload binário confiável no GitHub ou outro meio que permita versionar **exatamente** o candidato auditado.

Não regenerar silenciosamente o PDF para contornar o transporte. Se um novo binário for gerado, ele vira novo candidato e precisa repetir readback textual e inspeção visual integral antes de qualquer publicação.

O alvo é:

`materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`

## 2. Provar identidade depois da publicação

Após o upload:

1. ler do GitHub o Git blob do `APOSTILA.pdf` versionado;
2. exigir igualdade exata com:

`4eabdacec7858120792cf792ca227335e41730b6`

3. se houver igualdade, registrar `PASS_CANONICAL_BINARY_IDENTITY`;
4. se houver divergência, rejeitar o upload, não declarar PASS e manter `DIREITO-011` aberto.

O SHA-256 local, sozinho, não substitui o Git blob remoto.

## 3. Fechar QA-9 e atualizar continuidade somente após identidade exata

Se a identidade remota passar, atualizar:

- `APOSTILA_QA_0.1.0.md`;
- `MANIFEST.md`;
- `CHANGELOG.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- plano B2, quando necessário.

Registrar no estado canônico páginas, bytes, SHA-256, Git blob remoto e resultado de identidade.

## 4. Gate determinístico

Reexecutar ou reavaliar:

```bash
python tools/verify.py
```

Na tentativa de `2026-09-15`, o checkout falhou com:

```text
Could not resolve host: github.com
```

Exit code `128`. A impossibilidade continua sendo `NOT_EXECUTED_CURRENT_ENVIRONMENT`, nunca `PASS`.

## 5. Estágio seguinte somente após PDF canônico

Somente depois de `PASS_CANONICAL_BINARY_IDENTITY`, avançar para o smoke real do NotebookLM usando:

```text
FONTES
-> somente APOSTILA.pdf canônico

CONFIGURAÇÃO DA CONVERSA
-> bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

O smoke deverá testar chat explicativo, treino A-E uma questão por vez, Teste, Cartões, Mapa mental, ausência de IDs internos e pelo menos uma pergunta fora do corpus para verificar disciplina epistemológica.

Não presumir nenhuma interação externa não executada.

## Critério de saída de DIREITO-011

O gate só fecha quando:

- o arquivo canônico existir no GitHub;
- seu Git blob for exatamente `4eabdacec7858120792cf792ca227335e41730b6`;
- a identidade binária com o candidato auditado estiver comprovada;
- QA e continuidade registrarem os metadados exatos;
- `python tools/verify.py` tiver sido executado ou a impossibilidade atual tiver sido novamente documentada conforme DEC-0009.

Até lá, `DIREITO-011` permanece aberto como `CANONICAL_PDF_TRANSPORT_BLOCKED`.