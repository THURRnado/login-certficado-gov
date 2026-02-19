from playwright.sync_api import sync_playwright
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding, PrivateFormat, NoEncryption
import os

PFX_PATH = "auth/3S SOLUCOES CONTABEIS S_S LTDA_10587724000137.pfx"
PASSPHRASE = "senha_aq"
CERT_PEM = "auth/cert.pem"
KEY_PEM  = "auth/key.pem"

def converter_pfx_para_pem():
    with open(PFX_PATH, "rb") as f:
        pfx_data = f.read()
    private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
        pfx_data, PASSPHRASE.encode()
    )
    with open(CERT_PEM, "wb") as f:
        f.write(certificate.public_bytes(Encoding.PEM))
        if additional_certs:
            for cert in additional_certs:
                f.write(cert.public_bytes(Encoding.PEM))
    with open(KEY_PEM, "wb") as f:
        f.write(private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()))

if not os.path.exists(CERT_PEM) or not os.path.exists(KEY_PEM):
    converter_pfx_para_pem()

ORIGENS = [
    "https://sso.acesso.gov.br",
    "https://certificado.sso.acesso.gov.br",
    "https://acesso.gov.br",
    "https://staging.acesso.gov.br",
    "https://det.sit.trabalho.gov.br",
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        client_certificates=[
            {"origin": origem, "certPath": CERT_PEM, "keyPath": KEY_PEM}
            for origem in ORIGENS
        ],
        permissions=["geolocation"],
        geolocation={"latitude": -23.5505, "longitude": -46.6333},
    )

    page = context.new_page()

    page.goto(
        "https://det.sit.trabalho.gov.br/login?r=%2Fservicos",
        wait_until="networkidle"
    )

    print("=" * 50)
    print("Faça o login manualmente no browser.")
    print("Clique em certificado digital e complete o captcha.")
    print("O script continuará automaticamente após o login.")
    print("=" * 50)

    # Aguarda até chegar na página de serviços (login completo)
    page.wait_for_url("**/servicos**", timeout=120000)
    print("Login concluído! URL:", page.url)

    # Salva cookies da sessão autenticada para reutilizar
    cookies = context.cookies()
    import json
    with open("auth/session_cookies.json", "w") as f:
        json.dump(cookies, f)
    print("Sessão salva em auth/session_cookies.json")

    # A partir daqui o script continua automatizado
    page.goto("https://det.sit.trabalho.gov.br/servicos", wait_until="networkidle")
    print("Página de serviços:", page.url)

    input("Pressione Enter para fechar...")