import allure

from page.AuthPage import AuthPage
from page.MainPage import MainPage


def auth_test(browser,test_data: dict):
    email = test_data.get("email")
    password = test_data.get("password")
    username = test_data.get("username")
    
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    #Открываем иконку с пользователем в правом верхнему углу:
    main_page.open_menu()
    #Открываем информацию о пользователе:
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()
    with allure.step("Проверить, что URL " +current_url+ " заканчивается на username/boards"):
        assert main_page.get_current_url().endswith("elena_pakho/boards")
    with allure.step("Проверить, что указаны данные пользователя"):
            with allure.step("Имя пользователя должно быть " + username):
                assert info[0] == username
            with allure.step("Почта пользователя должна быть" + email):
                assert info[1] == email
