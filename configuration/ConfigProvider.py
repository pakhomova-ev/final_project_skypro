import configparser

config = configparser.ConfigParser()
config.read('test_config.ini')

class ConfigProvider:

    def __init__(self) -> None:
        self.config = config
        
    def get(self, section: str, prop: str):
        return self.config[section].get(prop)

    def get_int(self, section: str, prop: str):
        return self.config[section].getint(prop)
    
    def get_ui_url(self):
        return self.config["ui"].get("base_url")
    
