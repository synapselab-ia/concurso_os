# CHANGELOG — Direito Penal — TJSP Escrevente 2025

## `0.1.0-draft.3` — 2026-09-12

Fechamento do QA semântico `DIREITO-006`.

### Corrigido

- Q12 reformulada para testar isoladamente a consequência expressa do art. 311-A, § 2º, sem depender da combinação pedagógica com a majorante funcional do § 3º;
- Q29 reformulada com `atividade privada` suspensa por decisão judicial, eliminando a ambiguidade com o art. 324;
- contraste explícito `art. 324 x art. 359` acrescentado ao corpo e ao quadro geral;
- gabaritos e síntese final sincronizados com as correções.

### QA

- DP-01…DP-10: cobertura `pass`;
- revisão normativa completa: `pass_after_corrections`;
- didática/contrastes: `pass`;
- 30 questões autorais: `pass` — 30/30;
- requisitos Q-LIT/Q-CMP/Q-CAS: `pass`;
- corpus Markdown: `pass_for_markdown`;
- gate determinístico: `not_executed_current_environment` por falha DNS ao resolver `github.com`;
- PDF: não criado;
- NotebookLM: não testado.

O conteúdo está autorizado a avançar à preparação de release candidate, sem promoção automática a release.

## `0.1.0-draft.2` — 2026-09-12

Primeira passagem completa de QA editorial/normativo sobre o `draft.1`.

### Corrigido e aprofundado

- formas do art. 293 e regra de boa-fé/conhecimento posterior;
- hipóteses previdenciárias do art. 297;
- penas e distinções dos arts. 300–301;
- peculato culposo, excesso de exação e corrupção passiva do § 2º;
- arts. 321–325, resistência e aumentos dos arts. 342–344;
- três mini-casos por DP e maior explicitação de tipos vizinhos.

### Resultado intermediário

- QA-1 cobertura: pass;
- QA-2 normativo: pass_after_corrections;
- QA-3 didática: pass;
- QA-4 prática: fail — Q12 exigia revisão e Q29 era ambígua;
- QA-5 corpus Markdown: pass_for_markdown_draft.

A versão permaneceu bloqueada até corrigir Q12 e Q29.

## `0.1.0-draft.1` — 2026-09-12

Primeira implementação de autoria do SubjectPack `direito-penal` após o fechamento dos Gates 1–4 de B2.

### Adicionado

- workspace canônico em `materials/tjsp-escrevente-2025/direito-penal/`;
- `MANIFEST.md` com status `draft` e contrato DP-01…DP-10;
- `SOURCES.md` com edital, `SRC-B2-CP`, baseline `2025-07-29` e evidência empírica da banca;
- `APOSTILA.md` em primeira passagem completa, organizada pelas dez unidades de cobertura;
- quadros comparativos de tipos próximos;
- exemplos e mini-casos autorais;
- bloco de prática objetiva A–E com gabarito comentado separado.

### Limites desta versão

- não era release;
- ainda não havia passado pelo QA editorial/normativo específico do pack;
- não possuía `APOSTILA.pdf`;
- não havia sido submetida a smoke do NotebookLM;
- `METODOLOGIA_NOTEBOOKLM.md` ainda não havia sido criada.