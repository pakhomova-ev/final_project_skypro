import allure

from page.BoardApi import BoardApi

from page.ListApi import ListApi
from testdata.DataProvider import DataProvider

@allure.epic("API")
@allure.feature("Списки")
@allure.story("Создать список")
@allure.severity("allure.severity_level.NORMAL")
@allure.tag("Positive")
def test_create_list(api_board: BoardApi, api_list: ListApi, test_data: DataProvider):
    name_board = test_data.generate_board_name()
    resp_board = api_board.create_board(name_board, test_data.get_auth_creds())
    id_board = resp_board.get("id")

    name_list = test_data.generate_new_list_name()
    resp_list = api_list.create_new_list(name_list, id_board, test_data.get_auth_creds())
    id_list = resp_list.get("id")

    lists_list = api_board.get_list_boards_lists(id_board,test_data.get_auth_creds(), test_data.get_json_header())
    find_list_true = api_list.find_list_by_id_in_list(lists_list, id_list)

    with allure.step("Проверить, что создался список с заданным именем"):
        assert find_list_true is True

