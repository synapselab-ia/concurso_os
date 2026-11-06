# SHADOW_BASELINE | p001 | 2026-11-06

## Fonte e escopo de auditoria

- Base GitHub `main` observada antes do desenvolvimento: `121fe5318ec280a8281847a0c82ffd6ab064f638`.
- Referência de cobertura: `competitions/tjsp-escrevente-2025/SYLLABUS.md` e `BLUEPRINT.json` do mesmo estado.
- Dados observados: seis arquivos `block_review` de `p001`, sessão `chatgpt-20261009-p001-tjsp-adaptive-01`, Q01-Q60.
- Resultados: **60 questões principais**, **48 acertos**, **12 erros**, **80%**.
- Não contar o resumo histórico separado de 28 questões de Português; ele não possui evidência por questão compatível e não é combinado automaticamente.
- Reforços e itens excluídos por QA não contam novamente.
- O material dos **dois chats em andamento** não foi lido como resultado concluído nem modificado.

## Classificação de cobertura aproximada

Na conferência de aliases do catálogo de 56 categorias amplas com os rótulos de `subtopic` dos 60 itens persistidos:

- 59/60 itens tiveram associação inequívoca a uma categoria **indicativa**.
- 1 ficou `UNMAPPED`: Q33, `direito-administrativo / cf_37_v_funcao_de_confianca_vs_cargo_em_comissao`. Não se deve forçar correspondência a outra disciplina só porque a referência normativa menciona CF art. 37.
- 25 das 56 categorias receberam pelo menos um item; 31 ficaram sem item associado nesse snapshot.
- Nenhuma categoria ampla, mesmo com vários acertos, comprova cobertura integral de seus artigos/recortes do edital.

### Distribuição por grupo observada

| Grupo | Itens | Peso oficial por 70 |
|---|---:|---:|
| Português | 10 | 16 |
| Direito (todos os ramos) | 29 | 30 |
| Atualidades / PCD | 1 | 4 |
| Matemática | 6 | 4 |
| Informática | 7 | 9 |
| Raciocínio Lógico | 7 | 7 |

A coluna oficial não é uma cota obrigatória para 60 microdrills; é referência estatística e deve ser combinada com lacunas de cobertura, revisão, dificuldade individual e risco eliminatório.

## Limites e próximos gates

- Isto é uma auditoria de dados reais via GitHub API, **não** execução integral do Python remoto no checkout.
- Plano sugerido é read-only: não reserva questões, não altera CONFIG, não cria sessões e não ativa nada.
- `python tools/verify.py` deve ser executado sobre o checkout completo; falta de acesso Git no container deve ser registrada como impossibilidade, jamais como PASS.
- Antes de ativação futura: confirmar que os dois blocos em curso foram persistidos, recalcular o snapshot no SHA novo e implementar reservas de tópicos entre chats (ou admitir explicitamente que ainda podem selecionar o mesmo tema).
- O próximo checkpoint pedagógico esperado para a série Q01-Q60 é em 100 questões principais válidas, se o histórico consolidado confirmar continuidade sem duplicações.
