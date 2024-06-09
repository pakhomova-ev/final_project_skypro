
class BasePage:
   
    def get_current_url(self) -> str:
        """
        Метод возвращает адрес стекущей страницы
        """
        return self.__driver.current_url