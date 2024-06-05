from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def web_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver
