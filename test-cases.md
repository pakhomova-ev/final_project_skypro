### Allure
python -m pytest --alluredir allure/results
- copy folder history into allure/results from allure/final
- delete allure/final
allure generate allure/results -o allure/final
- deleted allure/results
allure open allure/final

### LP
- создание новой доски
  -[x] api
  -[x]ui
- удаление существующей доски
  -[x] api
  -[x]ui
- добавление карточки на доску
  -[x] api
  -[x]ui
- редактирование карточки
  -[x] api
  -[x]ui
- удаление карточки
  -[x] api
  -[]ui
- перемещение карточки в другую колонку
  -[x] api
  -[x]ui

### Список
- Получить списки на доске:
 -[x] Запрос GET, id board
 - --url 'https://api.trello.com/1/boards/{id}/lists?key=APIKey&token=APIToken' \
  --header 'Accept: application/json'
- Получить список по id
 - Запрос GET, id list
 -  --url 'https://api.trello.com/1/lists/{id}?key=APIKey&token=APIToken'
- []Создать список
 - Запрос POST, name_list, idBoard 
 - --url 'https://api.trello.com/1/lists?name={name}&idBoard=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken'


### Карточка
- [x] Добавление карточки на доску
 - Запрос POST, idList
 -  --url 'https://api.trello.com/1/cards?idList=5abbe4b7ddc1b351ef961414&key=APIKey&token=APIToken' \
  --header 'Accept: application/json'
- [x] Изменение карточки
 - Запрос PUT, id card
 -  --url 'https://api.trello.com/1/cards/{id}?key=APIKey&token=APIToken' \
  --header 'Accept: application/json'
- [x] Удаление карточки
 - Запрос DEL, id card
 -  --url 'https://api.trello.com/1/cards/{id}?key=APIKey&token=APIToken'
- [] Перемещение карточки в другую колонку
 -[] Запрос actions ui
 -[x] Запрос PUT, id card, new_id_list
  - 



  <ul class="123">
  <li class="board">
  <a class="board-tile" href="/b/heyer/fear">
  <div>fear</div>
  </a>
  </li>
  </ul>  

  <div class="1">
  <div class="2">
  <div class="3">
  <h2 class="u">fear</h2>
  </div>
  </div>
  </div> 
# ol#board >li[data-list-id="6654cccadb15713775b136cf"] > div[data-testid="list"] >div[data-testid="list-header"] textarea[data-testid="list-name-textarea"]
  <ol id="board">
  <li data-list-id="id_list1">
  <div data-testid="list">
  <div data-testid="list-header">
  <textarea data-testid="list-name-textarea"></textarea>
  </div>
  </div>
  </li>
  <li data-list-id="id_list2">
  <div data-testid="list">
  <div data-testid="list-header">
  <textarea data-testid="list-name-textarea">Gnom 567</textarea>
  </div>
  </div>
  </li>
  <li data-list-id="id_list3">
  <div data-testid="list">
  <div data-testid="list-header">
  <textarea data-testid="list-name-textarea">Mutf</textarea>
  </div>
  </div>
  </li>
  </ol>

  
         
 
@allure.step("Проверить есть ли доска")
def test_find_name(api_board: BoardApi, test_data: DataProvider):
    new_board_creds = test_data.get_create_creds()
    name_board = new_board_creds.get("name")
    resp = api_board.create_board(new_board_creds)
    id_new_board = resp.get("id")
    list_boards = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    
    name_find_after = api_board.find_board_by_name_in_list(list_boards, name_board)
    with allure.step("Проверяем, что в списке есть созданная доска"):
        assert name_find_after is True

    api_board.delete_board_by_id(id_new_board, test_data.get_auth_creds())
    
@allure.step("Получить списки доски")
def test_get_list_board_list(api_board: BoardApi, test_data: DataProvider):
    new_board_creds = test_data.get_create_creds()
    resp = api_board.create_board(new_board_creds)
    id_new_board = resp.get("id")

    list_lists = api_board.get_list_boards_lists(id_new_board, test_data.get_auth_creds(), test_data.get_json_header())
    with allure.step("api.Проверить, что лист To Do есть в списке"):
        assert list_lists[0]["name"] == "To Do"
    with allure.step("api.Проверить, что лист Doing есть в списке"):
        assert list_lists[1]["name"] == "Doing"
    with allure.step("api.Проверить, что лист Done есть в списке"):
        assert list_lists[2]["name"] == "Done"

    api_board.delete_board_by_id(id_new_board, test_data.get_auth_creds())


