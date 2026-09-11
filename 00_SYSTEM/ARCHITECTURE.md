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
estudo por matéria
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
