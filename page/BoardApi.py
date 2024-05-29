import re
import requests 
import allure


class BoardApi:
    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key

    @allure.step("api.Получить список досок организации - {org_id}")
    def get_all_boards_by_org_id(self, org_id:str, create_creds: dict) -> list[dict]:
        """
        Метод возвращает информацию о досках организации
        """
        path = "{trello}/organizations/{id}/boards".format(trello = self.base_url, id = org_id)
        resp = requests.get(path, params=create_creds)

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
    
    @allure.step("Найти сущность по id - {id}")
    def find_x_by_id_in_list(self, id_list: list, id: str) -> bool:
            new_id_list = []
            for i in range(len(id_list)):
                id = id_list[i].get("id")
                new_id_list.append(id)
            id_find = False
            for elem in new_id_list:
                if(elem == id):
                    id_find = True
                else: id_find = False
            return id_find

    @allure.step("Найти доску по id - {id_board}")
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
    
    @allure.step("Найти карточку по id  - {id_card}")
    def find_card_by_id_in_list(self, id_list: list, id_card: str) -> bool:
            new_id_list = []
            for i in range(len(id_list)):
                id = id_list[i].get("id")
                new_id_list.append(id)
            id_find = False
            for elem in new_id_list:
                if(elem == id_card):
                    id_find = True
                else: id_find = False
            return id_find
    
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
# https://api.trello.com/1/boards/66546e2e6200b92a307f34bf/lists?key={{key}}&token={{token}}&filter=open
  # curl --request GET \
  # --url 'https://api.trello.com/1/boards/{id}/lists?key=APIKey&token=APIToken' \
  # --header 'Accept: application/json'
    @allure.step("api.Получить списки доски по id - {id_board} доски")
    def get_list_boards_lists(self, id_board: str, auth_creds: dict, json_header: dict) -> list[dict]:
        path = "{trello}/boards/{id}/lists".format(trello = self.base_url, id = id_board)

        resp = requests.get(path, params=auth_creds, headers=json_header)
        return resp.json()

    #curl --request POST \
    #--url 'https://api.trello.com/1/lists?name={name}&idBoard=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken'
    @allure.step("api.Создать новый список на доске id - {id_board}")
    def create_new_list(self, name: str, id_board: str, auth_creds: dict):
        path = "{trello}/lists".format(trello = self.base_url)
        auth_creds["name"]= name
        auth_creds["idBoard"]= id_board
        resp = requests.post(path, params=auth_creds)

        return resp.json()
    # https://api.trello.com/1/cards?idList=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken
    @allure.step("api.Создать новую карточку")
    def create_card(self, card_creds: dict, json_header: dict):
        path = "{trello}/cards/".format(trello = self.base_url)
        resp = requests.post(path, params=card_creds, headers=json_header)
        return resp.json()

    # https://api.trello.com/1/lists/{id}/cards
    @allure.step("api.Получить список карточек списка id - {id_list}")
    def get_cards_of_list(self, auth_creds: dict, json_header: dict, id_list: str) -> list[dict]:
         path = "{trello}/lists/{id}/cards".format(trello = self.base_url, id = id_list)
         resp = requests.get(path, params=auth_creds, headers=json_header)
         return resp.json()
    

    #url = "https://api.trello.com/1/cards/{id}"
    @allure.step("api.Изменить карточку id - {id_card}, name - {name}")
    def update_card(self, auth_creds: dict, json_header: dict,name:str, id_card: str) -> list[dict]:
        path = "{trello}/cards/{id}".format(trello = self.base_url, id = id_card)
        auth_creds["name"] = name 
        resp = requests.put(path, params=auth_creds, headers=json_header)
        return resp.json()
          
    # https://api.trello.com/1/cards/{id}?key=APIKey&token=APIToken
    @allure.step("api.Удалить карточку")
    def delete_card_by_id(self, auth_creds: dict, id_card)-> None:
        path = "{trello}/cards/{id}".format(trello = self.base_url, id = id_card)
        requests.delete(path, params=auth_creds)

    
    #url = "https://api.trello.com/1/cards/{id}"
    # хочу один метод для изменения карточки с выбором свойст для изменения - это повтор
    @allure.step("api.Изменить карточку id - {id_card}, id нового списка - {new_id_list}")
    def update_list_of_card(self, auth_creds: dict, json_header: dict, new_id_list: str, id_card: str) -> list[dict]:
        path = "{trello}/cards/{id}".format(trello = self.base_url, id = id_card)
        auth_creds["idList"] = new_id_list 
        resp = requests.put(path, params=auth_creds, headers=json_header)
        return resp.json()

    def get_short_link(self, url):
        match = re.search(r"/b/([a-zA-Z0-9]+)", url)
        short_link = match.group(1)
        return short_link
    
    def get_list_id_by_name(self, list_lists: dict, name_list: str):
        id_list = ''
        for i in range(len(list_lists)):
            if(list_lists[i].get("name") == name_list):
                id_list = list_lists[i].get("id")
        return id_list
    
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
        
         
         
         

    
