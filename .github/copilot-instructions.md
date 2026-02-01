# Instruções rápidas para agentes de código (Copilot / AI)

Objetivo
- Ajudar agentes a tornar-se produtivos rapidamente neste repositório "LoginCertDigital": entender a arquitetura (backend/frontend), pontos de integração de certificado digital, e fluxos de build/test/CI.

Onde olhar primeiro (ordem recomendada)
- README.md (raiz) — visão geral do projeto e comandos de uso.
- Arquivos de entrada da aplicação: `Program.*`, `Startup.*`, `main.*` ou `app.js`.
- Diretórios principais: `src/`, `backend/`, `web/`, `frontend/`, `api/`, `services/`.
- Configurações: `appsettings*.json`, `.env`, `config/*.yml`, `package.json`, `requirements.txt`.
- Certificados / chaves: procurar arquivos `*.pfx`, `*.pem`, ou referências a `CERT_`, `PFX`, `certPath`.
- Scripts e automações: `scripts/`, `Makefile`, `Dockerfile`.
- Testes: `tests/`, `*.test.*`, `jest.config.js`, `pytest.ini`.
- CI: `.github/workflows/*` — comandos reais usados no pipeline.

"Big picture" — como deduzir a arquitetura
- Localize o arquivo de bootstrap (Program/Startup/main) para entender quais módulos são carregados.
- Procure por rotas/handlers (ex.: `Controllers/`, `routes/`) para mapear API vs UI.
- Identifique entradas de dependências (DI containers, import/require) para ver boundaries de serviços.
- Se houver Dockerfile e workflow de CI, siga esses arquivos para saber como o projeto é construído e testado no pipeline.

Padrões e convenções do projeto (o que buscar e replicar)
- Configuração por arquivo + variáveis de ambiente: prefira modificar/ler `appsettings.json` ou `.env` conforme o padrão do repositório.
- Busca por implementações de autenticação: pesquisar por termos `Certificate`, `Cert`, `ClientCertificate`, `Auth`, `Login`.
- Tratamento de secrets: evite colocar arquivos .pfx no repositório; prefira referências a variáveis de ambiente (ex.: `CERT_PATH`, `CERT_PASSWORD`).
- Nomeclatura comum: serviços em `*Service`, controllers em `*Controller`, repos em `*Repository`.

Fluxos de desenvolvimento e comandos úteis (verifique se estão presentes)
- Backend .NET (se aplicável): `dotnet build`, `dotnet run`, `dotnet test`.
- Node.js (se aplicável): `npm install`, `npm run build`, `npm test`.
- Python (se aplicável): `python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt`.
- Docker: `docker build -t logincertdigital .` e `docker run -e CERT_PATH=...`.
- CI: rever `.github/workflows/*.yml` para comandos exatos usados pelo pipeline.

Como editar sem quebrar o fluxo de certificado
- Ao alterar codepaths de autenticação, mantenha o mesmo contrato de configuração (mesmo nome das variáveis de ambiente / keys em appsettings).
- Não comitar certificados: altere apenas referências (p.ex. nome da variável) nas configurações e documente pré-requisitos (pfx path, password).

Buscas rápidas recomendadas (glob patterns)
- `**/*{Program,Startup,main}*.*`
- `**/*(Controller|Service|Repository)/**/*.*`
- `**/*(cert|certificate|pfx|pem|certPath|CERT_)*.*`
- `**/.github/workflows/*.yml`
- `**/Dockerfile`, `**/package.json`, `**/requirements.txt`, `**/appsettings*.json`

Exemplos práticos (o que o agente deve fazer)
- Antes de alterar autenticação: abra `Program.*`/`Startup.*` e procure onde o middleware de certificado é registrado.
- Para adicionar teste: siga padrão de testes existentes em `tests/` e execute o comando usado no CI.
- Para reproduzir bug localmente: siga comandos em `README.md` ou `.github/workflows/*` — reproduza o mesmo `dotnet/npm/python` command e variáveis de ambiente.

Notas finais
- Sempre preferir seguir comandos e variáveis descobertas no repositório (README e workflows) em vez de assumir valores.
- Se faltar documentação crítica (onde o certificado é carregado, nome das env vars), peça ao mantenedor trecho exato do arquivo de bootstrap ou mostre a busca que você fez.

Feedback
- Indique qual seção ficou ambígua ou se quer exemplos extraídos de arquivos específicos do repositório para incorporar aqui.