# NEXT_ACTION

## DIREITO-012: Executar o smoke real do NotebookLM de `direito-processual-penal`

`DIREITO-011` está fechado no `main` com `PASS_CANONICAL_BINARY_IDENTITY` para `direito-processual-penal 0.1.0-rc.1`. O conteúdo jurídico permanece congelado a partir do `0.1.0-draft.2`.

## Estado canônico de entrada

- `main` revalidado no início desta tentativa: `b63f9a8f4b51894bf37e070eee3feeb481781855`;
- PRs abertas no início desta tentativa: `0`;
- pack: `direito-processual-penal`;
- versão: `0.1.0-rc.1`;
- cobertura `DPP-01...DPP-25`: `PASS_AFTER_CORRECTIONS`;
- revisão normativa: `PASS_AFTER_CORRECTIONS`;
- prática: `60/60 PASS`;
- corpus Markdown: `PASS_FOR_MARKDOWN`;
- configuração do tutor: `PASS_STATIC`;
- NotebookLM corpus/tutor estático: `PASS_STATIC`;
- baseline: `2025-07-29`;
- CPP art. 584, § 4º, de 2026: fora do baseline estudável;
- Markdown congelado: Git blob `11a41d18ff3a8b03150923ec68d44087bded7267`;
- `APOSTILA.pdf`: 28 páginas A4, PDF 1.4, 37.894 bytes;
- SHA-256 do PDF: `608ce1a5fd08eaa76b5b7f6677ae71ab2d5ae2f3aeeb4df135b81083500d28b0`;
- Git blob canônico do PDF: `4eabdacec7858120792cf792ca227335e41730b6`;
- PDF textual: `PASS_TEXT_READBACK`;
- PDF visual: `PASS_VISUAL_28_OF_28`;
- identidade binária: `PASS_CANONICAL_BINARY_IDENTITY`.

## Estado da tentativa atual

O runtime desta execução não disponibilizou uma sessão autenticada do NotebookLM nem um canal interativo já conectado capaz de operar a interface do produto em nome do usuário.

Nenhuma conversa, Teste, Cartão, Mapa mental ou outro artefato do NotebookLM foi criado ou inspecionado.

Resultado registrado:

`EXTERNAL_SMOKE_NOT_EXECUTED`

Isso não é `PASS`, `PASS_WITH_OBSERVATIONS` nem `FAIL` do NotebookLM. `DIREITO-012` permanece aberto como `blocked_external_access`.

O registro desta tentativa está em:

`materials/tjsp-escrevente-2025/direito-processual-penal/NOTEBOOKLM_SMOKE_0.1.0.md`

## Entradas obrigatórias ao retomar

Ler conjuntamente:

- `AGENTS.md`;
- `00_SYSTEM/START_HERE.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7/QA-10;
- `00_SYSTEM/QA_PROTOCOL.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA_QA_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/MANIFEST.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/METODOLOGIA_NOTEBOOKLM.md`;
- `materials/tjsp-escrevente-2025/direito-processual-penal/NOTEBOOKLM_SMOKE_0.1.0.md`;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md` somente como referência metodológica do smoke anterior.

Antes de registrar qualquer resultado, confirmar novamente `main`, PRs abertas, existência do PDF canônico e Git blob `4eabdacec7858120792cf792ca227335e41730b6`.

## 1. Configurar o notebook com corpus limpo

Quando houver acesso efetivo ao NotebookLM, usar:

```text
FONTES DO NOTEBOOKLM
-> somente o APOSTILA.pdf canônico de direito-processual-penal

CONFIGURAÇÃO DA CONVERSA
-> Personalizado ou mecanismo equivalente
-> colar somente o bloco entre INICIO_CONFIG e FIM_CONFIG de METODOLOGIA_NOTEBOOKLM.md
-> tamanho de resposta Padrão, salvo necessidade concreta
```

Não carregar como fontes `METODOLOGIA_NOTEBOOKLM.md`, `MANIFEST.md`, `SOURCES.md`, QA, matriz, análise de banca, edital ou outros artefatos de backoffice apenas para controlar o comportamento do tutor.

## 2. Smoke do chat

Executar interações reais suficientes para verificar:

1. explicação de um contraste processual, por exemplo `citação por edital x hora certa` ou `RESE x apelação`;
2. treino objetivo A-E com uma questão por vez;
3. ausência de dica ou gabarito antes da tentativa;
4. correção com artigo/regra e elemento decisivo após a resposta;
5. manutenção do fluxo sem avançar automaticamente antes de concluir a correção;
6. respeito ao baseline e à separação entre regra expressa, explicação e caso hipotético.

## 3. Smoke epistemológico fora do corpus

Fazer pelo menos uma pergunta cuja resposta dependa de informação que o PDF não fornece, preferencialmente jurisprudência, doutrina ou atualização normativa posterior não documentada.

Comportamento esperado: formular a ausência como limite da fonte, por exemplo:

`a fonte selecionada não traz essa informação; com base apenas nela, não posso afirmar isso`

Não aceitar silêncio do corpus convertido em negativa universal ou conteúdo externo inventado como se estivesse na apostila.

## 4. Smoke dos artefatos do Estúdio

Gerar amostras reais de:

- `Teste`;
- `Cartões`;
- `Mapa mental`.

Verificar:

- utilidade sobre o conteúdo da apostila;
- ausência de perguntas sobre metodologia, manifest, QA ou engenharia editorial;
- ausência de IDs `DPP-*`, gate labels ou outros metadados internos;
- conceitos, regras, prazos, contrastes e fluxos recuperados de forma coerente com o corpus.

## 5. Registrar evidência real

Depois do smoke efetivamente executado:

- atualizar `APOSTILA_QA_0.1.0.md`;
- completar `NOTEBOOKLM_SMOKE_0.1.0.md` com interações e artefatos realmente observados;
- atualizar `MANIFEST.md`, `CHANGELOG.md`, `PROJECT_CONTROL.md`, `CHECKPOINT.md` e este arquivo;
- atualizar `DIREITO_B2_AUTHORING_PLAN.md` quando necessário;
- classificar o gate como `PASS`, `PASS_WITH_OBSERVATIONS` ou `FAIL` somente conforme evidência real.

Se o smoke passar sem bloqueio, o próximo pack na ordem canônica é `direito-processual-civil`. Se houver falha bloqueante de conteúdo, retornar ao gate adequado em vez de promover silenciosamente o RC.

## 6. Gate determinístico

Nova tentativa nesta execução:

```text
git clone --depth 1 https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d012
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Exit code: `128`.

`python tools/verify.py` permanece `NOT_EXECUTED_CURRENT_ENVIRONMENT`, nunca `PASS`, conforme `DEC-0009`.

## Critério de saída de DIREITO-012

O gate só fecha quando o smoke real tiver sido executado e registrado com evidência suficiente. Enquanto este ambiente não tiver acesso efetivo ao NotebookLM, manter `DIREITO-012` aberto como `blocked_external_access` e não inventar resultado.
