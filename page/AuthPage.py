import allure 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider

class AuthPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.url = ConfigProvider().get("ui", "base_url")
        self.__url = self.url + "/login"
        

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        """
        Метод открывает страницу авторизации пользователя Trello
        """
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email} : {password}")
    def login_as(self, email: str, password: str) -> None:
        """
        Метод проходит по шагам для авторизации зарегистрированного пользователя
        """
        self.__driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.css-o6ruxu svg[role=presentation]")))

        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    def get_current_url(self) -> str:
        """
        Метод возвращает адрес стекущей страницы
        """
        return self.__driver.current_url
    
    def auth_user(self, email: str, password: str):
        self.go()
        self.login_as(email, password)