# CHANGELOG - Direito Processual Penal - TJSP Escrevente 2025

## `0.1.0-draft.1` - 2026-09-14

Primeira implementação completa do SubjectPack `direito-processual-penal` sob `DIREITO-008`.

### Adicionado

- workspace canônico em `materials/tjsp-escrevente-2025/direito-processual-penal/`;
- `MANIFEST.md` com status de draft, recorte oficial e rastreabilidade `DPP-01...DPP-25` mantida no backoffice;
- `SOURCES.md` com edital, `SRC-B2-CPP`, `SRC-B2-L9099`, baseline `2025-07-29` e controle explícito do drift posterior do CPP art. 584, § 4º;
- `APOSTILA.md` em primeira passagem completa;
- fluxos de citação, intimação, procedimento comum, Tribunal do Júri, procedimento sumário, recursos, habeas corpus e JECrim;
- quadros de contraste entre institutos próximos;
- mini-casos autorais;
- prática objetiva A-E com gabarito comentado separado.

### Engenharia de corpus

As lições do smoke de Direito Penal foram aplicadas desde a primeira autoria:

- nenhum `DPP-*` foi usado em título ou subtítulo estudável;
- coverage IDs e rótulos de gate permanecem no `MANIFEST` e na matriz, fora do StudentContent;
- a redação evita tratar ausência de conteúdo externo na lei como prova de inexistência externa;
- a futura configuração do tutor e o smoke final deverão testar explicitamente disciplina epistemológica e vazamento de metadados.

### Versão normativa

- baseline do pack: `2025-07-29`;
- CPP oficial e Lei n.º 9.099/1995 oficial foram reabertos durante a autoria em `2026-09-14`;
- o art. 584, § 4º, do CPP, incluído pela Lei n.º 15.358/2026, foi mantido fora da apostila por ser posterior ao cutoff;
- a Lei n.º 9.099/1995 permanece `cutoff_closed_no_scoped_drift` no inventário canônico.

### Estado de QA

- implementação das 25 coverage rows: `complete_first_pass_pending_semantic_qa`;
- fontes e baseline: `recorded`;
- contrastes e fluxos: `implemented_pending_qa`;
- prática autoral: `implemented_pending_qa`;
- cobertura IDs em títulos estudáveis: `selfcheck_pass`;
- QA semântico/normativo específico: `not_started`;
- PDF: `not_created_by_design`;
- NotebookLM: `not_started`;
- `python tools/verify.py`: `not_executed_current_environment`, pois o runtime continua sem resolução DNS de `github.com` para checkout canônico; a impossibilidade não é tratada como PASS.

### Limites desta versão

Este draft não está aprovado como release nem como release candidate. A próxima etapa deve revisar integralmente conteúdo e questões contra as fontes primárias e a matriz, corrigir eventuais ambiguidades, registrar QA e somente depois considerar PDF ou NotebookLM.
