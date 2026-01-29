import os
from scripts.startBrowser import start_browser
from scripts import comandosSelenium

URL_LOGIN = "https://det.sit.trabalho.gov.br/login?r=%2Fservicos"
PROFILE_PATH = os.path.abspath("./chrome_profile")

# Abre VISÍVEL para o CAPTCHA
driver = start_browser(
    headless=False,
    profile_path=PROFILE_PATH
)

comandosSelenium.ir_para_url(driver, URL_LOGIN)

comandosSelenium.clicar_xpath(driver, '//*[@id="botao"]')
comandosSelenium.clicar_xpath(driver, '//*[@id="login-certificate"]')

# Aguarda o humano resolver
comandosSelenium.aguardar_resolucao_captcha(driver)

print("CAPTCHA resolvido. Reiniciando em headless...")

# Fecha navegador visível
driver.quit()

# Reabre HEADLESS com o MESMO profile
driver = start_browser(
    headless=False,
    profile_path=PROFILE_PATH
)

#AQUI DEVO IR DIRETO PRA ABA DO DET, LEVAR EM CONTA DE QUE O LOGIN COM CERTIFICADO FOI CONCLUÍDO

# Continua já autenticado
#comandosSelenium.ir_para_url(driver, "https://det.sit.trabalho.gov.br/servicos")

print("Automação rodando em headless.")

input("Pressione ENTER para encerrar")
driver.quit()
