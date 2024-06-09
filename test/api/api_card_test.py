import allure

from page.BoardApi import BoardApi
from page.CardApi import CardApi
from page.ListApi import ListApi
from testdata.DataProvider import DataProvider

@allure.epic("API")
@allure.feature("Карточки")
@allure.story("Создать карточку")
@allure.severity("allure.severity_level.BLOCKED")
@allure.tag("Positive")
def test_create_card(api_board: BoardApi, api_list: ListApi, api_card: CardApi,test_data: DataProvider):
    name_board = test_data.generate_board_name()
    
    resp_board = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    id_board = resp_board.get("id")

    name_list = test_data.generate_new_list_name()
    resp_list = api_list.create_new_list(name_list, id_board, test_data.get_auth_creds())
    id_list = resp_list.get("id")

    name_card = test_data.generate_card_name()
    resp_card = api_card.create_card(id_list, test_data.get_card_creds(id_list, name_card), test_data.get_json_header())

    card_list = api_card.get_cards_of_list(id_list, test_data.get_auth_creds(), test_data.get_json_header())
    find_card_true = api_card.find_card_by_name_in_list(card_list, name_card)

    with allure.step("Проверить, что созданная карточка есть в списке"):
        assert find_card_true is True
    
    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())

@allure.epic("API")
@allure.feature("Карточки")
@allure.story("Изменить карточку")
@allure.title("Изменить имя карточки")
@allure.severity("allure.severity_level.NORMAL")
@allure.tag("Positive")
def test_change_name_card(api_board: BoardApi, api_list: ListApi, api_card: CardApi,test_data: DataProvider):
    name_board = test_data.generate_board_name()
    resp_board = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    id_board = resp_board.get("id")

    name_list = test_data.generate_new_list_name()
    resp_list = api_list.create_new_list(name_list, id_board, test_data.get_auth_creds())
    id_list = resp_list.get("id")

    name_card = test_data.generate_card_name()
    resp_card = api_card.create_card(id_list, test_data.get_card_creds(id_list, name_card), test_data.get_json_header())


    name_card_2 = test_data.generate_new_list_name()

    api_card.change_name_card(name_card_2, resp_card.get("id"), test_data.get_auth_creds(), test_data.get_json_header())

    card_list = api_card.get_cards_of_list(id_list, test_data.get_auth_creds(), test_data.get_json_header())
    find_card_true = api_card.find_card_by_name_in_list(card_list, name_card_2)
    find_card_false = api_card.find_card_by_name_in_list(card_list, name_card)

    with allure.step("Проверить, что у карточки новое имя"):
        assert find_card_true is True

    with allure.step("Проверить, что карточки cо старым именем нет в списке"):
        assert find_card_false is False

    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())

@allure.epic("API")
@allure.feature("Карточки")
@allure.story("Переместить карточку")
@allure.title("Переместить карточку в другой список")
@allure.severity("allure.severity_level.NORMAL")
@allure.tag("Positive")
def test_move_card_another_list(api_board: BoardApi, api_list: ListApi, api_card: CardApi,test_data: DataProvider):
    name_board = test_data.generate_board_name()
    resp_board = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    id_board = resp_board.get("id")

    name_list = test_data.generate_new_list_name()
    resp_list = api_list.create_new_list(name_list, id_board, test_data.get_auth_creds())
    id_list = resp_list.get("id")

    name_list_2 = test_data.generate_new_list_name()
    resp_list_2 = api_list.create_new_list(name_list_2, id_board, test_data.get_auth_creds())
    id_list_2 = resp_list_2.get("id")

    name_card = test_data.generate_card_name()
    resp_card = api_card.create_card(id_list, test_data.get_card_creds(id_list, name_card), test_data.get_json_header())
    id_card = resp_card.get("id")

    api_card.move_card_another_list(id_card, id_list_2, test_data.get_auth_creds(), test_data.get_json_header())
    card_list_2 = api_card.get_cards_of_list(id_list_2, test_data.get_auth_creds(), test_data.get_json_header())
    card_list = api_card.get_cards_of_list(id_list, test_data.get_auth_creds(), test_data.get_json_header())
    
    find_card_true = api_card.find_card_by_name_in_list(card_list_2, name_card)
    find_card_false = api_card.find_card_by_name_in_list(card_list, name_card)

    with allure.step("Проверить, что в новом списке есть перенесенная карточка"):
        assert find_card_true is True

    with allure.step("Проверить, что в первоначальном списке нет перенесенной карточки"):
        assert find_card_false is False

    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())
    
@allure.epic("API")
@allure.feature("Карточки")
@allure.story("Удалить карточку")
@allure.severity("allure.severity_level.NORMAL")
@allure.tag("Positive")
def test_delete_card(api_board: BoardApi, api_list: ListApi, api_card: CardApi,test_data: DataProvider):
    name_board = test_data.generate_board_name()
    resp_board = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    id_board = resp_board.get("id")

    name_list = test_data.generate_new_list_name()
    resp_list = api_list.create_new_list(name_list, id_board, test_data.get_auth_creds())
    id_list = resp_list.get("id")

    name_card = test_data.generate_card_name()
    resp_card = api_card.create_card(id_list, test_data.get_card_creds(id_list, name_card), test_data.get_json_header())
    id_card = resp_card.get("id")

    api_card.delete_card(id_card, test_data.get_auth_creds())

    card_list = api_card.get_cards_of_list(id_list, test_data.get_auth_creds(), test_data.get_json_header())
    find_card_false = api_card.find_card_by_name_in_list(card_list, name_card)

    with allure.step("Проверить, что карточки нет в списке"):
        assert find_card_false is False

    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())





