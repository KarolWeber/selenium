from configuration.web_driver import web_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.side_menu_locators import side_menu_locators


class SideMenu:
    @staticmethod
    def payments(driver):
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, side_menu_locators['side_menu_payments'])))
        driver.find_element(By.ID, side_menu_locators['side_menu_payments']).click()

