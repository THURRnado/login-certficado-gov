from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time



def captcha_presente(driver):
    try:
        driver.find_element(By.XPATH, "//iframe[contains(@src,'captcha')]")
        return True
    except NoSuchElementException:
        return False


def aguardar_resolucao_captcha(driver, intervalo=2):
    print("\n🛑 CAPTCHA detectado!")
    print("👉 Resolva manualmente no navegador.")
    print("⏳ Aguardando...\n")

    while captcha_presente(driver):
        time.sleep(intervalo)

    print("✅ CAPTCHA resolvido.\n")


def ir_para_url_cert(driver, url):
    driver.get(url)


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


def obter_url_botao_xpath(driver, xpath, timeout=10):
    """
    Obtém a URL de um botão/link localizado por XPath.
    Tenta capturar de atributos href, onclick, data-url ou formaction.
    
    Args:
        driver: WebDriver.
        xpath: XPath do elemento.
        timeout: Tempo máximo de espera.
    
    Returns:
        str: URL encontrada ou None se não houver.
    """
    elemento = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    
    # Tenta diferentes atributos que podem conter URLs
    atributos = ['href', 'onclick', 'data-url', 'formaction', 'data-href']
    
    for atributo in atributos:
        url = elemento.get_attribute(atributo)
        if url:
            # Se for onclick, pode estar em formato: window.location='URL'
            if atributo == 'onclick' and 'http' in url:
                import re
                match = re.search(r'https?://[^\s\'"]+', url)
                if match:
                    return match.group(0)
            elif url.startswith('http'):
                return url
    
    return None


def selecionar_certificado_digital(driver, nome_certificado=None, timeout=10):
    """
    Seleciona o certificado digital na janela do gov.br e clica em OK.
    
    Args:
        driver: WebDriver
        nome_certificado: Nome parcial do certificado (opcional). 
                         Se None, seleciona o primeiro disponível.
        timeout: Tempo máximo de espera
    """
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    
    try:
        print("⏳ Aguardando janela de seleção de certificado...")
        time.sleep(2)
        
        if nome_certificado:
            # Seleciona certificado específico
            xpath_cert = f"//div[contains(text(), '{nome_certificado}')]"
            print(f"🔍 Procurando certificado: {nome_certificado}")
        else:
            # Seleciona o primeiro da lista
            xpath_cert = "//div[@class='certificate-item'] | //tr[contains(@class, 'certificate')]//td[1]"
            print("🔍 Selecionando primeiro certificado disponível...")
        
        certificado = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath_cert))
        )
        certificado.click()
        print("✅ Certificado selecionado")
        
        time.sleep(0.5)
        
        # Clica no botão OK
        print("👆 Clicando em OK...")
        botao_ok = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='OK' or text()='Ok']"))
        )
        botao_ok.click()
        print("✅ Certificado confirmado!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao selecionar certificado: {e}")
        return False


def fechar_browser(driver):
    """Fecha o navegador (driver.quit)."""
    driver.quit()