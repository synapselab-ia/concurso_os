# DATA_MODEL

## Participant

Perfil público mínimo. IDs estáveis (`p001`, `p002`, ...). Não armazenar CPF, telefone, endereço, saúde, credenciais ou qualquer dado sem necessidade pedagógica explícita.

## Competition

Define identidade do concurso, versão/edital, banca, blocos, regras eliminatórias e referências de fonte. Não contém desempenho de participante.

## Enrollment

Vínculo entre `participant_id` e `competition_id`. Guarda configuração do ciclo de preparação e aponta para os eventos daquele vínculo.

## Competency

Unidade de desempenho observável. O objeto principal do domínio não é a questão, mas a competência que uma questão ajuda a medir.

## EvidenceEvent

Registro append-only. Campos mínimos canônicos:

- `schema_version`
- `event_id`
- `event_type`
- `occurred_at`
- `participant_id`
- `competition_id`
- `enrollment_id`
- `competency_ids`
- `payload`
- `provenance`

## DerivedState

Qualquer estado de domínio, retenção, calibração, risco ou prioridade deve ser derivável dos eventos. Arquivos de estado derivado não substituem a história.

## IDs

IDs não devem depender de nomes mutáveis. Participantes usam `pNNN`; concursos usam slug versionado; competências usam namespace estável de conhecimento.
