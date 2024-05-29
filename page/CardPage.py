import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider


class CardPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver


    def create_new_card(self, id_list, name_card):
        
        # with allure.step("ui.Прокрутить страницу до нужного списка {id_list}"):
        #     iframe = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"]')
        #     ActionChains(self.__driver)\
        #         .scroll_to_element(iframe)\
        #         .perform()
            
        # with allure.step("ui.Навести мышку на кнопку Add a card"):
        #     hoverable = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] button[data-testid="list-add-card-button"]')
        #     ActionChains(self.__driver)\
        #     .move_to_element(hoverable)\
        #     .click(hoverable)\
        #     .perform()

        
<<<<<<< HEAD
=======

>>>>>>> d6fc7e5df8f0857eb377e32acc54f136dcd58b36
        with allure.step("ui.Нажать на кнопку Add a card"):
            # li[data-list-id="665655a76c7007157023eeb8"] > div[data-testid="list"] div[data-testid="list-footer"] button[data-testid="list-add-card-button"]
            button_add_card = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] > div[data-testid="list"] div[data-testid="list-footer"] button[data-testid="list-add-card-button"]')
            button_add_card.click()
        
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[data-testid='list-card-composer-textarea']")))
        
        with allure.step("ui.Ввести имя новой карточки {name_card}"):
            type_name = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,  f'li[data-list-id="{id_list}"] form textarea[data-testid="list-card-composer-textarea"]')))
            type_name.send_keys(name_card)
        
        with allure.step("ui.Нажать кнопку Add a card"):
            add_card_button = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] form button[data-testid="list-card-composer-add-card-button"]')))
            add_card_button.click()
        
        with allure.step("ui.Нажать кнопку x"):
            x_card_button = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] form button[data-testid="list-card-composer-cancel-button"]')))
            x_card_button.click
<<<<<<< HEAD

=======
            
>>>>>>> d6fc7e5df8f0857eb377e32acc54f136dcd58b36
    def scroll_to_list(self, id_list):
        iframe = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"]')
        ActionChains(self.__driver)\
            .scroll_to_element(iframe)\
            .perform()


    def click_add_a_card(self,id_list):
        self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] button.O9vivwyDxMqo3q.bxgKMAm3lq5BpA.iUcMblFAuq9LKn.PnEv2xIWy3eSui.SEj5vUdI3VvxDc').click()
        time.sleep(3)


    def type_name_card(self, name_card: str, id_list: str) -> None:
        type_name = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,  f'li[data-list-id="{id_list}"] form textarea[data-testid="list-card-composer-textarea"]')))
        type_name.send_keys(name_card)

    def click_add_card_with_text(self, id_list: str):
        add_card_button = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] form button[data-testid="list-card-composer-add-card-button"]')))
        add_card_button.click()
        time.sleep(3)

    def click_x_new_card(self):
        self.__driver.find_element(By.CSS_SELECTOR, "div.Y44OETtkQ7R6r5 button.bxgKMAm3lq5BpA.iUcMblFAuq9LKn.HAVwIqCeMHpVKh.SEj5vUdI3VvxDc").click()
        time.sleep(3)

        


