# NEXT_ACTION

## DIREITO-007 — Concluir release candidate do SubjectPack `direito-penal`

O conteúdo jurídico de `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` foi aprovado em `0.1.0-draft.3` e congelado no release candidate `0.1.0-rc.1`.

Já foram executados nesta passagem:

- criação e auditoria estática de `METODOLOGIA_NOTEBOOKLM.md`;
- sincronização de `APOSTILA.md`, `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md` e QA para `0.1.0-rc.1`;
- QA estático do corpus para NotebookLM;
- geração e QA textual/visual de um candidato local de PDF com 18 páginas A4, 48.593 bytes e SHA-256 `d190a2a73b6e6ad84d60d2a241ca8574ac4f34a75cfba1d8f643dbf95f9ea469`.

O pack **ainda não é release**. O PDF auditado nesta passagem é local e não está publicado no GitHub. O smoke real do NotebookLM também não foi executado. Não marcar esses gates como PASS canônico antes da execução real.

## Entradas obrigatórias

Ler conjuntamente:

- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.md` — conteúdo congelado do `0.1.0-rc.1`;
- `materials/tjsp-escrevente-2025/direito-penal/APOSTILA_QA_0.1.0.md` — evidência dos gates já realizados e dos bloqueios atuais;
- `materials/tjsp-escrevente-2025/direito-penal/METODOLOGIA_NOTEBOOKLM.md`;
- `materials/tjsp-escrevente-2025/direito-penal/MANIFEST.md`, `SOURCES.md` e `CHANGELOG.md`;
- `00_SYSTEM/APOSTILA_AUTHORING_PROTOCOL.md`, especialmente QA-7, QA-9 e QA-10;
- `00_SYSTEM/QA_PROTOCOL.md`;
- arquitetura NotebookLM em `00_SYSTEM/PROJECT_SPEC.md` e `00_SYSTEM/ARCHITECTURE.md`.

## 1. Preservar o conteúdo congelado

Não reabrir escopo nem alterar silenciosamente DP-01…DP-10 ou as 30 questões.

Se surgir erro material no conteúdo jurídico, voltar o estado para draft, corrigir e registrar nova passagem semântica antes de qualquer PDF final.

## 2. Publicar `APOSTILA.pdf` canônico

O repositório ainda não contém o binário.

Quando houver caminho confiável para transferir ou regenerar o PDF no ambiente de implementação:

1. produzir o PDF exclusivamente a partir do `APOSTILA.md` congelado;
2. preferir reproduzir o candidato local já auditado quando tecnicamente possível;
3. se o binário diferir, registrar novo número de páginas, tamanho e SHA-256;
4. versionar `materials/tjsp-escrevente-2025/direito-penal/APOSTILA.pdf` no GitHub.

Não usar o hash do candidato local como se fosse hash do repositório enquanto o arquivo não estiver efetivamente versionado.

## 3. Confirmar QA-9 no binário versionado

Sobre o `APOSTILA.pdf` efetivamente publicado:

- confirmar que é pesquisável;
- fazer readback textual;
- conferir acentos e símbolos;
- renderizar e inspecionar todas as páginas;
- verificar clipping, sobreposição, tabelas, hierarquia e legibilidade;
- verificar separação entre perguntas e gabarito;
- registrar páginas, tamanho, SHA-256 e, quando disponível, Git blob.

Somente essa verificação fecha o gate canônico de PDF.

## 4. Executar smoke real do NotebookLM

Quando houver acesso efetivo à interface:

```text
FONTES
→ somente APOSTILA.pdf canônico

CONFIGURAÇÃO DA CONVERSA
→ bloco operacional de METODOLOGIA_NOTEBOOKLM.md
```

Inspecionar, no mínimo:

- chat configurado para dúvida jurídica e correção;
- Teste ou artefato de recuperação equivalente;
- Cartões;
- Mapa mental ou artefato hierárquico equivalente.

Confirmar que metodologia/backoffice não viram conteúdo estudável e que o tutor não inventa jurisprudência ou doutrina ausente da fonte.

Enquanto a interface estiver indisponível, manter `pending_user_smoke`.

## 5. Gate canônico do repositório

Antes de encerrar `DIREITO-007`:

```bash
python tools/verify.py
```

Neste runtime, `git ls-remote https://github.com/synapselab-ia/concurso_os.git HEAD` continua falhando com `Could not resolve host: github.com`, impedindo checkout canônico. Enquanto isso persistir, registrar `not_executed_current_environment`; não tratar como PASS.

## 6. Critério de saída

`DIREITO-007` só fecha quando houver evidência real de:

- `METODOLOGIA_NOTEBOOKLM.md` criada e auditada;
- metadados do `0.1.0-rc.1` coerentes;
- `APOSTILA.pdf` versionado e QA textual/visual confirmado sobre o binário canônico;
- QA NotebookLM estático concluído e smoke real registrado;
- `MANIFEST.md`, `SOURCES.md`, `CHANGELOG.md` e QA refletindo exatamente o estado;
- `python tools/verify.py` executado ou impossibilidade atual explicitamente reavaliada conforme DEC-0009.

Somente depois disso decidir explicitamente se o candidato pode ser promovido a release final. Os outros cinco SubjectPacks de B2 permanecem aguardando a validação completa deste primeiro pipeline jurídico.