import allure

from page.AuthPage import AuthPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider

@allure.epic("UI")
@allure.feature("Регистрация/Вход")
@allure.story("Залогиниться сайте")
@allure.severity("allure.severity_level.BLOCKED")
@allure.tag("Positive")
def auth_test(browser,test_data: DataProvider):
    email = test_data.get("email")
    password = test_data.get("password")
    username = test_data.get("username")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " + " заканчивается на username/boards"):
        assert current_url.endswith("elena_pakho/boards")
    with allure.step("Проверить, что указаны данные пользователя"):
            with allure.step("Имя пользователя должно быть " + username):
                assert info[0] == username
            with allure.step("Почта пользователя должна быть " + email):
                assert info[1] == email


    
