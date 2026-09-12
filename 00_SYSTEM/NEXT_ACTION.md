# NEXT_ACTION

## DIREITO-002B — Fechar fontes estaduais e internas do TJSP no Gate 2

O subgate federal de fontes/versões foi concluído em `2026-09-11`. O Gate 2 global continua aberto apenas porque as fontes estaduais e internas do TJSP ainda precisam ser reconciliadas com o cutoff do edital de **2025-07-29**.

**Não iniciar a redação de nenhuma apostila.** Gates 3 e 4 também continuam bloqueados pela ordem canônica de autoria.

## Evidência canônica

Usar conjuntamente:

- `competitions/tjsp-escrevente-2025/SYLLABUS.md` para o recorte oficial;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md` para a fronteira editorial;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` para o inventário e o audit trail de versão;
- `SRC-TJSP-EDITAL-2025-02` como autoridade de escopo;
- fontes oficiais ALESP/TJSP para legislação estadual e interna;
- `00_SYSTEM/SOURCE_POLICY.md` e DEC-0010/DEC-0011 para autoridade, proveniência e política de binários.

## Estado federal já fechado

Não repetir a auditoria federal sem evidência nova. O inventário registra:

- Código Penal — sem drift textual pós-cutoff dentro do recorte;
- CPP — drift pós-cutoff no art. 584, § 4º, pela Lei n.º 15.358/2026;
- Lei n.º 9.099/1995 — sem drift textual direto identificado;
- CPC — drift nos arts. 196, 529-A e 998 por Leis n.º 15.479/2026 e 15.484/2026, com controle de vigência;
- Lei n.º 12.153/2009 — sem drift textual direto identificado;
- Constituição — drift no art. 37, XVI, `b`, pela EC n.º 138/2025;
- Lei n.º 8.429/1992 — sem alteração efetiva pós-cutoff; o art. 18 da Lei n.º 15.269/2025 foi vetado.

A versão-base autoral permanece a vigente em `2025-07-29`; alterações posteriores ficam rastreadas separadamente.

## Trabalho obrigatório agora

### 1. Lei Estadual n.º 10.261/1968

Recorte: arts. `1–86`, `171–175`, `239–323`.

A compilação ALESP atual contém alterações posteriores ao cutoff. Reconstruir com histórico oficial:

- quais dispositivos do recorte estavam vigentes em `2025-07-29`;
- quais leis posteriores alteraram dispositivos efetivamente cobrados;
- data de eficácia quando diferente da publicação;
- baseline autoral e drift posterior, sem misturá-los.

### 2. LC Estadual n.º 1.111/2010

O edital cobra o diploma integral. A compilação ALESP atual contém alteração posterior ao cutoff.

Fechar:

- texto aplicável em `2025-07-29`;
- atos alteradores posteriores;
- dispositivos atingidos;
- vigência/efeitos quando relevante.

### 3. Resolução TJSP n.º 850/2021

A fonte oficial hoje indica compilação anterior ao cutoff e está marcada como `candidate_closed`.

Confirmar, pela própria base legislativa do TJSP ou histórico oficial equivalente:

- que não houve alteração entre a última compilação registrada e `2025-07-29`;
- se houve ato posterior relevante até `2026-09-11`;
- qual identificação oficial será usada como versão-base.

### 4. Resolução TJSP n.º 963/2025

A resolução é anterior ao cutoff e está marcada como `candidate_closed`.

Confirmar:

- texto vigente em `2025-07-29`;
- atos alteradores/complementares posteriores;
- se alguma norma superveniente é indispensável ao tópico eproc na forma prevista pelo edital.

### 5. Regimento Interno do TJSP

O PDF oficial atual já é posterior ao cutoff.

Localizar ou reconstruir, com atos oficiais:

- a versão vigente em `2025-07-29`;
- alterações posteriores até a data de verificação;
- regra segura para produzir a futura apostila sem ensinar texto de 2026 como se fosse o texto-base do edital.

### 6. NSCGJ — Tomo I

O Tomo I oficial atual também é posterior ao cutoff. Usar apenas os recortes impressos no edital e reconstruir a versão aplicável em `2025-07-29`.

Recortes canônicos:

1. Capítulo II — Seção I — subseções I e II;
2. Capítulo III — Seções I, II, V, VI e VII;
3. Capítulo III — Seção VIII — subseções I, II e III;
4. Capítulo III — Seções IX a XIX;
5. Capítulo XI — Seções I, IV e V;
6. Capítulo XI — Seções I a VII.

O edital repete **Capítulo XI** nos itens 5 e 6. Não corrigir por plausibilidade. Somente resolver se fonte oficial inequívoca demonstrar que há erro material e qual é a referência correta; do contrário, encerrar o Gate 2 com a ambiguidade explicitamente documentada.

## Proveniência mínima

Para cada fonte fechada, registrar em `DIREITO_SOURCES.md`, quando aplicável:

- `source_id`;
- autoridade;
- diploma/ato;
- recorte;
- URL ou identificador oficial;
- cutoff/version date;
- atos alteradores relevantes;
- vigência/efeitos;
- data de verificação;
- hash SHA-256 e tamanho de arquivo estável quando obtido para auditoria local.

Não publicar binários-fonte de terceiros no repositório público, conforme DEC-0011.

## Critério de fechamento do Gate 2

Marcar B2 Gate 2 como `closed` somente quando:

- as sete fontes federais permanecerem fechadas;
- Lei 10.261/1968 e LC 1.111/2010 tiverem baseline do cutoff reconstruído;
- Resoluções 850/2021 e 963/2025 tiverem histórico confirmado;
- Regimento Interno e NSCGJ tiverem versão-base validada ou reconstruída;
- a duplicidade do Capítulo XI estiver resolvida por fonte oficial **ou** registrada como ambiguidade oficial não resolvida;
- nenhuma fonte atual posterior ao cutoff tiver sido usada silenciosamente como baseline.

## Depois do Gate 2 — DIREITO-003

Só então iniciar o Gate 3: classificar de forma reproduzível as questões de Direito das provas de 2021, 2023, 2024 e 2025, preservando o edital como autoridade de escopo.

A análise deverá registrar, por questão, ao menos:

- domínio;
- fonte/dispositivo ou instituto principal;
- operação cognitiva;
- literalidade versus aplicação;
- tipo de distractor/armadilha;
- distinção jurídica relevante.

A frequência histórica servirá à engenharia silenciosa da apostila e não poderá alterar o conteúdo programático vigente.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

Neste runtime, a tentativa de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` em `2026-09-11` ainda falhou com `Could not resolve host: github.com`. Se a condição persistir, registrar a impossibilidade; não tratá-la como `PASS`, conforme DEC-0009.
