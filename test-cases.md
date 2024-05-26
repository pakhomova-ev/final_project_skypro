### Доска
- Создать доску
 - Создать по шаблону
 - Со списками
- Изменить доску
 - имя
 - описание
 - кол-во список

- Удалить доску


### Список
- Получить списки на доске:
 - Запрос GET, id board
 - --url 'https://api.trello.com/1/boards/{id}/lists?key=APIKey&token=APIToken' \
  --header 'Accept: application/json'
- Получить список по id
 - Запрос GET, id list
 -  --url 'https://api.trello.com/1/lists/{id}?key=APIKey&token=APIToken'
- []Создать список
 - Запрос POST, name_list, idBoard 
 - --url 'https://api.trello.com/1/lists?name={name}&idBoard=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken'


### Карточка
- [] Добавление карточки на доску
 - Запрос POST, idList
 -  --url 'https://api.trello.com/1/cards?idList=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken' \
  --header 'Accept: application/json'
- [] Изменение карточки
 - Запрос PUT, id card
 -  --url 'https://api.trello.com/1/cards/{id}?key=APIKey&token=APIToken' \
  --header 'Accept: application/json'
- [] Удаление карточки
 - Запрос DEL, id card
 -  --url 'https://api.trello.com/1/cards/{id}?key=APIKey&token=APIToken'
- [] Перемещение карточки в другую колонку
 - Запрос actions