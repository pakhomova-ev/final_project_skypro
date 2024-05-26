import requests 
import allure
import webdriver_manager

from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class CardApi:
    #  --url 'https://api.trello.com/1/cards?idList=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken' \
  # --header 'Accept: application/json

    def __init__(self, base_url: str, token: str, key: str) -> None:
        self.base_url = base_url
        self.token = token
        self.key = key


    @allure.step("api.Создать новую карточку")
    def create_card(self, card_creds: dict):
        path = "{trello}/cards/".format(trello = self.base_url)
        resp = requests.get(path, params=card_creds)
        return resp.json()


