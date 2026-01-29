from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


def start_browser(headless=False, profile_path=None, certificado_pfx=None):
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    
    # Ignora erros de certificado
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")

    if profile_path:
        options.add_argument(f"--user-data-dir={profile_path}")

    # Configuração do certificado digital
    if certificado_pfx and os.path.exists(certificado_pfx):
        # Converte para caminho absoluto
        cert_path = os.path.abspath(certificado_pfx)
        
        # Adiciona o certificado ao Chrome
        options.add_argument(f"--auto-select-certificate-for-urls={cert_path}")
        
        # Preferências para seleção automática de certificado
        prefs = {
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
        }
        options.add_experimental_option("prefs", prefs)

    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())

    return webdriver.Chrome(service=service, options=options)