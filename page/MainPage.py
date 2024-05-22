import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider

class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get("ui", "base_url")
        self.__url = self.url + "/u/elena_pakho/boards"

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