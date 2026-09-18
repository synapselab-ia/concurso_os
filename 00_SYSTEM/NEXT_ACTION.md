# NEXT_ACTION

## DIREITO-015: Gerar e validar novo PDF de `direito-processual-penal 0.1.0-rc.2`

`DIREITO-014` promove o conteúdo corrigido de `0.1.0-draft.3` para `0.1.0-rc.2` sem nova alteração jurídica.

## Estado de entrada esperado após merge de DIREITO-014

- pack: `direito-processual-penal`;
- versão: `0.1.0-rc.2`;
- Markdown congelado: Git blob `8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18`;
- base semântica corrigida: `0.1.0-draft.3`, blob `135592d9762b8f639a199ebe795ffcca71e747bd`;
- promoção para rc.2: metadados somente;
- DPP-05: `PASS_AFTER_CORRECTION`;
- 25 unidades e 60 questões preservadas;
- IDs `DPP-*` em headings: ausentes;
- tutor: `0.1.0-rc.2`, comportamento inalterado;
- `APOSTILA.pdf` vigente: ausente;
- PDF rc.1: `INVALIDATED_SEMANTICALLY`, não reutilizar.

## Trabalho obrigatório

1. Obter o Markdown rc.2 exatamente correspondente ao Git blob acima.
2. Gerar PDF A4 pesquisável exclusivamente desse Markdown.
3. Executar readback textual e confirmar, no mínimo:
   - título e versão rc.2;
   - Unidade 5;
   - redação correta do art. 371 sobre intimação por despacho na petição;
   - redação correta do art. 372 sobre adiamento da instrução criminal;
   - Prática autoral e Gabarito comentado.
4. Renderizar todas as páginas e inspecionar clipping, sobreposição, glifos, tabelas, separação entre prática e gabarito e legibilidade.
5. Calcular tamanho, páginas, SHA-256 e Git blob do candidato final.
6. Publicar exatamente o binário auditado em `materials/tjsp-escrevente-2025/direito-processual-penal/APOSTILA.pdf`.
7. Ler o caminho remoto e comprovar identidade binária com o candidato local.
8. Atualizar QA, MANIFEST, CHANGELOG, PROJECT_CONTROL, CHECKPOINT, NEXT_ACTION e plano B2.
9. Executar `python tools/verify.py` ou documentar a impossibilidade real.
10. Revisar diff, abrir PR e mesclar sob DEC-0009 se limpo.

## Gate seguinte

Depois do PDF corrigido e versionado, o usuário fará um smoke curto de regressão no NotebookLM. Não é necessário repetir toda a bateria anterior; confirmar apenas o novo PDF, a correção dos arts. 371/372, um treino sem vazamento e ausência de metadados internos.
