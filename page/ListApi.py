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

    @allure.step("api.Получить id списка по имени {name_list}")
    def get_list_id_by_name(self, list_lists: dict, name_list: str):
        id_list = ''
        for i in range(len(list_lists)):
            if(list_lists[i].get("name") == name_list):
                id_list = list_lists[i].get("id")
        return id_list
