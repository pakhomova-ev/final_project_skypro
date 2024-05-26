import allure
from page.BoardApi import BoardApi
from testdata.DataProvider import DataProvider

@allure.story("Создать карточку")
def test_create_new_card(api_client: BoardApi, test_data: DataProvider):
    new_board_creds = test_data.get_create_creds()
    resp = api_client.create_board(new_board_creds)
    id_new_board = resp.get("id")
    list_board_lists = api_client.get_list_boards_lists(id_new_board, test_data.get_auth_creds(), test_data.get_json_headers())
    api_client.create_card(test_data.get_card_creds(list_board_lists))
    y = 67
