from scripts.startBrowser import start_browser
from scripts import comandosSelenium
import time
import random

driver = start_browser()

comandosSelenium.ir_para_url(driver, "https://det.sit.trabalho.gov.br/login?r=%2Fservicos")
comandosSelenium.clicar_xpath(driver, '//*[@id="botao"]')
comandosSelenium.clicar_xpath(driver, '//*[@id="login-certificate"]')

input("Pressione Enter para fechar...")
comandosSelenium.fechar_browser(driver)