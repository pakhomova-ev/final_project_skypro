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
  -[]ui
- редактирование карточки
  -[x] api
  -[]ui
- удаление карточки
  -[x] api
  -[]ui
- перемещение карточки в другую колонку
  -[x] api
  -[]ui

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
  <textarea data-testid="list-name-textarea"></textarea>
  </div>
  </div>
  </li>
  <li data-list-id="id_list3">
  <div data-testid="list">
  <div data-testid="list-header">
  <textarea data-testid="list-name-textarea"></textarea>
  </div>
  </div>
  </li>
  </ol>

  поиск на главной странице по доски по локатору ul.boards-page-board-section-list a[href*="simple"]