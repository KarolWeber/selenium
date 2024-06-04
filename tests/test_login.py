import allure
import pytest
from locators.dashboard_locators import user_data_locators
from test_data.login_data import login_data
from selenium.webdriver.common.by import By
from configuration.web_driver import web_driver
from pages.login import LoginPage
from utilities.tools import assertion_teardown


@pytest.mark.login
@allure.suite("Login")
class TestLogin:
    @allure.title("Successful")
    def test_login_successful(self):
        driver = web_driver()
        login_page = LoginPage(driver)
        login_page.login()
        expected = login_data['username']
        current = driver.find_element(By.ID, user_data_locators['username']).text
        assertion_teardown(driver, expected, current)




