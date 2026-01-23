from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ir_para_url(driver, url, timeout=10):
    """Navega para uma URL"""
    driver.get(url)
    # Aguarda a página carregar
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )


def clicar_por_id(driver, elemento_id, timeout=10):
    """Clica em elemento encontrado por ID (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.ID, elemento_id))
    )
    elemento.click()


def clicar_por_css(driver, seletor, timeout=10):
    """Clica em elemento encontrado por CSS (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, seletor))
    )
    elemento.click()


def clicar_por_xpath(driver, xpath, timeout=10):
    """Clica em elemento encontrado por XPath (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    elemento.click()


def escrever_por_id(driver, elemento_id, texto, timeout=10):
    """Escreve texto em campo encontrado por ID (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, elemento_id))
    )
    elemento.clear()
    elemento.send_keys(texto)


def escrever_por_css(driver, seletor, texto, timeout=10):
    """Escreve texto em campo encontrado por CSS (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )
    elemento.clear()
    elemento.send_keys(texto)


def escrever_por_xpath(driver, xpath, texto, timeout=10):
    """Escreve texto em campo encontrado por XPath (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    elemento.clear()
    elemento.send_keys(texto)


def apagar_por_id(driver, elemento_id, timeout=10):
    """Apaga o conteúdo de um campo encontrado por ID (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, elemento_id))
    )
    elemento.clear()


def apagar_por_css(driver, seletor, timeout=10):
    """Apaga o conteúdo de um campo encontrado por CSS (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )
    elemento.clear()


def apagar_por_xpath(driver, xpath, timeout=10):
    """Apaga o conteúdo de um campo encontrado por XPath (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    elemento.clear()


def obter_texto_por_id(driver, elemento_id, timeout=10):
    """Obtém o texto de um elemento encontrado por ID (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, elemento_id))
    )
    return elemento.text


def obter_texto_por_css(driver, seletor, timeout=10):
    """Obtém o texto de um elemento encontrado por CSS (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, seletor))
    )
    return elemento.text


def obter_texto_por_xpath(driver, xpath, timeout=10):
    """Obtém o texto de um elemento encontrado por XPath (com wait)"""
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return elemento.text

def fechar_browser(driver):
    """Fecha o navegador"""
    driver.quit()