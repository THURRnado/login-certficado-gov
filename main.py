from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        url = "https://det.sit.trabalho.gov.br/login?r=%2Fservicos"
        print(f"Acessando a URL: {url}")
        page.goto(url)

        print("Aguardando e clicando no botão 'Entrar com gov.br'...")
        page.locator("#botao").click()

        page.wait_for_load_state("networkidle")
        
        # Clicando no botão do certificado digital pelo ID
        print("Clicando em 'Seu certificado digital'...")
        page.locator("#login-certificate").click()

        print("=" * 50)
        print("ATENÇÃO: HORA DO TRABALHO MANUAL")
        print("1. Resolva o CAPTCHA que apareceu na tela.")
        print("2. Selecione o seu Certificado Digital (a janela do Windows/Linux vai abrir).")
        print("3. Digite o PIN (se pedir).")
        print("O script está em pausa e aguardando você chegar na página final...")
        print("=" * 50)

        # O script vai congelar aqui até a URL mudar para o painel de serviços.
        # Coloquei timeout=0 para ele esperar o tempo que for necessário.
        page.wait_for_url("**/servicos**", timeout=0) 
        
        print("Login detectado com sucesso!")
        print(f"URL atual: {page.url}")

        # Salvar os cookies mágicos (Sessão)
        print("Salvando cookies da sessão para uso futuro...")
        cookies = context.cookies()
        import json
        import os
        os.makedirs("auth", exist_ok=True)
        with open("auth/session_cookies.json", "w") as f:
            json.dump(cookies, f)

        input("Tudo certo! Pressione Enter para fechar...")
        browser.close()

if __name__ == "__main__":
    main()