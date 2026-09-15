# NEXT_ACTION

## DIREITO-012: Executar o smoke real do NotebookLM de `direito-processual-penal`

`DIREITO-011` fechou o gate de PDF de `direito-processual-penal 0.1.0-rc.1` com identidade binária canônica comprovada. O conteúdo jurídico permanece congelado a partir do `0.1.0-draft.2`.

## Estado de entrada esperado após merge da PR 31

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
- identidade binária: `PASS_CANONICAL_BINARY_IDENTITY`;
- NotebookLM live smoke: `NOT_STARTED`;
- `python tools/verify.py`: `NOT_EXECUTED_CURRENT_ENVIRONMENT` por falha DNS ao obter checkout canônico; isso não é PASS.

## Entradas obrigatórias

Antes do smoke, ler:

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
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md` somente como referência metodológica do smoke anterior.

Confirmar novamente `main`, PRs abertas, existência do PDF canônico e Git blob antes de registrar qualquer resultado.

## 1. Configurar o notebook com corpus limpo

Usar:

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

O comportamento esperado é equivalente a:

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

Se a interface oferecer outros artefatos e eles forem testados, registrar apenas resultados realmente observados.

## 5. Registrar o smoke

Atualizar `APOSTILA_QA_0.1.0.md` com:

- data;
- corpus efetivamente carregado;
- configuração efetivamente usada;
- interações e artefatos realmente testados;
- resultado de cada verificação;
- observações bloqueantes e não bloqueantes;
- classificação final `PASS`, `PASS_WITH_OBSERVATIONS` ou `FAIL` somente conforme evidência real.

Não presumir interação externa, artefato ou comportamento não observado.

## 6. Atualizar continuidade

Depois do smoke, atualizar conforme o estado real:

- `MANIFEST.md`;
- `CHANGELOG.md`;
- `PROJECT_CONTROL.md`;
- `00_SYSTEM/CHECKPOINT.md`;
- este arquivo;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md`, quando necessário.

Se o smoke passar sem bloqueio, o próximo pack na ordem canônica é `direito-processual-civil`. Se houver falha bloqueante de conteúdo, retornar ao gate adequado em vez de promover silenciosamente o RC.

## 7. Gate determinístico

Reexecutar ou reavaliar:

```bash
python tools/verify.py
```

Na tentativa mais recente de `2026-09-15`, o clone falhou com:

```text
Could not resolve host: github.com
```

Exit code `128`. A impossibilidade é `NOT_EXECUTED_CURRENT_ENVIRONMENT`, nunca `PASS`.

## Critério de saída de DIREITO-012

O gate fecha somente quando o smoke real tiver sido executado e registrado com evidência suficiente. Se este ambiente não tiver acesso efetivo ao NotebookLM, registrar `EXTERNAL_SMOKE_NOT_EXECUTED`, manter `DIREITO-012` aberto e não inventar resultado.