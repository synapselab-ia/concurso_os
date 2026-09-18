# NEXT_ACTION

## DIREITO-016: Executar smoke curto de regressão no NotebookLM para `direito-processual-penal 0.1.0-rc.2`

`DIREITO-015` gerou, auditou e publicou o PDF corrigido de `0.1.0-rc.2` com identidade binária exata.

## Estado de entrada esperado após merge de DIREITO-015

- pack: `direito-processual-penal`;
- versão: `0.1.0-rc.2`;
- Markdown congelado: Git blob `8e68fe2ec3e79ade50b9c3c4cecb53ae8049bd18`;
- DPP-05 / CPP 370-372: `PASS_AFTER_CORRECTION`;
- `APOSTILA.pdf`: 28 páginas A4, PDF 1.4, 37.917 bytes, pesquisável;
- SHA-256 do PDF: `aeaa44ac6a275623d79098d0699c18899f83d6ade75be8661f71a3ad9dfc36fe`;
- Git blob canônico do PDF: `6374969ba722451dd6740364e24c41f25e730b54`;
- readback textual: `PASS_TEXT_READBACK`;
- inspeção visual: `PASS_VISUAL_28_OF_28`;
- identidade binária remota: `PASS_CANONICAL_BINARY_IDENTITY`;
- PDF rc.1: histórico apenas, `INVALIDATED_SEMANTICALLY`;
- smoke comportamental amplo anterior: `PASS_BEHAVIORAL_ON_RC1_CORPUS_INVALIDATED`.

## Objetivo de DIREITO-016

Fazer apenas uma regressão curta no NotebookLM. O usuário executa essa etapa manualmente.

### Configuração

```text
FONTE DO NOTEBOOKLM
-> somente o APOSTILA.pdf canônico de direito-processual-penal 0.1.0-rc.2

CONFIGURAÇÃO DA CONVERSA
-> usar o bloco operacional de METODOLOGIA_NOTEBOOKLM.md rc.2
```

Não carregar QA, MANIFEST, SOURCES, matriz, edital ou outros artefatos de backoffice como fonte estudável.

## Smoke mínimo obrigatório

1. Perguntar sobre os arts. 371 e 372 do CPP. O tutor deve refletir a correção:
   - art. 371: intimação por despacho na petição em que for requerida, observado o art. 357;
   - art. 372: adiamento da instrução criminal e marcação de dia e hora para prosseguimento na presença das partes e testemunhas, com termo nos autos.
2. Pedir uma questão objetiva A-E, uma por vez, e confirmar ausência de dica/gabarito antes da tentativa.
3. Confirmar que não aparecem IDs `DPP-*`, QA, gates ou metadados internos.

Não é necessário repetir Teste, Cartões, Mapa mental nem a bateria epistemológica completa já observada no smoke anterior.

## Registro

Depois da evidência real do usuário:

- atualizar `NOTEBOOKLM_SMOKE_0.1.0.md`;
- atualizar QA, MANIFEST, CHANGELOG, PROJECT_CONTROL, CHECKPOINT, NEXT_ACTION e plano B2;
- classificar a regressão somente conforme evidência observada.

Se a regressão passar, encerrar o pipeline deste SubjectPack como release candidate validado e iniciar o próximo pack canônico: `direito-processual-civil`.

## Gate determinístico de DIREITO-015

A última tentativa de checkout falhou antes de `python tools/verify.py`:

```text
git clone --depth 1 --branch release/direito-processual-penal-0.1.0-rc.2-pdf https://github.com/synapselab-ia/concurso_os.git /tmp/concurso_os_d015
fatal: unable to access 'https://github.com/synapselab-ia/concurso_os.git/': Could not resolve host: github.com
```

Exit code: `128`.

Resultado: `NOT_EXECUTED_CURRENT_ENVIRONMENT`, nunca `PASS`.
