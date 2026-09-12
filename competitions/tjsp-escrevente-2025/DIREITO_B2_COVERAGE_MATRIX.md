# DIREITO B2 — Matriz de cobertura e autoria

**Competition:** `tjsp-escrevente-2025`  
**Gate:** `DIREITO-004`  
**Matrix status:** `closed`  
**Row status:** `planned` — a matriz está fechada; a redação ainda não começou.  
**Authority:** `SRC-TJSP-EDITAL-2025-02` / `SYLLABUS.md`  
**Normative baseline:** `2025-07-29`, conforme `DIREITO_SOURCES.md`  
**Banca evidence:** `DIREITO_B2_BANCA_ANALYSIS.md`

## 1. Contrato da matriz

Esta matriz é o contrato de cobertura para as seis apostilas de B2. Ela não altera o edital, não transforma frequência histórica em previsão e não absorve silenciosamente legislação posterior ao cutoff.

Cada linha contém: `coverage_id`, `pack`, `source_id`, recorte exato, tema/objetivo de aprendizagem, forma pedagógica principal, contraste/risco, sinal empírico da banca, risco de versão, profundidade e requisito de prática/QA.

### Códigos de forma

- `EXP` — exposição estruturada;
- `CMP` — quadro comparativo;
- `FLX` — fluxo/sequência;
- `TAB` — tabela recuperável;
- `CAS` — mini-caso aplicado;
- `LIN` — linha do tempo.

### Códigos de banca

- `B-PEN` — tipos próximos, elemento/requisito decisivo e mini-casos;
- `B-PP` — sujeitos, etapas, decisões, recursos e prazos;
- `B-PC` — regra/exceção, competência, efeitos, JEC/JEFaz e casos curtos;
- `B-CF` — regra/exceção, pares conceituais, nacionalidade e servidores;
- `B-ADM` — hipótese→requisito→efeito, disciplina e modalidade→sanção;
- `B-LI` — texto operacional, sujeitos, condições, prazos e aderência de versão;
- `B-Ø` — sem evidência histórica específica suficiente; não reduzir profundidade por isso.

### Códigos de prática/QA

- `Q-LIT` — conferir texto-base, requisito, exceção e consequência; mínimo de 2 microitens A–E;
- `Q-CAS` — mínimo de 3 mini-casos com mudança de um único elemento decisivo;
- `Q-CMP` — quadro de diferenças + mínimo de 3 pares de alternativas plausíveis;
- `Q-FLX` — sequência/fluxo reproduzível + mínimo de 3 armadilhas de etapa/prazo/recurso;
- `Q-VER` — QA de versão obrigatório contra `DIREITO_SOURCES.md`; não absorver drift sem nota deliberada;
- `Q-FULL` — QA de cobertura: todos os dispositivos, subseções ou anexos do recorte devem ser rastreáveis no texto final.

Profundidade: `alta`, `média` ou `base`. `B-Ø` nunca justifica omissão: o edital continua soberano.

---

# 2. `direito-penal`

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| DP-01 | direito-penal | SRC-B2-CP | arts. 293–295 | papéis públicos e petrechos → identificar núcleo, objeto, sujeito e majorante/regra associada | EXP+CMP+CAS | falsificação x petrechos; qualidade funcional | B-PEN | baseline estável | alta | Q-LIT+Q-CAS+Q-CMP |
| DP-02 | direito-penal | SRC-B2-CP | arts. 296–305 | falsidades documental/material/ideológica, certidões, atestados, uso e supressão → reconhecer o tipo pelo elemento decisivo | EXP+CMP+CAS | documento público x particular; falsificar x usar x suprimir; conteúdo x materialidade | B-PEN | baseline estável | alta | Q-LIT+Q-CAS+Q-CMP |
| DP-03 | direito-penal | SRC-B2-CP | arts. 307–308 | falsa identidade e uso/cessão de documento de identidade alheio → separar identidade declarada de documento alheio | CMP+CAS | art. 307 x art. 308 | B-PEN | baseline estável | alta | Q-CMP+Q-CAS |
| DP-04 | direito-penal | SRC-B2-CP | art. 311-A | fraude em certame de interesse público → identificar objeto protegido, verbos, finalidade e consequências | EXP+CAS | divulgação/utilização indevida; finalidade; agente | B-PEN | baseline estável | alta | Q-LIT+Q-CAS |
| DP-05 | direito-penal | SRC-B2-CP | arts. 312–317 | crimes funcionais nucleares → distinguir peculato, inserção/alteração de dados, extravio/inutilização, emprego irregular, concussão/excesso e corrupção passiva | CMP+CAS | tipos funcionais vizinhos; dolo/finalidade; sujeito ativo | B-PEN | baseline estável | alta | Q-LIT+Q-CMP+Q-CAS |
| DP-06 | direito-penal | SRC-B2-CP | arts. 319–327 | prevaricação e demais crimes funcionais do intervalo → reconhecer requisito subjetivo, conduta e consequência | EXP+CMP+CAS | prevaricação x condescendência x advocacia administrativa e vizinhos | B-PEN | baseline estável | alta | Q-LIT+Q-CMP+Q-CAS |
| DP-07 | direito-penal | SRC-B2-CP | arts. 328–333 | crimes praticados por particular contra a Administração → separar usurpação, resistência, desobediência, desacato, tráfico de influência e corrupção ativa | CMP+CAS | sujeito; violência/ameaça; vantagem; influência | B-PEN | baseline estável | alta | Q-LIT+Q-CMP+Q-CAS |
| DP-08 | direito-penal | SRC-B2-CP | arts. 336 e 337 | inutilização de edital/sinal e subtração/inutilização de livro ou documento → identificar objeto material e conduta | CMP+CAS | objeto e verbo do tipo | B-PEN | baseline estável; art. 338-A posterior está fora do recorte | média | Q-LIT+Q-CAS |
| DP-09 | direito-penal | SRC-B2-CP | arts. 339–347 | crimes contra a Administração da Justiça → diferenciar denunciação, comunicação falsa, autoacusação, falso testemunho/perícia, corrupção de testemunha, coação e fraude processual | CMP+CAS | tipos muito próximos; falsidade da imputação; sujeito; finalidade | B-PEN | baseline estável | alta | Q-LIT+Q-CMP+Q-CAS |
| DP-10 | direito-penal | SRC-B2-CP | arts. 357 e 359 | exploração de prestígio e desobediência a decisão judicial sobre perda/suspensão de direito → reconhecer hipótese e consequência | CMP+CAS | vantagem/influência x descumprimento de decisão | B-PEN | baseline estável | média | Q-LIT+Q-CAS |

**Ledger Penal:** `293–305 + 307 + 308 + 311-A + 312–317 + 319–333 + 336 + 337 + 339–347 + 357 + 359` → 100% mapeado em DP-01…DP-10.

---

# 3. `direito-processual-penal`

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| DPP-01 | direito-processual-penal | SRC-B2-CPP | arts. 251–258 | juiz, impedimento, suspeição e funções institucionais do intervalo → reconhecer causa, efeito e extensão | CMP+CAS | impedimento x suspeição; juiz x MP/serventuário | B-PP | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPP-02 | direito-processual-penal | SRC-B2-CPP | arts. 261–267 | acusado e defensor → identificar defesa técnica, substituição, abandono e limites de atuação | EXP+CMP+CAS | defesa pessoal x técnica; escolha x nomeação | B-PP | baseline | alta | Q-LIT+Q-CAS |
| DPP-03 | direito-processual-penal | SRC-B2-CPP | art. 274 | extensão de impedimentos/incompatibilidades no dispositivo → saber a quem e como se aplica | EXP+CMP | sujeito alcançado x regra do juiz | B-PP | baseline | média | Q-LIT+Q-CMP |
| DPP-04 | direito-processual-penal | SRC-B2-CPP | arts. 351–369 | citações → escolher modalidade, requisitos, hipóteses e efeitos | FLX+TAB+CAS | pessoal/edital/hora certa/cartas; revelia e comparecimento | B-PP | baseline | alta | Q-FLX+Q-LIT+Q-CAS |
| DPP-05 | direito-processual-penal | SRC-B2-CPP | arts. 370–372 | intimações → reconhecer destinatário, forma e efeito | FLX+TAB | citação x intimação; acusado x defensor/MP | B-PP | baseline | alta | Q-FLX+Q-LIT |
| DPP-06 | direito-processual-penal | SRC-B2-CPP | arts. 394–405 | procedimento comum: espécies e fase inicial → selecionar rito, resposta, rejeição e absolvição sumária | FLX+CMP+CAS | rito ordinário/sumário; rejeição x absolvição | B-PP | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DPP-07 | direito-processual-penal | SRC-B2-CPP | arts. 406–421 | júri: primeira fase → ordenar acusação, instrução e decisões de encerramento | FLX+CMP+CAS | pronúncia x impronúncia x absolvição sumária x desclassificação | B-PP | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DPP-08 | direito-processual-penal | SRC-B2-CPP | arts. 422–431 | júri: preparação, desaforamento e pauta → reconhecer atos, legitimados e momento | FLX+TAB | preparação x desaforamento; ordem/pauta | B-PP | baseline | média | Q-FLX+Q-LIT |
| DPP-09 | direito-processual-penal | SRC-B2-CPP | arts. 432–452 | jurados e Conselho de Sentença → dominar composição, sorteio, impedimentos e formação | TAB+CMP+CAS | jurado apto x impedido; composição do conselho | B-PP | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPP-10 | direito-processual-penal | SRC-B2-CPP | arts. 453–474 | sessão plenária e instrução → ordenar instalação, atos e prova em plenário | FLX+CAS | etapa/sujeito/ordem | B-PP | baseline | alta | Q-FLX+Q-CAS |
| DPP-11 | direito-processual-penal | SRC-B2-CPP | arts. 475–491 | debates, quesitação e votação → entender ordem, limites e decisão dos jurados | FLX+CMP | debate x quesito; ordem de votação | B-PP | baseline | alta | Q-FLX+Q-CMP |
| DPP-12 | direito-processual-penal | SRC-B2-CPP | arts. 492–497 | sentença, ata e atribuições finais/presidenciais → ligar resultado do júri ao ato judicial correspondente | FLX+TAB | decisão dos jurados x sentença do juiz-presidente | B-PP | baseline | média | Q-LIT+Q-FLX |
| DPP-13 | direito-processual-penal | SRC-B2-CPP | arts. 531–538 | procedimento sumário → reproduzir sequência, prazos e diferenças do ordinário | FLX+CMP+CAS | ordinário x sumário | B-PP | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DPP-14 | direito-processual-penal | SRC-B2-CPP | arts. 541–548 | restauração de autos extraviados/destruídos → reconhecer iniciativa, reconstrução e efeitos | FLX+EXP | restauração x recurso/procedimento principal | B-PP | baseline | média | Q-FLX+Q-LIT |
| DPP-15 | direito-processual-penal | SRC-B2-CPP | arts. 574–580 | recursos: regras gerais → identificar voluntariedade, legitimidade, extensão e efeitos | EXP+CMP | recurso cabível x efeito; parte legitimada | B-PP | baseline | alta | Q-LIT+Q-CMP |
| DPP-16 | direito-processual-penal | SRC-B2-CPP | arts. 581–592 | recurso em sentido estrito → mapear hipóteses, processamento e efeitos | TAB+FLX+CAS | RESE x apelação/outro meio | B-PP | **art. 584 §4: baseline 2025-07-29; alteração pela Lei 15.358/2026 separada** | alta | Q-FLX+Q-CMP+Q-VER |
| DPP-17 | direito-processual-penal | SRC-B2-CPP | arts. 593–603 | apelação → reconhecer cabimento, razões, processamento e efeitos | TAB+FLX+CAS | apelação x RESE; júri x juiz singular | B-PP | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DPP-18 | direito-processual-penal | SRC-B2-CPP | arts. 604–620 | processamento/julgamento recursal e meios do intervalo → identificar sequência, competência e efeito sem extrapolar o texto | FLX+TAB | meio recursal/efeito/órgão competente | B-PP | baseline | média | Q-FULL+Q-FLX |
| DPP-19 | direito-processual-penal | SRC-B2-CPP | arts. 621–631 | revisão criminal → reconhecer hipóteses, legitimidade, competência e efeitos | CMP+FLX+CAS | revisão x recurso; efeito favorável x agravamento | B-PP | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPP-20 | direito-processual-penal | SRC-B2-CPP | arts. 632–646 | meios de impugnação do intervalo, incluindo carta testemunhável → reconhecer cabimento e processamento | FLX+CMP | carta testemunhável x recurso negado/outros meios | B-PP | baseline | média | Q-FULL+Q-FLX+Q-CMP |
| DPP-21 | direito-processual-penal | SRC-B2-CPP | arts. 647–667 | habeas corpus → identificar coação, legitimidade, competência, rito e decisão | FLX+CAS+CMP | HC x recurso/revisão; ameaça x coação consumada | B-PP | baseline | alta | Q-LIT+Q-FLX+Q-CAS |
| DPP-22 | direito-processual-penal | SRC-B2-L9099 | arts. 60–68 | JECrim: competência, princípios e atos iniciais/comunicação → reconhecer quando incide o microssistema | EXP+TAB+CAS | JECrim x rito comum; competência e comunicação | B-PP | baseline estável | alta | Q-LIT+Q-CAS |
| DPP-23 | direito-processual-penal | SRC-B2-L9099 | arts. 69–76 | fase preliminar, composição civil e transação penal → ordenar soluções consensuais e efeitos | FLX+CMP+CAS | composição x transação; representação/ação | B-PP | baseline estável | alta | Q-FLX+Q-CMP+Q-CAS |
| DPP-24 | direito-processual-penal | SRC-B2-L9099 | arts. 77–83 | procedimento sumaríssimo e recursos do intervalo → reproduzir denúncia/queixa, audiência, sentença e impugnação | FLX+TAB | sumaríssimo x comum; recurso/prazo | B-PP | baseline estável | alta | Q-FLX+Q-LIT |
| DPP-25 | direito-processual-penal | SRC-B2-L9099 | arts. 88–89 | representação e suspensão condicional do processo → reconhecer requisitos, prazo de prova e consequências | CMP+CAS+LIN | representação x ação incondicionada; suspensão x transação | B-PP | baseline estável | alta | Q-LIT+Q-CMP+Q-CAS |

**Ledger Processual Penal:** CPP `251–258 + 261–267 + 274 + 351–372 + 394–497 + 531–538 + 541–548 + 574–667` e Lei 9.099/1995 `60–83 + 88–89` → 100% mapeados em DPP-01…DPP-25.

---

# 4. `direito-processual-civil`

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| DPC-01 | direito-processual-civil | SRC-B2-CPC | arts. 144–155 | impedimento/suspeição e auxiliares da Justiça → reconhecer sujeitos, causas, deveres e responsabilidade | CMP+CAS | juiz x auxiliar; impedimento x suspeição | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-02 | direito-processual-civil | SRC-B2-CPC | arts. 188–211 | forma, documentação e prática dos atos processuais → reconhecer validade, instrumentalidade e registro | EXP+TAB | forma legal x validade; ato físico x eletrônico | B-PC | **art. 196: baseline do cutoff; alteração pela Lei 15.479/2026 separada** | média | Q-LIT+Q-VER |
| DPC-03 | direito-processual-civil | SRC-B2-CPC | arts. 212–217 | tempo e lugar dos atos → identificar horários, dias e exceções | TAB+CAS | regra temporal x urgência/exceção | B-PC | baseline | alta | Q-LIT+Q-CAS |
| DPC-04 | direito-processual-civil | SRC-B2-CPC | arts. 218–235 | prazos processuais → calcular início, suspensão, restituição e consequências | LIN+TAB+CAS | prazo legal/judicial; justa causa; contagem | B-PC | baseline | alta | Q-LIT+Q-CAS |
| DPC-05 | direito-processual-civil | SRC-B2-CPC | arts. 236–275 | comunicação dos atos: citação, intimação e cartas → escolher modalidade, momento e efeito | FLX+CMP+CAS | citação x intimação; meio eletrônico x demais; nulidade | B-PC | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DPC-06 | direito-processual-civil | SRC-B2-CPC | arts. 294–311 | tutela provisória → distinguir urgência/evidência, cautelar/antecipada e antecedente/incidental | CMP+FLX+CAS | tutela cautelar x antecipada; estabilização/revogação | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-07 | direito-processual-civil | SRC-B2-CPC | arts. 318–331 | procedimento comum e petição inicial → estruturar pedido, requisitos, emenda e resposta inicial do juízo | FLX+TAB+CAS | pedido/requisito/indeferimento; procedimento comum x especial | B-PC | baseline | alta | Q-FLX+Q-CAS |
| DPC-08 | direito-processual-civil | SRC-B2-CPC | arts. 332–333 | improcedência liminar e estado normativo do intervalo → reconhecer hipótese e efeito | CMP+CAS | improcedência liminar x indeferimento inicial x julgamento posterior | B-PC | baseline | média | Q-LIT+Q-CAS+Q-FULL |
| DPC-09 | direito-processual-civil | SRC-B2-CPC | art. 334 | audiência de conciliação/mediação → reconhecer designação, dispensa, comparecimento e consequências | FLX+CAS | dispensa x ausência; conciliação x instrução | B-PC | baseline | alta | Q-LIT+Q-CAS |
| DPC-10 | direito-processual-civil | SRC-B2-CPC | arts. 335–342 | contestação e matérias defensivas → ordenar prazo, concentração e alegações | FLX+TAB | preliminar x mérito; ônus do réu | B-PC | baseline | alta | Q-FLX+Q-LIT |
| DPC-11 | direito-processual-civil | SRC-B2-CPC | art. 343 | reconvenção → reconhecer cabimento, sujeitos e relação com contestação | CMP+CAS | reconvenção x defesa/ação autônoma | B-PC | baseline | média | Q-LIT+Q-CAS |
| DPC-12 | direito-processual-civil | SRC-B2-CPC | arts. 344–346 | revelia e efeitos → identificar quando incidem e exceções | CMP+CAS | revelia x confissão; regra x exceção | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-13 | direito-processual-civil | SRC-B2-CPC | arts. 347–357 | providências preliminares e saneamento → ligar controvérsia à decisão de organização do processo | FLX+TAB | julgamento imediato x saneamento/instrução | B-PC | baseline | alta | Q-FLX+Q-CAS |
| DPC-14 | direito-processual-civil | SRC-B2-CPC | arts. 358–368 | audiência de instrução e julgamento → ordenar atos, sujeitos e encerramento | FLX+CAS | conciliação x instrução; ordem dos atos | B-PC | baseline | média | Q-FLX+Q-CAS |
| DPC-15 | direito-processual-civil | SRC-B2-CPC | arts. 369–380 | teoria geral da prova → reconhecer admissibilidade, ônus, poderes e preservação | EXP+CMP+CAS | ônus estático/dinâmico; prova lícita/ilícita | B-PC | baseline | alta | Q-LIT+Q-CAS |
| DPC-16 | direito-processual-civil | SRC-B2-CPC | arts. 381–383 | produção antecipada da prova → reconhecer hipóteses, competência e efeitos | FLX+CAS | antecipada x prova no curso do processo | B-PC | baseline | alta | Q-LIT+Q-CAS |
| DPC-17 | direito-processual-civil | SRC-B2-CPC | art. 384 | ata notarial → compreender função e valor probatório | EXP+CAS | ata x prova testemunhal/documental comum | B-PC | baseline | base | Q-LIT+Q-CAS |
| DPC-18 | direito-processual-civil | SRC-B2-CPC | arts. 385–395 | depoimento pessoal e confissão → reconhecer sujeitos, recusa, indivisibilidade e efeitos | CMP+CAS | depoimento x confissão; confissão x revelia | B-PC | baseline | média | Q-LIT+Q-CMP+Q-CAS |
| DPC-19 | direito-processual-civil | SRC-B2-CPC | arts. 396–404 | exibição de documento ou coisa → identificar dever, procedimento e consequência da recusa | FLX+CAS | exibição x produção documental espontânea | B-PC | baseline | média | Q-FLX+Q-CAS |
| DPC-20 | direito-processual-civil | SRC-B2-CPC | arts. 405–438 | prova documental → dominar força probante, arguição, juntada e documentos | EXP+TAB+CAS | público x particular; autenticidade/falsidade; momento de juntada | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-21 | direito-processual-civil | SRC-B2-CPC | arts. 439–441 | documentos eletrônicos → reconhecer requisitos de utilização e valor | EXP+CMP | eletrônico x físico; autenticidade | B-PC | baseline | média | Q-LIT+Q-CMP |
| DPC-22 | direito-processual-civil | SRC-B2-CPC | arts. 442–463 | prova testemunhal → identificar admissibilidade, impedimentos/suspeições, rol e oitiva | FLX+TAB+CAS | testemunha x informante; prazo/ordem | B-PC | baseline | alta | Q-LIT+Q-FLX+Q-CAS |
| DPC-23 | direito-processual-civil | SRC-B2-CPC | arts. 464–480 | prova pericial → reconhecer cabimento, perito, assistentes, quesitos, laudo e esclarecimentos | FLX+TAB+CAS | perito x assistente; perícia x prova técnica simplificada | B-PC | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DPC-24 | direito-processual-civil | SRC-B2-CPC | arts. 481–484 | inspeção judicial → identificar objeto, iniciativa e documentação | EXP+CAS | inspeção x perícia | B-PC | baseline | base | Q-LIT+Q-CAS |
| DPC-25 | direito-processual-civil | SRC-B2-CPC | arts. 485–495 | sentença, extinção, fundamentação e efeitos → distinguir resolução ou não do mérito e requisitos decisórios | CMP+CAS | art. 485 x 487; decisão x fundamentação/efeito | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-26 | direito-processual-civil | SRC-B2-CPC | art. 496 | remessa necessária → reconhecer hipóteses e exceções | CMP+CAS | remessa necessária x recurso voluntário | B-PC | baseline | média | Q-LIT+Q-CAS |
| DPC-27 | direito-processual-civil | SRC-B2-CPC | arts. 497–501 | tutela específica e obrigações → ligar tipo de obrigação à técnica executiva/efeito | CMP+CAS | fazer/não fazer/entregar; conversão/perdas | B-PC | baseline | alta | Q-LIT+Q-CAS |
| DPC-28 | direito-processual-civil | SRC-B2-CPC | arts. 502–508 | coisa julgada → reconhecer limites objetivos/subjetivos e questões alcançadas | CMP+CAS | coisa julgada x preclusão; questão principal x prejudicial | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-29 | direito-processual-civil | SRC-B2-CPC | arts. 509–512 | liquidação de sentença → escolher modalidade e limites | FLX+CMP+CAS | liquidação x cumprimento; arbitramento x procedimento comum | B-PC | baseline | média | Q-FLX+Q-CMP+Q-CAS |
| DPC-30 | direito-processual-civil | SRC-B2-CPC | arts. 513–538 | cumprimento de sentença nas modalidades do intervalo → ordenar requerimento, defesa, alimentos, Fazenda, fazer/não fazer e entregar coisa | FLX+TAB+CAS | modalidade executiva; impugnação; prisão/expropriação; Fazenda | B-PC | **art. 529-A inexistente no baseline; inserção pela Lei 15.479/2026 rastreada separadamente** | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| DPC-31 | direito-processual-civil | SRC-B2-CPC | arts. 994–1008 | sistema recursal: espécies e regras gerais → dominar legitimidade, efeitos, desistência, preparo e prazo | TAB+CMP+CAS | recurso x sucedâneo; desistência x renúncia; efeito | B-PC | **art. 998: baseline do cutoff; alteração pela Lei 15.484/2026 separada** | alta | Q-LIT+Q-CMP+Q-VER |
| DPC-32 | direito-processual-civil | SRC-B2-CPC | arts. 1009–1014 | apelação → reconhecer cabimento, questões devolvidas e processamento | FLX+CAS | apelação x agravo; efeito suspensivo/exceção | B-PC | baseline | alta | Q-FLX+Q-CAS |
| DPC-33 | direito-processual-civil | SRC-B2-CPC | arts. 1015–1020 | agravo de instrumento → identificar hipóteses e procedimento | TAB+FLX+CAS | agravo x apelação | B-PC | baseline | alta | Q-LIT+Q-FLX+Q-CAS |
| DPC-34 | direito-processual-civil | SRC-B2-CPC | art. 1021 | agravo interno → reconhecer cabimento, processamento e efeito | FLX+CMP | agravo interno x instrumento | B-PC | baseline | média | Q-LIT+Q-CMP |
| DPC-35 | direito-processual-civil | SRC-B2-CPC | arts. 1022–1026 | embargos de declaração → reconhecer vícios, prazo, efeitos e integração da decisão | CMP+CAS | omissão/contradição/obscuridade/erro material; efeito modificativo | B-PC | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-36 | direito-processual-civil | SRC-B2-L9099 | arts. 3–4 | competência do JEC e foro → aplicar valor/matéria/exclusões e critério territorial | TAB+CAS | JEC x rito comum; competência material/territorial | B-PC | baseline estável | alta | Q-LIT+Q-CAS |
| DPC-37 | direito-processual-civil | SRC-B2-L9099 | arts. 5–7 | juiz, conciliadores e auxiliares → reconhecer poderes e funções | CMP+CAS | juiz x conciliador/juiz leigo | B-PC | baseline estável | média | Q-LIT+Q-CMP |
| DPC-38 | direito-processual-civil | SRC-B2-L9099 | arts. 8–11 | partes, capacidade, representação e intervenção → identificar quem pode demandar e como | TAB+CAS | pessoa admitida x excluída; advogado/representação | B-PC | baseline estável | alta | Q-LIT+Q-CAS |
| DPC-39 | direito-processual-civil | SRC-B2-L9099 | arts. 12–13 | atos processuais no JEC → dominar simplicidade, registro e validade | EXP+TAB | formalismo comum x simplicidade do JEC | B-PC | baseline estável | média | Q-LIT+Q-CMP |
| DPC-40 | direito-processual-civil | SRC-B2-L9099 | arts. 14–17 | pedido, sessão e conciliação → ordenar instauração e audiência | FLX+CAS | pedido oral/escrito; conciliação x instrução | B-PC | baseline estável | alta | Q-FLX+Q-CAS |
| DPC-41 | direito-processual-civil | SRC-B2-L9099 | arts. 18–19 | citação e intimações no JEC → reconhecer forma e restrições | CMP+CAS | citação x intimação; meio admitido x vedado | B-PC | baseline estável | alta | Q-LIT+Q-CAS |
| DPC-42 | direito-processual-civil | SRC-B2-L12153 | arts. 1–2 | JEFaz: sistema, competência, limite e exclusões → decidir se a causa pertence ao juizado | TAB+CAS | JEFaz x Fazenda comum/JEC; competência absoluta | B-PC | baseline estável | alta | Q-LIT+Q-CMP+Q-CAS |
| DPC-43 | direito-processual-civil | SRC-B2-L12153 | arts. 3–5 | tutela, recorribilidade e partes → reconhecer providência urgente, recurso e legitimidade | CMP+CAS | tutela interlocutória x sentença; autor/réu admitido | B-PC | baseline estável | alta | Q-LIT+Q-CAS |
| DPC-44 | direito-processual-civil | SRC-B2-L12153 | arts. 6–11 | comunicações, prazos, representação, documentos, prova técnica e remessa necessária → dominar regras processuais especiais | TAB+FLX+CAS | prazo comum x Fazenda; reexame necessário x inexistência | B-PC | baseline estável | alta | Q-FULL+Q-FLX+Q-CAS |
| DPC-45 | direito-processual-civil | SRC-B2-L12153 | arts. 12–13 | cumprimento de obrigações e pagamento/RPV/precatório → escolher forma executiva e limites | FLX+CMP+CAS | fazer/entregar x pagar; RPV x precatório; fracionamento | B-PC | baseline estável | alta | Q-FLX+Q-CMP+Q-CAS |
| DPC-46 | direito-processual-civil | SRC-B2-L12153 | arts. 14–17 | instalação, conciliadores/juízes leigos e Turmas Recursais → reconhecer estrutura e funções | TAB+CMP | conciliador x juiz leigo x juiz; turma recursal | B-PC | baseline estável | média | Q-LIT+Q-CMP |
| DPC-47 | direito-processual-civil | SRC-B2-L12153 | arts. 18–21 | uniformização e recurso extraordinário → reproduzir hipóteses e processamento | FLX+CMP+CAS | divergência estadual/federal; uniformização x RE | B-PC | baseline estável | alta | Q-FLX+Q-CMP+Q-CAS |
| DPC-48 | direito-processual-civil | SRC-B2-L12153 | arts. 22–28 | implantação, transição, suporte, subsidiariedade e vigência → conhecer regras institucionais/finais | EXP+TAB | regra transitória x regra permanente; aplicação subsidiária | B-Ø | baseline estável | base | Q-LIT+Q-FULL |

**Ledger Processual Civil:** CPC `144–155 + 188–275 + 294–311 + 318–538 + 994–1026`; Lei 9.099/1995 `3–19`; Lei 12.153/2009 `integral (arts. 1–28)` → 100% mapeados em DPC-01…DPC-48.

---

# 5. `direito-constitucional`

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| DC-01 | direito-constitucional | SRC-B2-CF88 | Título II, Cap. I — art. 5º | direitos e deveres individuais/coletivos e garantias → reconhecer regra, exceção, remédio e proteção aplicável | CMP+CAS+TAB | liberdade/garantia/remédio; reserva legal; exceções | B-CF | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DC-02 | direito-constitucional | SRC-B2-CF88 | Título II, Cap. II — arts. 6–11 | direitos sociais, trabalhadores, associação profissional e sindical → aplicar direitos, limites e exceções | CMP+CAS | direito social x garantia individual; regra x exceção sindical/trabalhista | B-CF | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DC-03 | direito-constitucional | SRC-B2-CF88 | Título II, Cap. III — arts. 12–13 | nacionalidade e símbolos/idioma → distinguir brasileiro nato/naturalizado, aquisição, perda e cargos reservados | CMP+CAS | nato x naturalizado; hipótese de aquisição/perda; cargo privativo | B-CF | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DC-04 | direito-constitucional | SRC-B2-CF88 | Título III, Cap. VII, Seção I — arts. 37–38 | Administração Pública: princípios, cargos, concurso, remuneração, acumulação e mandato eletivo → aplicar regra e exceções | TAB+CMP+CAS | cargo/emprego/função; acumulação; teto; mandato | B-CF | **art. 37, XVI, b: usar redação de 2025-07-29; EC 138/2025 é drift posterior** | alta | Q-LIT+Q-CMP+Q-CAS+Q-VER |
| DC-05 | direito-constitucional | SRC-B2-CF88 | Título III, Cap. VII, Seção II — arts. 39–41 | servidores públicos: regime, remuneração, previdência/estabilidade e perda do cargo → reconhecer condições e efeitos | CMP+CAS+LIN | efetividade x estabilidade; aposentadoria/regime; perda do cargo | B-CF | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DC-06 | direito-constitucional | SRC-B2-CF88 | art. 92 | órgãos do Poder Judiciário → identificar composição constitucional sem confundir órgãos externos | TAB+CMP | órgão do Judiciário x função essencial/órgão não listado | B-CF | baseline | média | Q-LIT+Q-CMP |

**Ledger Constitucional:** Título II, Caps. I–III; Título III, Cap. VII, Seções I–II; art. 92 → 100% mapeados em DC-01…DC-06.

---

# 6. `direito-administrativo`

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| DA-01 | direito-administrativo | SRC-B2-L10261 | arts. 1–10 | disposições iniciais, cargo e funcionário → dominar conceitos-base do Estatuto | EXP+CMP | cargo x função; quadro/lotação | B-ADM | baseline | média | Q-LIT+Q-CMP |
| DA-02 | direito-administrativo | SRC-B2-L10261 | arts. 11–25 | provimento, nomeação, concurso e substituição → ordenar ingresso e substituição | FLX+TAB+CAS | nomeação/provimento/posse/exercício; substituição | B-ADM | baseline | alta | Q-FLX+Q-CAS |
| DA-03 | direito-administrativo | SRC-B2-L10261 | arts. 26–45 | formas de movimentação/provimento do intervalo → distinguir transferência, reintegração, reversão, aproveitamento, readaptação e remoção | CMP+CAS | institutos funcionais próximos | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-04 | direito-administrativo | SRC-B2-L10261 | arts. 46–55 | posse → reconhecer requisitos, prazo, autoridade e efeito | FLX+CAS | posse x exercício | B-ADM | baseline | alta | Q-LIT+Q-FLX+Q-CAS |
| DA-05 | direito-administrativo | SRC-B2-L10261 | arts. 56–75 | exercício, lotação e afastamentos do intervalo → aplicar início, interrupção e hipóteses de afastamento | LIN+TAB+CAS | posse x exercício; afastamento x falta | B-ADM | baseline | alta | Q-FULL+Q-CAS |
| DA-06 | direito-administrativo | SRC-B2-L10261 | arts. 76–86 | efetivo exercício, contagem funcional e vacância → reconhecer hipóteses, prazos e efeitos | TAB+LIN+CAS | efetivo exercício x ausência; vacância x afastamento | B-ADM | **art. 78: baseline contém licença-paternidade de 5 dias; Lei 18.473/2026 é drift posterior** | alta | Q-LIT+Q-CAS+Q-VER |
| DA-07 | direito-administrativo | SRC-B2-L10261 | arts. 171–175 | acumulações remuneradas → aplicar vedações, exceções, compatibilidade e consequência | CMP+CAS | acumulação lícita x ilícita; boa-fé | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-08 | direito-administrativo | SRC-B2-L10261 | arts. 239–240 | direito de petição → reconhecer legitimidade, acesso e garantias | EXP+CAS | petição x recurso disciplinar | B-ADM | baseline | média | Q-LIT+Q-CAS |
| DA-09 | direito-administrativo | SRC-B2-L10261 | arts. 241–244 | deveres e proibições → distinguir conduta devida, proibida e exceções | CMP+CAS | dever x proibição; condutas próximas | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-10 | direito-administrativo | SRC-B2-L10261 | arts. 245–250 | responsabilidades → relacionar esfera, dano e consequência | CMP+CAS | civil/administrativa/penal; independência e efeitos | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-11 | direito-administrativo | SRC-B2-L10261 | arts. 251–263 | penalidades, aplicação, competência e prescrição → ligar infração, sanção, autoridade e prazo | TAB+LIN+CAS | repreensão/suspensão/multa/demissões/cassação; competência; prescrição | B-ADM | baseline inclui alterações anteriores ao cutoff | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-12 | direito-administrativo | SRC-B2-L10261 | arts. 264–267 e dispositivos intercalares vigentes | providências preliminares, autocomposição, TAC e suspensão condicional da sindicância → escolher resposta adequada e condições | FLX+CMP+CAS | apuração preliminar x sindicância/PAD; TAC x suspensão condicional | B-ADM | baseline inclui LC 1.361/2021 e alterações anteriores | alta | Q-FULL+Q-FLX+Q-CAS |
| DA-13 | direito-administrativo | SRC-B2-L10261 | arts. 268–273 | disposições gerais do procedimento disciplinar, sindicância e PAD → decidir via de apuração e medidas | FLX+CMP+CAS | sindicância x processo administrativo | B-ADM | baseline | alta | Q-FLX+Q-CMP+Q-CAS |
| DA-14 | direito-administrativo | SRC-B2-L10261 | arts. 274–311 | processo administrativo disciplinar: instauração, comissão, instrução, defesa, relatório e julgamento → reproduzir fluxo e garantias | FLX+LIN+TAB+CAS | etapa, autoridade, testemunha, prazo, revelia/defesa | B-ADM | baseline | alta | Q-FULL+Q-FLX+Q-CAS |
| DA-15 | direito-administrativo | SRC-B2-L10261 | arts. 312–313 | recurso e pedido de reconsideração → reconhecer cabimento, unicidade, prazo e tramitação | FLX+CMP+CAS | recurso x reconsideração | B-ADM | baseline | alta | Q-LIT+Q-FLX+Q-CAS |
| DA-16 | direito-administrativo | SRC-B2-L10261 | arts. 314–321 | revisão disciplinar → reconhecer fundamentos, legitimidade, processamento e efeitos | FLX+CMP+CAS | revisão x recurso; anulação/modificação/absolvição | B-ADM | baseline | alta | Q-LIT+Q-FLX+Q-CAS |
| DA-17 | direito-administrativo | SRC-B2-L10261 | arts. 322–323 | disposições finais do recorte e contagem de prazos → aplicar regra de dias corridos e prorrogação | TAB+CAS | prazo estatutário x prazo processual externo | B-ADM | baseline | média | Q-LIT+Q-CAS |
| DA-18 | direito-administrativo | SRC-B2-L8429 | arts. 1–8 e dispositivos intercalares vigentes | sistema da improbidade, sujeitos, âmbito e efeitos gerais → reconhecer quem pode responder e em quais condições | EXP+CMP+CAS | agente x terceiro; dolo/requisito; sucessão | B-ADM | baseline; sem drift textual efetivo pós-cutoff identificado | alta | Q-FULL+Q-LIT+Q-CAS |
| DA-19 | direito-administrativo | SRC-B2-L8429 | art. 9º | enriquecimento ilícito → identificar vantagem indevida e modalidade típica | TAB+CAS | enriquecimento x dano/princípios | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-20 | direito-administrativo | SRC-B2-L8429 | art. 10 | lesão ao erário → reconhecer dano, nexo e condutas | TAB+CAS | dano efetivo x mera irregularidade; art. 9/11 | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-21 | direito-administrativo | SRC-B2-L8429 | art. 11 | princípios da Administração → identificar condutas tipificadas e requisito subjetivo | TAB+CAS | princípio x dano/enriquecimento | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-22 | direito-administrativo | SRC-B2-L8429 | art. 12 | sanções → relacionar modalidade, limites, cumulação e dosimetria | TAB+CMP+CAS | modalidade x sanção; dosimetria | B-ADM | baseline | alta | Q-LIT+Q-CMP+Q-CAS |
| DA-23 | direito-administrativo | SRC-B2-L8429 | arts. 13–16 | declaração patrimonial, notícia/representação, apuração e indisponibilidade → ordenar medidas pré-processuais/patrimoniais | FLX+TAB+CAS | representação x ação; indisponibilidade x perda | B-ADM | baseline | alta | Q-FLX+Q-CAS |
| DA-24 | direito-administrativo | SRC-B2-L8429 | arts. 17–17-D e intercalares | ação de improbidade, procedimento e acordo de não persecução → dominar legitimidade, fases e soluções | FLX+CMP+CAS | ação x procedimento administrativo; acordo x sanção judicial | B-ADM | baseline | alta | Q-FULL+Q-FLX+Q-CAS |
| DA-25 | direito-administrativo | SRC-B2-L8429 | arts. 18–18-A e intercalares | efeitos patrimoniais e execução da condenação → reconhecer perda, ressarcimento e destinação | FLX+CAS | indisponibilidade x perda/ressarcimento | B-ADM | baseline; art. 18 da Lei 15.269/2025 que alteraria LIA foi vetado | média | Q-LIT+Q-CAS+Q-VER |
| DA-26 | direito-administrativo | SRC-B2-L8429 | arts. 19–22 e intercalares | consequências, relações com outras esferas e regras processuais complementares → aplicar independência/efeitos | CMP+CAS | ilícito penal/civil/administrativo; prova/efeito | B-ADM | baseline | média | Q-FULL+Q-CMP+Q-CAS |
| DA-27 | direito-administrativo | SRC-B2-L8429 | arts. 23–25 e intercalares | prescrição e disposições finais → calcular marcos e reconhecer regras de encerramento | LIN+TAB+CAS | prescrição x ressarcimento/efeito; marco interruptivo | B-ADM | baseline | alta | Q-FULL+Q-LIT+Q-CAS |

**Ledger Administrativo:** Lei SP 10.261/1968 `1–86 + 171–175 + 239–323`; Lei 8.429/1992 `integral, inclusive dispositivos intercalares vigentes` → 100% mapeados em DA-01…DA-27.

---

# 7. `legislacao-interna`

## 7.1 Resolução TJSP 850/2021 — teletrabalho

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| LI-R850-01 | legislacao-interna | SRC-B2-RES850 | Cap. I, arts. 1–6 | princípios, alcance e infraestrutura → reconhecer premissas e condições gerais do teletrabalho | EXP+TAB+CAS | teletrabalho x trabalho presencial; dever institucional x individual | B-LI | baseline compilado até Res. 864/2022 | alta | Q-LIT+Q-CAS+Q-VER |
| LI-R850-02 | legislacao-interna | SRC-B2-RES850 | Cap. II, arts. 7–22 | teletrabalho de servidores → dominar elegibilidade, autorização, metas, acompanhamento, deveres e hipóteses de retorno | FLX+TAB+CAS | autorização x direito subjetivo; meta/dever/controle | B-LI | baseline compilado até Res. 864/2022 | alta | Q-FULL+Q-LIT+Q-CAS+Q-VER |
| LI-R850-03 | legislacao-interna | SRC-B2-RES850 | Cap. III, arts. 23–27 | teletrabalho de magistrados → reconhecer regime, requisitos e controles específicos | CMP+TAB+CAS | magistrado x servidor | B-LI | baseline compilado até Res. 864/2022 | alta | Q-LIT+Q-CMP+Q-VER |
| LI-R850-04 | legislacao-interna | SRC-B2-RES850 | Cap. IV, arts. 28–37 | regime para pessoa com deficiência, necessidade especial ou doença grave e dependente → aplicar critérios e proteção específica | CMP+CAS | regra geral x regime especial; titular x dependente | B-LI | baseline compilado até Res. 864/2022 | alta | Q-LIT+Q-CMP+Q-CAS+Q-VER |
| LI-R850-05 | legislacao-interna | SRC-B2-RES850 | Cap. V, arts. 38–40 | disposições finais/transitórias → reconhecer regras de implementação e fechamento | EXP+TAB | permanente x transitório | B-LI | art. 40 já integra baseline por Res. 864/2022 | média | Q-LIT+Q-FULL+Q-VER |

## 7.2 Resolução TJSP 963/2025 — eproc

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| LI-R963-01 | legislacao-interna | SRC-B2-RES963 | arts. 1–8 | escopo, princípios e governança do eproc → distinguir órgãos, objetivos e competências de governança | TAB+CMP+CAS | CGe x NGN x NGT; governança x operação | B-LI | baseline DJE 29/05/2025 | alta | Q-LIT+Q-CMP+Q-VER |
| LI-R963-02 | legislacao-interna | SRC-B2-RES963 | arts. 9–14 | implantação → reconhecer etapas, unidades e condições de adoção | FLX+TAB | implantação x uso ordinário | B-LI | baseline; atos posteriores complementares não são absorvidos automaticamente | alta | Q-FLX+Q-VER |
| LI-R963-03 | legislacao-interna | SRC-B2-RES963 | arts. 15–21 | usuários, credenciais, deveres, acesso, indisponibilidade e prazos → aplicar responsabilidade e efeito de indisponibilidade | TAB+CAS+LIN | credencial pessoal x acesso institucional; indisponibilidade x falha local | B-LI | baseline | alta | Q-LIT+Q-CAS+Q-VER |
| LI-R963-04 | legislacao-interna | SRC-B2-RES963 | arts. 22–29 | integrações e prática dos atos/processamento → compreender distribuição, movimentos, certificação, custas e interoperabilidade | FLX+TAB+CAS | integração x acesso; ato automático x intervenção humana | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-R963-05 | legislacao-interna | SRC-B2-RES963 | arts. 30–36 | consulta, sigilo, certidões e processamento em segundo grau/recursos → reconhecer acesso e fluxo | FLX+CMP+CAS | consulta pública x sigilo; primeiro x segundo grau | B-LI | baseline | alta | Q-LIT+Q-FLX+Q-VER |
| LI-R963-06 | legislacao-interna | SRC-B2-RES963 | arts. 37–43 | uso indevido, bloqueio, API e disposições finais/transitórias → reconhecer sanções operacionais e regras de encerramento | TAB+CAS | uso regular x indevido; bloqueio x indisponibilidade | B-LI | baseline; complementos posteriores avaliados separadamente | média | Q-LIT+Q-CAS+Q-VER |

## 7.3 LC SP 1.111/2010 — Plano de Cargos e Carreiras

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| LI-LC1111-01 | legislacao-interna | SRC-B2-LC1111 | Caps. I–II, arts. 1–2 | plano e quadro de pessoal → reconhecer estrutura de cargos efetivos/em comissão | EXP+TAB | cargo efetivo x comissão | B-LI | baseline 2025-07-29 | média | Q-LIT+Q-VER |
| LI-LC1111-02 | legislacao-interna | SRC-B2-LC1111 | Cap. III, arts. 3–7 | vencimentos, jornadas e vantagens → ligar cargo/jornada a escala e vantagens | TAB+CMP+CAS | vencimento x remuneração/vantagem; jornada | B-LI | baseline; extinções de saúde por Lei 18.373/2025 são posteriores | alta | Q-LIT+Q-CAS+Q-VER |
| LI-LC1111-03 | legislacao-interna | SRC-B2-LC1111 | Cap. IV, arts. 8–10 | ingresso → reconhecer concurso, enquadramento inicial e relação com estágio | FLX+CAS | ingresso x desenvolvimento posterior | B-LI | baseline | média | Q-LIT+Q-CAS |
| LI-LC1111-04 | legislacao-interna | SRC-B2-LC1111 | Cap. V, art. 11 | estágio probatório → dominar duração e critérios de avaliação | TAB+CAS | estágio probatório x progressão | B-LI | baseline | alta | Q-LIT+Q-CAS |
| LI-LC1111-05 | legislacao-interna | SRC-B2-LC1111 | Cap. VI, arts. 12–33 | desenvolvimento: progressão, promoção e acesso → distinguir institutos, requisitos, interstícios, recursos e reserva de cargos | CMP+FLX+CAS | progressão x promoção x acesso; requisito/interstício/recurso | B-LI | baseline | alta | Q-FULL+Q-CMP+Q-CAS |
| LI-LC1111-06 | legislacao-interna | SRC-B2-LC1111 | Cap. VII, art. 34 | Comitê de Recursos Humanos → reconhecer atribuições e papel decisório | TAB | Comitê x Secretaria de RH | B-LI | baseline | média | Q-LIT+Q-CMP |
| LI-LC1111-07 | legislacao-interna | SRC-B2-LC1111 | Cap. VIII, arts. 35–37-B | gratificações, RETEJ e Adicional de Qualificação → aplicar requisitos e percentuais do cutoff | TAB+CMP+CAS | gratificação x AQ; cumulatividade; título | B-LI | **art. 37-B no baseline: 12,5% doutor; 10% mestre; 7,5% especialização; 5% graduação. LC 1.441/2026 é posterior** | alta | Q-LIT+Q-CAS+Q-VER |
| LI-LC1111-08 | legislacao-interna | SRC-B2-LC1111 | Cap. IX, arts. 38–51 | disposições gerais/finais, cargos, enquadramento, benefícios, vigência e remoção → compreender efeitos estruturais | TAB+EXP | criação/extinção/enquadramento; benefício absorvido; remoção | B-LI | baseline inclui atos de 16/07/2025; Lei 18.373/2025 posterior | alta | Q-FULL+Q-LIT+Q-VER |
| LI-LC1111-09 | legislacao-interna | SRC-B2-LC1111 | Cap. X — Disposições Transitórias, arts. 1–3 | enquadramento transitório e complemento → entender migração para o plano | FLX+TAB | regra permanente x transição | B-Ø | baseline | média | Q-LIT+Q-FULL+Q-VER |
| LI-LC1111-10 | legislacao-interna | SRC-B2-LC1111 | Anexos I–IX e atos oficiais incorporados ao baseline | cargos, referências, escalas, enquadramentos, atribuições e percentuais → localizar informação tabular necessária | TAB | cargo/referência/anexo correto; quadro vigente | B-LI | **baseline inclui criações de 16/07/2025; não usar alterações de 23/12/2025 ou 2026 como cutoff** | alta | Q-FULL+Q-VER |

## 7.4 Regimento Interno do TJSP — integral

**Regra de versão para todas as linhas LI-RI:** baseline reconstruído até **Assento Regimental 591/2025**; Assento 592/2025 e Assentos 593–596/2026 ficam fora do baseline e só podem ser tratados como drift/complemento deliberado.

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| LI-RI-01 | legislacao-interna | SRC-B2-RITJSP | art. 1º | disposição inicial → compreender objeto e alcance do Regimento | EXP | regimento x lei processual | B-LI | baseline 591 | base | Q-LIT+Q-VER |
| LI-RI-02 | legislacao-interna | SRC-B2-RITJSP | Tít. I, Cap. I, arts. 2–29 | Tribunal: composição, Pleno, Órgão Especial, CSM, direção, Presidente, Vice, Corregedor e Decano → reconhecer órgão e atribuição | TAB+CMP+CAS | órgão colegiado x cargo de direção; competência institucional | B-LI | baseline 591 | alta | Q-FULL+Q-CMP+Q-CAS+Q-VER |
| LI-RI-03 | legislacao-interna | SRC-B2-RITJSP | Tít. I, Cap. II, arts. 30–72 | Seções e órgãos fracionários → mapear estrutura, funcionamento, presidentes, comissões e desembargadores | TAB+CMP | seção/grupo/câmara/comissão; função do presidente | B-LI | baseline 591 | alta | Q-FULL+Q-CMP+Q-VER |
| LI-RI-04 | legislacao-interna | SRC-B2-RITJSP | Tít. I, Cap. III, arts. 73–102 | juízes → dominar ingresso, antiguidade, promoção/remoção, reaproveitamento, aposentadoria, investigação e regras gerais | FLX+TAB+CAS | promoção x remoção; vitaliciamento; investigação | B-LI | baseline 591 | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-RI-05 | legislacao-interna | SRC-B2-RITJSP | Tít. II, arts. 103–115 | competência jurisdicional, prevenção, juiz certo, impedimento/suspeição → selecionar regra competente | CMP+CAS | prevenção x juiz certo; impedimento x suspeição | B-LI | baseline 591 | alta | Q-LIT+Q-CMP+Q-CAS+Q-VER |
| LI-RI-06 | legislacao-interna | SRC-B2-RITJSP | Tít. III, Cap. I, arts. 116–166 | sessões, reuniões, audiências, pauta, ordem dos trabalhos, sustentação, votação, acórdão e publicidade → reproduzir funcionamento colegiado | FLX+TAB+CAS | pauta x ordem; sustentação x votação; publicidade/exceção | B-LI | baseline 591 | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-RI-07 | legislacao-interna | SRC-B2-RITJSP | Tít. III, Cap. II, arts. 167–189 | feitos, apresentação, registro, autuação, distribuição e controle → ordenar tramitação interna | FLX+TAB | registro x distribuição x passagem de autos | B-LI | baseline 591 | alta | Q-FULL+Q-FLX+Q-VER |
| LI-RI-08 | legislacao-interna | SRC-B2-RITJSP | Tít. IV, Cap. I, arts. 190–228 | incidentes → diferenciar uniformização, inconstitucionalidade, reclamação, conflitos, desaforamento, fiança, correição e exceção da verdade | CMP+FLX+CAS | incidentes vizinhos; competência/cabimento | B-LI | baseline 591 | alta | Q-FULL+Q-CMP+Q-CAS+Q-VER |
| LI-RI-09 | legislacao-interna | SRC-B2-RITJSP | Tít. IV, Cap. II, arts. 229–249 | ações do Regimento → reconhecer ADI, cautelares, MS/MI/HD, rescisória, dissídio de greve e HC | CMP+FLX+CAS | ação/remédio/cabimento/competência | B-LI | baseline 591 | alta | Q-FULL+Q-CMP+Q-CAS+Q-VER |
| LI-RI-10 | legislacao-interna | SRC-B2-RITJSP | Tít. IV, Cap. III, arts. 250–258 | recursos → dominar regras gerais, agravo regimental e recursos aos Tribunais Superiores | FLX+CMP | agravo/regra geral/recurso superior | B-LI | baseline 591 | alta | Q-FULL+Q-FLX+Q-CMP+Q-VER |
| LI-RI-11 | legislacao-interna | SRC-B2-RITJSP | Tít. IV, Cap. IV, arts. 259–270 | intervenções federal/municipal e precatórios → identificar hipótese, competência e fluxo | FLX+CMP+CAS | intervenção federal x estadual/município; precatório | B-LI | baseline 591 | média | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-RI-12 | legislacao-interna | SRC-B2-RITJSP | Tít. V, Cap. I, arts. 271–279 | atos de administração e reforma do Regimento → reconhecer competência e procedimento de alteração | FLX+TAB | ato administrativo x reforma regimental | B-LI | baseline 591 | média | Q-FULL+Q-LIT+Q-VER |
| LI-RI-13 | legislacao-interna | SRC-B2-RITJSP | Tít. V, Cap. II, arts. 280–290 | Secretaria e disposições finais/transitórias → compreender organização de suporte e regras finais | EXP+TAB | regra estrutural x transitória | B-Ø | baseline 591 | média | Q-FULL+Q-LIT+Q-VER |

## 7.5 Normas da Corregedoria — Tomo I, recortes literais do edital

A duplicidade oficial de **Capítulo XI** permanece intocada. O primeiro recorte (`Seções I, IV e V`) é mantido como linha de autoridade e referencia as mesmas unidades substantivas que também aparecem no segundo recorte (`Seções I a VII`). Isso evita dupla redação sem “corrigir” o edital.

| coverage_id | pack | source_id | recorte | tema → objetivo de aprendizagem | forma | contraste/risco | banca | versão | profundidade | prática/QA |
|---|---|---|---|---|---|---|---|---|---|---|
| LI-NS-01 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. II, Seção I: regra geral art. 5º + Subseção I arts. 6–14 + Subseção II arts. 15–18 | função correcional, Corregedoria Permanente, correições/visitas e apurações preliminares/sindicâncias/PAD → distinguir procedimento e autoridade | FLX+TAB+CAS | correição x visita; apuração preliminar x sindicância/PAD | B-LI | baseline; **Subseção III/art. 19 não integra o recorte** | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-02 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção I, arts. 26–27 | disposições iniciais dos ofícios → reconhecer organização básica | EXP+TAB | regra geral x regra de seção posterior | B-LI | baseline | média | Q-LIT+Q-VER |
| LI-NS-03 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção II, arts. 28–29 | atribuições → identificar responsabilidades funcionais | TAB+CAS | atribuição do ofício x do servidor/juízo | B-LI | baseline | alta | Q-LIT+Q-CAS+Q-VER |
| LI-NS-04 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção V, arts. 46–62 | sistema informatizado oficial, segurança, cadastro, movimentação e controle → aplicar deveres operacionais | TAB+FLX+CAS | cadastro x movimentação; acesso x segurança | B-LI | baseline; Seção IV-A posterior não entra | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-05 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção VI, arts. 63–79 | livros e classificadores obrigatórios → reconhecer finalidade, manutenção e controle | TAB+CAS | livro/classificador correto; físico x sistema | B-LI | baseline | alta | Q-FULL+Q-CAS+Q-VER |
| LI-NS-06 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção VII, arts. 80–86 | escrituração → aplicar regras formais e vedadas | CMP+CAS | forma correta x vício de escrituração | B-LI | baseline | alta | Q-LIT+Q-CMP+Q-CAS+Q-VER |
| LI-NS-07 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção VIII, **somente Subseções I–III, arts. 87–99** | autuação, recepção/juntada e movimentação → ordenar atos cartorários | FLX+TAB+CAS | autuação x juntada x movimentação | B-LI | baseline; **Subseções IV–V, arts. 100–102, fora do recorte** | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-08 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seções IX–XII, arts. 103–111 | papéis findos, certidões, mandados e ofícios → selecionar expediente e regra aplicável | TAB+CMP+CAS | certidão x mandado x ofício; dispositivo revogado x vigente | B-LI | baseline | alta | Q-FULL+Q-CMP+Q-CAS+Q-VER |
| LI-NS-09 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XIII, arts. 112–121-C | comunicações e informações, inclusive rotinas de dados/sistemas previstas → reconhecer canal, autoridade e requisito | TAB+FLX+CAS | comunicação ordinária x informação protegida/sistema | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-10 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XIV, arts. 122–131 | cartas precatórias, rogatórias e arbitrais → distinguir espécie, expedição e cumprimento | CMP+FLX+CAS | precatória x rogatória x arbitral | B-LI | baseline | alta | Q-FULL+Q-CMP+Q-CAS+Q-VER |
| LI-NS-11 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XV, arts. 132–142 | intimações → reconhecer forma, destinatário e cumprimento | FLX+TAB+CAS | intimação x demais comunicações | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-12 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XVI, arts. 143–156-A | audiências → dominar preparação, registro e providências de secretaria | FLX+TAB+CAS | audiência x ato cartorário anterior/posterior | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-13 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XVII, arts. 157–169 | consulta e carga de autos → reconhecer legitimados, controle e restrições | TAB+CMP+CAS | consulta x carga; legitimado x terceiro | B-LI | baseline | alta | Q-FULL+Q-CMP+Q-CAS+Q-VER |
| LI-NS-14 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XVIII, arts. 170–175 | desentranhamento → identificar hipótese, autorização e registro | FLX+CAS | desentranhamento x juntada/retirada | B-LI | baseline | média | Q-FULL+Q-CAS+Q-VER |
| LI-NS-15 | legislacao-interna | SRC-B2-NSCGJ-T1 | Cap. III, Seção XIX, arts. 176–189-G | arquivamento, desarquivamento, rearquivamento e rotinas correlatas → ordenar guarda/retorno/pesquisa | FLX+TAB+CAS | arquivo x desarquivo x rearquivo | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-16 | legislacao-interna | SRC-B2-NSCGJ-T1 | **linha literal 5 do edital:** Cap. XI, Seções I, IV e V | preservar o primeiro recorte oficial sem duplicar conteúdo → remeter a LI-NS-17, LI-NS-20 e LI-NS-21 | CMP | duplicidade do edital; não inferir outro capítulo | B-LI | ambiguidade oficial preservada | alta | Q-FULL+Q-VER |
| LI-NS-17 | legislacao-interna | SRC-B2-NSCGJ-T1 | **linha literal 6:** Cap. XI, Seção I, arts. 1189–1195 | sistema de processamento eletrônico → reconhecer bases e regras gerais | EXP+TAB+CAS | processo eletrônico x rotina física | B-LI | baseline | alta | Q-FULL+Q-CAS+Q-VER |
| LI-NS-18 | legislacao-interna | SRC-B2-NSCGJ-T1 | linha literal 6: Cap. XI, Seção II, arts. 1196–1208 | peticionamento eletrônico, indisponibilidade e exceções → aplicar envio, prazo e efeito da indisponibilidade | FLX+TAB+CAS | peticionamento x indisponibilidade; exceção x regra | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-19 | legislacao-interna | SRC-B2-NSCGJ-T1 | linha literal 6: Cap. XI, Seção III, arts. 1209–1219 | distribuição eletrônica → ordenar cadastramento, distribuição e providências | FLX+TAB | cadastro x distribuição | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-VER |
| LI-NS-20 | legislacao-interna | SRC-B2-NSCGJ-T1 | linha literal 6: Cap. XI, Seção IV, arts. 1220–1223 | protocolo de petições intermediárias → reconhecer forma e fluxo | FLX+CAS | petição inicial x intermediária | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-21 | legislacao-interna | SRC-B2-NSCGJ-T1 | linha literal 6: Cap. XI, Seção V, arts. 1224–1227 | consulta de movimentações e decisões → aplicar acesso e limites | TAB+CAS | consulta x ciência/intimação; acesso x sigilo | B-LI | baseline | alta | Q-FULL+Q-CAS+Q-VER |
| LI-NS-22 | legislacao-interna | SRC-B2-NSCGJ-T1 | linha literal 6: Cap. XI, Seção VI, arts. 1228–1289 no baseline | tramitação do processo eletrônico → dominar operações, documentos, comunicações e rotinas do fluxo | FLX+TAB+CAS | etapa/sujeito/rotina eletrônica; regra atual x baseline | B-LI | **Prov. CG 30/2025 alterou art. 1236 após cutoff; Prov. CG 04/2026 incluiu dispositivo/subseção posterior. Não absorver no baseline** | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |
| LI-NS-23 | legislacao-interna | SRC-B2-NSCGJ-T1 | linha literal 6: Cap. XI, Seção VII, arts. 1290–1301 | precatórios e RPV no processo eletrônico → reconhecer fluxo e responsabilidades | FLX+TAB+CAS | precatório x RPV; rotina eletrônica x competência decisória | B-LI | baseline | alta | Q-FULL+Q-FLX+Q-CAS+Q-VER |

**Ledger Legislação Interna:** Res. 850/2021 integral; Res. 963/2025 integral; LC 1.111/2010 integral (arts. 1–51, Disposições Transitórias arts. 1–3 e Anexos I–IX); RITJSP integral (arts. 1–290 no baseline); NSCGJ nos seis recortes literais do edital → 100% mapeados. A linha 5 de Cap. XI permanece explicitamente representada em LI-NS-16 e é satisfeita substantivamente pelas Seções I, IV e V também contidas na linha 6.

---

# 8. Verificação cruzada de cobertura

| pack | fontes | resultado de rastreabilidade |
|---|---|---|
| direito-penal | SRC-B2-CP | `complete` — todos os artigos isolados/faixas do syllabus aparecem no ledger e em coverage_id específico |
| direito-processual-penal | SRC-B2-CPP; SRC-B2-L9099 | `complete` — todos os intervalos do CPP e recortes penais da Lei 9.099 estão particionados sem lacunas |
| direito-processual-civil | SRC-B2-CPC; SRC-B2-L9099; SRC-B2-L12153 | `complete` — todos os intervalos do CPC, arts. 3–19 da Lei 9.099 e Lei 12.153 integral estão mapeados |
| direito-constitucional | SRC-B2-CF88 | `complete` — todos os capítulos/seções e art. 92 estão mapeados |
| direito-administrativo | SRC-B2-L10261; SRC-B2-L8429 | `complete` — três recortes da Lei 10.261 e LIA integral estão mapeados, inclusive dispositivos intercalares vigentes |
| legislacao-interna | SRC-B2-RES850; SRC-B2-RES963; SRC-B2-LC1111; SRC-B2-RITJSP; SRC-B2-NSCGJ-T1 | `complete` — cinco fontes integrais/recortadas mapeadas; duplicidade Cap. XI preservada |

## Pontos de drift obrigatoriamente associados

- DPP-16 → CPP art. 584, § 4º;
- DPC-02 → CPC art. 196;
- DPC-30 → CPC art. 529-A posterior ao cutoff;
- DPC-31 → CPC art. 998;
- DC-04 → CF art. 37, XVI, `b`;
- DA-06 → Lei SP 10.261/1968 art. 78;
- LI-LC1111-02/07/08/10 → alterações posteriores da LC 1.111/2010 e atos de quadro;
- LI-RI-01…13 → baseline RITJSP até Assento 591/2025, sem Assentos 592–596;
- LI-NS-22 → alterações pós-cutoff do Cap. XI/Seção VI;
- LI-NS-16 → duplicidade oficial de Capítulo XI, sem correção inferida.

## 9. Critério de saída

Gate 4 pode ser considerado `closed` porque:

- existem seis matrizes independentes;
- todos os recortes do syllabus possuem `coverage_id` ou remissão explícita sem perda de conteúdo;
- todos os `source_id` do Gate 2 estão associados às unidades pertinentes;
- riscos de confusão e sinais de banca foram convertidos em decisões pedagógicas, sem previsão estatística;
- os pontos de drift estão presos às unidades afetadas;
- a anomalia oficial das NSCGJ permanece documentada;
- cada linha define requisito de prática/QA suficiente para servir de contrato de redação.

**Gate 4: `closed`.**

Próximo passo: `DIREITO-005` — autorizar e iniciar a autoria de `direito-penal` usando DP-01…DP-10 como contrato.
