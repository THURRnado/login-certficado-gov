import os
from scripts.startBrowser import start_browser
from scripts import comandosSelenium
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL_LOGIN = "https://det.sit.trabalho.gov.br/login?r=%2Fservicos"
PROFILE_PATH = os.path.abspath("./chrome_profile")
CERTIFICADO_PATH = os.path.abspath("./certificadoDig/certificado.pfx")
SENHA_PATH = os.path.abspath("./certificadoDig/senha.txt")

# Lê a senha do certificado
with open(SENHA_PATH, 'r') as f:
    senha_certificado = f.read().strip()

print(f"📁 Certificado: {CERTIFICADO_PATH}")
print(f"🔐 Senha carregada")

# Abre VISÍVEL para o CAPTCHA
driver = start_browser(
    headless=False,
    profile_path=PROFILE_PATH,
    certificado_pfx=CERTIFICADO_PATH
)

comandosSelenium.ir_para_url(driver, URL_LOGIN)

comandosSelenium.clicar_xpath(driver, '//*[@id="botao"]')

url_certificado = comandosSelenium.obter_url_botao_xpath(driver, '//*[@id="login-certificate"]')
if url_certificado:
    print(f"🔗 URL capturada: {url_certificado}")
    comandosSelenium.ir_para_url_cert(driver, url_certificado)

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ENTER)

sleep(5)

driver.quit()