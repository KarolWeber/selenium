import allure
import pytest
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.dashboard_locators import user_data_locators
from locators.login_locators import login_locators
from locators.dashboard_locators import dashboard_locators
from test_data.login_data import login_data, login_errors
from selenium.webdriver.common.by import By
from test_data.payments_data import cash_transfer_data
from configuration.web_driver import web_driver
from pages.login_page import LoginPage
from pages.payments_page import PaymentPage
from components.side_menu import SideMenu
from utilities.tools import assertion_teardown


@pytest.mark.login
@allure.suite("Payments")
class TestPayments:
    def setup_method(self):
        """
        Instantiate a WebDriver instance.
        """
        self.driver = web_driver()
        LoginPage(self.driver).login()
        SideMenu.payments(self.driver)
        self.payment_page = PaymentPage(self.driver)

    def teardown_method(self):
        """
        Close WebDriver instance.
        """
        self.driver.quit()

    @allure.title("Simple Cash Transfer")
    def test_simple_cash_transfer(self):
        """
        Verify simple cash transfer functionality.

        Steps:
        1. Initiate a simple cash transfer.
        2. Check the displayed success message.
        """
        self.payment_page.simple_transfer()
        expected = f"Przelew wykonany! {cash_transfer_data['amount']},00PLN dla {cash_transfer_data['receiver']}"
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, dashboard_locators['message']))).text
        assertion_teardown(self.driver, expected, current)




