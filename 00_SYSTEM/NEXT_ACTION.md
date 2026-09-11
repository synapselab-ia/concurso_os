# NEXT_ACTION

## STUDIO-001 — Smoke test do `Teste` nativo do NotebookLM com Português 1.0.1

O SubjectPack de Português foi simplificado para uma UX **Studio-first**. O próximo passo é testar o comportamento real do botão `Teste` antes de otimizar prompts ou replicar a metodologia para outras matérias.

### O usuário faz no NotebookLM

Se o notebook já estiver com as fontes do `MANIFEST.md`, não reorganizar nada agora.

1. abrir **Estúdio → Teste**;
2. deixar **Número de questões = Padrão**;
3. deixar **Nível de dificuldade = Médio (padrão)**;
4. manter as fontes carregadas como estão;
5. no campo `Qual deve ser o tema?`, escrever apenas:

> `Teste de Português no padrão TJSP/VUNESP das provas carregadas.`

6. clicar em **Gerar**;
7. responder algumas questões normalmente;
8. usar a revisão/explicação nativa se quiser;
9. trazer ao ChatGPT **somente** uma questão, explicação ou comportamento que pareça fora do padrão — ou dizer que o teste pareceu bom.

### O que NÃO fazer ainda

- não escrever prompt gigante;
- não ficar selecionando/desmarcando fontes por ferramenta;
- não marcar `Difícil` só porque a banca é VUNESP;
- não tentar configurar todos os recursos do Estúdio de uma vez;
- não produzir outro SubjectPack antes de observar esse teste.

### O que vamos avaliar

- conteúdo dentro do edital;
- alternativas plausíveis;
- linguagem e operação compatíveis com as provas carregadas;
- dificuldade razoavelmente compatível com o corpus;
- ausência de dificuldade artificial/obscura;
- utilidade das explicações.

### Critério de aprovação

`STUDIO-001` passa quando o usuário consegue gerar e usar um teste útil com poucos cliques e uma instrução curta, sem micro-orquestração.

Se passar, testar rapidamente `Cartões` e `Mapa mental` com a mesma filosofia e então promover o padrão Studio-first para os próximos SubjectPacks.

Se falhar, corrigir **o problema observado** no pack/metodologia em vez de antecipar configurações complexas.
