# NEXT_ACTION

## PACK-001 — Produzir o primeiro SubjectPack completo

A arquitetura canônica agora é GitHub + ChatGPT + NotebookLM. O próximo passo não é construir scheduler nem coletar baseline.

Produzir o primeiro pacote completo para `tjsp-escrevente-2025`, começando por **Língua Portuguesa** para validar o formato ponta a ponta.

O pacote deve conter:

```text
materials/tjsp-escrevente-2025/portugues/
├── MANIFEST.md
├── APOSTILA.md
├── APOSTILA.pdf
├── ANALISE_BANCA.md
├── METODOLOGIA_NOTEBOOKLM.md
├── SOURCES.md
└── CHANGELOG.md
```

Antes de considerar PACK-001 concluído:

1. mapear todo o recorte de Português do edital;
2. analisar de forma reproduzível as provas 2021/2023/2024/2025 para padrões da VUNESP;
3. escrever a apostila source-grounded e focada no edital;
4. adaptar a metodologia legada para uso específico no NotebookLM de Português;
5. gerar PDF de distribuição;
6. revisar o pacote contra edital, provas e política de fontes;
7. validar que um usuário consegue criar o notebook apenas seguindo o MANIFEST;
8. atualizar checkpoint e preparar a replicação para a próxima matéria.

Não retomar pipeline de mastery/scheduler questão a questão durante PACK-001.
