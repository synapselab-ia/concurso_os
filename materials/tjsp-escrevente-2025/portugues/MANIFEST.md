# MANIFEST — SubjectPack Português — TJSP Escrevente 2025

**Competition:** `tjsp-escrevente-2025`  
**Subject:** `portugues`  
**Pack version:** `1.0.3`  
**Status:** `content-rebuild-pending`  
**Release date:** `2026-09-11`

## Objetivo

Este pack separa o que é **conteúdo do estudante**, o que é **configuração do tutor** e o que é **backoffice**.

A versão `1.0.3` mantém a apostila/PDF atuais, mas melhora a instalação do NotebookLM: as instruções do chat deixam de ser carregadas como fonte e passam a ser usadas na configuração nativa da conversa (`Personalizado` ou equivalente).

A reconstrução qualitativa da apostila continua sendo a próxima ação canônica.

## Arquivos canônicos do pack

- `APOSTILA.md` — fonte autoral editável do material do estudante.
- `APOSTILA.pdf` — distribuição atual para o NotebookLM.
- `METODOLOGIA_NOTEBOOKLM.md` — configuração versionada do tutor no chat; **não é fonte de conteúdo**.
- `ANALISE_BANCA.md` — backoffice editorial.
- `SOURCES.md` — proveniência/backoffice.
- `CHANGELOG.md` — histórico de versão/backoffice.

## Apostila PDF atual

A versão `1.0.3` não altera o PDF. Ele continua sendo o artefato validado originalmente em `1.0.0`:

- páginas: `8`;
- tamanho: `13950 bytes`;
- SHA-256: `e203e62c6be1207dc5ca475e61460d9619be4bfeeeeb32bcf90990b485e8cc23`;
- Git blob: `2287be2ba025228cc311722effc794fc9edf476f`.

**Importante:** o PDF atual não é considerado qualidade final para replicação. `APOSTILA-002` deverá reconstruí-lo.

## Instalação no NotebookLM

### Fontes

Carregue como fonte, por padrão:

1. `APOSTILA.pdf`

Não carregar como fonte:

- `METODOLOGIA_NOTEBOOKLM.md`;
- `ANALISE_BANCA.md`;
- `MANIFEST.md`;
- `SOURCES.md`;
- `CHANGELOG.md`;
- edital/provas históricas apenas para dar contexto de projeto.

Esses documentos permanecem no GitHub/ChatGPT para análise, autoria, QA ou configuração.

### Configurar as conversas

Na interface observada do NotebookLM:

1. abrir `Configurar as conversas`;
2. escolher `Personalizado`;
3. copiar o bloco operacional de `METODOLOGIA_NOTEBOOKLM.md` para o campo de meta/estilo/papel;
4. manter `Tamanho da resposta = Padrão` inicialmente;
5. salvar.

Se os nomes da interface mudarem, usar o controle equivalente de instruções persistentes da conversa.

## Uso cotidiano

Depois da instalação:

- **Estúdio:** usar normalmente com a apostila como fonte;
- **Chat:** conversar normalmente; as instruções do tutor já ficam na configuração da conversa;
- não precisa marcar/desmarcar metodologia;
- não precisa citar TJSP/VUNESP a cada comando;
- não precisa administrar os arquivos de backoffice dentro do notebook.

Exemplos de chat:

- `não entendi este tópico`
- `me explica por que a B está errada`
- `me testa nisso`
- `faz mais uma questão`
- `resume meus acertos, erros e dúvidas desta sessão`

## O que os smoke tests mostraram

- Com a metodologia incluída no `Teste`, o NotebookLM gerou pergunta sobre a própria metodologia.
- Sem a metodologia, o `Teste` gerou pergunta conceitual diretamente baseada na apostila.
- No chat, a metodologia funcionou melhor: questão por vez, alternativas A–E, resposta + confiança e possibilidade de relatório da sessão.
- A interface do NotebookLM também oferece configuração personalizada da conversa, que é um canal mais apropriado para as instruções do tutor do que uma fonte documental.

## Múltiplos participantes

O mesmo SubjectPack pode alimentar notebooks separados para `p001`, `p002`, `p003` etc. O material é compartilhado; histórico pessoal pode permanecer isolado no notebook de cada participante.

## Próxima versão de conteúdo

A próxima mudança substancial deve reconstruir `APOSTILA.md` e `APOSTILA.pdf` para que sejam materiais fortes por si só e alimentem bem os recursos do NotebookLM.

Target recomendado após reconstrução: `2.0.0`.

## Atualização

Quando o pack mudar:

- se mudar `APOSTILA.pdf`, substituir a fonte no notebook;
- se mudar `METODOLOGIA_NOTEBOOKLM.md`, atualizar a configuração personalizada da conversa;
- se mudar apenas backoffice, nenhuma ação no NotebookLM é necessária.

## Limites

- não implementa mastery questão a questão;
- não mistura participantes;
- não presume que `Teste` nativo simula automaticamente a banca;
- não transforma backoffice em conteúdo de estudo;
- não transforma instruções de chat em fonte estudável;
- detalhes da UI do NotebookLM podem mudar.
