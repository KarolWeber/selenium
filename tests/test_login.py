import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.dashboard_locators import user_data_locators
from locators.login_locators import login_locators
from test_data.login_data import login_data, login_errors
from selenium.webdriver.common.by import By
from configuration.web_driver import web_driver
from pages.login_page import LoginPage
from utilities.tools import assertion_teardown


@pytest.mark.login
@allure.suite("Login")
class TestLogin:
    def setup_method(self):
        """
        Instantiate a WebDriver instance.
        """
        self.driver = web_driver()
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        """
        Close WebDriver instance.
        """
        self.driver.quit()

    @allure.title("Successful")
    def test_login_successful(self):
        """
        Verify successful user login.

        Steps:
        1. Perform user login.
        2. Check the displayed username.
        """
        self.login_page.login()
        expected = login_data['username']
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, user_data_locators['username']))).text
        assertion_teardown(self.driver, expected, current)

    @allure.title("Invalid username length")
    def test_login_invalid_username_length(self):
        """
        Verify login length error message.

        Steps:
        1. Enter a login with invalid length.
        2. Enter a password.
        3. Check the displayed login length error message.
        """
        self.login_page.enter_login("Test")
        self.login_page.enter_password("Test1234")
        expected = login_errors['login_length_error']
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_id']))).text
        assertion_teardown(self.driver, expected, current)

    @allure.title("Invalid password length")
    def test_login_invalid_password_length(self):
        """
        Verify password length error message.

        Steps:
        1. Enter a password with invalid length.
        2. Enter a login.
        3. Check the displayed password length error message.
        """
        self.login_page.enter_password("Test")
        self.login_page.enter_login("Test1234")
        expected = login_errors['password_length_error']
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_password']))).text
        assertion_teardown(self.driver, expected, current)

    @allure.title("No username")
    def test_login_no_username(self):
        """
        Verify empty login field error message.

        Steps:
        1. Leave the login field empty.
        2. Enter a password.
        3. Check the displayed error message for empty login field.
        """
        self.login_page.enter_login("")
        self.login_page.enter_password("Test")
        expected = login_errors['field_required']
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_id']))).text
        assertion_teardown(self.driver, expected, current)

    @allure.title("No password")
    def test_login_no_password(self):
        """
        Verify empty password field error message.

        Steps:
        1. Enter a login.
        2. Leave the password field empty.
        3. Check the displayed error message for empty password field.
        """
        self.login_page.enter_password("")
        self.login_page.enter_login("Test")
        expected = login_errors['field_required']
        current = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_password']))).text
        assertion_teardown(self.driver, expected, current)








