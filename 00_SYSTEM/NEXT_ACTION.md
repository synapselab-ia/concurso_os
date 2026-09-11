# NEXT_ACTION

## APOSTILA-002 — Reconstruir a apostila de Português para o NotebookLM

A arquitetura de uso do NotebookLM está definida por `DEC-0016`. O próximo trabalho não é testar mais prompts nem replicar packs: é **refazer a apostila de Português**, porque ela passou a ser o produto principal do estudante e o insumo dos recursos do Estúdio.

### Objetivo

Produzir uma nova `APOSTILA.md` e `APOSTILA.pdf` que sejam excelentes materiais de estudo por si só e funcionem bem como fonte para:

- leitura/consulta;
- `Teste`;
- `Cartões`;
- `Mapa mental`;
- `Relatórios`;
- `Tabela de dados`;
- resumos/áudio/apresentações;
- chat do NotebookLM.

Target recomendado do release: `portugues 2.0.0`.

## Recuperação obrigatória no próximo chat

Antes de escrever, seguir `AGENTS.md` e ler pelo menos:

1. `00_SYSTEM/START_HERE.md`;
2. `PROJECT_CONTROL.md`;
3. `00_SYSTEM/PROJECT_SPEC.md`;
4. `00_SYSTEM/ARCHITECTURE.md`;
5. `00_SYSTEM/DATA_MODEL.md`;
6. `00_SYSTEM/CHECKPOINT.md`;
7. este `NEXT_ACTION.md`;
8. `00_SYSTEM/DECISION_LOG.md`, especialmente DEC-0010, DEC-0013, DEC-0014 e DEC-0016;
9. `00_SYSTEM/SOURCE_POLICY.md` e `00_SYSTEM/QA_PROTOCOL.md`;
10. `competitions/tjsp-escrevente-2025/SYLLABUS.md`;
11. `materials/tjsp-escrevente-2025/portugues/ANALISE_BANCA.md`;
12. `materials/tjsp-escrevente-2025/portugues/SOURCES.md`;
13. `materials/tjsp-escrevente-2025/portugues/APOSTILA.md` atual, somente como objeto de auditoria/reaproveitamento seletivo.

Verificar também o estado real da `main` e PRs abertos antes de escrever.

## Princípios editoriais obrigatórios

### 1. A apostila é material do aluno, não relatório do projeto

Evitar poluir o texto didático com frases como:

- `segundo a análise da banca...`;
- `a VUNESP cobrou X vezes...`;
- `no TJSP 2025...`;
- referências a `source_id`, SHA, manifest, QA ou decisões internas.

Edital, provas e análise de banca orientam **o que entra, a profundidade, a ênfase, os exemplos e as distinções**, mas a engenharia fica no backoffice.

### 2. Cobrir integralmente o recorte do edital

Não sacrificar cobertura por concisão. Todo o recorte de Português do edital deve estar ensinável e recuperável na apostila.

### 3. Escrever para compreensão humana e recuperação pelo NotebookLM

Usar estrutura semântica forte:

```text
conceito
→ definição
→ como reconhecer
→ contraste com conceito próximo
→ exemplo
→ contraexemplo/caso-limite
→ erro típico
→ aplicação
→ síntese
```

Nem todo tópico precisa seguir mecanicamente essa sequência, mas a apostila deve conter informação explícita suficiente para o NotebookLM gerar artefatos úteis.

### 4. Densidade didática, não resumo raso

A apostila atual é curta demais para o novo papel. A nova versão deve ter explicações, exemplos e distinções suficientes para estudo real. Não limitar o material a 8 páginas ou ao tamanho atual.

Também evitar enciclopedismo: aprofundar o que é relevante ao edital e às operações observadas nas provas.

### 5. Exemplos e exercícios autorais

Incluir exemplos próprios e pequenas aplicações que ajudem tanto o estudante quanto os geradores do NotebookLM.

Quando útil, incluir:

- pares mínimos;
- reescritas;
- frases contrastivas;
- miniquestões;
- análise de alternativas hipotéticas;
- exercícios curtos com resposta/comentário em seção separada.

Não copiar questões reais extensamente para dentro da apostila.

### 6. Banca como engenharia silenciosa

Usar `ANALISE_BANCA.md` para priorizar tipos de operação, erros plausíveis e fronteiras conceituais. Não transformar a apostila em uma coleção de comentários sobre a VUNESP.

### 7. Compatibilidade com o chat

`METODOLOGIA_NOTEBOOKLM.md` 1.0.2 é chat-only. A nova apostila deve fornecer conteúdo suficiente para que o chat possa explicar dúvidas e gerar treino sem recorrer à análise de banca/backoffice.

## Processo de implementação

1. auditar a apostila atual e listar lacunas concretas;
2. desenhar novo sumário antes da reescrita completa;
3. reconstruir `APOSTILA.md`;
4. conferir cobertura contra o syllabus do edital;
5. conferir coerência com a análise reproduzível da banca sem inserir metadiscurso desnecessário;
6. fazer QA de precisão, exemplos, terminologia, completude e utilidade para NotebookLM;
7. gerar novo `APOSTILA.pdf` pesquisável;
8. fazer QA textual e visual do PDF;
9. atualizar `MANIFEST.md`, `CHANGELOG.md`, `CHECKPOINT.md`, `PROJECT_CONTROL.md` e `NEXT_ACTION.md`;
10. executar `python tools/verify.py` ou documentar explicitamente a impossibilidade;
11. revisar diff/readback, abrir PR e fazer merge quando couber sob DEC-0009.

## Definition of Done

`APOSTILA-002` só termina quando:

- o conteúdo cobre integralmente o edital de Português;
- a apostila é material didático suficiente por si só;
- a leitura não depende de conhecer este projeto/GitHub;
- Teste/Cartões/Mapa mental podem usar somente o PDF sem virar quiz sobre documentação interna;
- o chat pode usar `APOSTILA.pdf + METODOLOGIA_NOTEBOOKLM.md` para dúvidas/treino;
- PDF novo foi validado;
- continuidade e versão foram atualizadas no GitHub.

Não iniciar os SubjectPacks das outras matérias antes de fechar este padrão de apostila, salvo nova decisão canônica explícita.
