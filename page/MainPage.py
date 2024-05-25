import re
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.login = DataProvider().get("login")
        self.url = ConfigProvider().get("ui", "base_url")
        self.__url = self.url + f'/u/{self.login}/boards'

    @allure.step("ui.Перейти на главную страницу Trello")
    def open_main_page_trello(self):
        self.__driver.get(self.__url)

    @allure.step("ui.Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("ui.Открыть боковое меню")
    def open_menu(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR,
                                   "button[data-testid='header-member-menu-button']").click()

    @allure.step("ui.Прочитать информацию о пользователе")
    def get_account_info(self) -> list[str]:
        """
        Метод возвращает имя, эл.почта пользователя списком
        """

        container = self.__driver.find_element(By.CSS_SELECTOR,
                                       "div[data-testid=account-menu]>div>div>div.mJBO4dHZbrIG_0")
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        name = fields[0].text
        email = fields[1].text

        return [name, email]
    
    @allure.step("ui.Создать новую доску {name_board}")
    def create_new_board(self, name_board: str) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, "li[data-testid='create-board-tile']").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.rX4pAv5sWHFNjp")))

        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='create-board-title-input']").send_keys(name_board)
        button_active = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-testid='create-board-submit-button']")))
        button_active.click()
    
    #---------------------не работает, не находит элемент----------------------
    @pytest.mark.skip("не работает поиск элемента доска на странице")
    @allure.step("ui.Найти в списке досок доску по имени {name_board}")
    def find_by_name(self, name_board: str)-> bool:
        list_board = self.__driver.find_elements(By.CSS_SELECTOR, "div.content-all-boards > div > div >div.boards-page-board-section.mod-no-sidebar >div > ul.boards-page-board-section-list > li")
        print(list_board)
        name_new_board_find = False
        for i in range(len(list_board)):
            if(list_board[i].find_element(By.CSS_SELECTOR, "a >div > div[title='between']")):
                name_new_board_find is True
            else: name_new_board_find is False
        return name_new_board_find

    


