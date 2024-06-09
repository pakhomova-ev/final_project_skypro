import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.__driver = driver
        self.__url = url
        self.wait = WebDriverWait(self.__driver, 10)
   
    def get_current_url(self) -> str:
        """
        Метод возвращает адрес стекущей страницы
        """
        return self.__driver.current_url
    
    @allure.step("Дождаться когда элемент будет виден")
    def is_visible(self, locator)-> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))