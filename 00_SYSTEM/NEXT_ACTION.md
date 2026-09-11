# NEXT_ACTION

## BASE-001 — Executar baseline inicial de `p001` no TJSP

Pré-condições já satisfeitas: adapter, fontes, blueprint, enrollment e mapa mínimo de competências existem.

Próxima execução com participação do estudante:

1. carregar `competitions/tjsp-escrevente-2025/BASELINE_PLAN.json`;
2. aplicar o `stage_1` uma questão por vez, registrando resposta e confiança antes da correção;
3. usar questões inéditas por padrão e corrigir com fonte apropriada;
4. persistir cada observação como `EvidenceEvent` append-only no enrollment de `p001`;
5. não atribuir `MASTERED` com base nesse rastreio inicial;
6. ao concluir o stage 1, produzir o primeiro estado derivado e definir o stage 2 adaptativo;
7. fazer o writing screen depois do stage 1 objetivo.

O baseline exige respostas reais de `p001`; não inventar evidência para avançar o estado.
