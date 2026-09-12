# DIREITO B2 — Análise histórica reproduzível da banca

**Competition:** `tjsp-escrevente-2025`  
**Gate:** `DIREITO-003`  
**Status:** `closed`  
**Classificação:** `2026-09-12`

## Autoridade e método

O edital vigente define o escopo. As provas históricas calibram forma, profundidade, operação cognitiva, contraste e distractor; não criam peso futuro nem removem conteúdo do syllabus.

Os quatro PDFs locais foram conferidos contra `SOURCES.json` antes da extração:

- `SRC-TJSP-PROVA-2021` — SHA-256 `4368240090841eab1de84d20cfbfd0d8a86579a081136308f2409051f4e12d90`, 482030 bytes;
- `SRC-TJSP-PROVA-2023` — SHA-256 `ae203c145c68766c83aa4c4b35dbb2778854481f9d89fb752de28b649f3bfc4d`, 657527 bytes;
- `SRC-TJSP-PROVA-2024` — SHA-256 `05993d52b7cd955bb29ea14f175f60ecbde2f7f9b3b4c069143c249f1947836d`, 645374 bytes;
- `SRC-TJSP-PROVA-2025` — SHA-256 `068cfd0fbc929d250e2703cbf90ff2a7efde3bf4fb86915eeb9088a2a78a8b87`, 496275 bytes.

Extração: `pdftotext -raw`, ancoragem pelo número da questão e conferência semântica dos cabeçalhos/domínios. A ordem textual de páginas em duas colunas desloca alguns cabeçalhos; por isso a divisão não depende apenas da posição linear do cabeçalho no TXT.

Blocos: 2021 `25–64` (40); 2023 `25–64` (40); 2024 `25–64` (40); 2025 `17–46` (30). Total: **150 questões**.

## Esquema compacto

Cada linha usa:

`year_question|domain|source_or_institute|task_form|cognitive_operation|literalness|distractor_pattern|legal_contrast|editorial_signal`

Domínio: `P` Penal; `PP` Processual Penal; `PC` Processual Civil; `C` Constitucional; `A` Administrativo; `LI` Legislação Interna.

Forma: `D+` direta/correta; `D-` direta/incorreta; `C+` caso/correta; `X` comparação.

Operações: `LR` literal_recall; `RD` requirement_discrimination; `EI` exception_identification; `CA` case_application; `PS` procedure_sequence; `CD` competence_or_deadline; `IC` institute_comparison; `LC` legal_consequence.

Literalidade: `H` alta; `M` média; `L` baixa.

Distratores: `SS` subject_swap; `RS` requirement_swap; `DS` deadline_swap; `CS` competence_swap; `AR` action_or_remedy_swap; `CM` culpability_or_modality_swap; `DR` damage_or_result_requirement; `EX` exception_inversion; `OG` overgeneralization; `NI` neighboring_institute; `PT` partial_truth.

Contrastes: `K1` tipo/tipo vizinho; `K2` falsa identidade/documento alheio; `K3` impedimento/suspeição; `K4` rejeição/absolvição; `K5` ritos/atos/limites; `K6` decisões do júri; `K7` JECrim/rito comum; `K8` JEC/comum; `K9` JEFaz/comum; `K10` ações constitucionais; `K11` nato/naturalizado; `K12` servidor regra/exceção; `K13` hipótese/requisito/efeito; `K14` improbidade modalidade/requisito/sanção; `K15` regra operacional/semelhante; `K16` regra interna/semelhante; `K17` regra processual/exceção/efeito; `K18` CPP regra/hipótese próxima; `K19` CF regra/exceção; `K20` requisito/verdade parcial.

Sinais editoriais: `E1` tipos + mini-casos; `E2` fluxo + prazos; `E3` competência + casos-limite; `E4` regra/exceção + casos; `E5` hipótese→efeito + linha do tempo; `E6` modalidade→sanção; `E7` tabela operacional + exemplos; `E8` regra/exceção + mini-casos; `E9` requisito decisivo + contraste.

## Classificação por questão

```text
2021-25|P|CP:falsidade ideológica em documento público/formulário de trânsito|D+|LR,RD,LC|H|NI,RS,CM|K1|E1
2021-26|P|CP art. 294:petrechos de falsificação|C+|RD,CA,LC|M|NI,RS,CM|K1|E1
2021-27|P|CP:falsidades em atestado/documento+uso de documento falso|C+|RD,CA,IC|M|NI,RS,CM|K1|E1
2021-28|P|CP arts. 307–308:falsa identidade/uso/cessão de documento alheio|C+|RD,CA,IC,LC|M|NI,RS,CM|K2|E1
2021-29|P|CP art. 311-A:fraude em certame de interesse público|C+|RD,CA,LC|M|NI,RS,CM|K1|E1
2021-30|P|CP arts. 339–357:crimes AdmJust|D+|LR,RD,IC,LC|H|NI,RS|K1|E1
2021-31|PP|CPP arts. 252–258:impedimento+suspeição do juiz|D+|LR,RD,IC|H|NI,SS,RS|K3|E8
2021-32|PP|CPP:citação+intimação do acusado|D+|LR,RD,PS,CD,LC|H|RS,DS,SS|K18|E2
2021-33|PP|CPP arts. 395+397:rejeição da denúncia/absolvição sumária|X|LR,RD,IC,LC|M|RS,PT|K4|E8
2021-34|PP|CPP:recursos, revisão criminal+habeas corpus|D+|LR,RD,PS,CD,IC,LC|M|AR,DS,RS|K18|E8
2021-35|PP|CPP:procedimentos comum ordinário+sumário|D+|LR,RD,PS,CD,LC|M|RS,PT,DS|K5|E2
2021-36|PP|CPP:procedimento do Tribunal do Júri|D+|LR,RD,PS,CD,LC|M|RS,PT,DS|K6|E2
2021-37|PP|L9099:JECrim|D+|LR,RD,CD,LC|H|AR,DS,EX|K7|E3
2021-38|PC|CPC arts. 148–150:impedimento/suspeição de auxiliares+assistente técnico|C+|RD,CA,PS,LC|L|SS,NI,RS|K3|E8
2021-39|PC|CPC:restrições temporárias à citação|D+|LR,RD,EI,PS|H|DS,RS,EX|K17|E2
2021-40|PC|CPC:tutela cautelar requerida em caráter antecedente|D+|LR,RD,PS,CD|M|RS,DS,PT|K17|E8
2021-41|PC|CPC:obrigação de fazer+competência/procedimento|C+|RD,CA,PS,CD|L|RS,PT|K17|E2
2021-42|PC|CPC:embargos de declaração|D+|LR,RD,EI,CD,IC,LC|M|AR,DS,EX|K17|E8
2021-43|PC|L9099:JEC|D+|LR,RD,PS,CD|H|CS,RS,EX|K8|E3
2021-44|PC|L12153:JEFaz|C+|RD,CA,PS,CD,IC,LC|L|CS,RS,EX|K9|E3
2021-45|C|CF art. 5º:crimes inafiançáveis+garantias penais|D+|LR,RD,EI,LC|H|EX,OG,RS|K1|E1
2021-46|C|CF art. 5º:direitos+garantias individuais|D+|LR,RD,LC|H|EX,OG,RS|K19|E4
2021-47|C|CF art. 7º:dir.sociais|D+|LR,RD,EI|H|EX,OG,RS|K19|E4
2021-48|C|CF art. 12:naturalização|D+|LR,RD,IC,LC|H|SS,EX,RS|K11|E4
2021-49|C|CF art. 12, §3º:cargos privativos de brasileiro nato|D+|LR,RD|H|SS,EX,RS|K19|E4
2021-50|C|CF art. 37/41:readaptação de servidor|C+|RD,CA,IC|M|RS,EX,SS|K12|E4
2021-51|C|CF arts. 37–41:regime constitucional dos servidores públicos|D+|LR,RD,EI,CD|H|RS,EX,SS|K12|E4
2021-52|A|L10261:reintegração após absolvição judicial|C+|RD,CA,LC|M|RS,SS,PT|K20|E5
2021-53|A|L10261:falta disciplinar, aposentadoria+sanção|C+|RD,CA,PS,LC|M|RS,SS,PT|K20|E5
2021-54|A|L10261:PAD|D+|LR,RD,EI,PS,IC,LC|M|RS,EX,PT|K20|E2
2021-55|A|L10261:testemunhas no processo administrativo|C+|RD,CA,PS,CD|L|DS,RS,PT|K20|E2
2021-56|A|L10261:recursos+revisão administrativa|D-|LR,RD,PS,IC,LC|M|RS,SS,PT|K20|E5
2021-57|A|L8429:investigação/representação+indisponibilidade/medidas patrimoniais|C+|RD,CA,PS,LC|L|RS,DR,SS|K20|E9
2021-58|A|L8429:sucessão+ressarcimento|C+|RD,CA,PS,LC|M|RS,DR,SS|K20|E9
2021-59|A|L8429:ato contra princípios da Administração|C+|RD,CA,LC|M|RS,DR,SS|K20|E9
2021-60|LI|NSCGJ:correições|D+|LR,RD,PS|H|CS,RS,DS|K15|E7
2021-61|LI|NSCGJ:apuração disciplinar, sindicância/processo+aposentadoria|C+|RD,CA,PS,LC|L|RS,PT,SS|K15|E7
2021-62|LI|NSCGJ:movimentação/conclusão dos autos|D+|LR,RD,PS,CD|H|RS,PT,SS|K15|E7
2021-63|LI|NSCGJ:mandados judiciais|D+|LR,RD,EI,CD|H|RS,PT,SS|K15|E7
2021-64|LI|NSCGJ:consulta de movimentações processuais+decisões|D+|LR,RD,EI|H|RS,PT,SS|K15|E7
2023-25|P|CP:crimes contra a fé pública (falsidades documentais)|D+|LR,RD,IC,LC|H|NI,RS,CM|K1|E1
2023-26|P|CP:crimes AdmPub|C+|RD,CA,IC,LC|M|NI,RS|K1|E1
2023-27|P|CP:crimes AdmJust|D+|LR,RD,IC,LC|H|NI,RS|K1|E1
2023-28|P|CP art. 311-A:fraude em certame de interesse público|C+|RD,CA,LC|M|NI,RS,CM|K1|E1
2023-29|P|CP arts. 336–337:inutilização de edital/sinal/subtração/inutilização de livro/documento|D+|LR,RD,IC,LC|H|NI,RS|K1|E1
2023-30|P|CP:desobediência a decisão judicial / exercício de função vedada|C+|RD,EI,CA,LC|M|NI,RS|K1|E1
2023-31|PP|CPP arts. 252–258:impedimento+suspeição|D+|LR,RD,IC,LC|H|NI,SS,RS|K3|E8
2023-32|PP|CPP arts. 261–267:acusado+defensor|C+|RD,EI,CA,PS,LC|L|SS,RS,EX|K18|E8
2023-33|PP|CPP:citações+intimações|D+|LR,RD,EI,PS,CD,LC|H|RS,PT|K18|E8
2023-34|PP|CPP + L9099:definição do rito por pena máxima+citação|C+|RD,CA,PS,CD,LC|L|AR,DS,EX|K5|E2
2023-35|PP|CPP:primeira fase do Tribunal do Júri (pronúncia, impronúncia, absolvição sumária)|C+|RD,CA,PS,CD,LC|L|RS,PT,DS|K6|E2
2023-36|PP|CPP:restauração de autos extraviados ou destruídos|D+|LR,RD,PS,LC|H|RS,PT,DS|K18|E8
2023-37|PP|CPP:revisão criminal|D+|LR,RD,LC|H|AR,DS,RS|K18|E8
2023-38|PC|CPC arts. 144–155:impedimento/suspeição de auxiliares da justiça|C+|RD,CA,IC,LC|M|SS,NI,RS|K3|E8
2023-39|PC|CPC:citação eletrônica+termo inicial de prazo|D+|LR,RD,PS,CD|H|DS,RS,EX|K17|E2
2023-40|PC|CPC:tutela provisória|C+|RD,CA,LC|M|RS,DS,PT|K17|E8
2023-41|PC|CPC:produção antecipada de prova|D+|LR,RD,EI,PS,LC|M|RS,PT|K17|E8
2023-42|PC|CPC:recursos, renúncia/desistência+recurso adesivo|C+|RD,EI,CA,CD,IC,LC|M|AR,DS,EX|K17|E8
2023-43|PC|L9099:competência do JEC|D+|LR,RD,EI,CD|H|CS,RS,EX|K8|E3
2023-44|PC|L12153:JEFaz, tutela provisória, recurso+pagamento|C+|RD,CA,CD,LC|L|CS,RS,EX|K9|E3
2023-45|C|CF art. 5º:ações constitucionais|D+|LR,RD,EI,IC|M|AR,SS,EX|K10|E4
2023-46|C|CF art. 5º:requisição de propriedade+inviolabilidade do domicílio|C+|RD,CA|M|EX,OG,RS|K19|E4
2023-47|C|CF art. 5º:penas admitidas/vedadas|D+|LR,RD,EI,LC|H|EX,OG,RS|K19|E4
2023-48|C|CF arts. 37–41:provimento, estabilidade+servidor efetivo|C+|RD,CA,LC|M|RS,EX,SS|K12|E4
2023-49|C|CF art. 40:regime próprio de previdência|D+|LR,RD,CD|H|RS,EX,SS|K19|E4
2023-50|C|CF art. 92:órgãos do Poder Judiciário|D+|LR,RD,CD,IC|M|CS,SS,PT|K19|E4
2023-51|C|CF art. 12:nacionalidade+cargos privativos/reservados|D+|LR,RD,EI|H|SS,EX,RS|K11|E4
2023-52|A|L8429:notícia/representação de improbidade+requisitos|C+|RD,CA,CD,LC|L|RS,DR,SS|K14|E6
2023-53|A|L8429:indisponibilidade de bens em ação de improbidade|C+|RD,CA,PS|M|RS,DR,SS|K14|E6
2023-54|A|L8429:prescrição|D+|LR,RD,CD,LC|H|RS,DR,SS|K20|E9
2023-55|A|L10261:penas disciplinares|C+|RD,CA,CD,LC|M|RS,SS,PT|K20|E5
2023-56|A|L10261:infração funcional praticada no serviço|C+|RD,EI,CA,CD,LC|M|RS,EX,PT|K20|E5
2023-57|A|L10261:práticas autocompositivas, TAC+suspensão condicional da sindicância|D+|LR,RD,PS,CD|M|RS,SS,PT|K20|E5
2023-58|A|L10261:número de testemunhas no processo disciplinar|D+|LR,RD,PS|H|DS,RS,PT|K20|E2
2023-59|A|L10261:revisão de sanção disciplinar|C+|RD,CA,PS,CD,IC,LC|L|RS,SS,PT|K20|E5
2023-60|LI|NSCGJ:petições intermediárias no processo eletrônico|D+|LR,RD,PS|H|RS,DS,PT|K15|E7
2023-61|LI|NSCGJ:tramitação do processo eletrônico|D+|LR,RD,PS|H|RS,DS,PT|K15|E7
2023-62|LI|NSCGJ:retirada+consulta de autos físicos|D+|LR,RD,EI,CD|H|RS,PT,SS|K15|E7
2023-63|LI|NSCGJ:atividade correicional|D+|LR,RD,PS,CD|H|RS,PT,SS|K15|E7
2023-64|LI|NSCGJ:escrituração de autos físicos|D+|LR,RD,EI,PS|H|RS,PT,SS|K15|E7
2024-25|P|CP art. 294:petrechos de falsificação|C+|RD,CA,LC|M|NI,RS,CM|K1|E1
2024-26|P|CP:falsificação/uso de diploma particular|C+|RD,CA|M|NI,RS,CM|K1|E1
2024-27|P|CP arts. 307–308:uso/cessão de documento de identidade alheio|C+|RD,CA,LC|M|NI,RS|K2|E1
2024-28|P|CP art. 311-A:fraude em certame de interesse público|C+|RD,CA,LC|M|NI,RS,CM|K1|E1
2024-29|P|CP:peculato+reparação do dano|D+|LR,RD,LC|H|NI,RS,CM|K1|E1
2024-30|P|CP:crimes contra Administração Pública/Administração da Justiça|C+|RD,CA,PS,IC,LC|M|NI,RS|K1|E1
2024-31|PP|CPP arts. 252–258:impedimento/suspeição por relação com perito|C+|RD,CA,PS|M|NI,SS,RS|K3|E8
2024-32|PP|CPP:atos de comunicação processual|D+|LR,RD,PS,CD,LC|H|RS,PT|K18|E8
2024-33|PP|CPP:procedimento comum ordinário+sumário|D+|LR,RD,PS,CD,LC|M|RS,PT,DS|K5|E2
2024-34|PP|CPP:Tribunal do Júri: composição+Conselho de Sentença|D+|LR,RD,PS|H|RS,PT,DS|K6|E2
2024-35|PP|CPP:recursos+ações de impugnação|C+|RD,CA,PS,CD,IC,LC|M|AR,DS,RS|K18|E8
2024-36|PP|CPP:habeas corpus|D+|LR,RD,CD|H|AR,DS,RS|K18|E8
2024-37|PP|L9099:composição civil dos danos+representação|C+|RD,EI,CA,IC,LC|M|AR,DS,EX|K7|E9
2024-38|PC|CPC art. 155:responsabilidade civil do escrivão/chefe de secretaria|C+|RD,CA,PS,LC|M|RS,PT|K17|E8
2024-39|PC|CPC:intimações|D+|LR,RD,PS,LC|H|DS,RS,EX|K17|E8
2024-40|PC|CPC:estabilização da tutela antecipada antecedente|C+|RD,CA,PS,LC|L|RS,DS,PT|K17|E8
2024-41|PC|CPC:audiência de conciliação/mediação|C+|RD,CA,LC|M|RS,PT|K17|E8
2024-42|PC|CPC:apelação, tutela provisória+efeito suspensivo|C+|RD,EI,CA,PS,CD,LC|L|AR,DS,EX|K17|E8
2024-43|PC|L9099:competência do JEC|C+|RD,CA,CD,LC|L|CS,RS,EX|K8|E3
2024-44|PC|L12153:JEFaz|D+|LR,RD,EI,PS,CD,IC|M|CS,RS,EX|K9|E3
2024-45|C|CF art. 5º:direitos+deveres individuais+coletivos|D+|LR,RD|H|EX,OG,RS|K19|E4
2024-46|C|CF art. 7º:dir.sociais|D+|LR,RD|H|EX,OG,RS|K19|E4
2024-47|C|CF art. 12:nacionalidade/naturalização|C+|RD,CA,IC,LC|M|SS,EX,RS|K11|E4
2024-48|C|CF art. 8º:liberdade sindical+estabilidade sindical|D+|LR,RD,EI,LC|H|EX,OG,RS|K19|E4
2024-49|C|CF art. 37, XVI–XVII:acumulação remunerada|D+|LR,RD,CD,IC,LC|H|RS,EX,SS|K19|E4
2024-50|C|CF art. 38:servidor investido em mandato eletivo|C+|RD,EI,CA,CD|M|RS,EX,SS|K12|E4
2024-51|C|CF art. 40:aposentadoria por incapacidade permanente|D+|LR,RD,IC|H|EX,OG,RS|K19|E4
2024-52|A|L10261:deveres/proibições do funcionário|C+|RD,CA|M|RS,EX,PT|K13|E5
2024-53|A|L10261:independência das instâncias+processo disciplinar|C+|RD,CA,PS,LC|M|RS,EX,PT|K20|E2
2024-54|A|L10261:penas disciplinares|D+|LR,RD,EI,LC|H|RS,SS,PT|K20|E5
2024-55|A|L10261:sindicância+afastamento/designação preventiva|D+|LR,RD,EI,PS|M|RS,EX,PT|K20|E5
2024-56|A|L10261:autocomposição, TAC+suspensão condicional|D+|LR,RD,PS|H|RS,SS,PT|K20|E5
2024-57|A|L8429:representação/notícia de improbidade|D+|LR,RD|H|RS,DR,SS|K14|E6
2024-58|A|L8429:multa civil+dosimetria|D+|LR,RD,LC|H|RS,DR,SS|K20|E9
2024-59|A|L8429:procedimento administrativo+ação judicial|D+|LR,RD,PS|M|RS,DR,SS|K20|E2
2024-60|LI|NSCGJ:Corregedoria Permanente, correições+visitas|D+|LR,RD,EI,PS,CD|H|CS,RS,DS|K15|E7
2024-61|LI|NSCGJ:procedimento disciplinar+falta de autoria|D+|LR,RD,PS,LC|M|CS,RS,DS|K15|E7
2024-62|LI|NSCGJ:qualificação protegida de testemunha|D+|LR,RD,LC|H|RS,PT,SS|K15|E7
2024-63|LI|NSCGJ:certidões|D+|LR,RD,CD,LC|H|RS,PT,SS|K15|E7
2024-64|LI|NSCGJ:peticionamento eletrônico|D+|LR,RD,EI,PS,CD|H|RS,DS,PT|K15|E7
2025-17|P|CP art. 293:falsificação de papéis públicos+supressão de sinal de cancelamento|D+|LR,RD,LC|H|NI,RS,CM|K1|E1
2025-18|P|CP art. 307:falsa identidade|C+|RD,CA,LC|M|NI,RS,CM|K1|E1
2025-19|P|CP art. 313-A:inserção de dados falsos em sistema de informações|D+|LR,RD|H|NI,RS|K1|E1
2025-20|P|CP art. 320:condescendência criminosa|C+|RD,CA,CD,LC|M|NI,RS,CM|K1|E1
2025-21|PP|CPP arts. 252–258:impedimento+suspeição do juiz|D+|LR,RD,IC,LC|H|NI,SS,RS|K3|E8
2025-22|PP|CPP arts. 261–267:acusado+defensor|D+|LR,RD|H|SS,RS,EX|K18|E8
2025-23|PP|CPP:citação judicial|D+|LR,RD,PS,CD,LC|H|RS,DS,SS|K18|E2
2025-24|PP|CPP:procedimento comum/instrução criminal|D+|LR,RD,PS,CD,LC|M|RS,PT,DS|K18|E2
2025-25|PP|L9099:recursos no JECrim|D+|LR,RD,PS,CD,IC,LC|M|AR,DS,RS|K7|E3
2025-26|PC|CPC:tempo dos atos processuais+penhora por oficial de justiça|C+|RD,CA,PS,CD,LC|M|RS,PT|K17|E8
2025-27|PC|CPC:cumprimento/execução de alimentos|C+|RD,CA,CD|M|RS,PT|K17|E8
2025-28|PC|CPC:restituição de prazo por falecimento do advogado|C+|RD,CA,PS,CD|M|DS,RS,EX|K17|E8
2025-29|PC|L9099:pedido, conciliação, contraposto+assistência no JEC|C+|RD,CA,PS,CD|M|NI,RS,PT|K8|E3
2025-30|PC|L12153:competência+cumprimento de sentença no JEFaz|C+|RD,EI,CA,CD,LC|L|CS,RS,EX|K9|E3
2025-31|C|CF art. 5º, XI:inviolabilidade domiciliar, flagrante+ordem judicial|C+|RD,CA,LC|M|EX,OG,RS|K19|E4
2025-32|C|CF art. 5º:ações constitucionais|D+|LR,RD,EI,IC|M|AR,SS,EX|K10|E4
2025-33|C|CF art. 12:nacionalidade+cargos privativos de brasileiro nato|C+|RD,CA,LC|M|SS,EX,RS|K11|E4
2025-34|C|CF arts. 37–40:regime remuneratório/previdenciário de servidor|C+|RD,CA|M|RS,EX,SS|K12|E4
2025-35|C|CF arts. 7º+8º:jornada, negociação coletiva+prescrição trabalhista|C+|RD,CA,CD,LC|M|EX,OG,RS|K19|E4
2025-36|A|L10261:afastamento de servidor para competição esportiva|C+|RD,CA,PS|M|RS,EX,PT|K13|E5
2025-37|A|L10261:posse, exercício+licença por saúde|C+|RD,CA,CD,LC|M|DS,RS,PT|K20|E5
2025-38|A|L10261:reintegração|C+|RD,CA,LC|M|RS,SS,PT|K20|E5
2025-39|A|L8429:sanções por lesão ao erário+dosimetria|C+|RD,CA,LC|M|RS,DR,SS|K20|E9
2025-40|A|L8429:entidade privada subvencionada+sujeitos da improbidade|C+|RD,CA,IC,LC|L|RS,DR,SS|K14|E6
2025-41|A|L8429:enriquecimento ilícito, vantagem indevida+sanções|C+|RD,CA,PS,LC|M|RS,DR,SS|K20|E9
2025-42|LI|R963:implantação+funcionamento do eproc|C+|RD,CA,PS,CD,IC|L|RS,DS,PT|K16|E7
2025-43|LI|R850:teletrabalho|C+|RD,CA|M|SS,RS,EX|K16|E7
2025-44|LI|LC1111:cargos em comissão/função de chefia+requisitos|D+|LR,RD,IC,LC|M|SS,RS,EX|K16|E7
2025-45|LI|RITJSP:sessões, reuniões, audiências, pauta+ordem dos trabalhos|D+|LR,RD,EI,PS|H|CS,RS,DS|K16|E7
2025-46|LI|NSCGJ:ofícios/comunicações, dados fiscais+expediente judicial|C+|RD,CA,CD|L|RS,PT,SS|K15|E7
```

## Síntese observada

Distribuição por domínio:

| ano | P | PP | PC | C | A | LI | total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 | 6 | 7 | 7 | 7 | 8 | 5 | 40 |
| 2023 | 6 | 7 | 7 | 7 | 8 | 5 | 40 |
| 2024 | 6 | 7 | 7 | 7 | 8 | 5 | 40 |
| 2025 | 4 | 5 | 5 | 5 | 6 | 5 | 30 |

Forma: `D+` 79; `C+` 69; `X` 1; `D-` 1.

Literalidade:

| ano | H | M | L |
|---:|---:|---:|---:|
| 2021 | 17 | 17 | 6 |
| 2023 | 19 | 15 | 6 |
| 2024 | 18 | 19 | 3 |
| 2025 | 6 | 20 | 4 |

Operações multi-rótulo mais presentes: `RD` 150; `LC` 92; `LR` 81; `CA` 69; `PS` 62; `CD` 56; `IC` 35; `EI` 32. `RD` é amplo por construção: alternativas jurídicas normalmente diferem por requisito; não deve ser lido sozinho como medida de dificuldade.

Distratores multi-rótulo: `RS` 141; `SS` 58; `PT` 53; `EX` 52; `DS` 38; `NI` 29; `CM` 14; `AR` 13; `CS` 12; `DR` 12; `OG` 11.

## Sinais por domínio

**Penal.** Alterna texto legal e caso curto. Falsidades, crimes funcionais e crimes contra Administração/Justiça exploram tipos vizinhos, elemento subjetivo, sujeito e consequência. Autoria: elementos típicos + diferenças mínimas + mini-casos.

**Processual Penal.** Impedimento/suspeição, defesa, comunicação, rito, júri, recursos e JECrim. Erros giram em torno de decisão, recurso, prazo, sujeito e etapa. Autoria: fluxos compactos e tabelas decisão→recurso/prazo.

**Processual Civil.** Auxiliares, comunicações, tutelas, pedidos, recursos, JEC e JEFaz. Muitos casos têm uma única chave normativa. Autoria: regra-base + exceção + mini-caso; competência, prazos e efeitos em tabela.

**Constitucional.** Direitos fundamentais, ações constitucionais, direitos sociais, nacionalidade e servidores. Distratores usam exceção, sujeito e generalização. Autoria: regra/exceção e pares conceituais.

**Administrativo.** Estatuto paulista e improbidade. Questões aproximam hipótese, requisito, sanção, prazo e consequência em narrativas funcionais. Autoria: hipótese→requisito→efeito, linhas do tempo e matriz modalidade→sanção.

**Legislação Interna.** Até 2024 predominam NSCGJ e operação cartorária/correicional. Em 2025 aparecem R963, R850, LC1111, RITJSP e NSCGJ. É o domínio mais dependente de texto específico e versão. Autoria: tabelas operacionais, sujeitos, condições, prazos e exemplos.

## Contrastes que o Gate 4 deve tornar explícitos

Falsidades e tipos vizinhos; impedimento/suspeição; rejeição/absolvição; pronúncia/impronúncia/absolvição sumária; recurso adequado/recurso vizinho; JEC/JECrim/JEFaz/rito comum; tutela antecedente e efeitos; nato/naturalizado; regra/exceção do servidor; infração disciplinar e sanção; improbidade modalidade/requisito/dano/sanção; regras operacionais internas e procedimentos próximos.

## Limites

São quatro provas e houve mudança objetiva de blueprint em 2025. Contagens descrevem a amostra, não probabilidades. Quando uma questão envolve vários dispositivos, o campo `source_or_institute` registra o instituto principal. Operação, distractor, contraste e sinal editorial são classificação analítica de backoffice, separada do texto normativo.

## Fechamento

- 150/150 questões jurídicas classificadas e rastreáveis;
- taxonomia definida;
- quatro fontes verificadas por hash/tamanho;
- observação separada de inferência editorial;
- edital preservado como autoridade;
- mudança de blueprint e limites explicitados.

**Gate 3: `closed`.**

Próximo: `DIREITO-004` — construir as seis matrizes de cobertura/autoria antes de qualquer redação substancial.
