# ARCHITECTURE

## Entidades centrais

`Participant -> Enrollment -> Competition`

`KnowledgeUnit -> Competency -> EvidenceEvent -> DerivedState -> Scheduler`

## Separações obrigatórias

- **Participant:** pessoa que estuda.
- **Competition:** concurso/edital/banca e sua configuração de avaliação.
- **Enrollment:** vínculo de um participante com um concurso em um período específico.
- **KnowledgeUnit:** unidade reutilizável de conhecimento, independente de concurso quando possível.
- **Competency:** desempenho observável esperado sobre uma unidade.
- **EvidenceEvent:** observação histórica imutável de estudo/avaliação.
- **DerivedState:** inferência reconstruível a partir dos eventos.

## Direção dos dados

```text
fontes -> conhecimento/competências -> adapter do concurso
                                  \
participante -> enrollment -> evidence events -> derived state -> scheduler
```

## Persistência

Eventos são a verdade histórica. Matrizes, pontuações e filas de revisão são projeções derivadas e podem ser regeneradas quando o modelo mudar.

## Portabilidade

O kernel não pode conter condicionais específicas por pessoa, como `if participant == "lucas"`. Adapters de concurso também não devem conter estado individual.

## Infraestrutura

V0.1 usa Git + Markdown + JSON/JSONL + Python padrão. Dependências e serviços externos só entram quando houver benefício demonstrável.
