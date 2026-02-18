from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        client_certificates=[
            {
                "origin": "https://sso.acesso.gov.br",
                "pfx_path": "auth/3S SOLUCOES CONTABEIS S_S LTDA_10587724000137.pfx",
                "passphrase": "senha_aqui",
            }
        ],
        permissions=["geolocation"],
        geolocation={"latitude": -23.5505, "longitude": -46.6333},
    )

    page = context.new_page()

    page.on("request", lambda request: print(">>", request.url))

    # Página de login
    page.goto(
        "https://det.sit.trabalho.gov.br/login?r=%2Fservicos",
        wait_until="networkidle"
    )

    page.locator('#botao').click()

    login_cert = page.locator('#login-certificate')
    login_cert.wait_for(state="visible")

    with page.expect_navigation():
        page.evaluate("""
            const form = document.querySelector('#login-certificate').form;
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'operation';
            input.value = 'login-certificate';
            form.appendChild(input);
            form.submit();
        """)

    '''print("Login realizado:", page.url)

    page.goto(
        "https://det.sit.trabalho.gov.br/servicos",
        wait_until="networkidle"
    )

    print("Página serviços:", page.url)'''

    page.wait_for_timeout(8000)