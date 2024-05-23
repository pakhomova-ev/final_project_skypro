import requests 
import allure

class BoardApi:
    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key

    @allure.step("api.Получить список досок организации - {org_id}")
    def get_all_boards_by_org_id(self, org_id:str, auth_creds: dict) -> list[dict]:
        """
        Метод возвращает информацию о досках организации
        """
        path = "{trello}/organizations/{id}/boards".format(trello = self.base_url, id = org_id)
        resp = requests.get(path, params=auth_creds)

        return resp.json()
    
    @allure.step("api.Создать новую доску")
    def create_board(self, auth_creds: dict) -> dict:
        """
        Метод создает новую доску
        """

        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, params=auth_creds)

        return resp.json()
    
    @allure.step("api.Удалить доску с id - {id}")
    def delete_board_by_id(self, id: str, auth_creds: dict) -> dict:
        """
        Метод удаляет доску по id
        """
        path = "{trello}/boards/{board_id}".format(trello = self.base_url, board_id = id)
        resp = requests.delete(path, params=auth_creds)

        return resp.json()
    
    @allure.step("Найти доску по id")
    def find_board_by_id_in_list(self, id_list: list, id_board: str) -> bool:
            new_id_list = []
            for elem in id_list:
                id = elem.get("id")
                new_id_list.append(id)
            id_find = False
            for elem in new_id_list:
                if(elem == id_board):
                    id_find = True
                else: id_find = False
            return id_find
    
