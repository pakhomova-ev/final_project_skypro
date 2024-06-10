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
        Метод возвращает адрес текущей страницы
        """
        return self.__driver.current_url
    
    @allure.step("Дождаться когда элемент будет виден")
    def is_visible(self, locator)-> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_x_in_list(self, x_list: list, x_id: str) ->bool:
        new_id_list = []
        for item in x_list:
            if "id" in item:
                new_id_list.append(item["id"])
        
        id_find = False
        for elem in new_id_list:
            if elem == x_id:
                id_find = True
        
        return id_find
    
    def find_x_by_name_in_list(self, x_list: list, name_x: str) ->bool:
            name_find = False
            for x in x_list:
                if x.get("name") == name_x:
                    name_find = True
            return name_find
