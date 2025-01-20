from datetime import datetime, timedelta

# Функция ввода и проверки даты:
def check_date():
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
# Основная функция:
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
    issue_date = check_date()
    note = {'username' : username,
    'title' : title,
    'content' : content,
    'status' : status,
    'created_date' : created_date,
    'issue_date' : issue_date}
    notes.append(note)
    return notes

notes_list = []
create_note(notes_list)
print(notes_list)