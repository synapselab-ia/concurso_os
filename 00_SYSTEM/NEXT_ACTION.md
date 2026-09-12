# NEXT_ACTION

## DIREITO-006 — Executar QA editorial e normativo do draft `direito-penal`

A primeira implementação de `direito-penal` foi criada em `materials/tjsp-escrevente-2025/direito-penal/` como `0.1.0-draft.1`. O workspace contém `APOSTILA.md`, `SOURCES.md`, `MANIFEST.md` e `CHANGELOG.md`; DP-01…DP-10 estão redigidos e há 30 questões autorais A–E com gabarito comentado separado.

**O pack ainda é draft. Não gerar nem publicar `APOSTILA.pdf` como final e não promovê-lo a release antes deste QA.**

## Autoridade e entradas obrigatórias

Ler conjuntamente:

- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` — objeto do QA;
- `materials/tjsp-escrevente-2025/direito-penal/SOURCES.md` — proveniência do pack;
- `materials/tjsp-escrevente-2025/direito-penal/MANIFEST.md` e `CHANGELOG.md` — estado/versionamento;
- `competitions/tjsp-escrevente-2025/SYLLABUS.md` — autoridade de escopo;
- `competitions/tjsp-escrevente-2025/DIREITO_SOURCES.md` — baseline `2025-07-29`;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_COVERAGE_MATRIX.md` — contrato DP-01…DP-10 e requisitos Q-LIT/Q-CMP/Q-CAS;
- `competitions/tjsp-escrevente-2025/DIREITO_B2_BANCA_ANALYSIS.md` — sinais empíricos, sem peso preditivo;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, `SOURCE_POLICY.md` e `QA_PROTOCOL.md`.

Fonte normativa primária: `SRC-B2-CP`, Código Penal oficial no Planalto. O Gate 2 fechou o recorte como `cutoff_closed_no_scoped_drift`; o art. 338-A posterior permanece fora do syllabus.

## QA-1 — cobertura e rastreabilidade

Conferir artigo por artigo o recorte:

`293–305; 307; 308; 311-A; 312–317; 319–333; 336; 337; 339–347; 357; 359`.

Para cada `DP-01`…`DP-10`, verificar que:

- todos os artigos e dispositivos relevantes do intervalo aparecem no ensino ou em remissão inequívoca;
- nenhum artigo fora do recorte é ensinado como conteúdo obrigatório;
- dispositivos intercalares que pertencem ao intervalo, como 313-A/313-B e 319-A, não desaparecem;
- o art. 338-A não é absorvido por proximidade numérica;
- a tabela/ledger de cobertura pode ser promovida de `drafted` para `qa` somente depois da conferência.

## QA-2 — exatidão normativa

Fazer revisão completa contra `SRC-B2-CP`, não apenas amostragem. Conferir especialmente:

- sujeito ativo e vínculo funcional quando exigidos;
- verbos nucleares;
- objeto material;
- finalidade específica;
- penas e frações de aumento/diminuição quando o draft as informa;
- formas equiparadas, qualificadas, privilegiadas e subsidiárias mencionadas;
- condições temporais, como conhecimento posterior, reparação, retratação e momento processual;
- diferenças entre documento público/particular, falsidade material/ideológica e tipos funcionais próximos.

Não introduzir jurisprudência para corrigir ou ampliar silenciosamente a letra do recorte. Se uma observação jurisprudencial se mostrar pedagogicamente indispensável, ela exige decisão editorial e fonte própria, não inferência automática.

## QA-3 — didática e distinções

Revisar se cada unidade segue de forma suficiente:

```text
regra
→ elementos
→ hipótese
→ consequência
→ contraste
→ caso aplicado
→ síntese
```

Dar prioridade aos contrastes empiricamente sustentados no Gate 3: tipo vizinho, requisito, sujeito, objeto, modalidade/finalidade e consequência. Remover explicações vagas, atalhos que criem falsa regra e redundância que prejudique recuperação semântica.

## QA-4 — prática autoral

Revisar as 30 questões uma a uma. Cada item deve ter:

- exatamente uma resposta defensável dentro do conteúdo/fonte;
- cinco alternativas plausíveis;
- nenhuma ambiguidade involuntária;
- nenhum conteúdo fora do syllabus como requisito para resolver;
- gabarito coerente com o comentário;
- comentário que exponha o elemento decisivo, não apenas repita a alternativa.

Conferir também os mínimos `Q-LIT`, `Q-CMP` e `Q-CAS` por linha DP da matriz. Se o conjunto atual não testar suficientemente um requisito da linha, adicionar ou substituir prática; não aumentar volume mecanicamente.

## QA-5 — utilidade como corpus

Verificar títulos, hierarquia, consistência terminológica, proximidade entre regra/contraste/exemplo e legibilidade das tabelas. O texto deve funcionar sem depender de contexto do projeto e sem metadiscurso da banca.

Não fazer smoke do NotebookLM enquanto o conteúdo ainda tiver correções materiais abertas. Primeiro estabilizar o Markdown.

## Artefato esperado

Criar:

`materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md`

O arquivo deve registrar, no mínimo:

- resultado separado de QA-1 a QA-5;
- correções executadas e sua motivação;
- pendências reais;
- estado das 30 questões;
- decisão explícita sobre prontidão para release candidate.

Se qualquer gate semântico falhar, manter o pack como `draft` e atualizar `APOSTILA.md`; não maquiar falha como PASS.

## Critério de saída

`DIREITO-006` só fecha quando:

- DP-01…DP-10 estiverem integralmente rastreados;
- a revisão normativa completa do recorte tiver sido realizada contra a fonte oficial;
- os contrastes essenciais estiverem corretos e explícitos;
- todas as 30 questões tiverem sido revisadas semanticamente;
- `MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md` refletirem o estado real;
- `APOSTILA_QA_0.1.0.md` registrar os resultados sem promover gates não executados.

Se o draft ficar aprovado nesses gates, o próximo passo será preparar um release candidate do pack, incluindo a metodologia/configuração de tutor aplicável e o pipeline de PDF/NotebookLM previsto pelo protocolo. Isso ainda não equivale automaticamente a release final.

## Gate canônico

Antes de encerrar a implementação:

```bash
python tools/verify.py
```

Em `2026-09-12`, nova tentativa de `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` neste runtime falhou com `Could not resolve host: github.com`. Enquanto essa condição persistir, registrar a impossibilidade conforme DEC-0009; não tratá-la como `PASS`.