import allure
from page.BoardApi import BoardApi

token = "ATTAd5d9fb30a7c07d6de132838cc2b22b4d3334bc231422d3307ca11546238d3a2754E132E3"
key = "2ebc416bdd1c40e66bc7834e124c424b"
api_url = "https://api.trello.com/1"
org_id = "664cf65097e9b86e8bc07c20"
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
def test_get_boards():
    api = BoardApi(api_url, token, key)

    resp = api.create_board(create_dict)
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    board_list = api.get_all_boards_by_org_id(org_id, auth_dict)
    with allure.step("Проверить, что возвращается не пустой список"):
        assert len(board_list) !=0

@allure.story("Создать доску")
def test_create_board():
    api = BoardApi(api_url, token,key)
    with allure.step("Получить кол-во досок до создания новой доски"):
        board_list_before = api.get_all_boards_by_org_id(org_id, auth_dict)

    resp = api.create_board(create_dict)
    with allure.step("Получить кол-во досок после создания новой доски"):
        board_list_after = api.get_all_boards_by_org_id(org_id, auth_dict)
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_after) - len(board_list_before) == 1

@allure.story("Удалить доску")
def test_delete_board_by_id():
    api = BoardApi(api_url, token, key)
        
    resp = api.create_board(create_dict)
    with allure.step("Получить id созданной доски"):
        id_new_board = resp.get("id")

    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api.get_all_boards_by_org_id(org_id, auth_dict)

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
        
    api.delete_board_by_id(id_new_board, auth_dict)

    with allure.step("Получить кол-во досок после удаления доски"):
        board_list_after = api.get_all_boards_by_org_id(org_id, auth_dict)
    with allure.step("Проверить, что досок стало на 1 больше"):
        assert len(board_list_before) - len(board_list_after) == 1

@allure.story("Удалить все доски")
def test_deleted_all_boards():
    api = BoardApi(api_url, token, key)
    with allure.step("Получить кол-во досок до удаления доски"):
        board_list_before = api.get_all_boards_by_org_id(org_id, auth_dict)

    id_list = []
    for elem in board_list_before:
        id = elem.get("id")
        id_list.append(id)

    for elem in id_list:
        api.delete_board_by_id(elem, auth_dict)


