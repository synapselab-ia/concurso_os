# concurso_os

Sistema longitudinal, multi-participante e multi-concurso para preparação assistida por IA.

## Princípios

1. O GitHub é a fonte canônica do projeto.
2. Chats são processos descartáveis; o estado deve ser reconstruível apenas pelo repositório.
3. Participante, concurso, conhecimento, evidência e estado derivado são entidades distintas.
4. Eventos de aprendizagem são append-only; métricas de domínio são projeções reconstruíveis.
5. O repositório é público durante a fase de produção: não registrar dados sensíveis ou desnecessários.
6. Nenhum GitHub Action é usado nesta fase. A validação canônica é local por `python tools/verify.py`.

## Começo rápido para qualquer agente

Leia, nesta ordem:

1. `AGENTS.md`
2. `00_SYSTEM/START_HERE.md`
3. `PROJECT_CONTROL.md`
4. `00_SYSTEM/CHECKPOINT.md`
5. `00_SYSTEM/NEXT_ACTION.md`

Depois recupere o estado real do GitHub antes de alterar qualquer arquivo.

## Estrutura

- `00_SYSTEM/`: regras canônicas do sistema.
- `knowledge/`: conhecimento e competências reutilizáveis.
- `competitions/`: adapters de concursos, editais e bancas.
- `participants/`: perfis públicos mínimos e enrollments.
- `schemas/`: contratos de dados.
- `tools/`: auditoria, verificação e automação determinística.
- `tests/`: testes do contrato do repositório.

## Verificação

```bash
python tools/verify.py
```

A V0.1 não depende de frontend, banco de dados, autenticação ou CI remoto.
