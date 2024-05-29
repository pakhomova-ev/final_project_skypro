import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class ListApi:
     
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("ui.Создать новый список")
    def create_new_list(self, name_list):
        # button[data-testid="list-composer-button"]
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-button']").click()
        
        # form.vVqwaYKVgTygrk > textarea[data-testid="list-name-textarea"]
        self.__driver.find_element(By.CSS_SELECTOR, "form.vVqwaYKVgTygrk > textarea[data-testid='list-name-textarea']").send_keys(name_list)
        # button[data-testid="list-composer-add-list-button"]
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-add-list-button']").click()
        #получить список, чтобы удостовериться, что досок стало на 1 больше div.board-canvas ol#board >li - список досок

    def scroll_to_button_add_list(self):
        iframe = self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-button']")
        ActionChains(self.__driver)\
            .scroll_to_element(iframe)\
            .perform()
        
        time.sleep(3)