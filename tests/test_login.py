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
    @allure.title("Successful")
    def test_login_successful(self):
        driver = web_driver()
        login_page = LoginPage(driver)
        login_page.login()
        expected = login_data['username']
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, user_data_locators['username'])))
        current = driver.find_element(By.ID, user_data_locators['username']).text
        assertion_teardown(driver, expected, current)

    @allure.title("Invalid username length")
    def test_login_invalid_username_length(self):
        driver = web_driver()
        login_page = LoginPage(driver)
        login_page.enter_login("Test")
        login_page.enter_password("Test1234")
        expected = login_errors['login_length_error']
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_id'])))
        current = driver.find_element(By.ID, login_locators['login_error_id']).text
        assertion_teardown(driver, expected, current)

    @allure.title("Invalid password length")
    def test_login_invalid_password_length(self):
        driver = web_driver()
        login_page = LoginPage(driver)
        login_page.enter_password("Test")
        login_page.enter_login("Test1234")
        expected = login_errors['password_length_error']
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_password'])))
        current = driver.find_element(By.ID, login_locators['login_error_password']).text
        assertion_teardown(driver, expected, current)

    @allure.title("No username")
    def test_login_no_username(self):
        driver = web_driver()
        login_page = LoginPage(driver)
        login_page.enter_login("")
        login_page.enter_password("Test")
        expected = login_errors['field_required']
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_id'])))
        current = driver.find_element(By.ID, login_locators['login_error_id']).text
        assertion_teardown(driver, expected, current)

    @allure.title("No password")
    def test_login_no_password(self):
        driver = web_driver()
        login_page = LoginPage(driver)
        login_page.enter_password("")
        login_page.enter_login("Test")
        expected = login_errors['field_required']
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_error_password'])))
        current = driver.find_element(By.ID, login_locators['login_error_password']).text
        assertion_teardown(driver, expected, current)








