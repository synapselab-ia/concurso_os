# question_banks

Este diretório armazena **questões autorais reutilizáveis** quando a persistência melhora QA, rastreabilidade ou composição de simulados.

Não é um objetivo do projeto pré-gerar um banco gigantesco. O banco cresce por necessidade concreta.

## Convenção

```text
question_banks/
└── <competition_id>/
    └── <subject_id>/
        └── batches/
            └── <batch_id>.json
```

Cada lote deve usar itens compatíveis com `schemas/question_item.schema.json`.

## Modos

- `microdrill` — aquisição/recuperação rápida; não exige fidelidade integral à banca;
- `simulation` — transferência; exige aderência ao blueprint e QA de estilo/semântica.

## Regras

- autoria original;
- syllabus e fontes vigentes controlam conteúdo;
- provas históricas calibram forma e distratores, não são copiadas extensamente;
- `simulation` só entra em prova depois de QA item a item;
- itens rejeitados permanecem identificáveis ou são removidos do lote antes da promoção, sem fingir que passaram;
- um lote de geração não equivale automaticamente a um lote aprovado.

Ver `00_SYSTEM/PRACTICE_PROTOCOL.md` e `00_SYSTEM/SIMULATION_PROTOCOL.md`.
