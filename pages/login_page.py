import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_id'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_password'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, login_locators['login_button'])))
        self._login_input = self.driver.find_element(By.ID, login_locators['login_id'])
        self._password_input = self.driver.find_element(By.ID, login_locators['login_password'])
        self._login_button = self.driver.find_element(By.ID, login_locators['login_button'])

    @allure.step("Entering login ID")
    def enter_login(self, login_id):
        self._login_input = self.driver.find_element(By.ID, login_locators['login_id']).send_keys(login_id)

    @allure.step("Entering password")
    def enter_password(self, password):
        self._password_input = self.driver.find_element(By.ID, login_locators['login_password']).send_keys(password)

    @allure.step("Log in")
    def log_in(self):
        self._login_button = self.driver.find_element(By.ID, login_locators['login_button']).click()

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
