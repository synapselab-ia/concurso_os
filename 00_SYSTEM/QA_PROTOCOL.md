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
