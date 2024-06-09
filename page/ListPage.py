import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from configuration.ConfigProvider import ConfigProvider
from page.BasePage import BasePage
from testdata.DataProvider import DataProvider

button_add_new_list = "button[data-testid='list-composer-button']"


class ListPage(BasePage):

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("ui.Создать новую доску в списке {name_list}")
    def create_new_list(self, name_list):
        with allure.step("ui.Прокрутить страницу до кнопки Add another list"):
            iframe = self.__driver.find_element(By.CSS_SELECTOR, button_add_new_list)
            ActionChains(self.__driver)\
                .scroll_to_element(iframe)\
                .perform()
        
        with allure.step("ui.Навести мышку на кнопку Add another list"):
            hoverable = self.__driver.find_element(By.CSS_SELECTOR, button_add_new_list)
            ActionChains(self.__driver)\
            .move_to_element(hoverable)\
            .perform()

        with allure.step("ui.Нажать на кнопку Add another list"):
            self.__driver.find_element(By.CSS_SELECTOR, button_add_new_list).click()

        with allure.step("ui.Ввести название нового списка"):
            self.__driver.find_element(By.CSS_SELECTOR, "form.vVqwaYKVgTygrk > textarea[data-testid='list-name-textarea']").send_keys(name_list)

        with allure.step("ui.Нажать кнопку Add list"):
            self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-add-list-button']").click()
        

    @allure.step("ui.Получить id списка по его имени {name_list}")
    def get_id_list_by_name(self, name_list):
        id_list = ''
        elements = self.__driver.find_elements(By.CSS_SELECTOR, "ol#board > li")
        for elem in elements:
            text = elem.text
            list = text.splitlines()
            if(list[0] == name_list): 
                id_list = elem.get_attribute('data-list-id')
                break            
        return id_list
    
    @allure.step("ui.Перемотать на нужный список {id_list}")
    def scroll_list(self, id_list: str):
        list_element = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"]')
        self.__driver.execute_script("arguments[0].scrollIntoView(true);", list_element)

    @allure.step("ui.Промотать до списка с  id {id_list}")
    def elem_info(self, id_list):
        elem = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"]')
        return elem
    
    @allure.step("ui.Найти в списке lists по id {id_list}")
    def find_list_by_id(self, id_list: str)-> bool:
        find_id = False
        list_of_lists = self.__driver.find_elements(By.CSS_SELECTOR, f'ol#board > li')
        for elem in list_of_lists:
            if elem.find_element(By.CSS_SELECTOR, f'[data-list-id="{id_list}"]'):
                find_id = True
        return find_id
        
    @allure.step("ui.Перемотать на нужный список {id_list}")
    def scroll_to_list_action(self, id_list):
        iframe = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"]')
        ActionChains(self.__driver)\
            .scroll_to_element(iframe)\
            .perform()

