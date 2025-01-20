from datetime import datetime

# Функция вывода заметок
def display_notes(notes):
    # Проверяем на наличие заметок:
    if notes:
        print('Список заметок:')
        page = 1
        note_num = 1
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
                        break
                    elif continue_message.lower() == 'нет':
                        return
                    else:
                        print('Некорректный ввод, повторите попытку.')
                        continue
            note_num += 1
    else:
        print('У вас нет сохранённых заметок.')

# Выбор между заметками:
#note_empty = []
#one_note = [{'username': 'Алекс', 'title': 'Прогулка', 'content': 'Сходить погулять', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()}]
notes = [{'username': 'Пользователь', 'title': 'Заголовок', 'content': 'Описание', 'status' : 'В процессе', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status' : 'В процессе', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Спорт', 'content': 'Сходить в зал', 'status' : 'Выполнено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Выполнено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()},
         {'username': 'Мария', 'title': 'Конный', 'content': 'Спорт', 'status' : 'Отложено', 'created_date' : datetime.today(), 'issue_date' : datetime.today()}]
try:
    display_notes(note_empty)
except:
    None
try:
    display_notes(one_note)
except:
    None
try:
    display_notes(notes)
except:
    None