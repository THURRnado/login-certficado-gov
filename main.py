from playwright.sync_api import sync_playwright

CERT_PATH = "caminho_cert_aqui"
CERT_PASSWORD = "senha_aqui"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        args=["--no-sandbox", "--disable-dev-shm-usage"]
    )

    context = browser.new_context(
        ignore_https_errors=True,
        client_certificates=[
            {
                "origin": "https://sefaz.pb.gov.br",
                "pfxPath": CERT_PATH,
                "passphrase": CERT_PASSWORD,
            },
            {
                "origin": "https://www4.sefaz.pb.gov.br",
                "pfxPath": CERT_PATH,
                "passphrase": CERT_PASSWORD,
            }
        ]
    )

    page = context.new_page()
    page.goto("https://sefaz.pb.gov.br/servirtual")

    page.wait_for_load_state("networkidle")

    # 🔥 Agora acessando iframe correto pelo name
    frame = page.frame_locator("iframe[name='acessoATF']")

    frame.locator("a.atf-link-certificado").click()

    page.wait_for_timeout(10000)

    print("URL após login:", page.url)

    browser.close()