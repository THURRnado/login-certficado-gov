from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ir_para_url(driver, url, timeout=10):
    """Navega para uma URL e espera o carregamento da página."""
    driver.get(url)
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def clicar_xpath(driver, xpath, timeout=10):
    """Clica em um elemento localizado por XPath."""
    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    elemento.click()


def digitar_xpath(driver, xpath, texto, timeout=10, limpar_antes=True):
    """
    Digita texto em um campo localizado por XPath.

    Args:
        driver: WebDriver.
        xpath: XPath do elemento.
        texto: Texto a ser digitado.
        timeout: Tempo máximo de espera.
        limpar_antes: Se True, limpa o campo antes de digitar.
    """
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    if limpar_antes:
        elemento.clear()
    elemento.send_keys(texto)


def apagar_xpath(driver, xpath, timeout=10):
    """Apaga o conteúdo de um campo localizado por XPath."""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    elemento.clear()


def obter_texto_xpath(driver, xpath, timeout=10):
    """Obtém o texto de um elemento localizado por XPath."""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return elemento.text


def fechar_browser(driver):
    """Fecha o navegador (driver.quit)."""
    driver.quit()