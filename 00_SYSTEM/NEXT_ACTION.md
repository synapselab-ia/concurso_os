# NEXT_ACTION

## DIREITO-014: Preparar novo release candidate de `direito-processual-penal`

`DIREITO-013` corrige o defeito normativo identificado no art. 371 do CPP e retorna o pack para `0.1.0-draft.3`.

## Estado canônico esperado após merge de DIREITO-013

- pack: `direito-processual-penal`;
- versão corrente: `0.1.0-draft.3`;
- fonte Markdown corrigida: Git blob `135592d9762b8f639a199ebe795ffcca71e747bd`;
- DPP-05 / CPP 370-372: `PASS_AFTER_CORRECTION`;
- demais coverage rows: estado anterior preservado;
- prática: 60 questões, sem alteração pela correção;
- baseline: `2025-07-29`;
- CPP art. 584, § 4º, de 2026: continua fora do baseline;
- PDF de `0.1.0-rc.1`: identidade binária historicamente comprovada, mas `INVALIDATED_SEMANTICALLY` e removido do caminho canônico;
- smoke real já observado no RC antigo: `PASS_BEHAVIORAL_ON_RC1_CORPUS_INVALIDATED`;
- novo PDF: ainda não criado.

## Objetivo de DIREITO-014

Promover somente a identidade do conteúdo corrigido para um novo RC, preferencialmente `0.1.0-rc.2`, sem nova alteração jurídica.

### Trabalho obrigatório

1. Revalidar o estado real de `main` e PRs abertas.
2. Confirmar que o `APOSTILA.md` contém a redação correta dos arts. 371-372 e que a formulação defeituosa não reapareceu.
3. Promover metadados de versão/status de `APOSTILA.md`, `SOURCES.md`, `MANIFEST.md`, `METODOLOGIA_NOTEBOOKLM.md` e `CHANGELOG.md` para o novo RC.
4. Não modificar o corpo jurídico, prática ou gabarito nessa promoção.
5. Registrar a identidade congelada do Markdown corrigido.
6. Executar QA estático do corpus/tutor e revisar diff.
7. Executar `python tools/verify.py` ou documentar explicitamente a impossibilidade real.
8. Abrir PR e mesclar sob DEC-0009 se a revisão estiver limpa.

## Gate seguinte

Após `DIREITO-014`, gerar novo `APOSTILA.pdf` exclusivamente do RC corrigido, repetir readback textual e inspeção visual, provar identidade binária e só então recolocar o PDF no caminho canônico.

Depois do novo PDF, executar apenas um smoke curto de regressão no NotebookLM para confirmar:

- carregamento do PDF corrigido;
- resposta correta sobre art. 371/372;
- treino sem vazamento de gabarito;
- ausência de IDs/metadados internos.

Não reutilizar o PDF de `0.1.0-rc.1`.
