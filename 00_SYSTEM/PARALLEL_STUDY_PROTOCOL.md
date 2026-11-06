# PARALLEL_STUDY_PROTOCOL

## Objetivo e escopo

Permitir dois ou mais chats de estudo simultâneos para o mesmo `Enrollment`, sem que a ordem de conclusão das respostas, a concorrência de gravações ou o uso de outro participante cause perda, duplicação ou mistura de evidências. Este protocolo trata **exclusivamente da coordenação de sessões ChatGPT e persistência de feedback**, não altera `NEXT_ACTION` editorial, a metodologia de uma questão por vez *dentro de cada chat*, o blueprint, os SubjectPacks ou o pipeline de NotebookLM.

É uma convenção operacional para agentes usando GitHub Contents API/PRs. **Não existe serviço de lock, fila transacional, worker automático ou garantia de sincronização imediata**. Conflitos devem falhar de modo seguro e ser reconciliados.

## Unidade de isolamento

- Primeiro identificar `participant_id`, `competition_id` e `enrollment_id` pelo `CONFIG.json` real. Nunca misturar `p001` e `p002`.
- Cada chat concorrente recebe `session_id` próprio, pseudônimo e estável: `chatgpt-YYYYMMDD-<random_slug>`, onde `random_slug` é suficientemente distinto e não contém nome, telefone, endereço, identificador de conversa privado ou dados pessoais.
- Um `session_id` designa exatamente um chat/sessão; em retomada do mesmo chat, reutilizar seu ID. Não reutilizar o ID de outro chat para simular sequência global.
- `block_id` é local à sessão: `b01-q01-q10`, `b02-q11-q20` etc. **Q01** no chat A não é a mesma questão que Q01 no chat B.
- Para referência entre chats, usar chave composta `enrollment_id + session_id + local_question_id`; opcional `question_uid` estável e não pessoal para identificar item quando houver necessidade de deduplicação.
- Uma sessão começa com alocação de `session_id` e leitura da configuração vigente. Gravar o ID no próprio contexto de trabalho antes de iniciar questões, inclusive ao retomar.

## Persistência append-only

Usar o diretório existente:

```text
participants/<participant_id>/enrollments/<competition_id>/session_feedback/
  YYYY-MM-DD__<session_id>__b01-q01-q10.json
  YYYY-MM-DD__<session_id>__b02-q11-q20.json
  YYYY-MM-DD__<session_id>__active-review-q01-q20.json
  YYYY-MM-DD__<session_id>__session-summary.json
  YYYY-MM-DD__<session_id>__correction-<correction_id>.json
```

A convenção de nomes de `p002/session_feedback/README.md` permanece válida; o novo `session_id` especifica também o **chat paralelo**. Para reviews existentes, manter nome e identidade originais, sem renomear ou reindexar.

- Cada arquivo publicado contém exatamente um evento de feedback de sessão/bloco. `feedback_id` é idempotency key estável, composta por enrollment, session, record_type e block. Datas não são parte da identidade lógica.
- **Nunca usar `update_file` para substituir um registro de evidência já persistido.** Erros e novas evidências exigem arquivo `correction` append-only, com `supersedes_feedback_id`, motivo e referência ao registro anterior; a projeção aplica a retificação mantendo a trilha de auditoria.
- **Nunca atualizar cumulativos globais no commit do chat.** `cumulative_after_block` de um chat paralelo não deve ser considerado total global canônico se não resultar de consolidação abrangente; preferir omitir, ou marcar como `session_local` e `not_global`.
- Os registros preservam correção, confiança e estratégia como dimensões distintas; reforços e revisões não entram automaticamente nas 10 questões principais. Ausências viram `null`/não verificado, não inferências.

## Algoritmo de gravação de cada chat

1. Consultar o estado atual do `Enrollment` e procurar no GitHub `feedback_id` e o trio `session_id + block_id + record_type` entre arquivos do diretório, incluindo eventos de retificação. Buscar **antes** de gravar, não apenas no início do estudo.
2. Preparar JSON mínimo, sem dados pessoais nem transcrição, e validar localmente identidade, estrutura, contagem, `score.correct + score.incorrect = score.total` quando esses campos forem observados, e coerência de escopo. Não inventar telemetria.
3. Usar **criação condicional de arquivo novo** via Contents API (`create_file` somente se o caminho não existir); não substituir arquivos. Para o mesmo `feedback_id`, repetir é **no-op**, não duplicação.
4. Se o GitHub responder conflito, 409/422, arquivo existente ou branch desatualizada, **interromper a escrita**, reler a branch, comparar identidade e conteúdo e decidir: igual -> no-op; distinto para a mesma chave -> discrepância pendente de reconciliação/retificação, **nunca sobrescrever**.
5. Ler novamente o arquivo publicado, conferir `feedback_id`, `session_id`, `enrollment_id`, `block_id`, `record_type` e conteúdo esperado. Só então declarar `PERSISTED_VERIFIED`.
6. Se API indisponível, conservar o JSON na conversa como `PENDING_SYNC` e comunicar explicitamente que não foi persistido. Um novo chat não pode presumir que exista no GitHub.
7. Não atualizar `CHECKPOINT`/`NEXT_ACTION` nem `PROJECT_CONTROL` para cada bloco individual; esses são documentos de **engenharia do projeto**, não placar pessoal de chat.

## Fluxo GitHub, branches e conflitos

- Para eventos normais independentes, preferir **criação de arquivo único diretamente em `main`** com caminho exclusivo e readback; não criar PR por questão. O recurso `create_file` deve rejeitar caminho já existente. Um commit independente por arquivo não faz leitura-modificação-escrita do mesmo documento.
- Para alterações estruturais/código/índices consolidados, criar branch a partir do head verificado de `main`, PR, revisar diff, executar `python tools/verify.py` ou registrar impossibilidade segundo DEC-0009, conferir que o head/base não mudou de forma incompatível e só então merge.
- **Não fazer force push, `update_ref(force=true)`, rebase destrutivo ou resolução de conflitos que descarte um dos feedbacks.** Se uma PR acumulou arquivos de sessões distintas, conferir que todos continuam presentes após o merge por readback.
- Dois chats podem criar arquivos em paralelo, mas o GitHub não fornece lock distribuído entre chats. Em erro de concorrência, buscar a versão mais recente e refazer apenas a operação ainda necessária, mantendo o mesmo `feedback_id`.
- Operações de consolidação são responsabilidade de **um agente por execução**, sempre reavaliando a versão atual da base antes de gravar seu resultado. Não permitir múltiplos consolidadores atualizarem o mesmo índice sem controle por SHA/PR.

## Consolidação segura

1. Enumerar arquivos de feedback do `Enrollment` na **mesma referência Git/commit**, registrar `source_commit_sha` e lista ordenada de `feedback_id` efetivamente incluídos.
2. Validar unicidade lógica, proveniência, participant/enrollment, intervalos **por sessão**, consistência de tipos e correções. Sobreposição local dentro da mesma sessão é erro; números iguais em sessões diferentes são legítimos.
3. Computar métricas globais somente dos `block_review` válidos, sem contar `active_review`, `session_summary` ou reforços duas vezes. Aplicar retificações declaradas; sinalizar divergências não resolvidas em vez de adivinhar.
4. A saída de consolidação é **derivada**, nunca substitui eventos; deve informar data, SHA-base, cobertura e IDs fonte. Se houver novos eventos após o SHA lido, marcar o resultado como snapshot, recalcular antes de usá-lo como estado atualizado.
5. Não somar percentuais nem categorias sobrepostas: acertos/erros são partições quando total definido; confiança, estratégia e natureza do erro são dimensões independentes.
6. Retestes adaptativos usam evidências unificadas somente após readback e identificação de qual chat/assunto gerou a dúvida. O scheduler não pode assumir sequência temporal total entre chats a partir dos números locais.
7. Se os dados forem ambíguos, registrar `NEEDS_RECONCILIATION` e manter os eventos brutos íntegros.

## Critérios de aceitação do protocolo

Cenários mínimos de verificação antes de afirmar automação operacional:

- Chat A e B, mesmo enrollment, ambos `b01-q01-q10`: dois arquivos distintos, sem colisão.
- Reenvio do mesmo feedback: nenhum novo registro duplicado.
- Mesmo caminho/chave com conteúdo divergente: conflito detectado; conteúdo anterior preservado.
- Chat A de `p001` e chat B de `p002`: diretórios e agregações isolados.
- Dois blocos e revisão ativa: apenas blocos principais entram no total de questões.
- Retificação: evento original preservado e apenas uma versão efetiva computada.
- Snapshot calculado antes de um novo bloco: não declarar atualização global, refazer consolidação.
- Falha de GitHub: `PENDING_SYNC`, sem falso `PASS`.
- Nenhuma alteração no próximo gate editorial `DIREITO-016`.

## Checklist prático para novos chats

Ler `AGENTS.md`, `START_HERE.md`, `PROJECT_CONTROL.md`, `CHECKPOINT.md`, `NEXT_ACTION.md` e este protocolo. Validar `Enrollment`; atribuir ou recuperar `session_id` exclusivo; aplicar metodologia de estudo da competição; publicar somente eventos próprios; reler o GitHub; consultar feedback dos demais chats para planejar retestes **sem editar seus registros**.

## Limitações assumidas

A implementação atual é **um protocolo de gravação via API e documentação de operação**, não um motor transacional automático. Segurança de write depende de cada agente cumprir criação condicional, chaves estáveis, readback e reconciliação; a consolidação automática e seus testes de concorrência requerem implementação e gate determinístico próprios. A próxima ação editorial `DIREITO-016` segue bloqueada até evidência manual do NotebookLM, independentemente deste protocolo.
