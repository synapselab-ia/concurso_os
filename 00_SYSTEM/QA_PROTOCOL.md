# QA_PROTOCOL

## Gate canônico

Durante a produção, usar localmente:

```bash
python tools/verify.py
```

## O que a automação determinística deve verificar

- arquivos canônicos obrigatórios;
- JSON e JSONL válidos;
- IDs e referências estruturais;
- eventos apontando para participantes existentes;
- campos proibidos em perfis públicos;
- ausência de GitHub Actions nesta fase;
- testes unitários.

## Limite do auditor

O auditor valida invariantes do repositório. Não substitui revisão semântica de conteúdo, interpretação jurídica, correção de questão ou qualidade pedagógica.

## QA editorial de apostilas

Criação e reconstrução substancial de `APOSTILA.md`/`APOSTILA.pdf` devem seguir `APOSTILA_AUTHORING_PROTOCOL.md`.

O gate determinístico **não basta** para liberar uma apostila. O release também precisa passar pelos gates semânticos aplicáveis do protocolo:

1. cobertura do edital/syllabus;
2. exatidão e sustentação por fonte;
3. qualidade didática;
4. distinções e casos-limite;
5. qualidade da prática/exercícios;
6. coerência com análise empírica da banca sem overfitting;
7. utilidade como corpus do NotebookLM;
8. redundância, terminologia e coerência interna;
9. QA textual/visual do PDF;
10. atualização de versão, manifest, changelog e continuidade.

A validação semântica deve ser registrada no `CHECKPOINT.md`, PR ou outro artefato canônico adequado. Não marcar um gate como `pass` sem ter realizado a verificação correspondente.
