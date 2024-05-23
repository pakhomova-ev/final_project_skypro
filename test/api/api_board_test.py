import allure
from page.BoardApi import BoardApi

name = "test_api_5"

auth_dict = {
    "key": key,
    "token": token,
    "filter": "open"
}
create_dict = {
    "name": name,
    "key": key,
    "token": token
}

@allure.story("Получить список досок")
def test_get_boards(api_client: BoardApi, test_data: dict):

    resp = api_client.create_board(create_dict)
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    board_list = api_client.get_all_boards_by_org_id(test_data.get("org_id"), auth_dict)
    with allure.step("Проверить, что возвращается не пустой список"):
        assert len(board_list) !=0

@allure.story("Создать доску")
def test_create_board(api_client: BoardApi, test_data: dict):
    with allure.step("Получить кол-во досок до создания новой доски"):
        board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), auth_dict)

    resp = api_client.create_board(create_dict)
    with allure.step("Получить кол-во досок после создания новой доски"):
        board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"), auth_dict)
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_after) - len(board_list_before) == 1

@allure.story("Удалить доску")
def test_delete_board_by_id(api_client: BoardApi, test_data: dict):
  
    resp = api_client.create_board(create_dict)
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), auth_dict)

    id_list = []
    for elem in board_list_before:
        id = elem.get("id")
        id_list.append(id)
    id_list 
    id_find = False
    for elem in id_list:
        if(elem == id_new_board):
            id_find = True
        else: id_find = False
    with allure.step("Проверяем, что в списке досок есть созданная доска"):
        assert id_find is True
        
    api_client.delete_board_by_id(id_new_board, auth_dict)

    with allure.step("Получить кол-во досок после удаления доски"):
        board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"), auth_dict)
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_before) - len(board_list_after) == 1

@allure.story("Удалить все доски")
def test_deleted_all_boards(api_client: BoardApi, test_data: dic):
    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), auth_dict)

    id_list = []
    for elem in board_list_before:
        id = elem.get("id")
        id_list.append(id)

    for elem in id_list:
        api_client.delete_board_by_id(elem, auth_dict)


