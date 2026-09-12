# NEXT_ACTION

## DIREITO-005 — Iniciar autoria do SubjectPack `direito-penal`

Os Gates 1–4 de B2 estão fechados. O escopo editorial, o baseline normativo, a análise histórica da banca e a matriz de cobertura/autoria já estão definidos e rastreáveis.

A redação substancial está agora **autorizada somente para o primeiro SubjectPack**, `direito-penal`, como validação do pipeline jurídico. Os demais cinco packs permanecem posteriores na ordem operacional.

## Contrato obrigatório

Usar conjuntamente:

- `competitions/tjsp-escrevente-2025/SYLLABUS.md` — autoridade de escopo;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` — baseline e proveniência;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md` — sinais empíricos de forma, sem peso preditivo;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md` — contrato DP-01…DP-10;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md` — fronteira e ordem de produção;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md` — processo obrigatório;
- `00_SYSTEM/SOURCE_POLICY.md` e `00_SYSTEM/QA_PROTOCOL.md` — proveniência e gates de qualidade.

## Escopo exato

Código Penal:

`arts. 293–305; 307; 308; 311-A; 312–317; 319–333; 336–337; 339–347; 357; 359`.

A versão-base autoral é a vigente em `2025-07-29`. O Gate 2 não identificou drift textual pós-cutoff dentro desse recorte. O art. 338-A, incluído posteriormente, está fora do recorte e não deve ser absorvido por proximidade numérica.

## Unidade de autoria

Criar o workspace:

`materials/tjsp-escrevente-2025/direito-penal/`

A primeira implementação deve estabelecer, no mínimo:

- `APOSTILA.md` — corpo didático em versão de trabalho;
- `SOURCES.md` — referências do pack para `SRC-B2-CP`, edital e evidência empírica aplicável, sem copiar binário de terceiro;
- `MANIFEST.md` — identidade, escopo, versão e estado do material;
- `CHANGELOG.md` — histórico desde o primeiro draft.

O documento de QA deve ser criado/atualizado quando houver uma versão suficientemente completa para os gates editoriais. Não publicar `APOSTILA.pdf` como final antes do fluxo de QA previsto no protocolo.

## Contrato DP-01…DP-10

A apostila deve tornar rastreáveis as dez unidades da matriz:

1. `DP-01` — arts. 293–295: papéis públicos e petrechos;
2. `DP-02` — arts. 296–305: falsidades documentais, atestados, uso e supressão;
3. `DP-03` — arts. 307–308: falsa identidade x documento de identidade alheio;
4. `DP-04` — art. 311-A: fraude em certame de interesse público;
5. `DP-05` — arts. 312–317: crimes funcionais nucleares;
6. `DP-06` — arts. 319–327: prevaricação e crimes funcionais do intervalo;
7. `DP-07` — arts. 328–333: crimes de particular contra a Administração;
8. `DP-08` — arts. 336–337: inutilização/subtração de edital, sinal, livro ou documento;
9. `DP-09` — arts. 339–347: crimes contra a Administração da Justiça;
10. `DP-10` — arts. 357 e 359: exploração de prestígio e desobediência a decisão judicial sobre perda/suspensão de direito.

Nenhuma linha pode desaparecer na redação. Agrupamentos pedagógicos são permitidos se a rastreabilidade continuar explícita no QA.

## Engenharia didática obrigatória

Para Direito Penal, seguir a família jurídica do `APOSTILA_AUTHORING_PROTOCOL.md`:

```text
regra/fonte normativa
→ elementos/requisitos
→ hipótese de incidência
→ consequência
→ exceção
→ contraste com tipo próximo
→ caso aplicado
→ síntese
```

A evidência histórica do Gate 3 exige atenção especial a tipos vizinhos, sujeito ativo, objeto material, elemento subjetivo/finalidade, modalidade da conduta e consequência jurídica. Converter isso em explicação, quadros comparativos, pares mínimos e mini-casos; não inserir metadiscurso como “a VUNESP cobra”.

## Prática mínima

Respeitar os requisitos `Q-LIT`, `Q-CMP` e `Q-CAS` definidos por linha na matriz. Questões autorais devem usar cinco alternativas plausíveis quando em formato objetivo, separar pergunta/gabarito e explicar o elemento decisivo.

Questões reais ficam no backoffice para calibração; não copiar extensamente conteúdo protegido para a apostila.

## Critério da primeira implementação

A primeira branch de autoria só deve ser considerada pronta para revisão quando:

- DP-01…DP-10 estiverem cobertos ou explicitamente rastreados no draft;
- nenhuma afirmação normativa extrapolar `SRC-B2-CP`/baseline do cutoff;
- os contrastes jurídicos essenciais estiverem explícitos;
- houver exemplos e mini-casos suficientes para ligar regra a aplicação;
- a estrutura funcionar como material de aprendizado e como corpus recuperável pelo NotebookLM;
- `MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md` estiverem coerentes com o estado do draft;
- o próximo QA estiver claramente indicado, sem promover draft a release prematuramente.

## Depois da primeira implementação

Executar QA editorial/normativo e iterar o draft de `direito-penal`. Só após os gates de conteúdo, PDF e NotebookLM o pack pode ser promovido a release final. O resultado desse primeiro pipeline jurídico deve informar apenas ajustes operacionais; não pode alterar silenciosamente o syllabus ou a matriz dos demais packs.

## Gate canônico

Antes de encerrar cada implementação:

```bash
python tools/verify.py
```

Neste runtime, nova tentativa em `2026-09-12` de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` falhou com `Could not resolve host: github.com`. Enquanto essa condição persistir, registrar a impossibilidade conforme DEC-0009; não tratá-la como `PASS`.
