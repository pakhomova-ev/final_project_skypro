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
            for i in range(len(id_list)):
                id = id_list[i].get("id")
                new_id_list.append(id)
            id_find = False
            for elem in new_id_list:
                if(elem == id_board):
                    id_find = True
                else: id_find = False
            return id_find
    
    
    @allure.step("Проверить есть ли доска с таким именем - {name}")
    def find_board_by_name_in_list(self, boards_list: list, name: str) -> bool:
            new_name_list = []
            for i in range(len(boards_list)):
                 name = boards_list[i].get("name")
                 new_name_list.append(name)
            name_find = False
            for elem in new_name_list:
                if(elem == name):
                    name_find = True
                else: name_find = False
            return name_find
    
    @allure.step("Проверить есть ли доска с таким именем - {name}")
    def find_board_by_name_in_list(self, boards_list: list, name: str) -> bool:
            new_name_list = []
            for i in range(len(boards_list)):
                 name = boards_list[i].get("name")
                 new_name_list.append(name)
            name_find = False
            for elem in new_name_list:
                if(elem == name):
                    name_find = True
                else: name_find = False
            return name_find
    
    @allure.step("api.Удалить все доски организации")
    def delete_all_board_of_org(self, org_id: int, auth_creds: dict)-> None:
        with allure.step("Получить кол-во досок до удаления доски"):
            board_list_before = self.get_all_boards_by_org_id(org_id, auth_creds)

        id_list = []
        for elem in board_list_before:
            id = elem.get("id")
            id_list.append(id)

        for elem in id_list:
            self.delete_board_by_id(elem, auth_creds)

# https://api.trello.com/1/boards/{id}/lists
    @allure.step("api.Получить списки доски по id - {id_board} доски")
    def get_list_boards_lists(self, id_board: int, auth_creds: dict, json_headers: dict) -> list[dict]:
        path = "{trello}/boards/{id}/lists".format(trello = self.base_url, id = id_board)

        resp = requests.get(path, params=auth_creds, headers=json_headers)

        return resp.json()


         
    

    
