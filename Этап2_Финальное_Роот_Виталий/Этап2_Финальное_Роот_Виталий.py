from datetime import datetime

# Функция удаления заметок
def delete_note(notes):
    # Выводим заметки.
    print('Список текущих заметок: ')
    for i in notes:
        print(f'''
            Имя пользователя: {i.get('username')}
            Заголовок: {i.get('title')}
            Описание: {i.get('content')}''')
    notes_to_delete = []
    new_notes = notes.copy()
    # Запрашиваем критерий удаления заметок.
    # Если заметки по данному критерию находится, добавляем их в список заметок на удаление.
    delete_criteria = input('Введите имя пользователя или заголовок для удаления заметки: ')
    for i in notes:
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
        for i in notes:
            if i in notes_to_delete:
                new_notes.remove(i)
        notes = new_notes
        if not notes:
            print('Список заметок пуст')
        else:
            print('Заметки успешно удалены. Остались следующие заметки:')
            for i in notes:
                print(f'''
                            Имя пользователя: {i.get('username')}
                            Заголовок: {i.get('title')}
                            Описание: {i.get('content')}''')
    else:
        print('Текущий список заметок не изменился.')
    return notes

# Функция ввода заголовков.
def add_titles_loop():
    # Запрос на ввод заголовков
    titles = []
    titles.append(input("Введите заголовок (или оставьте пустым для завершения): "))
    # Удаление стопового значения из списка заголовков
    for title in titles:
        if title == '':
            titles.remove(title)
            break
        titles.append(input("Введите заголовок (или оставьте пустым для завершения): "))
    # Вывод заголовков
    print('Заголовки заметки:')
    for i in titles:
        print('-', i)
    return titles

# Функция обновления статуса заметки.
# В будущем нужно будет добавить аргументы для функции, чтобы менять существующие статусы.
def update_status():
    status_list = {'1': 'Выполнено', '2': 'В процессе', '3': 'Отложено'}
    current_status = status_list.get('2')
    print('Текущий статус заметки: ', current_status)
    # Даём пользователю выбрать новый статус заметки.
    print('Ввыберите новый статус заметки:\n'
          '1. Выполнено\n'
          '2. В процессе\n'
          '3. Отложено')
    current_status_input = input('Ваш выбор: ')
    # Поиск соответствующих значений статуса по ключам и значениям
    # из словаря и проверка ввода на корректность
    while True:
        # Проверка на соответствие ключам
        if status_list.get(current_status_input) is not None:
            current_status = status_list.get(current_status_input)
            break
        # Проверка на соответствие значениям
        elif current_status_input in status_list.values():
            current_status = current_status_input
            break
        else:
            current_status_input = input('Некорректный ввод. \n'
                                         'Статус заметки может быть: "Выполнено", "В процессе", "Отложено".\n'
                                         'Введите один из предложенных вариантов: ')
    print('Статус заметки успешно изменён на: ', current_status)
    return current_status

# Функция обработки дедлайнов.
# В будущем нужно будет добавить аргументы для функции, чтобы проверять дедлайн для существующих заметок
def check_deadline():
    current_date = datetime.today().date()
    print('Текущая дата: ', current_date.strftime("%d-%m-%Y"))
    # Ввод даты дедлайна и проверка на корректность ввода
    while True:
        issue_date_str = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')
        try:
            issue_date = datetime.strptime(issue_date_str, '%d-%m-%Y').date()
        except:
            print('Вы ввели дату неверно! Используйте предложенный формат. Пример: 10-12-2024')
        else:
            break
    # Сравнение текущей даты с датой дедлайна
    if current_date < issue_date:
        print(f'До дедлайна осталось {(issue_date - current_date).days} дней.')
    elif current_date == issue_date:
        print('Дедлайн сегодня! Поторопитесь!')
    else:
        print(f'Дедлайн истёк {(current_date - issue_date).days} дней назад.')

# Функция ввода имени пользователя.
def username_input():
    username = input('Введите имя пользователя: ')
    if username == '':
        return 'Пользователь'
    else:
        return username

# Функция ввода описания заметки.
def content_input():
    content = input('Введите описание заметки: ')
    if content == '':
        return 'Без описания'
    else:
        return content

# Функция ввода статуса заметки.
def status_input():
    status_list = {'1': 'Выполнено', '2': 'В процессе', '3': 'Отложено'}
    print('Ввыберите статус заметки:\n'
          '1. Выполнено\n'
          '2. В процессе\n'
          '3. Отложено')
    current_status_input = input('Ваш выбор: ')
    while True:
        if status_list.get(current_status_input) is not None:
            current_status = status_list.get(current_status_input)
            break
        elif current_status_input in status_list.values():
            current_status = current_status_input
            break
        elif current_status_input == '':
            current_status = 'В процессе'
            break
        else:
            current_status_input = input('''Некорректный ввод.
                                         Статус заметки может быть: "Выполнено", "В процессе", "Отложено".
                                         Введите один из предложенных вариантов: ''')
    return current_status

# Функция ввода даты дедлайна.
def deadline_input():
    while True:
        issue_date_str = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')
        try:
            issue_date = datetime.strptime(issue_date_str, '%d-%m-%Y').date()
        except ValueError:
            print('Вы ввели дату неверно! Используйте предложенный формат. Пример: 10-12-2024')
        else:
            return issue_date

# Функция ввода данных заметки.
def note_input():
    username = username_input()
    title = add_titles_loop()
    content = content_input()
    status = status_input()
    created_date = datetime.today().date()
    issue_date = deadline_input()
    note = {'username' : username,
    'title' : title,
    'content' : content,
    'status' : status,
    'created_date' : created_date,
    'issue_date' : issue_date}
    return note

# Функция создания заметки.
def create_note(notes):
    # Создание новой заметки.
    notes.append(note_input())
    # Запрос на создание еще одной заметки.
    while True:
        input_check = input('Хотите добавить ещё одну заметку? (да/нет): ')
        if input_check.lower() == 'да':
            notes.append(note_input())
            continue
        elif input_check.lower() == 'нет':
            break
        else:
            print('Я вас не понял, повторите ввод. (да/нет)')
        return notes

# Функция вывода заметок.
def show_notes(notes):
    # Вывод всех заметок:
    note_index = 1  # Для отображения номера заметки, чтобы было проще ориентироваться.
    for i in notes:
        print(f'''
            {note_index}.Имя пользователя: {i.get('username')}
              Заголовок: {i.get('title')}
              Описание: {i.get('content')}
              Статус: {i.get('status')}
              Дата создания: {i.get('created_date').strftime('%d-%m-%Y')}
              Дедлайн: {i.get('issue_date').strftime('%d-%m-%Y')} ''')
        note_index = note_index + 1

# Основной код.
def main():
    notes = []
    while True:
        print('Добро пожаловать в "Менеджер заметок"! Вы желаете добавить новую заметку? (да/нет)')
        create_note_input_check = input()
        if create_note_input_check.lower() == 'да':
            notes = create_note(notes)
            break
        elif create_note_input_check.lower() == 'нет':
            break
        else:
            print('Я вас не понял, повторите ввод. (да/нет)')
    # Тестирование.
    # Часть функций пока не обращается к заметкам, а просто работает как есть.
    if input('Использовать заранее составленные заметки? (да, если да): ').lower() == 'да':
        # Создаём список заметок.
        notes = [{'username': 'Пользователь', 'title': 'Заголовок', 'content': 'Описание', 'status' : 'В процессе', 'created_date' : datetime(2025, 1, 19), 'issue_date' : datetime(2025, 1, 19)},
                 {'username': 'Мария', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status' : 'В процессе', 'created_date' : datetime(2025, 1, 19), 'issue_date' : datetime(2025, 1, 19)},
                 {'username': 'Мария', 'title': 'Спорт', 'content': 'Сходить в зал', 'status' : 'Выполнено', 'created_date' : datetime(2025, 1, 19), 'issue_date' : datetime(2025, 1, 19)},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Выполнено', 'created_date' : datetime(2025, 1, 19), 'issue_date' : datetime(2025, 1, 19)},
                 {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime(2025, 1, 19), 'issue_date' : datetime(2025, 1, 19)}]
    while True:
        action_list = {'1' : 'Создать заметку', '2' : 'Посмотреть заметки', '3' : 'Удалить заметку',
                       '4' : 'Обновить статус заметки.', '5' : 'Проверить дедлайн.',
                       '6' : 'Закончить тестирование'}
        print('''Выберите действие:
        1. Создать заметку.
        2. Посмотреть заметки.
        3. Удалить заметку.
        4. Обновить статус заметки.
        5. Проверить дедлайн.
        6. Закончить тестирование.''')
        action_check = input(': ')
        if action_check == '1':
            notes = create_note(notes)
        elif action_check == '2':
            show_notes(notes)
        elif action_check == '3':
            notes = delete_note(notes)
        elif action_check == '4':
            update_status()
        elif action_check == '5':
            check_deadline()
        elif action_check == '6':
            print('Остановка программы.')
            break
        else:
            print('Что-то пошло не так. Повторите.')
            continue

main()