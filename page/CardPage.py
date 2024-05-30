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

    @allure.step("ui.Создать новую карточку {name_card}  в списке id {id_list}")
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

    @allure.step("ui.Изменить имя карточки {name_card}")
    def update_name_card(self, name_card: str, new_name_card: str):
        with allure.step("ui.Нажать на название карточки"):
            name_click = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="board"]//a[contains(text(), "{name_card}")]')))
            name_click.click()

        with allure.step("ui.Стереть имя карточки {name_card} и ввести новое имя {new_name_card}"):
            textarea = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ySQIVFZtJ_1G5J.QIUmf9rrTzMUV2 div[role='dialog'] div.window-title >textarea")))
            textarea.click()
            textarea.send_keys(Keys.CONTROL, "a")
            textarea.send_keys(Keys.BACKSPACE)

            textarea.send_keys(new_name_card)

            textarea.send_keys(Keys.ENTER)

        with allure.step("ui.Закрыть карточку"):
            card_close = self.__driver.find_element(By.CSS_SELECTOR, "button.js-close-window.dialog-close-button")
            card_close.click()

    @allure.step("ui.Переместить карточку {id_card} в другой список {id_new_list}")
    def move_to_another_list(self, id_card, id_new_list):

        draggable = self.__driver.find_element(By.CSS_SELECTOR, f'div.board-canvas div[data-card-id="{id_card}"] > div.amUfYqLTZOvGsn > a')
        droppable = self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_new_list}"] ol.RD2CmKQFZKidd6')
        ActionChains(self.__driver)\
        .drag_and_drop(draggable, droppable)\
        .pause(1)\
        .perform()
        
    @allure.step("ui.Удалить карточку")
    def delete_card(self, id_card):

        hoverable = self.__driver.find_element(By.CSS_SELECTOR, f'div.board-canvas div[data-card-id="{id_card}"] > div.amUfYqLTZOvGsn')
        ActionChains(self.__driver)\
        .move_to_element(hoverable)\
        .perform()

        name_card = self.__driver.find_element(By.CSS_SELECTOR, f'div.board-canvas div[data-card-id="{id_card}"] > div.amUfYqLTZOvGsn > a')
        name_card.click()

        button_archive = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='dialog'] > div.BXekJYFkPyovJz a.button-link.js-archive-card")))
        button_archive.click()

        elem = self.__driver.find_element(By.CSS_SELECTOR, "div[role='dialog'] > div.BXekJYFkPyovJz a.button-link.js-delete-card.negate")
        elem.click()

        button2 = WebDriverWait(self.__driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.pop-over.is-shown input.js-confirm.full.nch-button--danger")))
        button2.click()



        


