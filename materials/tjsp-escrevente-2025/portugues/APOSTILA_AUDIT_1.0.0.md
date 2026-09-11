# AUDITORIA EDITORIAL — APOSTILA Português 1.0.0

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Objeto auditado:** `APOSTILA.md` / `APOSTILA.pdf` da distribuição 1.0.0  
**Protocolo:** `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`  
**Data:** 2026-09-11

## 1. Síntese

A versão 1.0.0 cobre nominalmente os 13 itens do syllabus, mas funciona predominantemente como **resumo de revisão**. Ela não atinge a densidade exigida pelo protocolo para um estudante aprender do zero nem oferece matéria-prima suficiente para o NotebookLM gerar prática variada sem depender de inferências ou do backoffice.

O principal problema não é erro grosseiro de escopo; é **compressão excessiva**. Regras complexas aparecem em listas curtas, conceitos próximos não são separados com a profundidade necessária e praticamente não há exercícios autorais com gabarito comentado.

## 2. Lacunas por categoria do protocolo

### 2.1 Cobertura ausente ou insuficientemente explícita

- textos **não verbais** aparecem no syllabus, mas a apostila não ensina leitura de imagem, charge, tira, gráfico verbal-visual ou relação entre elementos verbais e visuais;
- textos **literários e não literários** são mencionados, porém sem critérios operacionais de leitura, voz narrativa, efeitos expressivos ou diferenças entre informação e construção estética;
- `classes de palavras` recebe apenas um inventário resumido e não inclui, com clareza suficiente, flexão, valor contextual, locuções, substantivação, mudança de classe e efeito semântico;
- valores de tempos e modos verbais aparecem em seção isolada, mas sem integração suficiente a reescrita e relações de sentido;
- coesão é tratada sobretudo por pronomes e conectivos; faltam elipse, substituição lexical, repetição controlada, paralelismo e encadeamento referencial mais amplo.

### 2.2 Cobertura superficial

- interpretação: boa distinção inicial entre literalidade/inferência/extrapolação, mas faltam método de reconstrução de tese, pressupostos, modalização, ironia e leitura de alternativas por grau de abrangência;
- relações lógico-semânticas: tabela útil, porém curta para distinguir pares críticos como `causa x consequência`, `condição x concessão`, `finalidade x consequência`, `explicação x causa` e `conclusão x consequência`;
- semântica: pouca exploração de polissemia, ambiguidade, denotação/conotação, intensidade lexical e efeito de substituição;
- concordância: apenas regra-base e poucos casos; faltam sujeitos compostos, porcentagens, expressões partitivas, pronomes relativos, `se`, concordância ideológica e vários casos nominais frequentes;
- regência: lista mínima de verbos, sem contraste por mudança de sentido nem aplicação com pronomes relativos e crase;
- crase: regra básica correta, mas sem mapa completo de ocorrência, proibição, facultatividade e casos especiais;
- colocação pronominal: apresenta próclise/ênclise/mesóclise, mas sem fronteiras suficientes em locuções verbais, infinitivo, futuro, início de oração e partículas atrativas;
- pontuação: regras centrais corretas, mas faltam coordenação/subordinação, orações deslocadas, aposto, vocativo, enumeração complexa, ponto e vírgula, parênteses e impacto semântico sistemático.

### 2.3 Definições imprecisas ou potencialmente simplificadoras

Não foram encontrados erros factuais centrais inequívocos na auditoria, mas há formulações que, por serem muito comprimidas, podem induzir generalização. Exemplos:

- `o, a, os, as costumam exercer objeto direto` e `lhe, lhes costumam exercer objeto indireto` precisam ser apresentados com função sintática e limites, não como substituição mecânica;
- `onde` e `aonde` precisam ser ligados a antecedente locativo e regência verbal, evitando a regra simplista de “lugar/movimento” sem estrutura;
- a relação entre artigo, preposição e crase precisa incluir demonstrativos e relativos, para não parecer restrita a substantivo feminino com artigo.

### 2.4 Regra sem exemplo / exemplo sem explicação

- muitos tópicos têm apenas um exemplo curto;
- quase não há **pares mínimos**, isto é, duas frases que mudam um único elemento decisivo;
- os exemplos raramente são seguidos por explicação do motivo da correção/erro;
- faltam casos-limite que mostrem quando uma regra aparentemente semelhante produz resultado diferente.

### 2.5 Distinções críticas ausentes

Precisam ganhar tratamento explícito:

- literalidade x inferência x extrapolação;
- fato textual x opinião do autor x fala citada;
- tema x tese x argumento;
- causa x explicação;
- consequência x conclusão;
- condição x concessão;
- restrição x explicação em oração adjetiva;
- sentido próprio x sentido figurado;
- classe morfológica x função/valor contextual;
- sujeito indeterminado x oração sem sujeito;
- `se` apassivador x índice de indeterminação;
- objeto direto x indireto na escolha de pronomes;
- regência verbal x regência nominal;
- preposição `a` x artigo `a` x crase;
- próclise obrigatória x colocação possível/preferencial;
- vírgula estrutural x vírgula facultativa por deslocamento curto;
- frase gramatical x reescrita semanticamente equivalente.

### 2.6 Exercícios

A versão 1.0.0 não contém bloco robusto de prática autoral com perguntas e gabaritos estruturalmente separados. Isso falha diretamente o QA-5 do protocolo.

A 2.0.0 deve conter:

- microaplicações dentro das unidades;
- pares certo/errado;
- reescritas;
- miniquestões objetivas com cinco alternativas plausíveis;
- bloco cumulativo final;
- gabarito separado e comentado pelo elemento decisivo.

### 2.7 Sequência pedagógica

A estrutura atual acompanha grandes categorias úteis, mas separa tópicos que precisam conversar mais. A reconstrução deve:

1. começar por leitura, inferência e arquitetura textual;
2. tratar coesão e relações de sentido antes da gramática normativa;
3. colocar classes de palavras como ponte para concordância, regência e pontuação;
4. integrar regência + pronomes + crase;
5. integrar sintaxe + pontuação + reescrita;
6. terminar com estratégia de alternativa e prática cumulativa.

### 2.8 Utilidade para NotebookLM

Problemas da 1.0.0:

- baixa variedade de exemplos reduz a geração de perguntas de aplicação;
- vários tópicos são listas, dificultando explicações intermediárias;
- conceitos confundíveis nem sempre estão na mesma seção;
- não há corpus de exercícios autorais suficiente;
- metadiscurso sobre VUNESP, estratégia de prova e NotebookLM ocupa espaço que poderia ser conteúdo didático.

### 2.9 Redundância e metadiscurso

Há repetição da ideia de “alternativa quase correta”, “preservação de sentido” e “VUNESP” em diversos pontos. Esses princípios devem permanecer, mas ser incorporados à didática sem transformar a apostila em relatório da banca.

A seção `USO NO NOTEBOOKLM` e referências internas de engenharia editorial não pertencem ao corpus final do estudante na 2.0.0. A configuração do tutor já está isolada em `METODOLOGIA_NOTEBOOKLM.md`.

## 3. Decisão editorial para 2.0.0

A versão 2.0.0 será uma **reconstrução**, não uma expansão incremental da 1.0.0.

Será preservado seletivamente apenas o que continua didaticamente útil:

- distinção literalidade/inferência/extrapolação;
- método de testar reescrita por `gramática + sentido`;
- tabelas de relações lógico-semânticas como base, com ampliação;
- regra operacional `regência antes da crase`;
- atenção a alternativas com erro localizado.

Todo o restante será reorganizado pelo novo sumário e pela matriz de autoria.
