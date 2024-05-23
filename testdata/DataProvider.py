import configparser
import json
from faker import Faker

my_file = open("test_data.json")
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
    
    def get_create_creds(self) -> dict:
        create_creds = {}
        create_creds["key"] = self.data.get("key")
        create_creds["token"] = self.data.get("token")
        create_creds["name"] = self.generate_board_name()
        return create_creds
    
    def generate_board_name(self):
        fake = Faker()
        board_name = fake.file_name(extension='')
        return board_name