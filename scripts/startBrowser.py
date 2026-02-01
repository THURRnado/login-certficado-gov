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
    
    # Auto-select certificate: substitua pattern e ISSUER/CN pelos valores reais
    auto_select = [
        {
            "pattern": "https://*.acesso.gov.br/*",
            "filter": {
                "ISSUER": {
                    "CN": "AC SyngularID Multipla"
                }
            }
        }
    ]
    options.add_argument(f'--auto-select-certificate-for-urls={json.dumps(auto_select)}')
    
    # Recomendações anti-detect
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    
    if profile_path:
        options.add_argument(f"--user-data-dir={profile_path}")
    
    if headless:
        options.add_argument("--headless=new")
    
    service = Service(ChromeDriverManager().install())
    
    return webdriver.Chrome(service=service, options=options)