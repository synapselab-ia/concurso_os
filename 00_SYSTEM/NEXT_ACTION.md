# NEXT_ACTION

## INSTALL-001 — Validar o SubjectPack de Português no NotebookLM

O `SubjectPack` de Língua Portuguesa `1.0.0` está produzido e pronto para teste de instalação. O próximo passo é validar a experiência real de uso no NotebookLM antes de replicar o formato para as demais matérias.

### Execução manual pelo usuário

1. criar um notebook novo de Português;
2. carregar, nesta ordem:
   - `METODOLOGIA_NOTEBOOKLM.md`;
   - `APOSTILA.pdf`;
   - `ANALISE_BANCA.md`;
   - edital 2025 original;
   - prova TJSP/VUNESP 2025;
   - opcionalmente, provas 2024, 2023 e 2021;
3. executar os quatro testes descritos em `materials/tjsp-escrevente-2025/portugues/MANIFEST.md`;
4. confirmar que o notebook identifica a versão `1.0.0`, o escopo de 16 questões, a distinção entre inferência e extrapolação e a dinâmica de uma questão por vez;
5. testar uma sessão curta de 3 a 5 questões e observar se as correções seguem a metodologia;
6. trazer ao ChatGPT apenas os desvios relevantes ou um `SESSION_REPORT` curto.

### Critério de aprovação

`INSTALL-001` passa quando o notebook consegue ser montado apenas com o MANIFEST e executa o protocolo sem depender de contexto deste chat.

Após aprovação, a próxima ação será replicar o padrão de `SubjectPack` para a próxima matéria prioritária, reutilizando o que funcionou em Português e corrigindo qualquer problema detectado na instalação.

Não iniciar outro pack antes de concluir este smoke test, salvo decisão canônica explícita.
