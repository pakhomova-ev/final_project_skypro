import requests 
import allure

class ListApi:

    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key

    #curl --request POST \
    #--url 'https://api.trello.com/1/lists?name={name}&idBoard=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken'
    @allure.step("api.Создать новый список на доске id - {id_board}")
    def create_new_list(self, name: str, id_board: str, auth_creds: dict):
        path = "{trello}/lists".format(trello = self.base_url)
        auth_creds["name"]= name
        auth_creds["idBoard"]= id_board
        resp = requests.post(path, params=auth_creds)
        return resp.json()
    
    @allure.step("Найти список по id - {id_list}")
    def find_list_by_id_in_list(self, lists_list: list, id_list: str) -> bool:
            new_id_list = []
            for i in range(len(lists_list)):
                id = lists_list[i].get("id")
                new_id_list.append(id)
            id_find = False
            for elem in new_id_list:
                if(elem == id_list):
                    id_find = True
            return id_find

   
