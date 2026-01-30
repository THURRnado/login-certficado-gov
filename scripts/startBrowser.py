from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

def start_browser(headless=False, profile_path=None):
    options = Options()
    
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    
    # Política de seleção automática de certificado (formato JSON correto)
    cert_policy = json.dumps({
        "pattern": "https://*.gov.br",
        "filter": {
            "ISSUER": {
                "CN": "AC SyngularID Multipla"
            }
        }
    })
    
    # Adiciona a política - IMPORTANTE: use lista JSON
    prefs = {
        "profile.managed_auto_select_certificate_for_urls": [cert_policy]
    }
    options.add_experimental_option("prefs", prefs)
    
    if profile_path:
        options.add_argument(f"--user-data-dir={profile_path}")
    
    if headless:
        options.add_argument("--headless=new")
    
    service = Service(ChromeDriverManager().install())
    
    return webdriver.Chrome(service=service, options=options)