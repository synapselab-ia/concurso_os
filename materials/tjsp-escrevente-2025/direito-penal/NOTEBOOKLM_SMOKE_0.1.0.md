# NOTEBOOKLM_SMOKE_0.1.0 - Direito Penal - TJSP Escrevente 2025

**Data:** `2026-09-14`  
**Pack:** `direito-penal`  
**Versao testada:** `0.1.0-rc.1`  
**Fonte do notebook:** somente `APOSTILA.pdf` canonico  
**Configuracao da conversa:** bloco operacional de `METODOLOGIA_NOTEBOOKLM.md`  
**Resultado:** `PASS_WITH_OBSERVATIONS`

## Escopo do smoke

O teste real cobriu:

- chat explicativo;
- treino interativo objetivo;
- Teste do Estudio;
- Cartoes;
- Mapa mental;
- pergunta de limite epistemologico sobre jurisprudencia.

## Resultado observado

### Chat explicativo - PASS

Pergunta de contraste entre concussao e corrupcao passiva foi respondida com os arts. 316 e 317, distinguindo corretamente `exigir` de `solicitar`, `receber` ou `aceitar promessa`, com exemplos curtos e criterio decisivo adequado.

### Treino interativo - PASS

O tutor:

- apresentou uma questao por vez;
- nao revelou o gabarito antes da tentativa;
- aguardou a resposta do estudante;
- corrigiu a alternativa escolhida;
- explicou a alternativa correta e os distratores;
- identificou o elemento juridico decisivo;
- ofereceu reteste somente depois da correcao.

### Teste do Estudio - PASS na amostra observada

As questoes observadas permaneceram dentro do corpus e testaram adequadamente arts. 293, 302 e 313-A, sem evidencia de conteudo estranho ao recorte.

### Cartoes - PASS na amostra observada

Os cartoes observados recuperaram corretamente nucleos, regras e penas do art. 293 e foram adequados para revisao curta.

### Mapa mental - PASS_WITH_OBSERVATION

A hierarquia juridica e os grandes blocos do conteudo ficaram corretos e uteis. O mapa, porem, exibiu identificadores internos `DP-01`, `DP-02` etc., porque esses identificadores aparecem nos proprios titulos do StudentContent.

Classificacao: observacao cosmetica/de engenharia de corpus, nao erro juridico e nao bloqueio de release candidate.

Melhoria obrigatoria para os proximos SubjectPacks: identificadores de cobertura, IDs de matriz e outros rotulos de backoffice nao devem ser incluidos em titulos visiveis do StudentContent. A rastreabilidade deve permanecer em manifest, matriz, QA ou outro backoffice.

### Limite epistemologico sobre jurisprudencia - PASS_WITH_OBSERVATION

Ao ser perguntado se havia jurisprudencia importante para decorar, o tutor nao inventou precedentes e respeitou a fonte. A resposta, contudo, iniciou com uma negativa categorica (`Nao`) antes de explicar que a fonte nao traz jurisprudencia.

Classificacao: formulacao epistemica aperfeicoavel, sem alucinacao material e sem bloqueio.

Melhoria obrigatoria para os proximos SubjectPacks/configuracoes: quando a fonte nao sustentar uma afirmacao sobre o mundo externo, preferir formulacoes do tipo `a fonte selecionada nao traz essa informacao; com base apenas nela, nao posso afirmar...`, evitando transformar ausencia no corpus em inexistencia externa.

## Decisao de QA

O smoke real e aceito como `PASS_WITH_OBSERVATIONS`.

Nao sera criado `rc.2` apenas para remover os IDs `DP-*` dos titulos ou para refinar a frase inicial sobre jurisprudencia. Esses pontos nao alteram escopo, exatidao normativa, utilidade principal do tutor, Teste, Cartoes ou hierarquia juridica do mapa.

As duas observacoes ficam registradas como melhoria de processo para os proximos SubjectPacks e devem ser consideradas antes de sua autoria/QA de NotebookLM.

## Evidencias fornecidas pelo usuario

Foram inspecionadas capturas de tela do Teste, Cartoes e Mapa mental, alem da transcricao das interacoes de chat e treino. O resultado acima se limita ao que foi efetivamente observado e nao presume testes nao executados.
