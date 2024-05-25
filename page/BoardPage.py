import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class BoardPage:

    # https://trello.com/b/KjaoiGyt/rte
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get("ui", "base_url")
    
    @allure.step("ui.Перейти на страницу доски")
    def open_board_page(self, name_board,short_link):
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



    # div.content-all-boards > div > div >div.boards-page-board-section.mod-no-sidebar >div > ul.boards-page-board-section-list > li > a >div > div[title="against"] 
    



        
