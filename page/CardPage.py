import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider


class CardPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver


    def create_new_card(self, id_list, name_card):

        with allure.step("ui.Нажать на кнопку Add a card"):
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

    def update_name_card(self, name_card: str, new_name_card: str):
        with allure.step("ui.Нажать на название карточки"):
            name_click = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="board"]//a[contains(text(), "{name_card}")]')))
            name_click.click()

        # div.ySQIVFZtJ_1G5J.QIUmf9rrTzMUV2 div[role='dialog']-card
        with allure.step("ui.Стереть имя карточки {name_card} и ввести новое имя {new_name_card}"):
            clear_name = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ySQIVFZtJ_1G5J.QIUmf9rrTzMUV2 div[role='dialog']")))
            clear_name.click()
            clear_name.send_keys(Keys.BACKSPACE)
            clear_name.send_keys(new_name_card)
            clear_name.send_keys(Keys.ENTER)

        with allure.step("ui.Закрыть карточку"):
            card_close = self.__driver.find_element(By.CSS_SELECTOR, "button.js-close-window.dialog-close-button")
            card_close.click()

        

      

    def scroll_to_list(self, id_list):
        iframe = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"]')
        ActionChains(self.__driver)\
            .scroll_to_element(iframe)\
            .perform()

        


