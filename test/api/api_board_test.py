import allure
from page.BoardApi import BoardApi
from testdata.DataProvider import DataProvider

@allure.epic("API")
@allure.feature("Доски")
@allure.story("Получить доску")
@allure.severity("allure.severity_level.NORMAL")
@allure.tag("Positive")
def test_get_boards(api_board: BoardApi, test_data: DataProvider):
    name_board = test_data.generate_board_name()
    resp = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    board_list = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    with allure.step("Проверить, что возвращается не пустой список"):
        assert len(board_list) !=0

    api_board.delete_board_by_id(id_new_board, test_data.get_auth_creds())

@allure.epic("API")
@allure.feature("Доски")
@allure.story("Создать доску")
@allure.severity("allure.severity_level.BLOCKED")
@allure.tag("Positive")
def test_create_board(api_board: BoardApi, test_data: DataProvider):
    with allure.step("Получить кол-во досок до создания новой доски"):
        board_list_before = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    name_board = test_data.generate_board_name()
    new_board_creds = test_data.get_create_creds_with_name(name_board)
    name_new_board_creds = new_board_creds.get("name")

    resp = api_board.create_board(new_board_creds)
    name_new_board = resp.get("name")
    id_new_board = resp.get("id")

    with allure.step("Получить кол-во досок после создания новой доски"):
        board_list_after = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_after) - len(board_list_before) == 1

    with allure.step('Проверить, что имя новой доски верное'):
        assert name_new_board_creds == name_new_board
  
    api_board.delete_board_by_id(id_new_board, test_data.get_auth_creds())

@allure.epic("API")
@allure.story("Удалить доску")
@allure.severity("allure.severity_level.CRITICAL")
@allure.feature("Доски")
@allure.tag("Positive")
def test_delete_board_by_id(api_board: BoardApi, test_data: DataProvider):
    name_board = test_data.generate_board_name()
    new_board_creds = test_data.get_create_creds_with_name(name_board)
    resp = api_board.create_board(new_board_creds)

    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    with allure.step("Проверяем, что в списке досок есть созданная доска"):
        id_find_ex = api_board.find_board_by_name_in_list(board_list_before, name_board)
        assert id_find_ex is True
    
    api_board.delete_board_by_id(id_new_board, test_data.get_auth_creds())

    with allure.step("Получить кол-во досок после удаления доски"):
        board_list_after = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    with allure.step("Проверить, что досок стало на 1 меньше"):
        assert len(board_list_before) - len(board_list_after) == 1

    id_find_after = api_board.find_board_by_name_in_list(board_list_after, name_board)
    with allure.step("Проверяем, что в списке нет удаленной доски"):
        assert id_find_after is False

@allure.epic("API")
@allure.feature("Доски")
@allure.story("Удалить доску")
@allure.severity("allure.severity_level.NORMAL")
def test_deleted_all_boards(api_board: BoardApi, test_data: dict):
    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    id_list = []
    for elem in board_list_before:
        id = elem.get("id")
        id_list.append(id)

    for elem in id_list:
        api_board.delete_board_by_id(elem, test_data.get_auth_creds())
 