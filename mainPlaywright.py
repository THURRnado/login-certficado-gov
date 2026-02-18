from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    context = browser.new_context(
        client_certificates=[
            {
                "origin": "https://certificado.sso.acesso.gov.br",
                "cert_path": "auth/client.pem",
                "key_path": "auth/client.key",
            }
        ]
    )

    page = context.new_page()
    page.goto("https://certificado.sso.acesso.gov.br")

    # Continue navegando normalmente aqui
    print(page.title())

    browser.close()