# CHANGELOG — Direito Penal — TJSP Escrevente 2025

## `0.1.0-rc.1` — 2026-09-12

Preparação de release candidate sob `DIREITO-007`, sem promoção a release final.

### Adicionado

- `METODOLOGIA_NOTEBOOKLM.md` específica de Direito Penal, destinada à configuração nativa da conversa e não ao corpus estudável;
- regras de tutoria para distinguir texto legal, explicação didática e aplicação hipotética, sem inventar jurisprudência ou doutrina ausente da fonte.

### Sincronizado

- `APOSTILA.md` promovida para identidade `0.1.0-rc.1`, mantendo congelado o conteúdo editorial/normativo aprovado no `0.1.0-draft.3`;
- `MANIFEST.md`, `SOURCES.md` e registro de QA alinhados ao estado real do candidato.

### QA executado

- QA estático de utilidade do corpus no NotebookLM: `pass_static`;
- candidato local de `APOSTILA.pdf` gerado a partir do Markdown congelado, pesquisável e em A4;
- candidato local de PDF: `18` páginas, `48.593` bytes, SHA-256 `d190a2a73b6e6ad84d60d2a241ca8574ac4f34a75cfba1d8f643dbf95f9ea469`;
- readback textual confirmou títulos, unidades, gabarito, artigos e caracteres jurídicos relevantes;
- todas as 18 páginas foram renderizadas e inspecionadas sem clipping, sobreposição, glifos quebrados ou mistura acidental entre questões e gabarito;
- o gate determinístico permaneceu `not_executed_current_environment`: `git ls-remote` continua falhando com `Could not resolve host: github.com`.

### Bloqueios mantidos

- `APOSTILA.pdf` ainda não está publicado no GitHub. O conector disponível neste runtime não oferece caminho confiável para gravar o artefato binário local como arquivo canônico; o PDF local auditado não é tratado como binário versionado;
- smoke real do NotebookLM: `pending_user_smoke`;
- `python tools/verify.py`: não executado por impossibilidade de obter checkout canônico neste runtime.

Nenhuma alteração semântica de Direito Penal foi introduzida no `rc.1`.

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