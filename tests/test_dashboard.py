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
    @allure.title("Quick payment")
    def test_quick_payment(self):
        driver = web_driver()
        LoginPage(driver).login()
        dashboard_page = DashboardPage(driver)
        dashboard_page.quick_payment()
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, dashboard_locators['message'])))
        expected = f"Przelew wykonany! {quick_payment_data['receiver']} - {quick_payment_data['amount']},00PLN - {quick_payment_data['title']}"
        current = driver.find_element(By.ID, dashboard_locators['message']).text
        assertion_teardown(driver, expected, current)

    @allure.title("Phone top up")
    def test_phone_top_up(self):
        driver = web_driver()
        LoginPage(driver).login()
        dashboard_page = DashboardPage(driver)
        dashboard_page.phone_top_up()
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, dashboard_locators['message'])))
        expected = f"Doładowanie wykonane! {phone_top_up_data['amount']},00PLN na numer {phone_top_up_data['receiver']}"
        current = driver.find_element(By.ID, dashboard_locators['message']).text
        assertion_teardown(driver, expected, current)
