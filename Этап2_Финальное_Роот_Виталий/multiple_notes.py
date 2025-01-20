from datetime import datetime

#Функция ввода имени пользователя
def username_input():
    username = input('Введите имя пользователя: ')
    if username == '':
        return 'Пользователь'
    else:
        return username

# Функция ввода заголовка.
def title_input():
    title = input('Введите заголовок заметки: ')
    if title == '':
        return 'Без названия'
    else:
        return title

def content_input():
    content = input('Введите описание заметки: ')
    if content == '':
        return 'Без описания'
    else:
        return content
# Функция ввода статуса.
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


# Функция создания заметки.
def create_note():
    username = username_input()
    title = title_input()
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

# Основной код.
notes = []
print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
first_note = create_note()
notes.append(first_note)
# Запрос на создание новой заметки.
while True:
    input_check = input('Хотите добавить ещё одну заметку? (да/нет): ')
    if input_check.lower() == 'да':
        notes.append(create_note())
        continue
    elif input_check.lower() == 'нет':
        break
    else:
        print('Я вас не понял, повторите ввод. (да/нет)')
# Вывод всех заметок:
note_index = 1 # Для отображения номера заметки, чтобы было проще ориентироваться.
for i in notes:
    print(f'''
    {note_index}.Имя пользователя: {i.get('username')}
    Заголовок: {i.get('title')}
    Описание: {i.get('content')}
    Статус: {i.get('status')}
    Дата создания: {i.get('created_date').strftime('%d-%m-%Y')}
    Дедлайн: {i.get('issue_date').strftime('%d-%m-%Y')} 
''')
    note_index = note_index + 1