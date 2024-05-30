import allure

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider


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
    with allure.step("Проверить, что URL " +current_url+ " заканчивается на username/boards"):
        assert main_page.get_current_url().endswith("elena_pakho/boards")
    with allure.step("Проверить, что указаны данные пользователя"):
            with allure.step("Имя пользователя должно быть " + username):
                assert info[0] == username
            with allure.step("Почта пользователя должна быть " + email):
                assert info[1] == email

def find_board_test(browser,test_data: DataProvider, api_board: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    new_board = api_board.create_board(DataProvider().get_create_creds())
    name_board = new_board.get("name")

    board_list = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    

    name_find = api_board.find_board_by_name_in_list(board_list, name_board)
    assert name_find is True

    
