import undetected_chromedriver as uc


def start_browser():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("--headless=new")

    driver = uc.Chrome(
        options=options,
        use_subprocess=True
    )

    return driver
