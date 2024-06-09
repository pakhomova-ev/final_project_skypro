import allure 
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

from configuration.ConfigProvider import ConfigProvider
from page.BasePage import BasePage

username_input = ("css selector", "#username")
password_input = ("css selector", "#password")
submit_btn = ("css selector", "#login-submit")
see_pass_btn = ("css selector", "button.css-o6ruxu svg[role=presentation]")

class AuthPage(BasePage):
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
        self.__driver.find_element(*username_input).send_keys(email)
        self.__driver.find_element(*submit_btn).click()

        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((see_pass_btn)))

        self.__driver.find_element(*password_input).send_keys(password)
        self.__driver.find_element(*submit_btn).click()
    
    def auth_user(self, email: str, password: str):
        self.go()
        self.login_as(email, password)