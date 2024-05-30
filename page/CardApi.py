import requests 
import allure

class CardApi:
#     #  --url 'https://api.trello.com/1/cards?idList=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken' \
#   # --header 'Accept: application/json

    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key

    
    # https://api.trello.com/1/cards?idList=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken
    @allure.step("api.Создать новую карточку")
    def create_card(self, id_list: str, card_creds: dict, json_header: dict):
        card_creds["idList"]= id_list
        path = "{trello}/cards".format(trello = self.base_url)
        resp = requests.post(path, params=card_creds, headers=json_header)
        return resp.json()
    
    # --url 'https://api.trello.com/1/lists/{id}/cards?key=APIKey&token=APIToken' \
    # --header 'Accept: application/json'
    @allure.step("api.получить список карточек листа {id_list}")
    def get_cards_of_list(self, id_list: str, auth_creds: dict, json_header:dict) -> list[dict]:
        path = "{trello}/lists/{id_list}/cards".format(trello = self.base_url, id_list=id_list)
        resp = requests.get(path, params=auth_creds, headers=json_header)
        return resp.json()
        
    #url = "https://api.trello.com/1/cards/{id}"
    @allure.step("api.Изменить карточку id - {id_card}, name - {name}")
    def update_card(self, name:str, id_card: str, auth_creds: dict, json_header: dict) -> list[dict]:
        path = "{trello}/cards/{id}".format(trello = self.base_url, id = id_card)
        auth_creds["name"] = name
        resp = requests.put(path, params=auth_creds, headers=json_header)
        return resp.json()
    

    @allure.step("api.Проверить есть ли картчка с таким именем - {name} - существует в списке")
    def find_card_by_name_in_list(self, card_list: list, name: str) -> bool:
            new_name_list = []
            for i in range(len(card_list)):
                 name = card_list[i].get("name")
                 new_name_list.append(name)
            name_find = False
            for elem in new_name_list:
                if(elem == name):
                    name_find = True
                else: name_find = False
            return name_find
    
    def find_id_card_by_name_in_list(self, card_list: list, name: str) -> str:
        id_card = ''
        for elem in card_list:
            if elem.get("name") == name:
                id_card = elem.get("id")
        return id_card
    
    @allure.step("Найти карточку по id  - {id_card}")
    def find_card_by_id_in_list(self, card_list: list, id_card: str) -> bool:
            new_id_list = []
            id_find = False
            if len(card_list) > 0:
                for i in range(len(card_list)):
                    id = card_list[i].get("id")
                    new_id_list.append(id)
                for elem in new_id_list:
                    if(elem == id_card):
                        id_find = True
                    else: id_find = False
            else: id_find = False
            return id_find


