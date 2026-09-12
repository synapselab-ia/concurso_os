# simulations

Este diretório armazena simulados autorais quando eles forem produzidos/aplicados.

## Convenção

```text
simulations/
└── <competition_id>/
    └── <simulation_id>/
        ├── MANIFEST.json
        ├── SIMULADO.md
        ├── GABARITO.md
        └── QA.md
```

- `MANIFEST.json` segue `schemas/simulation.schema.json`;
- `SIMULADO.md` contém somente a prova aplicável ao estudante;
- `GABARITO.md` permanece separado até o encerramento da aplicação;
- `QA.md` registra revisão item a item/conjunto e correções;
- resultados pessoais não são publicados automaticamente no repositório público.

Para TJSP Escrevente 2025, `weekly_full_objective` segue `competitions/tjsp-escrevente-2025/SIMULATION_BLUEPRINT.json`.

Ver `00_SYSTEM/SIMULATION_PROTOCOL.md`.
