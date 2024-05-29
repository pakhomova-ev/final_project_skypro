import allure

from selenium.webdriver.chrome.webdriver import WebDriver

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.CardPage import CardPage
from page.ListPage import ListPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By

@allure.story("ui.Создать новую карточку в листе")
def test_create_card(browser: WebDriver, test_data: DataProvider, api_client: BoardApi):
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    board_page = BoardPage(browser)
    card_page = CardPage(browser)

    auth_page.auth_user(test_data.get("email"), test_data.get("password"))

    name_board = DataProvider().generate_board_name()
    new_board_dict = api_client.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    board_page.open_board_page(name_board, short_link)
    name_new_list = test_data.generate_new_list_name()
    list = api_client.create_new_list(name_new_list, id_board, test_data.get_auth_creds())
    id_list = list.get("id")

    name_card = test_data.generate_card_name()
    card_page.create_new_card(id_list, name_card)

    cards_list = api_client.get_cards_of_list(test_data.get_auth_creds(), test_data.get_json_header(),id_list)
    y=8
    




