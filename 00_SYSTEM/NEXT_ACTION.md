# NEXT_ACTION

## DIREITO-002 — Fechar o Gate 2 de fontes e versões de Conhecimentos em Direito

O Gate 1 foi concluído: B2 permanece um único bloco estatístico de 30 questões no edital, mas sua entrega editorial foi dividida, sob DEC-0019, em seis SubjectPacks: `direito-penal`, `direito-processual-penal`, `direito-processual-civil`, `direito-constitucional`, `direito-administrativo` e `legislacao-interna`.

**Não iniciar a redação de nenhuma apostila.** O próximo objetivo é tornar cada fonte normativa autorável, versionada e verificável para o corte do edital.

## Evidência canônica

Usar conjuntamente:

- `competitions/tjsp-escrevente-2025/SYLLABUS.md` para o recorte oficial;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_AUTHORING_PLAN.md` para a fronteira editorial;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` para o inventário em andamento;
- `SRC-TJSP-EDITAL-2025-02` como autoridade de escopo;
- `00_SYSTEM/SOURCE_POLICY.md` e DEC-0010/DEC-0011 para autoridade e proveniência.

O cutoff-base registrado para o edital é **2025-07-29**. O próprio edital admite legislação superveniente ou complementar quando relacionada ou indispensável ao tópico, portanto qualquer atualização posterior deve ser analisada e não simplesmente ignorada ou absorvida pela versão atual.

## Gate 2 — Trabalho obrigatório

### 1. Auditar fontes federais

Para cada recorte abaixo, comparar o texto aplicável no cutoff com a compilação oficial atual e identificar alterações posteriores que atinjam artigos exigidos:

- Código Penal;
- Código de Processo Penal;
- Lei n.º 9.099/1995;
- Código de Processo Civil;
- Lei n.º 12.153/2009;
- Constituição Federal;
- Lei n.º 8.429/1992.

Registrar em `DIREITO_SOURCES.md` o resultado por fonte. Não basta apontar a URL atual.

### 2. Reconstruir as fontes estaduais com drift confirmado

A compilação oficial atual já demonstra mudanças posteriores ao cutoff em pelo menos:

- Lei Estadual n.º 10.261/1968;
- LC Estadual n.º 1.111/2010.

Determinar, com histórico legislativo oficial, quais dispositivos do recorte do edital estavam vigentes em 2025-07-29 e quais alterações posteriores atingem esse recorte.

### 3. Fechar fontes internas do TJSP

- confirmar o histórico da Resolução TJSP n.º 850/2021 até o cutoff;
- confirmar a versão da Resolução TJSP n.º 963/2025 em 2025-07-29 e atos posteriores relevantes;
- localizar/validar a versão do Regimento Interno vigente em 2025-07-29;
- localizar/validar o Tomo I das Normas da Corregedoria vigente em 2025-07-29.

### 4. Não resolver a duplicidade do Capítulo XI por inferência

O edital imprime dois recortes sucessivos como `Tomo I — Capítulo XI`. Essa anomalia já está registrada no syllabus e no plano de autoria.

Somente corrigir ou reinterpretar essa referência se uma fonte oficial inequívoca permitir fazê-lo. Caso contrário, manter a ambiguidade documentada e tratá-la explicitamente no planejamento de cobertura.

### 5. Completar proveniência

Para cada fonte fechada, registrar quando aplicável:

- `source_id`;
- autoridade;
- título/diploma;
- recorte;
- URL ou identificação oficial;
- data/versão relevante;
- histórico de alteração necessário;
- data de verificação;
- hash SHA-256 e tamanho quando um arquivo estável tiver sido obtido localmente para auditoria.

Binários-fonte de terceiros não entram no repositório público, conforme DEC-0011.

## Critério de fechamento do Gate 2

Marcar o Gate 2 como `closed` somente quando todos os diplomas e recortes de B2 tiverem versão aplicável definida ou uma ambiguidade oficial explicitamente registrada sem falsa resolução.

A existência de uma página oficial atual **não** equivale a fechar a versão do edital quando houver alteração posterior ao cutoff.

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

Antes de encerrar a próxima implementação:

```bash
python tools/verify.py
```

Se o runtime continuar incapaz de obter um checkout canônico por falha de resolução de `github.com`, registrar a tentativa e a impossibilidade; não tratar como `PASS`, conforme DEC-0009.
