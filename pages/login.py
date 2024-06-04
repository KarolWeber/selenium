import allure

from configuration.url import base_url
from configuration.web_driver import web_driver
from selenium.webdriver.common.by import By
from test_data.login_data import login_data
from locators.login_locators import login_locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        if driver is None:
            self.driver = web_driver()
        self.driver.get(base_url)
        self.login_input = self.driver.find_element(By.ID, login_locators['login_id'])
        self.password_input = self.driver.find_element(By.ID, login_locators['login_password'])
        self.login_button = self.driver.find_element(By.ID, login_locators['login_button'])

    @allure.step("Entering login ID")
    def enter_login(self, login_id):
        """
        Filling login input.
        :param login_id: User login ID.
        """
        self.login_input = self.driver.find_element(By.ID, login_locators['login_id']).send_keys(login_id)

    @allure.step("Entering password")
    def enter_password(self, password):
        """
        Filling password input.
        :param password: User password.
        """
        self.password_input = self.driver.find_element(By.ID, login_locators['login_password']).send_keys(password)

    @allure.step("Log in")
    def log_in(self):
        """
        Clickin on login button.
        :return: If credentials are correct -> Login the user into the system.
        """
        self.login_button = self.driver.find_element(By.ID, login_locators['login_button']).click()

    def login(self, user_id=login_data["login_id"], user_password=login_data["login_password"], log_in=True):
        """
        Login the user into the system
        :param user_id: User login ID. Default get from test data
        :param user_password: User password. Default get from test data
        :param log_in: If True (default), user click login button
        :return: If credentials are correct and log_in is True -> Login the user into the system
        """
        self.enter_login(user_id)
        self.enter_password(user_password)
        if log_in:
            self.log_in()
