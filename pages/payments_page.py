import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.web_driver import web_driver
from selenium.webdriver.common.by import By
from test_data.payments_data import cash_transfer_data
from locators.payments_locators import payment_locators
from locators.dashboard_locators import dashboard_locators


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, payment_locators['receiver'])))
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, payment_locators['iban'])))
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, payment_locators['amount'])))
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, payment_locators['title'])))
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, payment_locators['execute_button'])))
        self._recivier_input = self.driver.find_element(By.ID, payment_locators['receiver'])
        self._account_input = self.driver.find_element(By.ID, payment_locators['iban'])
        self._amount_input = self.driver.find_element(By.ID, payment_locators['amount'])
        self._title_input = self.driver.find_element(By.ID, payment_locators['title'])
        self._execution_button = self.driver.find_element(By.ID, payment_locators['execute_button'])

    @allure.step("Entering recievier")
    def enter_reciever(self, recievier):
        self._recivier_input = self.driver.find_element(By.ID, payment_locators['receiver']).send_keys(recievier)

    @allure.step("Entering iban number")
    def enter_iban_number(self, iban):
        self._account_input = self.driver.find_element(By.ID, payment_locators['iban']).send_keys(iban)

    @allure.step("Entering amount")
    def enter_amount(self, amount):
        self._amount_input = self.driver.find_element(By.ID, payment_locators['amount']).send_keys(amount)

    @allure.step("Entering title")
    def enter_title(self, title):
        self._amount_input = self.driver.find_element(By.ID, payment_locators['title']).send_keys(title)

    @allure.step("Send transfer")
    def send_transfer(self):
        self._execution_button = self.driver.find_element(By.ID, payment_locators['execute_button']).click()

    @allure.step("Close pop up")
    def close_pop_up(self):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, dashboard_locators['close_button'])))
        self._close_popup_button = self.driver.find_element(By.CSS_SELECTOR, dashboard_locators['close_button']).click()

    def simple_transfer(self, reciever=cash_transfer_data["receiver"], iban=cash_transfer_data["iban"], amount=cash_transfer_data["amount"], title=cash_transfer_data["title"]):
        """
        Execute simpler cash transfer
        :param reciever: Reciever
        :param iban: Reviecer iban number
        :param amount: Cash transfer amount
        :param title: Cash transfer title
        :return: Execute cash transfer if parameters are correct
        """
        self.enter_reciever(reciever)
        self.enter_iban_number(iban)
        self.enter_amount(amount)
        self.send_transfer()
        self.close_pop_up()