# APOSTILA_AUTHORING_PROTOCOL

## 1. Finalidade

Este protocolo define **como transformar edital + fontes + provas + análise empírica em uma apostila didática forte, auditável e adequada ao NotebookLM**.

Ele é backoffice do projeto. Não é material do estudante e não deve ser carregado no NotebookLM.

A partir de `DEC-0018`, este protocolo é obrigatório para:

- reconstruções substanciais de apostilas existentes;
- criação da primeira versão de apostila de uma nova matéria;
- revisões major que alterem cobertura, estrutura ou abordagem pedagógica.

O objetivo não é padronizar todas as matérias no mesmo formato. O objetivo é padronizar **o processo de qualidade**.

---

## 2. Produto esperado

A apostila deve funcionar simultaneamente em três cenários:

1. **aprendizado** — um estudante consegue aprender o conteúdo sem depender de conhecer este projeto;
2. **revisão** — a estrutura permite recuperar rapidamente regras, distinções, exemplos e sínteses;
3. **corpus para IA** — o NotebookLM encontra conteúdo explícito e semanticamente organizado o suficiente para explicar, gerar Testes, Cartões, Mapas mentais, Relatórios e outros artefatos úteis.

Apostila de concurso não é:

- relatório de análise de banca;
- transcrição do edital;
- resumo telegráfico para quem já domina a matéria;
- enciclopédia indiscriminada;
- coleção de questões sem estrutura didática;
- documentação interna do projeto.

---

## 3. Princípios não negociáveis

### 3.1 Cobertura antes de redação

Não começar escrevendo capítulos antes de mapear integralmente o escopo.

Todo item do syllabus deve terminar em um dos estados:

- `covered` — ensinado de forma suficiente;
- `cross_reference` — ensinado em outra unidade claramente identificada;
- `source_direct` — deliberadamente remetido a fonte primária por motivo pedagógico explícito;
- `out_of_scope` — somente quando sustentado pelo edital/adapter.

Nenhum item pode desaparecer por simplificação editorial.

### 3.2 Fonte antes de formulação

Afirmações factuais específicas de edital, norma, versão de software, competência institucional ou regra técnica precisam estar sustentadas pelas fontes apropriadas conforme `SOURCE_POLICY.md`.

A redação didática pode sintetizar. A síntese não autoriza inventar, completar lacunas silenciosamente ou transformar interpretação em fato.

### 3.3 Banca como engenharia silenciosa

Edital e fontes definem **o que é verdade e o que está no escopo**. Provas e `ANALISE_BANCA.md` ajudam a decidir:

- profundidade;
- ordem de apresentação;
- distinções que precisam ficar explícitas;
- tipos de aplicação;
- erros plausíveis;
- exemplos e contraexemplos;
- quantidade relativa de prática.

A apostila não deve ficar poluída por metadiscurso como `a VUNESP cobra`, `no TJSP apareceu`, contagens históricas ou referências à análise interna, salvo quando isso tiver valor pedagógico direto e deliberado.

### 3.4 Densidade suficiente

Nenhum conceito relevante deve depender de conhecimento implícito que o estudante ou o NotebookLM precisem adivinhar.

Ser conciso não significa omitir a ponte entre definição e aplicação.

### 3.5 Distinção antes de memorização

Quando dois conceitos podem ser confundidos, a apostila deve explicitamente mostrar a fronteira entre eles.

Preferir:

```text
conceito A
→ conceito B próximo
→ critério decisivo
→ exemplo A
→ exemplo B
→ caso-limite
```

em vez de duas definições isoladas.

### 3.6 Exemplo como parte do conteúdo

Exemplos não são decoração. Devem mostrar a regra funcionando.

Contraexemplos, pares mínimos e casos-limite são obrigatórios quando a compreensão depende de diferenças sutis.

### 3.7 Apostila para humano e máquina

A estrutura deve ser clara para leitura humana e recuperação semântica por IA:

- títulos informativos;
- terminologia consistente;
- conceitos definidos explicitamente;
- tabelas com função real;
- exemplos próximos da explicação que ilustram;
- gabaritos separados das perguntas;
- referências internas claras;
- evitar depender de layout visual para transmitir significado essencial.

---

## 4. Entradas obrigatórias

Antes de criar ou reescrever uma apostila, o agente deve ler, no mínimo:

1. `AGENTS.md`;
2. `00_SYSTEM/START_HERE.md`;
3. `PROJECT_CONTROL.md`;
4. `00_SYSTEM/CHECKPOINT.md`;
5. `00_SYSTEM/NEXT_ACTION.md`;
6. este protocolo;
7. `00_SYSTEM/SOURCE_POLICY.md`;
8. `00_SYSTEM/QA_PROTOCOL.md`;
9. edital/syllabus canônico da competição;
10. `SOURCES.md` da matéria/competição quando existir;
11. `ANALISE_BANCA.md` quando existir;
12. apostila anterior, se houver, **como objeto de auditoria**, não como fonte automática de verdade;
13. fontes primárias necessárias ao conteúdo;
14. configuração/metodologia do tutor NotebookLM apenas para verificar compatibilidade do corpus final.

Também deve verificar a `main`, PRs abertos e estado real do GitHub antes de escrever.

---

## 5. Processo canônico

## Etapa A — Auditoria do estado atual

Quando já houver apostila, começar por uma auditoria concreta.

Classificar problemas em pelo menos:

- cobertura ausente;
- cobertura superficial;
- definição imprecisa;
- regra sem exemplo;
- exemplo sem explicação;
- distinção crítica ausente;
- excesso de metadiscurso de concurso/banca;
- excesso de resumo;
- redundância;
- sequência pedagógica ruim;
- conteúdo potencialmente desatualizado;
- conteúdo difícil de recuperar pelo NotebookLM;
- exercício fraco ou inexistente.

Não preservar uma seção apenas porque já existe.

## Etapa B — Matriz de cobertura e autoria

Antes da redação completa, construir uma matriz de trabalho com, no mínimo, estas colunas conceituais:

| Campo | Função |
|---|---|
| `syllabus_ref` | item do edital/syllabus coberto |
| `learning_goal` | o que o estudante precisa conseguir compreender/fazer |
| `concepts` | conceitos/regras necessários |
| `contrasts` | conceitos próximos que precisam ser separados |
| `applications` | tipos de aplicação/exercício adequados |
| `source_refs` | fontes que sustentam o conteúdo |
| `banca_signal` | operação/padrão empírico relevante, sem virar previsão |
| `depth` | profundidade editorial planejada |
| `status` | planned/drafted/qa/covered |

A matriz pode ser mantida como artefato de trabalho da branch/PR; se revelar valor duradouro para manutenção, pode ser persistida no pack. O requisito obrigatório é que a cobertura seja verificável no QA final.

### Regra de profundidade

Profundidade não é frequência bruta.

Ela deve considerar conjuntamente:

```text
escopo oficial
+ complexidade conceitual
+ risco de confusão
+ dependência para outros tópicos
+ evidência empírica da banca
+ valor didático para o NotebookLM
```

## Etapa C — Sumário pedagógico

Só depois da matriz, desenhar o sumário.

O sumário deve refletir dependências de aprendizado, não necessariamente a ordem literal do edital.

Critérios:

- pré-requisitos antes de aplicações dependentes;
- conceitos fortemente relacionados próximos entre si;
- tópicos muito densos subdivididos;
- tópicos pequenos podem ser agrupados quando a junção melhora compreensão;
- nenhum agrupamento pode esconder cobertura do syllabus.

## Etapa D — Redação das unidades

Uma unidade didática pode usar a seguinte estrutura semântica como padrão adaptável:

```text
1. O que é
2. Como reconhecer / quando se aplica
3. Como funciona
4. Com o que pode ser confundido
5. Exemplo explicado
6. Contraexemplo ou caso-limite
7. Erro típico
8. Aplicação / miniquestão
9. Síntese de recuperação
```

Não transformar essa sequência em formulário mecânico. Tópicos simples podem ser menores; tópicos complexos podem precisar de múltiplas camadas.

### Regra de explicitação

Se uma pergunta razoável de um aluno exigir uma informação intermediária para chegar da regra ao exemplo, essa informação provavelmente deve aparecer na apostila.

### Regra de terminologia

Definir um termo de uma forma e mantê-la consistente ao longo do documento. Sinônimos úteis podem ser indicados explicitamente; variação estilística não deve criar ambiguidade conceitual.

---

## 6. Padrões por família de matéria

O protocolo comum é obrigatório; a forma didática varia por domínio.

### 6.1 Direito e legislação

Estrutura preferida:

```text
regra/fonte normativa
→ elementos/requisitos
→ hipótese de incidência
→ consequência
→ exceção
→ contraste com instituto próximo
→ caso aplicado
→ síntese
```

Regras adicionais:

- diferenciar texto normativo de explicação editorial;
- não inventar jurisprudência;
- versão/recorte normativo precisam estar controlados;
- prazos, competências, requisitos, exceções e efeitos merecem estrutura altamente recuperável;
- tabelas comparativas são úteis quando evitam confusão, não como substituto de explicação.

### 6.2 Língua Portuguesa

Estrutura preferida:

```text
conceito linguístico
→ efeito de sentido / regra
→ como reconhecer no contexto
→ contraste
→ exemplos e pares mínimos
→ reescrita
→ aplicação em texto/frase
```

Regras adicionais:

- gramática deve ser aplicada ao contexto, não só definida;
- interpretação precisa diferenciar literalidade, inferência e extrapolação;
- relações lógico-semânticas devem incluir marcadores + função + contraste;
- reescrita precisa discutir preservação ou alteração de sentido quando relevante.

### 6.3 Matemática

Estrutura preferida:

```text
conceito
→ representação
→ método
→ exemplo resolvido passo a passo
→ verificação
→ erro de procedimento
→ problema análogo
```

Regras adicionais:

- mostrar por que o método funciona quando isso reduz memorização mecânica;
- incluir checagem dimensional/ordem de grandeza quando útil;
- separar erro aritmético de erro de modelagem;
- exercícios devem variar números e contexto sem mudar apenas superficialmente o exemplo.

### 6.4 Raciocínio Lógico

Estrutura preferida:

```text
formalização
→ regra de inferência/relação
→ exemplo
→ contraexemplo
→ dedução
→ verificação/contraprova
→ variação estrutural
```

Não confundir memorização de padrão visual com compreensão da estrutura lógica.

### 6.5 Informática

Estrutura preferida:

```text
função/recurso
→ comportamento real
→ onde/quando usar
→ sequência operacional
→ diferença para recurso próximo
→ cenário aplicado
```

Regras adicionais:

- controlar versão do software/serviço;
- evitar afirmar comportamento de interface sem fonte adequada;
- distinguir conceito geral de passo específico de UI;
- comandos, funções e recursos próximos devem ser comparados explicitamente.

### 6.6 Atualidades

Estrutura preferida:

```text
fato/contexto
→ atores
→ sequência temporal
→ relação causal documentada
→ implicações
→ conceitos necessários
→ limites/controvérsias factuais
```

Regras adicionais:

- conteúdo precisa ser datado;
- separar fato, interpretação e hipótese;
- evitar transformar opinião editorial em verdade;
- revisão de validade temporal faz parte do QA.

### 6.7 Redação

Estrutura preferida:

```text
critério
→ função no texto
→ exemplo
→ falha típica
→ reescrita
→ exercício de produção
→ rubrica de revisão
```

A apostila deve ensinar produção e revisão, não apenas listar critérios.

---

## 7. Exemplos, contraexemplos e exercícios

### 7.1 Exemplos autorais

Preferir exemplos próprios, curtos e controlados, criados para demonstrar exatamente a regra discutida.

Quando útil, usar:

- par mínimo;
- antes/depois;
- frase correta/incorreta;
- caso positivo/caso negativo;
- mesma estrutura com mudança de um único elemento decisivo;
- mini texto + pergunta;
- problema resolvido + problema análogo.

### 7.2 Questões reais

Questões reais servem ao backoffice para análise e calibração. Não copiar extensamente questões protegidas para a apostila.

Quando for pedagogicamente necessário mencionar uma questão real, preferir referência curta/identificadora e paráfrase compatível com a política de fontes e direitos autorais.

### 7.3 Miniquestões autorais

Devem testar a habilidade ensinada, não vocabulário acidental da seção.

Evitar:

- alternativa obviamente absurda;
- correta que repete literalmente a definição enquanto as demais não são plausíveis;
- ambiguidade não intencional;
- questão que exige conteúdo ainda não ensinado;
- dificuldade artificial por obscuridade lexical.

### 7.4 Gabarito e comentário

Perguntas e respostas precisam ficar estruturalmente separadas.

O comentário deve explicar **o elemento decisivo**, não apenas repetir a alternativa correta.

---

## 8. Engenharia para NotebookLM

A apostila deve ser útil mesmo fora do NotebookLM, mas algumas decisões aumentam a qualidade do corpus.

### 8.1 Informação explícita

O NotebookLM recupera melhor quando:

- conceitos têm definição clara;
- diferenças aparecem na mesma seção;
- exceções estão associadas à regra correspondente;
- exemplos indicam por que são exemplos;
- sínteses nomeiam os critérios decisivos.

### 8.2 Hierarquia semântica

Usar títulos e subtítulos que descrevem conteúdo real.

Evitar dezenas de cabeçalhos genéricos como `Observação`, `Importante`, `Dica` sem contexto.

### 8.3 Tabelas

Usar tabela quando a relação é genuinamente tabular.

Uma tabela deve ser compreensível em texto e não depender exclusivamente de cor ou posição visual.

### 8.4 Artefatos do Estúdio

A apostila deve fornecer matéria-prima suficiente para:

- `Teste`: conceitos, aplicações, exemplos e distinções;
- `Cartões`: definições, regras, exceções, contrastes e fórmulas curtas;
- `Mapa mental`: hierarquia conceitual explícita;
- `Tabela de dados`: campos comparáveis reais;
- `Relatórios/Áudio/Apresentação`: narrativa coerente e sínteses;
- chat: explicações suficientes para aprofundar dúvidas sem acessar o backoffice.

### 8.5 Não escrever para enganar o gerador

Não inserir prompts, instruções escondidas ou metadados pedagógicos artificiais dentro da apostila apenas para controlar o NotebookLM.

O conteúdo deve ser bom o suficiente para humanos e máquinas pelo mesmo motivo: clareza.

---

## 9. Estilo editorial

### Preferir

- português claro e preciso;
- parágrafos curtos quando o raciocínio permitir;
- definição seguida de consequência prática;
- exemplos imediatamente relevantes;
- listas quando há itens discretos;
- tabelas apenas para comparação real;
- sinalização explícita de exceções e casos-limite;
- sínteses de alta densidade ao final de blocos importantes.

### Evitar

- frases promocionais;
- motivação genérica;
- `macetes` sem explicação;
- jargão não definido;
- excesso de caixas visuais;
- repetição da mesma regra em capítulos distintos sem necessidade;
- metadiscurso sobre GitHub, QA, hashes, decisões internas ou processo de autoria;
- referências constantes a concurso/banca quando não agregam compreensão;
- “resumo do resumo” que sacrifica conteúdo essencial.

---

## 10. Gates de QA editorial

A apostila só pode ser promovida a release depois de passar por todos os gates aplicáveis.

### QA-1 — Cobertura

Perguntas:

- todo item do syllabus foi coberto ou explicitamente referenciado?
- há item resumido demais para ser realmente ensinável?
- pré-requisitos necessários foram incluídos?

Saída esperada: matriz de cobertura sem lacunas silenciosas.

### QA-2 — Exatidão e fonte

Perguntas:

- cada afirmação sensível está sustentada?
- versões normativas/técnicas estão corretas?
- interpretações foram apresentadas como interpretações?
- a apostila antiga introduziu alguma regra sem fonte que foi carregada adiante?

### QA-3 — Didática

Perguntas:

- um aluno que ainda não domina o assunto consegue seguir o raciocínio?
- existem pontes entre regra e aplicação?
- exemplos realmente demonstram o conceito?
- há excesso de compressão?

### QA-4 — Distinções

Perguntas:

- conceitos confundíveis foram comparados explicitamente?
- exceções estão próximas da regra?
- existem casos-limite onde a fronteira é difícil?

### QA-5 — Prática

Perguntas:

- os exercícios cobrem aplicação, e não só definição?
- gabaritos estão separados e comentados?
- existe variação suficiente para evitar mera repetição?

### QA-6 — Banca

Perguntas:

- as operações enfatizadas são coerentes com a análise empírica disponível?
- houve overfitting a poucas provas?
- frequência histórica foi indevidamente transformada em previsão?
- a banca influenciou a engenharia sem dominar o texto didático?

### QA-7 — NotebookLM

Perguntas:

- Teste pode gerar perguntas úteis usando apenas a apostila?
- Cartões têm conceitos/regras recuperáveis?
- Mapa mental consegue reconstruir a hierarquia?
- o chat configurado consegue explicar dúvidas usando apenas o corpus didático?
- algum trecho depende de documento de backoffice para fazer sentido?

### QA-8 — Redundância e coerência

Perguntas:

- a mesma regra aparece em múltiplos lugares com formulações conflitantes?
- termos são usados de modo consistente?
- há seções que não contribuem para edital, compreensão ou aplicação?

### QA-9 — PDF

Depois da aprovação de conteúdo:

- gerar PDF pesquisável;
- conferir extração textual;
- conferir acentos e símbolos;
- renderizar/inspecionar páginas;
- verificar clipping, sobreposição e tabelas quebradas;
- verificar hierarquia de títulos e legibilidade;
- verificar que respostas/gabaritos não ficaram acidentalmente colados às perguntas de modo confuso.

### QA-10 — Repositório

- atualizar versão e changelog;
- atualizar manifest;
- atualizar continuidade;
- executar `python tools/verify.py` ou documentar explicitamente por que não foi possível;
- revisar diff/readback;
- abrir PR e mesclar quando couber sob `DEC-0009`.

---

## 11. Definition of Done de uma apostila major

Uma release major de apostila só está pronta quando:

- cobre integralmente o escopo oficial aplicável;
- pode ser estudada sem conhecer o backoffice;
- contém densidade didática suficiente para aprendizado real;
- distinções críticas são explícitas;
- exemplos e prática autoral são suficientes;
- fatos sensíveis estão source-grounded;
- análise de banca influenciou profundidade sem virar metadiscurso dominante;
- funciona como corpus limpo do NotebookLM;
- todos os gates de QA aplicáveis passaram;
- PDF pesquisável foi validado textual e visualmente;
- versão, manifest, changelog, checkpoint e next action foram atualizados;
- gate determinístico foi executado ou sua impossibilidade foi registrada.

---

## 12. Handoff entre chats

Antes de encerrar uma sessão de autoria, registrar no GitHub:

- etapa atual do protocolo;
- cobertura já concluída;
- lacunas abertas;
- decisões editoriais novas que tenham efeito futuro;
- branch/PR esperados;
- validação executada;
- próxima ação exata.

Nunca deixar como única orientação para o próximo chat algo como `continuar a apostila`.

A continuidade deve permitir que um novo agente identifique **onde o processo parou e qual gate vem a seguir**.

---

## 13. Regra final

> **Apostila boa não é a que contém mais páginas; é a que cobre o escopo certo, explica o necessário, separa o que se confunde, pratica o que precisa ser aplicado e oferece ao estudante — e ao NotebookLM — informação explícita suficiente para aprender e recuperar sem adivinhação.**
