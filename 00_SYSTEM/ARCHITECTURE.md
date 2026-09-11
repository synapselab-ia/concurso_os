# ARCHITECTURE

## Visão

A arquitetura da V0.1 é uma cadeia editorial e pedagógica, não um LMS próprio.

```text
fontes oficiais + provas
        ↓
     ChatGPT
análise / autoria / QA
        ↓
      GitHub
subject packs versionados
        ↓
 sincronização manual
        ↓
   NotebookLM
Estúdio + chat por matéria
        ↓
feedback opcional
        ↓
     ChatGPT
```

## Papéis

### GitHub

Fonte canônica de:

- edital e mapa do concurso;
- registro de fontes;
- análise de banca;
- apostilas;
- metodologias de NotebookLM por matéria;
- manifests/changelogs;
- QA;
- continuidade entre chats.

GitHub não é o ambiente primário de estudo nem precisa armazenar cada resposta do aluno.

### ChatGPT

Responsável por:

- pesquisar e verificar;
- analisar provas e edital;
- produzir e atualizar materiais;
- fazer QA source-grounded;
- integrar feedback de sessões;
- manter a continuidade canônica no GitHub.

### NotebookLM

Ambiente principal de estudo source-grounded. A unidade recomendada é um notebook por matéria; quando houver histórico individual relevante, cada participante usa sua própria instância baseada no mesmo pacote de fontes.

A interface de estudo **não é apenas o chat**. O Estúdio do NotebookLM é parte central da experiência: testes, cartões, mapas mentais, relatórios, tabelas, resumos e demais artefatos podem ser usados diretamente conforme forem úteis à matéria. O chat fica disponível para dúvida, aprofundamento, correção diagnóstica e tarefas que realmente exigem interação.

### Regra de usabilidade

O pacote deve reduzir decisões operacionais do estudante, não aumentá-las.

Por padrão:

- carregar o corpus recomendado uma vez;
- manter as fontes disponíveis no notebook;
- usar os recursos nativos do Estúdio com seus controles padrão;
- adicionar apenas uma instrução curta quando for necessário calibrar objetivo ou banca;
- não exigir seleção manual de subconjuntos de fontes para cada artefato, salvo quando um teste real mostrar que isso melhora o resultado;
- não tratar `Fácil`, `Médio` ou `Difícil` como equivalentes automáticos a uma banca específica.

A calibração de estilo e nível vem do **corpus da banca + análise reproduzível**, e não de burocracia de configuração.

## Unidade canônica de entrega

O objeto principal da V0.1 é o `SubjectPack`:

```text
Competition + Subject
        ↓
MANIFEST
APOSTILA
ANALISE_BANCA
METODOLOGIA_NOTEBOOKLM
SOURCES
CHANGELOG
```

Conhecimento pode continuar reutilizável entre concursos, mas a primeira prioridade é produzir um pacote de estudo correto e utilizável para o concurso-alvo.

## Participantes

Perfis de participantes continuam permitidos para organizar materiais e feedback, mas o kernel não depende de lógica específica por pessoa. Progresso individual, quando persistido, deve ser resumido e separado do material compartilhado.

## Evidência e scheduler

O modelo de `EvidenceEvent` e projeções permanece como experimento possível, mas **não é requisito nem caminho crítico da V0.1**. Não construir infraestrutura de rastreamento questão a questão antes de provar que ela melhora o fluxo NotebookLM + ChatGPT + GitHub.

## Continuidade

Chats são descartáveis. Decisões, versões de pacote, estado de produção e próxima ação devem permanecer no repositório.

## Especificação detalhada

Ver `docs/STACK_NOTEBOOKLM.md`.
