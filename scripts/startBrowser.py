from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def start_browser(headless=False, profile_path=None):
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    if profile_path:
        options.add_argument(f"--user-data-dir={profile_path}")

    if headless:
        options.add_argument("--headless=new")

    service = Service(ChromeDriverManager().install())

    return webdriver.Chrome(service=service, options=options)
