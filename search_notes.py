from datetime import datetime

# Функция вывода заметки:
def display_notes(notes):
    # Проверяем на наличие заметок:
    if notes:
        print('Список заметок:')
        page = 1
        note_num = 1
        print('Страница 1')
        # Выводим заметки:
        for i in notes:
            print(f'''____________________________________________________________________
Заметка #{note_num}
Имя пользователя: {i.get('username')}
Заголовок: {i.get('title')}
Описание: {i.get('content')}
Статус: {i.get('status')}
Дата создания: {i.get('created_date').strftime('%d-%m-%Y')}
Дедлайн: {i.get('issue_date').strftime('%d-%m-%Y')}
____________________________________________________________________''')
            if note_num % 5 == 0:
                # На странице вмещается 5 заметок. Если их больше, спрашиваем, выводить ли остальные.
                while True:
                    continue_message = input('Желаете вывести следующие заметки? (да/нет): ')
                    if continue_message.lower() == 'да':
                        page += 1
                        print(f'Страница {page}')
                        break
                    elif continue_message.lower() == 'нет':
                        return
                    else:
                        print('Некорректный ввод, повторите попытку.')
                        continue
            note_num += 1
    else:
        print('У вас нет сохранённых заметок.')

# Функция поиска заметок:
def search_notes(notes, keyword = None, status = None):
    found_notes = []
    if not notes:
        print('Список заметок пустой')
        return
    # Поиск по ключевому слову и статусу:
    if keyword and status:
        for i in notes:
            if (keyword.lower() in i.get('title').lower() or keyword.lower() in i.get('content').lower() or
            keyword.lower() in i.get('username').lower()) and status.lower() in i.get('status').lower():
                found_notes.append(i)
    # Поиск по ключевому слову:
    elif keyword:
        for i in notes:
            if (keyword.lower() in i.get('title').lower() or keyword.lower() in i.get('content').lower() or
            keyword.lower() in i.get('username').lower()):
                found_notes.append(i)
    # Поиск по статусу:
    elif status:
        for i in notes:
            if status.lower() in i.get('status').lower():
                found_notes.append(i)
    # 3 строчки, которые скорее всего никогда не задействуются, но на всякий случай пусть будут.
    # Оказалось, задействуются.
    else:
        print('Критерий не указан')
        return
    return found_notes

# Заранее подготовленный список заметок:
#notes = []
#notes = [{'username': 'Алекс', 'title': 'Прогулка', 'content': 'Сходить погулять', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()}]
notes = [{'username': 'Пользователь', 'title': 'Заголовок', 'content': 'Описание', 'status' : 'В процессе', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status' : 'В процессе', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Спорт', 'content': 'Сходить в зал', 'status' : 'Выполнено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Выполнено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()}]
print(notes)
if notes:
    # Запрос критерия:
    while True:
        found_notes = []
        search_what = input('''По какому критерию искать заметки?
1. Ключевые слова
2. Статус
3. Ключевые слова и статус
: ''')
        # Поиск по ключевым словам:
        if search_what == '1' or search_what.lower() == 'ключевые слова':
            keyword = input('Введите ключевое слово: ')
            found_notes = search_notes(notes, keyword=keyword)
            break
        # Поиск по статусу:
        elif search_what == '2' or search_what.lower() == 'статус':
            status = input('Введите статус заметки: ')
            found_notes = search_notes(notes, status=status)
            break
        # Поиск по ключевым словам и статусу:
        elif search_what == '3' or search_what.lower() == 'ключевые слова и статус':
            keyword = input('Введите ключевое слово: ')
            status = input('Введите статус: ')
            found_notes = search_notes(notes, keyword=keyword, status=status)
            break
        # Некорректный ввод:
        else:
            print('Ввод непонятен, повторите попытку.')
            continue
    if found_notes:
        display_notes(found_notes)
    else:
        print('Указанный ключ или статус не подходит ни одной заметке.')
else:
    print('Заметок нет, искать нечего.')