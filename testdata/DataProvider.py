import configparser
import json
from faker import Faker

my_file = open("testdata/test_data.json")
data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = data
        
    def get(self, prop: str) -> str:
        return self.data.get(prop)
    
    def getint(self, prop: str) -> int:
        val = self.data.get(prop)
        return int(val)
    
    
    def get_token(self)-> str:
        return self.data.get("token")
    
    def get_key(self)-> str:
        return self.data.get("key")
    
    def get_auth_creds(self) -> dict:
        auth_creds = {}
        auth_creds["key"] = self.data.get("key")
        auth_creds["token"] = self.data.get("token")
        auth_creds["filter"] = self.data.get("filter")
        return auth_creds
    
    def get_create_creds_with_name(self, name_board) -> dict:
        create_creds = {}
        create_creds["key"] = self.get_key()
        create_creds["token"] = self.get_token()
        create_creds["name"] = name_board
        return create_creds
    
    def get_card_creds(self, id_list: str, name_card) -> dict:
        card_creds = {}
        card_creds["idList"] = id_list
        card_creds["key"] = self.get_key()
        card_creds["token"] = self.get_token()
        card_creds["name"] = name_card
        return card_creds
    
    def generate_board_name(self):
        fake = Faker()
        board_name = fake.file_name(extension='')
        return board_name
    
    def generate_card_name(self):
        fake = Faker()
        card_name = fake.color_name()
        return card_name

    def get_json_header(self) -> dict:
        return {"Accept": "application/json"} 
    
    def generate_new_card_name(self):
        fake = Faker()
        new_card_name = f'{fake.color_name()} {fake.pystr(max_chars = 3)}'
        return new_card_name
    
    def generate_new_list_name(self):
        fake = Faker()
        new_list_name = f'{fake.color_name()} {str(fake.pyint(max_value = 5673))}'
        return new_list_name
    
    def generate_board_name_max_char(self):
        fake=Faker()
        big_board_name = fake.pystr(max_chars=16384)
        return big_board_name
        