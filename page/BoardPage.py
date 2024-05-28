import allure
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class BoardPage:

    # https://trello.com/b/KjaoiGyt/rte
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get("ui", "base_url")
    
    @allure.step("ui.Перейти на страницу доски")
    def open_board_page(self, name_board: str, short_link:str):
        self.__url = self.url + f'/b/{short_link}/{name_board}'
        self.__driver.get(self.__url)


    @allure.step("ui.удалить доску")
    def delete_board(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RPO6eTW4FLJhI0")))
        self.__driver.find_element(By.CSS_SELECTOR, "button.frrHNIWnTojsww.GDunJzzgFqQY_3 span[data-testid='OverflowMenuHorizontalIcon']").click()
        
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.board-menu-container")))
        self.__driver.find_element(By.CSS_SELECTOR, "a.js-close-board").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.no-back")))
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='close-board-confirm-button']").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.board-menu-container")))
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='close-board-delete-board-button']").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.rX4pAv5sWHFNjp")))
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='close-board-delete-board-confirm-button']").click()

    @allure.step("ui.Создать новую доску")
    def create_new_board(self):
        self.__driver.find_element(By.CSS_SELECTOR, "li[data-testid='create-board-tile']").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.rX4pAv5sWHFNjp")))

        name_board = DataProvider().generate_board_name()
        name_list = DataProvider().generate_board_name()

        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='create-board-title-input']").send_keys(name_board)
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='create-board-submit-button']").click()

        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid='list-name-textarea']").send_keys(name_list)
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-add-list-button']").click()

    @allure.step("ui.Создать новый список")
    def create_new_list(self, name_list):
        # button[data-testid="list-composer-button"]
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-button']").click()
        

        # form.vVqwaYKVgTygrk > textarea[data-testid="list-name-textarea"]
        self.__driver.find_element(By.CSS_SELECTOR, "form.vVqwaYKVgTygrk > textarea[data-testid='list-name-textarea']").send_keys(name_list)
        # button[data-testid="list-composer-add-list-button"]
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='list-composer-add-list-button']").click()
        #получить список, чтобы удостовериться, что досок стало на 1 больше div.board-canvas ol#board >li - список досок

    # def create_new_card(self):

    # div.content-all-boards > div > div >div.boards-page-board-section.mod-no-sidebar >div > ul.boards-page-board-section-list > li > a >div > div[title="against"] 
    @allure.step("ui.Создать новую карточку")
    def create_new_card(self, id_list: str):
        time.sleep(3)
        self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id={id_list}] button[data-testid="list-add-card-button"]').click()
        time.sleep(3)
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[data-testid='list-card-composer-textarea']")))
        time.sleep(3)
        self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id={id_list}] form textarea[data-testid="list-card-composer-textarea"]').send_keys("jfijdf")
        time.sleep(3)
        self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id={id_list}] form button[data-testid="list-card-composer-add-card-button"]').click()

    def click_add_a_card(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button.O9vivwyDxMqo3q.bxgKMAm3lq5BpA.iUcMblFAuq9LKn.PnEv2xIWy3eSui.SEj5vUdI3VvxDc").click()
        time.sleep(3)

    def type_name_card(self, name_card):
        self.__driver.find_element(By.CSS_SELECTOR, "textarea[data-testid='list-card-composer-textarea']").send_keys(name_card)

    def click_add_card_with_text(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button.bxgKMAm3lq5BpA.SdamsUKjxSBwGb.SEj5vUdI3VvxDc").click()

    def click_x_new_card(self):
        self.__driver.find_element(By.CSS_SELECTOR, "div.Y44OETtkQ7R6r5 button.bxgKMAm3lq5BpA.iUcMblFAuq9LKn.HAVwIqCeMHpVKh.SEj5vUdI3VvxDc").click()
        time.sleep(3)

    def find_lists(self, id_list):

        list_lists = self.__driver.find_element(
            By.CSS_SELECTOR, 'li[data-list-id]')
        list_lists.click()

    def open_card(self):
        elem = self.__driver.find_element(By.CSS_SELECTOR, "div[data-card-id='6655e55dee96e693b90ac09a'] > div.amUfYqLTZOvGsn > a")
        elem.click()
        WebDriverWait(self.__driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.NauH5zhD2hZvpP.R6tO1m6fTtV8_6.DVtxDmkCMy5qRd")))

    def change_name_card(self):
        elem_name = self.__driver.find_element(By.CSS_SELECTOR, "div.NauH5zhD2hZvpP.R6tO1m6fTtV8_6.DVtxDmkCMy5qRd textarea[data-testid='card-back-title-input']")
        elem_name.send_keys(Keys.CONTROL, "a")
        elem_name.send_keys("222")
        time.sleep(3)
        elem_but = self.__driver.find_element(By.CSS_SELECTOR, "button.Y9J4BArcarEAX9.js-close-window.dialog-close-button.nHJWKNB8DHe00C")
        elem_but.click()

    def add_to_archive_card(self):
        elem = self.__driver.find_element(By.CSS_SELECTOR, "div.NauH5zhD2hZvpP.R6tO1m6fTtV8_6.DVtxDmkCMy5qRd a.button-link.js-archive-card")
        elem.click()

    def delete_card(self):
        elem = self.__driver.find_element(By.CSS_SELECTOR, "div.NauH5zhD2hZvpP.R6tO1m6fTtV8_6.DVtxDmkCMy5qRd a.button-link.js-delete-card.negate")
        elem.click()
        # WebDriverWait(self.__driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.pop-over is-shown")))
        elem2 = self.__driver.find_element(By.CSS_SELECTOR, "div.pop-over.is-shown input.js-confirm.full.nch-button--danger")
        elem2.click()
# 6654ccb4785ba13674028bfb
    def move_card_to_another_list(self):
        draggable = self.__driver.find_element(By.CSS_SELECTOR, "div[data-card-id='6655e728e29f88096f781f4d'] > div.amUfYqLTZOvGsn > a")
        droppable = self.__driver.find_element(By.CSS_SELECTOR, "li[data-list-id='6654ccb4785ba13674028bfd'] ol.RD2CmKQFZKidd6")
        ActionChains(self.__driver)\
        .drag_and_drop(draggable, droppable)\
        .perform()

    def click_text_area_by_id(self, id_list):
        element =self.__driver.find_element(By.CSS_SELECTOR, f'li[data-list-id="{id_list}"] button[data-testid="list-add-card-button"]')
        element.click()

# div.NauH5zhD2hZvpP.R6tO1m6fTtV8_6.DVtxDmkCMy5qRd textarea[data-testid="card-back-title-input"]
# button.Y9J4BArcarEAX9.js-close-window.dialog-close-button.nHJWKNB8DHe00C
    
    # ol#board >li[data-list-id="6654cccadb15713775b136cf"] > div[data-testid="list"] >div[data-testid="list-header"]
    # find_lists("6654de22886e975b680f2d60")
    # ol#board >li[data-list-id="6654de22886e975b680f2d60"] > div[data-testid="list"] >div[data-testid="list-header"] textarea[data-testid="list-name-textarea"]



    # li[data-list-id=""]

    # def click_name_list(self):
    #     webelem = self.__driver.find_element(By.CSS_SELECTOR, "button.O9vivwyDxMqo3q.bxgKMAm3lq5BpA.iUcMblFAuq9LKn.PnEv2xIWy3eSui.SEj5vUdI3VvxDc")
    #     time.sleep(3)
    #     webelem.click()
    #     time.sleep(3)
    # li[data-list-id="6654cccadb15713775b136cf"]  div.mKJWg6W_CLHoiO > textarea

    # li[data-list-id="6654cccadb15713775b136cf"]  div[data-testid="list-footer"] > button[data-testid="list-add-card-button"]

# li[data-list-id="6654c15a347e3e8cdc310eb9"] button[data-testid="list-add-card-button"]
# li[data-list-id="6654c15a347e3e8cdc310eb9"] form textarea[data-testid="list-card-composer-textarea"]
# li[data-list-id="6654c15a347e3e8cdc310eb9"] form button[data-testid="list-card-composer-add-card-button"]
# li[data-list-id="6654c86b4739a4ab195e7cf6"] button[data-testid="list-add-card-button"]
# li[data-list-id="6654c86b4739a4ab195e7cf6"] button[data-testid="list-add-card-button"]

       
