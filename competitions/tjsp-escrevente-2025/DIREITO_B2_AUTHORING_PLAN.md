# DIREITO B2 — Plano canônico de autoria

**Competition:** `tjsp-escrevente-2025`  
**Syllabus block:** `B2 — Conhecimentos em Direito`  
**Authority:** `SRC-TJSP-EDITAL-2025-02`  
**Status:** Gates 1 e 2 fechados; Gate 3 pendente  

## Objetivo

Transformar o bloco B2 do edital em unidades de autoria, fonte e QA que possam ser mantidas sem perder a unidade estatística da prova.

O edital continua tratando **Conhecimentos em Direito como um único bloco de 30 questões**. A divisão abaixo é exclusivamente editorial e pedagógica; não altera o blueprint do concurso nem autoriza inferir distribuição fixa de questões entre os subdomínios.

## Decisão de fronteira

B2 será entregue como **seis SubjectPacks**, um para cada domínio explicitamente separado no edital:

1. `direito-penal`;
2. `direito-processual-penal`;
3. `direito-processual-civil`;
4. `direito-constitucional`;
5. `direito-administrativo`;
6. `legislacao-interna`.

A decisão é registrada em `00_SYSTEM/DECISION_LOG.md` como DEC-0019.

## Razões

### 1. Escopo normativo

Um único PDF de Direito teria de reunir, entre outros, grandes recortes do CPP e do CPC, legislação federal e estadual, Constituição, Regimento Interno, resoluções do TJSP e Normas da Corregedoria. A unidade resultante seria excessivamente grande para leitura, revisão dirigida e manutenção normativa.

### 2. Coerência pedagógica

Os seis domínios já aparecem separados no edital e possuem vocabulário, institutos, relações conceituais e tipos de erro próprios. O protocolo de autoria permite estruturas específicas por domínio sem exigir que todo B2 use um único encadeamento didático.

### 3. Manutenção e versionamento

Normas internas do TJSP, legislação estadual e códigos federais têm ciclos de alteração diferentes. Packs separados permitem revisar uma fonte sem republicar toda a disciplina jurídica.

### 4. NotebookLM

A unidade recomendada de estudo é a matéria. Separar os domínios reduz ruído de recuperação, facilita Testes/Cartões/Mapas mentais temáticos e evita um corpus jurídico monolítico.

### 5. Fontes compartilhadas

A divisão não duplica binários. Fontes comuns são referenciadas por proveniência. Exemplo: a Lei n.º 9.099/1995 aparece em `direito-processual-penal` nos arts. 60 a 83, 88 e 89 e em `direito-processual-civil` nos arts. 3º a 19.

## Escopo canônico por pack

### `direito-penal`

Código Penal: arts. 293 a 305; 307; 308; 311-A; 312 a 317; 319 a 333; 336 e 337; 339 a 347; 357 e 359.

### `direito-processual-penal`

Código de Processo Penal: arts. 251 a 258; 261 a 267; 274; 351 a 372; 394 a 497; 531 a 538; 541 a 548; 574 a 667.  
Lei n.º 9.099/1995: arts. 60 a 83; 88 e 89.

### `direito-processual-civil`

Código de Processo Civil: arts. 144 a 155; 188 a 275; 294 a 311; 318 a 538; 994 a 1026.  
Lei n.º 9.099/1995: arts. 3º a 19.  
Lei n.º 12.153/2009: integral, porque o edital não restringe artigos.

### `direito-constitucional`

Constituição Federal: Título II, Capítulos I, II e III; Título III, Capítulo VII, Seções I e II; art. 92.

### `direito-administrativo`

Lei Estadual n.º 10.261/1968: arts. 1º a 86; 171 a 175; 239 a 323.  
Lei Federal n.º 8.429/1992: integral, porque o edital não restringe artigos.

### `legislacao-interna`

- Resolução TJSP n.º 850/2021;
- Resolução TJSP n.º 963/2025;
- Lei Complementar Estadual n.º 1.111/2010;
- Regimento Interno do TJSP;
- Normas da Corregedoria Geral da Justiça, exatamente nos recortes impressos no edital:
  - Tomo I — Capítulo II — Seção I — subseções I e II;
  - Tomo I — Capítulo III — Seções I, II, V, VI e VII;
  - Tomo I — Capítulo III — Seção VIII — subseções I, II e III;
  - Tomo I — Capítulo III — Seções IX a XIX;
  - Tomo I — Capítulo XI — Seções I, IV e V;
  - Tomo I — Capítulo XI — Seções I a VII.

### Anomalia textual do edital

O último par de recortes das Normas da Corregedoria referencia o **Capítulo XI duas vezes**. O repositório preserva essa literalidade porque não foi localizada fonte oficial inequívoca que autorize corrigir o segundo apontamento. Para cobertura, a segunda linha literal (`Seções I a VII`) engloba as seções I, IV e V da primeira; essa relação de inclusão não altera a referência oficial.

## Gate 2 — versão normativa fechada

`competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` fecha a versão-base de todas as fontes em `2025-07-29` e separa drift posterior.

Pontos de manutenção que não podem ser perdidos na autoria:

- CPP: art. 584, § 4º sofreu alteração posterior pela Lei n.º 15.358/2026;
- CPC: alterações posteriores em arts. 196, 529-A e 998, com vigências distintas;
- Constituição: EC n.º 138/2025 alterou art. 37, XVI, `b` após o cutoff;
- Lei Estadual n.º 10.261/1968: Lei n.º 18.473/2026 atingiu o art. 78 dentro do recorte;
- LC Estadual n.º 1.111/2010: Lei n.º 18.373/2025 e LC n.º 1.441/2026 são posteriores ao cutoff;
- Regimento Interno: baseline inclui Assento n.º 591/2025 e exclui 592–596;
- NSCGJ: baseline dos recortes literais exclui, entre outras alterações posteriores identificadas, Provimentos CG n.º 30/2025 e 04/2026 no Capítulo XI.

A cláusula do edital sobre legislação superveniente/complementar continua válida. Fechar o Gate 2 significa controlar a versão e o drift, não afirmar que toda norma posterior deve ser ignorada.

## Ordem de produção

A ordem abaixo é operacional, não estatística:

1. **concluído** — inventário e versão de todas as fontes de B2;
2. concluir análise histórica reproduzível de 2021/2023/2024/2025;
3. construir a matriz de cobertura dos seis packs;
4. iniciar autoria por `direito-penal`, o menor recorte normativo independente e um bom primeiro teste do pipeline jurídico;
5. seguir para `direito-processual-penal`;
6. `direito-processual-civil`;
7. `direito-constitucional`;
8. `direito-administrativo`;
9. `legislacao-interna`.

A sequência pode ser alterada por decisão canônica posterior, mas nenhum pack pode começar redação substancial antes dos gates comuns de fonte, análise e cobertura.

## Gates

| Gate | Estado | Critério |
|---|---|---|
| 1 — fronteira | `closed` | seis SubjectPacks definidos e decisão registrada |
| 2 — fontes/versões | `closed` | inventário oficial, cutoff, proveniência e drift normativo fechados em `DIREITO_SOURCES.md` |
| 3 — banca | `pending` | questões de Direito de 2021/2023/2024/2025 classificadas de forma reproduzível |
| 4 — matriz | `pending` | todos os recortes do syllabus mapeados sem lacunas |
| 5 — autorização de redação | `blocked` | depende dos Gates 1–4 |

## Regra de autoridade

O edital vigente determina escopo e prevalece sobre provas históricas. Provas históricas servem apenas para calibrar profundidade, operação cognitiva, distinções, armadilhas e prática, conforme DEC-0010 e `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`.
