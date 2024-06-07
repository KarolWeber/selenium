import allure
from locators.dashboard_locators import phone_top_up_locators, quick_payment_locators, dashboard_locators
from test_data.dashboard_data import quick_payment_data, phone_top_up_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configuration.web_driver import web_driver
from selenium.webdriver.support.ui import Select

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        if self.driver is None:
            self.driver = web_driver()
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, quick_payment_locators['reciever'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, quick_payment_locators['amount'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, quick_payment_locators['title'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, quick_payment_locators['execute_button'])))
        self._quick_payment_reciver_input = self.driver.find_element(By.ID, quick_payment_locators['reciever'])
        self._quick_payment_amount_input = self.driver.find_element(By.ID, quick_payment_locators['amount'])
        self._quick_payment_title_input = self.driver.find_element(By.ID, quick_payment_locators['title'])    
        self._quick_payment_execute_button = self.driver.find_element(By.ID, quick_payment_locators['execute_button'])    

        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, phone_top_up_locators['reciever'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, phone_top_up_locators['amount'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, phone_top_up_locators['checkbox'])))
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, phone_top_up_locators['execute_button'])))
        self._top_up_phone_reciver_input = self.driver.find_element(By.ID, phone_top_up_locators['reciever'])
        self._top_up_phone_amount_input = self.driver.find_element(By.ID, phone_top_up_locators['amount'])
        self._top_up_phone_checkbox = self.driver.find_element(By.ID, phone_top_up_locators['checkbox'])
        self._top_up_phone_execute_button = self.driver.find_element(By.ID, phone_top_up_locators['execute_button'])


    @allure.step("Entering quick payment reciever")
    def enter_quick_payment_reciever(self, reciever):
        """
        Enter receiver for quick payment.
        :param reciever: Receiver's name for the quick payment.
        """
        dropdown_element = self.driver.find_element(By.ID, quick_payment_locators['reciever'])
        select = Select(dropdown_element)
        select_text = reciever
        for option in select.options:
            if select_text in option.text:
                select.select_by_visible_text(option.text)
                break

    @allure.step("Entering quick payment amount")
    def enter_quick_payment_amount(self, amount):
        """
        Enter amount for quick payment.
        :param amount: Amount for the quick payment.
        """
        self._quick_payment_amount_input = self.driver.find_element(By.ID, quick_payment_locators['amount']).send_keys(amount)

    @allure.step("Entering quick payment title")

    def enter_quick_payment_title(self, title):
        """
        Enter title for quick payment.
        :param title: Title for quick payment.
        """
        self._quick_payment_title_input = self.driver.find_element(By.ID, quick_payment_locators['title']).send_keys(title)

    @allure.step("Execute quick payment")
    def execute_quick_payment(self):
        """
        Click the execute button for quick payment.
        """
        self._quick_payment_execute_button = self.driver.find_element(By.ID, quick_payment_locators['execute_button']).click()

    @allure.step("Entering phone top-up number")
    def enter_phone_top_up_reciever(self, reciever):
        """
        Select receiver for phone top-up.
        :param reciever: Receiver's number for the phone top-up.
        """
        dropdown_element = self.driver.find_element(By.ID, phone_top_up_locators['reciever'])
        select = Select(dropdown_element)
        select_text = reciever
        for option in select.options:
            if select_text in option.text:
                select.select_by_visible_text(option.text)
                break

    @allure.step("Entering phone top-up amount")
    def enter_phone_top_up_amount(self, amount):
        """
        Enter amount for phone top-up.
        :param amount: Amount for phone top-up.
        """
        self._top_up_phone_amount_input = self.driver.find_element(By.ID, phone_top_up_locators['amount']).send_keys(amount)

    @allure.step("Select phone top-up checkbox")
    def select_phone_top_up_checkbox(self):
        """
        Click the checkbox for phone top-up.
        """
        self._top_up_phone_checkbox = self.driver.find_element(By.ID, phone_top_up_locators['checkbox']).click()

    @allure.step("Execute phone top-up")
    def execute_phone_top_up(self):
        """
        Click the execute button for phone top-up.
        """
        self._top_up_phone_execute_button = self.driver.find_element(By.ID, phone_top_up_locators['execute_button']).click()

    @allure.step("Close popup")
    def close_pop_up(self):
        """
        Wait for and click the close button on the dashboard popup.
        """
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, dashboard_locators['close_button'])))
        self._close_popup_button = self.driver.find_element(By.CSS_SELECTOR, dashboard_locators['close_button']).click()

    def quick_payment(self, reciever=quick_payment_data['receiver'], amount=quick_payment_data['amount'], title=quick_payment_data['title']):
        """
        Perform a quick payment.
        :param reciever: Receiver's name for the quick payment.
        :param amount: Amount for the quick payment.
        :param title: Title for quick payment.
        """
        self.enter_quick_payment_reciever(reciever)
        self.enter_quick_payment_amount(amount)
        self.enter_quick_payment_title(title)
        self.execute_quick_payment()
        self.close_pop_up()

    def phone_top_up(self, reciever=phone_top_up_data['receiver'], amount=phone_top_up_data['amount']):
        """
        Perform a phone top-up
        :param reciever: Receiver's number for the phone top-up.
        :param amount: Amount for phone top-up.
        """
        self.enter_phone_top_up_reciever(reciever)
        self.enter_phone_top_up_amount(amount)
        self.select_phone_top_up_checkbox()
        self.execute_phone_top_up()
        self.close_pop_up()
            

        
