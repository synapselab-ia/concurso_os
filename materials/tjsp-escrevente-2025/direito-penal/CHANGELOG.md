# CHANGELOG - Direito Penal - TJSP Escrevente 2025

## `0.1.0-rc.1` - 2026-09-12

Preparação de release candidate sob `DIREITO-007`, sem promoção a release final.

### Adicionado

- `METODOLOGIA_NOTEBOOKLM.md` específica de Direito Penal, destinada à configuração nativa da conversa e não ao corpus estudável;
- regras de tutoria para distinguir texto legal, explicação didática e aplicação hipotética, sem inventar jurisprudência ou doutrina ausente da fonte.

### Sincronizado

- `APOSTILA.md` promovida para identidade `0.1.0-rc.1`, mantendo congelado o conteúdo editorial/normativo aprovado no `0.1.0-draft.3`;
- `MANIFEST.md`, `SOURCES.md` e registro de QA alinhados ao estado real do candidato.

### QA executado

- QA estático de utilidade do corpus no NotebookLM: `pass_static`;
- primeiro candidato local de `APOSTILA.pdf`: `18` páginas, `48.593` bytes, SHA-256 `d190a2a73b6e6ad84d60d2a241ca8574ac4f34a75cfba1d8f643dbf95f9ea469`;
- candidato preferido regenerado do Markdown congelado: `17` páginas A4, `30.167` bytes, PDF 1.4, SHA-256 `42b1aae4b5614a2e381373ecbae8a766090cee68a035ec8749208f4879687394`, Git blob local esperado `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`;
- readback textual confirmou títulos, unidades, gabarito, artigos e caracteres jurídicos relevantes;
- todas as 17 páginas do candidato preferido foram renderizadas e inspecionadas sem clipping, sobreposição, glifos quebrados ou mistura acidental entre questões e gabarito;
- o gate determinístico permaneceu `not_executed_current_environment`: `git ls-remote` continua falhando com `Could not resolve host: github.com`.

### Publicação do PDF - 2026-09-14

- o candidato preferido foi enviado manualmente à branch `upload/direito-penal-apostila-pdf`;
- caminho publicado: `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf`;
- Git blob remoto observado: `5bf149e5a5d23c3b9ee08c7c3716431dd8aa210e`;
- o blob remoto coincide exatamente com o Git blob do candidato local integralmente auditado;
- commit de upload/rename observado: `fd7f0f78b16f85d06979ab1e6cc86762c1bd1d00`;
- QA-9 foi fechado por identidade binária exata;
- readback textual e renderização visual de `17/17` páginas foram novamente executados em `2026-09-14` sobre o binário local de identidade idêntica e permaneceram `PASS`.

### Bloqueios mantidos

- smoke real do NotebookLM: `pending_user_smoke`;
- `python tools/verify.py`: não executado por impossibilidade de obter checkout canônico neste runtime; nova tentativa de resolução de `github.com` em `2026-09-14` continuou falhando.

Nenhuma alteração semântica de Direito Penal foi introduzida no `rc.1`.

## `0.1.0-draft.3` - 2026-09-12

Fechamento do QA semântico `DIREITO-006`.

### Corrigido

- Q12 reformulada para testar isoladamente a consequência expressa do art. 311-A, § 2º, sem depender da combinação pedagógica com a majorante funcional do § 3º;
- Q29 reformulada com `atividade privada` suspensa por decisão judicial, eliminando a ambiguidade com o art. 324;
- contraste explícito `art. 324 x art. 359` acrescentado ao corpo e ao quadro geral;
- gabaritos e síntese final sincronizados com as correções.

### QA

- DP-01...DP-10: cobertura `pass`;
- revisão normativa completa: `pass_after_corrections`;
- didática/contrastes: `pass`;
- 30 questões autorais: `pass` - 30/30;
- requisitos Q-LIT/Q-CMP/Q-CAS: `pass`;
- corpus Markdown: `pass_for_markdown`;
- gate determinístico: `not_executed_current_environment` por falha DNS ao resolver `github.com`;
- PDF: não criado nessa versão;
- NotebookLM: não testado.

O conteúdo está autorizado a avançar à preparação de release candidate, sem promoção automática a release.

## `0.1.0-draft.2` - 2026-09-12

Primeira passagem completa de QA editorial/normativo sobre o `draft.1`.

### Corrigido e aprofundado

- formas do art. 293 e regra de boa-fé/conhecimento posterior;
- hipóteses previdenciárias do art. 297;
- penas e distinções dos arts. 300-301;
- peculato culposo, excesso de exação e corrupção passiva do § 2º;
- arts. 321-325, resistência e aumentos dos arts. 342-344;
- três mini-casos por DP e maior explicitação de tipos vizinhos.

### Resultado intermediário

- QA-1 cobertura: pass;
- QA-2 normativo: pass_after_corrections;
- QA-3 didática: pass;
- QA-4 prática: fail - Q12 exigia revisão e Q29 era ambígua;
- QA-5 corpus Markdown: pass_for_markdown_draft.

A versão permaneceu bloqueada até corrigir Q12 e Q29.

## `0.1.0-draft.1` - 2026-09-12

Primeira implementação de autoria do SubjectPack `direito-penal` após o fechamento dos Gates 1-4 de B2.

### Adicionado

- workspace canônico em `materials/tjsp-escrevente-2025/direito-penal/`;
- `MANIFEST.md` com status `draft` e contrato DP-01...DP-10;
- `SOURCES.md` com edital, `SRC-B2-CP`, baseline `2025-07-29` e evidência empírica da banca;
- `APOSTILA.md` em primeira passagem completa, organizada pelas dez unidades de cobertura;
- quadros comparativos de tipos próximos;
- exemplos e mini-casos autorais;
- bloco de prática objetiva A-E com gabarito comentado separado.

### Limites desta versão

- não era release;
- ainda não havia passado pelo QA editorial/normativo específico do pack;
- não possuía `APOSTILA.pdf`;
- não havia sido submetida a smoke do NotebookLM;
- `METODOLOGIA_NOTEBOOKLM.md` ainda não havia sido criada.