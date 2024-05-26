import allure
from page.BoardApi import BoardApi
from testdata.DataProvider import DataProvider


@allure.story("Получить список досок")
def test_get_boards(api_client: BoardApi, test_data: DataProvider):
    resp = api_client.create_board(test_data.get_create_creds())
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    board_list = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    with allure.step("Проверить, что возвращается не пустой список"):
        assert len(board_list) !=0

    api_client.delete_board_by_id(id_new_board, test_data.get_auth_creds())


@allure.story("Создать доску")
def test_create_board(api_client: BoardApi, test_data: DataProvider):
    with allure.step("Получить кол-во досок до создания новой доски"):
        board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    new_board_creds = test_data.get_create_creds()
    name_new_board_creds = new_board_creds.get("name")

    resp = api_client.create_board(new_board_creds)
    name_new_board = resp.get("name")
    id_new_board = resp.get("id")

    with allure.step("Получить кол-во досок после создания новой доски"):
        board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_after) - len(board_list_before) == 1

    with allure.step('Проверить, что имя новой доски верное'):
        assert name_new_board_creds == name_new_board
  
    api_client.delete_board_by_id(id_new_board, test_data.get_auth_creds())

@allure.story("Удалить доску")
def test_delete_board_by_id(api_client: BoardApi, test_data: DataProvider):
  
    new_board_creds = test_data.get_create_creds()
    resp = api_client.create_board(new_board_creds)
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    id_find = api_client.find_board_by_id_in_list(board_list_before, id_new_board)
    with allure.step("Проверяем, что в списке досок есть созданная доска"):
        assert id_find is True
        
    api_client.delete_board_by_id(id_new_board, test_data.get_auth_creds())

    with allure.step("Получить кол-во досок после удаления доски"):
        board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_before) - len(board_list_after) == 1

    id_find_after = api_client.find_board_by_id_in_list(board_list_after, id_new_board)
    with allure.step("Проверяем, что в списке нет удаленной доски"):
        assert id_find_after is False

def test_find_name(api_client: BoardApi, test_data: DataProvider):
    new_board_creds = test_data.get_create_creds()
    name_board = new_board_creds.get("name")
    resp = api_client.create_board(new_board_creds)
    list_boards = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    
    name_find_after = api_client.find_board_by_name_in_list(list_boards, name_board)
    with allure.step("Проверяем, что в списке есть созданная доска"):
        assert name_find_after is True
@allure.story("получить списки доски")
def test_get_list_board_list(api_client: BoardApi, test_data: DataProvider):
    new_board_creds = test_data.get_create_creds()
    resp = api_client.create_board(new_board_creds)
    id_board = resp.get("id")

    list_lists = api_client.get_list_boards_lists(id_board, test_data.get_auth_creds(), test_data.get_json_header())
    with allure.step("api.Проверить, что лист To Do есть в списке"):
        assert list_lists[0]["name"] == "To Do"
    with allure.step("api.Проверить, что лист Doing есть в списке"):
        assert list_lists[1]["name"] == "Doing"
    with allure.step("api.Проверить, что лист Done есть в списке"):
        assert list_lists[2]["name"] == "Done"






@allure.story("Удалить все доски")
def test_deleted_all_boards(api_client: BoardApi, test_data: dict):
    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    id_list = []
    for elem in board_list_before:
        id = elem.get("id")
        id_list.append(id)

    for elem in id_list:
        api_client.delete_board_by_id(elem, test_data.get_auth_creds())



