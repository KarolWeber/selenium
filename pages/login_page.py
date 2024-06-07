import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.web_driver import web_driver
from selenium.webdriver.common.by import By
from test_data.login_data import login_data
from locators.login_locators import login_locators
import os
from dotenv import load_dotenv

load_dotenv()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        if driver is None:
            self.driver = web_driver()
        self.driver.get(os.getenv('BASE_URL'))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_id'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_password'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_button'])))
        self._login_input = self.driver.find_element(By.ID, login_locators['login_id'])
        self._password_input = self.driver.find_element(By.ID, login_locators['login_password'])
        self._login_button = self.driver.find_element(By.ID, login_locators['login_button'])

    @allure.step("Entering login ID")
    def enter_login(self, login_id):
        """
        Enter login ID.
        :param login_id: Login ID to be entered.
        """
        self._login_input = self.driver.find_element(By.ID, login_locators['login_id']).send_keys(login_id)

    @allure.step("Entering password")
    def enter_password(self, password):
        """
        Enter password.
        :param password: Password to be entered.
        """
        self._password_input = self.driver.find_element(By.ID, login_locators['login_password']).send_keys(password)

    @allure.step("Log in")
    def log_in(self):
        """
        Click the login button.
        """
        self._login_button = self.driver.find_element(By.ID, login_locators['login_button']).click()

    def login(self, user_id=login_data["login_id"], user_password=login_data["login_password"], log_in=True):
        """
        Perform user login.
        :param user_id: Login ID to be entered.
        :param user_password: Password to be entered.
        :param log_in: Flag indicating whether to perform login (default True).
        """
        self.enter_login(user_id)
        self.enter_password(user_password)
        if log_in:
            self.log_in()
