from datetime import datetime, timedelta

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
    # 3 строчки, которые скорее всего никогда не задействуются, но на всякий случай пусть будут:
    # Оказалось, задействуются.
    else:
        print('Критерий не указан')
        return
    return found_notes

# Функция с вводом критериев для поиска заметок:
def search_notes_input(notes_to_search_in):
    if notes_to_search_in:
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
                found_notes = search_notes(notes_to_search_in, keyword=keyword)
                break
            # Поиск по статусу:
            elif search_what == '2' or search_what.lower() == 'статус':
                status = input('Введите статус(Выполнено, В процессе, Отложено): ')
                found_notes = search_notes(notes_to_search_in, status=status)
                break
            # Поиск по ключевым словам и статусу:
            elif search_what == '3' or search_what.lower() == 'ключевые слова и статус':
                keyword = input('Введите ключевое слово: ')
                status = input('Введите статус (Выполнено, В процессе, Отложено): ')
                found_notes = search_notes(notes_to_search_in, keyword=keyword, status=status)
                break
            # Некорректный ввод:
            else:
                print('Ввод непонятен, повторите попытку.')
                continue
        if found_notes:
            display_notes(found_notes)
        else:
            print('Указанный ключ или статус не подходит ни одной заметке.')
            return
    else:
        print('Заметок нет.')
        return
# Функция удаления заметок:

# Функция удаления заметки:
def delete_note(notes_init):
    # Выводим заметки.
    print('Список текущих заметок: ')
    for i in notes_init:
        print(f'''
            Имя пользователя: {i.get('username')}
            Заголовок: {i.get('title')}
            Описание: {i.get('content')}''')
    notes_to_delete = []
    new_notes = notes_init.copy()
    # Запрашиваем критерий удаления заметок.
    # Если заметки по данному критерию находится, добавляем их в список заметок на удаление.
    delete_criteria = input('Введите имя пользователя или заголовок для удаления заметки: ')
    for i in notes_init:
        if delete_criteria.lower() in i.get('username').lower() or delete_criteria.lower() in i.get('title').lower():
            notes_to_delete.append(i)
    print('Список заметок на удаление:')
    for i in notes_to_delete:
        print(f'''
                                Имя пользователя: {i.get('username')}
                                Заголовок: {i.get('title')}
                                Описание: {i.get('content')}''')
    # Удаляем заметки или говорим, что заметки по критерию не были найдены.
    if not notes_to_delete:
        print('Заметок с таким именем пользователя или заголовком не найдено.')
    elif input('Вы уверены, что хотите удалить заметки? (да/нет): ') == 'да':
        for i in notes_init:
            if i in notes_to_delete:
                new_notes.remove(i)
        notes_init = new_notes
        if not notes:
            print('Список заметок пуст')
            return notes_init
        else:
            print('Заметки успешно удалены. Остались следующие заметки:')
            for i in notes_init:
                print(f'''
                            Имя пользователя: {i.get('username')}
                            Заголовок: {i.get('title')}
                            Описание: {i.get('content')}''')
            return notes_init
    else:
        print('Текущий список заметок не изменился.')

# Функция изменения даты:
def update_date(init_date):
    while True:
        date_str = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')
        # Возврат изначальной даты, если поле ввода пустое
        if not date_str:
            print('Дедлайн не поменялся')
            return init_date
        else:
            try:
                date_to_update = datetime.strptime(date_str, '%d-%m-%Y').date()
            except:
                print('Вы ввели дату неверно! Используйте предложенный формат. Пример: 10-12-2024')
            else:
                break
    while True:
        save_changes = input('Вы уверены, что хотите обновить issue_date? (да/нет): ')
        if save_changes.lower() == 'да':
            return date_to_update
        elif save_changes.lower() == 'нет':
            return init_date
        else:
            print('Некорректный ввод. Введите "да" или "нет".')
            continue

# Функция изменения статуса заметки:
def update_status(init_status):
    status_list = {'1': 'Выполнено', '2': 'В процессе', '3': 'Отложено'}
    print('''Выберите статус заметки:
              1. Выполнено
              2. В процессе
              3. Отложено''')
    status_input = input('Ваш выбор: ')
    # Поиск соответствующих значений статуса по ключам и значениям
    # из словаря и проверка ввода на корректность
    while True:
        # Проверка на соответствие ключам
        if status_list.get(status_input) is not None:
            status_to_update = status_list.get(status_input)
            break
        # Проверка на соответствие значениям
        elif status_input in status_list.values():
            status_to_update = status_input
            break
        elif not status_input:
            print('Статус не изменился')
            return init_status
        else:
            status_input = input('''Некорректный ввод.
    Статус заметки может быть: "Выполнено", "В процессе", "Отложено".
    Введите один из предложенных вариантов: ''')
    while True:
        save_changes = input('Вы уверены, что хотите обновить status? (да/нет): ')
        if save_changes.lower() == 'да':
            return status_to_update
        elif save_changes.lower() == 'нет':
            return init_status
        else:
            print('Некорректный ввод. Введите "да" или "нет".')
            continue

# Функция изменения заметки:
def update_note(note_to_update):
    print('''Выберите, какое поле вы хотите изменить:
username
title
content
status
issue_date''')
    while True:
        update_field = input('Ваш выбор: ')
        # Проверка на корректность ввода:
        if update_field in note_to_update.keys() and update_field != 'created_date':
            # Изменение даты:
            if update_field == 'issue_date':
                note_to_update.update({update_field : update_date(note_to_update.get('issue_date'))})
            # Изменение статуса:
            elif update_field == 'status':
                note_to_update.update({update_field : update_status(note_to_update.get('status'))})
            # Изменение других полей:
            else:
                new_value = input('Введите новые данные: ')
                if new_value:
                    # Сохранение изменения:
                    while True:
                        save_changes = input(f'Вы уверены, что хотите обновить {update_field}? (да/нет): ')
                        if save_changes.lower() == 'да':
                            note_to_update.update({update_field: new_value})
                            break
                        elif save_changes.lower() == 'нет':
                            break
                        else:
                            print('Некорректный ввод. Введите "да" или "нет".')
                            continue
                else:
                    print('Данные не изменились')
            # Обновление нескольких функций за раз:
            while True:
                another_update = input('Желаете изменить что-то ещё? (да/нет): ')
                if another_update.lower() == 'да':
                    break
                elif another_update.lower() == 'нет':
                    return note_to_update
                else:
                    print('Некорректный ввод. Ответьте "да" или "нет".')
        else:
            print('Вы ввели некорректное имя поля, повторите ввод, используя предложенные имена полей.')
            continue

# Функция вывода заметок
def display_notes(notes_to_display=None):
    # Проверяем на наличие заметок:
    if notes_to_display:
        print('Список заметок:')
        page = 1
        note_num = 1
        # Выводим заметки:
        for i in notes_to_display:
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
                        break
                    elif continue_message.lower() == 'нет':
                        return
                    else:
                        print('Некорректный ввод, повторите попытку.')
                        continue
            note_num += 1
    else:
        print('У вас нет сохранённых заметок.')

# Функция ввода и проверки даты:
def set_date():
    while True:
        date_str = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')
        if date_str == '':
            date = (timedelta(7) + datetime.today()).date()
            return date
        else:
            try:
                date = datetime.strptime(date_str, '%d-%m-%Y').date()
            except:
                print('Вы ввели дату неверно! Используйте предложенный формат. Пример: 10-12-2024')
            else:
                return date

# Функция создания заметки:
def create_note():
    username = input('Имя пользователя: ')
    if username == '':
        username = 'Пользователь'
    title = input('Заголовок заметки: ')
    if title == '':
        title = 'Без названия'
    content = input('Описание заметки: ')
    if content == '':
        content = 'Без описания'
    # Даём пользователю выбрать статус заметки.
    status_list = {'1': 'Выполнено', '2': 'В процессе', '3': 'Отложено'}
    print('''Выберите статус заметки:
          1. Выполнено
          2. В процессе
          3. Отложено''')
    status_input = input('Ваш выбор: ')
    # Поиск соответствующих значений статуса по ключам и значениям
    # из словаря и проверка ввода на корректность
    while True:
        # Проверка на соответствие ключам
        if status_list.get(status_input) is not None:
            status = status_list.get(status_input)
            break
        # Проверка на соответствие значениям
        elif status_input in status_list.values():
            status = status_input
            break
        else:
            status_input = input('''Некорректный ввод.
Статус заметки может быть: "Выполнено", "В процессе", "Отложено".
Введите один из предложенных вариантов: ''')
    print('Статус заметки: ', status)
    created_date = datetime.today().date()
    issue_date = set_date()
    new_note = {'username' : username,
    'title' : title,
    'content' : content,
    'status' : status,
    'created_date' : created_date,
    'issue_date' : issue_date}
    return new_note

# Меню:
def menu(notes=None):
    if notes is None:
        notes = []
    # Заранее заготовленные заметки:
    if __name__ == '__main__':
        notes = [{'username': 'Пользователь', 'title': 'Заголовок', 'content': 'Описание', 'status': 'В процессе',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
                  'status': 'В процессе', 'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Спорт', 'content': 'Сходить в зал', 'status': 'Выполнено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status': 'Выполнено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status': 'Отложено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status': 'Отложено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status': 'Отложено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status': 'Отложено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status': 'Отложено',
                  'created_date': datetime.today(), 'issue_date': datetime.today()}]
    while True:
        menu_num = input('''Добро пожаловать в менеджер заметок!
Введите нужное действие:
1. Создать новую заметку
2. Показать все заметки
3. Обновить заметку
4. Удалить заметку
5. Найти заметки
6. Выйти из программы
Ваш выбор: ''')
        if menu_num.lower() == ('1' or 'создать новую заметку' or 'создать'):
            notes.append(create_note())
        elif menu_num.lower() == ('2' or 'показать все заметки' or 'показать'):
            display_notes(notes)
        elif menu_num.lower() == ('3' or 'обновить заметку' or 'обновить'):
            while True:
                try:
                    note_count = int(input('Заметку с каким номером вы хотите обновить?\nВаш выбор: '))
                except ValueError:
                    print('Некорректный ввод. Введите число.')
                    continue
                else:
                    if len(notes) >= note_count > 0:
                        for i in notes:
                            if (notes.index(i) + 1) == note_count:
                                update_note(i)
                                print(f'''____________________________________________________________________
Обновлённая Заметка #{note_count}
Имя пользователя: {i.get('username')}
Заголовок: {i.get('title')}
Описание: {i.get('content')}
Статус: {i.get('status')}
Дата создания: {i.get('created_date').strftime('%d-%m-%Y')}
Дедлайн: {i.get('issue_date').strftime('%d-%m-%Y')}
____________________________________________________________________''')
                                break
                        break
                    else:
                        print('Заметки с таким номером нет.')
                        break
        elif menu_num.lower() == ('4' or 'удалить заметки' or 'удалить'):
            notes = delete_note(notes)
        elif menu_num.lower() == ('5' or 'найти заметки' or 'найти'):
            search_notes_input(notes)
        elif menu_num.lower() == ('6' or 'выйти из программы' or 'выйти'):
            break
        else:
            print('Некорректный ввод, повторите попытку.')
            continue
    print('Программа завершилась.')
    return notes

menu()
