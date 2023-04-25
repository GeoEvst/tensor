from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не найден локатор {locator}")

    # def find_elements(self, locator, time=10):
    #     return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
    #                                                   message=f"Не найден локатор {locator}")

    def check_element_id(self, locator):
        try:
            self.driver.find_element(By.ID, locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_class_name(self, locator):
        try:
            self.driver.find_element(By.CLASS_NAME, locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_xpath(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
            return True
        except NoSuchElementException:
            return False

    def check_element_css(self, locator):
        try:
            self.driver.find_element(By.CSS_SELECTOR, locator)
            return True
        except NoSuchElementException:
            return False

    def return_url(self):
        return self.driver.current_url

    def open_site(self):
        return self.driver.get(self.base_url)