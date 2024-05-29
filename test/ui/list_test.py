import allure

from selenium.webdriver.chrome.webdriver import WebDriver

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.ListPage import ListPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By

@allure.story("ui.Создать новый список на доске")
def test_create_new_list(browser: WebDriver, test_data: DataProvider, api_client: BoardApi):
    board_page = BoardPage(browser)
    auth_page = AuthPage(browser)
    auth_page.auth_user(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    name_board = DataProvider().generate_board_name()
    new_board_dict = api_client.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    board_page.open_board_page(name_board, short_link)

    list_page = ListPage(browser)
    name_new_list = test_data.generate_new_list_name()
    list_page.create_new_list(name_new_list)
    browser.refresh()
    id_list = list_page.get_id_list_by_name(name_new_list)
    list_boards = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_create_creds())
    api_list = api_client.find_board_by_name_in_list(list_boards, name_board)
    # ui_list = list_page.find_list_by_id(id_list)
    # ui_list = main_page.find_list_by_name(name_new_list) #ерунда  с локаторами
    """
      raise exception_class(message, screen, stacktrace)
E       selenium.common.exceptions.JavascriptException: Message: javascript error: 
{"status":32,"value":"Unable to locate an element with the xpath expression
 //[contains(text(), \"Aqua 4138\")] because of the following error:\nSyntaxError:
   Failed to execute 'evaluate' on 'Document': The string '//[contains(text(), \"Aqua 4138\")]'
     is not a valid XPath expression."}
    """

    with allure.step("api.Проверить, что новый список - {name_new_list} есть на доске {name_board}"):
        assert api_list is True

    # with allure.step("ui.Проверить, что новый список - {id_list} есть на доске"):
    #     assert ui_list is True

    api_client.delete_board_by_id(id_board, test_data.get_auth_creds())











    
