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
        """
        Enter receiver for payment.
        :param recievier: Receiver's name to be entered.
        """
        self._recivier_input = self.driver.find_element(By.ID, payment_locators['receiver']).send_keys(recievier)

    @allure.step("Entering iban number")
    def enter_iban_number(self, iban):
        """
        Enter IBAN for payment.
        :param iban: IBAN to be entered.
        """
        self._account_input = self.driver.find_element(By.ID, payment_locators['iban']).send_keys(iban)

    @allure.step("Entering amount")
    def enter_amount(self, amount):
        """
        Enter amount for payment.
        :param amount: Amount for payment.
        """
        self._amount_input = self.driver.find_element(By.ID, payment_locators['amount']).send_keys(amount)

    @allure.step("Entering title")
    def enter_title(self, title):
        """
        Enter title for payment.
        :param title: Title for payment.
        """
        self._amount_input = self.driver.find_element(By.ID, payment_locators['title']).send_keys(title)

    @allure.step("Send transfer")
    def send_transfer(self):
        """
        Click the execute button for payment.
        """
        self._execution_button = self.driver.find_element(By.ID, payment_locators['execute_button']).click()

    @allure.step("Close pop up")
    def close_pop_up(self):
        """
        Wait for and click the close button on the dashboard popup.
        """
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, dashboard_locators['close_button'])))
        self._close_popup_button = self.driver.find_element(By.CSS_SELECTOR, dashboard_locators['close_button']).click()

    def simple_transfer(self, reciever=cash_transfer_data["receiver"], iban=cash_transfer_data["iban"], amount=cash_transfer_data["amount"], title=cash_transfer_data["title"]):
        """
        Execute simpler cash transfer
        :param reciever: Receiver's name to be entered.
        :param iban: IBAN to be entered.
        :param amount: Amount for payment.
        :param title: Title for payment.
        """
        self.enter_reciever(reciever)
        self.enter_iban_number(iban)
        self.enter_amount(amount)
        self.send_transfer()
        self.close_pop_up()