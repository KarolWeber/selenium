import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configuration.web_driver import web_driver
from test_data.dashboard_data import quick_payment_data, phone_top_up_data
from test_data.login_data import login_data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from locators.dashboard_locators import dashboard_locators
from utilities.tools import assertion_teardown


@pytest.mark.dashboard
@allure.suite("Dashboard")
class TestDashboard:
    def setup_method(self):
        self.driver = web_driver()
        LoginPage(self.driver).login()
        self.dashboard_page = DashboardPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Quick payment")
    def test_quick_payment(self):
        self.dashboard_page.quick_payment()
        expected = f"Przelew wykonany! {quick_payment_data['receiver']} - {quick_payment_data['amount']},00PLN - {quick_payment_data['title']}"
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, dashboard_locators['message']))).text
        assertion_teardown(self.driver, expected, current)

    @allure.title("Phone top up")
    def test_phone_top_up(self):
        self.dashboard_page.phone_top_up()
        expected = f"Doładowanie wykonane! {phone_top_up_data['amount']},00PLN na numer {phone_top_up_data['receiver']}"
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, dashboard_locators['message']))).text
        assertion_teardown(self.driver, expected, current)
