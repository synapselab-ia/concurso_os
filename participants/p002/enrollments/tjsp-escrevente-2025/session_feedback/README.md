# Feedback de estudo do participante p002

Este diretório pertence **exclusivamente ao enrollment `p002__tjsp-escrevente-2025`** (`participants/p002`, alias público `duda`). O histórico de `p001` pertence a outro participante e **não pode** ser utilizado como desempenho da Duda.

## Finalidade e escopo

Guardar reviews estruturados das sessões adaptativas do ChatGPT, sem depender da memória de chats. O método de treinamento do projeto exige:

- **A cada 10 questões principais válidas e respondidas:** review do bloco e persistência de métricas observadas.
- **A cada 20 questões principais:** revisão ativa com 3 perguntas rápidas, 3 flashcards, 1 questão sobre erro, 1 sobre acerto instável e 1 comparação entre institutos confundidos, quando houver evidência para isso. Esses itens não entram automaticamente na contagem das 10 questões principais.
- **Ao encerrar a sessão:** placar final, pontos fracos, dúvidas, flashcards e plano da próxima sessão, conforme a metodologia do projeto.
- **Na retomada:** consultar os arquivos deste enrollment e dar continuidade aos retestes sem presumir histórico não registrado.

Este repositório não contém, nesta criação, resultados de questões da Duda. Arquivo ausente significa **não persistido**, e não significa que a pessoa nunca tenha estudado.

## Convenção de arquivos

Um registro JSON por sessão/bloco ou relatório final, usando data de registro e IDs estáveis:

```text
session_feedback/
  README.md
  YYYY-MM-DD__<session_slug>__b01-q01-q10.json
  YYYY-MM-DD__<session_slug>__b02-q11-q20.json
  YYYY-MM-DD__<session_slug>__active-review-q01-q20.json
  YYYY-MM-DD__<session_slug>__session-summary.json
```

Os nomes acima são **padrões**, não registros reais. O `session_slug` deve ser exclusivo e não identificável, por exemplo `chatgpt-YYYYMMDD-01`; em retomadas da mesma sessão, preservar seu `session_id`. `block_id` identifica o bloco dentro da sessão; `feedback_id` combina participante, concurso, sessão, tipo e bloco e deve ser único. **Antes de criar**, procurar o mesmo `session_id + block_id + record_type` para evitar duplicações. Correções de evidência já persistida devem ser documentadas por registro de retificação, não apagadas silenciosamente.

## Conteúdo dos reviews de 10 questões

Usar como referência os reviews já existentes de `p001`, mas sempre com `participant_id: "p002"`, `enrollment_id: "p002__tjsp-escrevente-2025"` e `competition_id: "tjsp-escrevente-2025"`.

Registrar, quando efetivamente observados:

1. **Identidade/proveniência:** `schema_version`, `feedback_id`, `session_id`, `block_id`, `record_type: "block_review"`, `occurred_at`, `recorded_at`, `source` e abrangência de questões.
2. **Placar:** total de questões principais válidas, acertos, erros, taxa de acerto, itens excluídos por defeito/ambiguidade, contagem de reforços fora da pontuação principal.
3. **Confiança:** acertos firmes, acertos inseguros, confiança declarada, chutes e erros com alta confiança; não inferir confiança silenciosamente.
4. **Estratégia e tipo de erro, separadamente:** eliminação/inferência, erro de conteúdo, leitura, prazo, requisito, exceção, pegadinha, falso conhecimento, quando comprovados. Correção, confiança e estratégia **não são categorias mutuamente exclusivas**.
5. **Diagnóstico:** matéria, subtema, dúvida inicial e pós-explicação, fundamento legal ou regra, padrão de confusão, prioridades de reteste e próximo bloco.
6. **Limites da evidência:** itens ainda não verificados, dados ausentes, restrições de generalização. Um bloco não demonstra domínio permanente.

Pode haver `questions` com dados mínimos (número, matéria, subtema, alternativa escolhida/gabarito, classificação e dúvida), **sem** enunciados integrais, dados pessoais, transcrições ou conversas completas. Usar `null` ou `"not_reported"` para o que não foi observado e explicar limites; não preencher números com estimativas.

Os relatórios de revisão ativa e de encerramento devem ter `record_type` distinto (`active_review` ou `session_summary`) e suas métricas não podem ser somadas novamente aos reviews de 10 questões.

## Segurança, prioridade e validação

- Repositório **público**: manter apenas dados pseudonimizados e pedagogicamente necessários. Não incluir nomes completos, dados de identificação, saúde, contatos, relato pessoal, links privados ou transcrições.
- Seguir `00_SYSTEM/ASSESSMENT_PROTOCOL.md`, `00_SYSTEM/CONTINUITY_PROTOCOL.md` e `00_SYSTEM/DATA_MODEL.md`; o edital de 2025 e a `competitions/tjsp-escrevente-2025/BLUEPRINT.json` continuam controlando o escopo da prova.
- Ao salvar, reler o JSON pela API do GitHub para confirmar persistência. Em falha, indicar **sincronização pendente** e entregar o JSON para registro posterior.
- A rotina de 10/20 questões organiza feedback do treinamento em chat. Não altera o ciclo padrão `microdrill` / `simulation` herdado da competição e não cria resultados que ainda não ocorreram.
