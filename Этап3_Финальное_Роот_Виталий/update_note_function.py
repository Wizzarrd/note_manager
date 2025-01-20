from datetime import datetime, timedelta

# Ввод и проверка формата даты:
def update_date(init_date):
    while True:
        date_str = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')
        # Возврат изначальной даты, если поле ввода пустое
        if not date_str:
            print('Дедлайн не поменялся')
            return init_date
        else:
            try:
                date = datetime.strptime(date_str, '%d-%m-%Y').date()
            except:
                print('Вы ввели дату неверно! Используйте предложенный формат. Пример: 10-12-2024')
            else:
                break
    while True:
        save_changes = input('Вы уверены, что хотите обновить issue_date? (да/нет): ')
        if save_changes.lower() == 'да':
            return date
        elif save_changes.lower() == 'нет':
            return init_date
        else:
            print('Некорректный ввод. Введите "да" или "нет".')
            continue

# Ввод статуса заметки:
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
            status = status_list.get(status_input)
            break
        # Проверка на соответствие значениям
        elif status_input in status_list.values():
            status = status_input
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
            return status
        elif save_changes.lower() == 'нет':
            return init_status
        else:
            print('Некорректный ввод. Введите "да" или "нет".')
            continue

# Функция изменения заметки:
def update_note(note):
    print('''Выберите, какое поле вы хотите изменить:
username
title
content
status
issue_date''')
    while True:
        update_field = input('Ваш выбор: ')
        # Проверка на корректность ввода:
        if update_field in note.keys() and update_field != 'created_date':
            # Изменение даты:
            if update_field == 'issue_date':
                note.update({update_field : update_date(note.get('issue_date'))})
            # Изменение статуса:
            elif update_field == 'status':
                note.update({update_field : update_status(note.get('status'))})
            # Изменение других полей:
            else:
                new_value = input('Введите новые данные: ')
                if new_value:
                    # Сохранение изменения:
                    while True:
                        save_changes = input(f'Вы уверены, что хотите обновить {update_field}? (да/нет): ')
                        if save_changes.lower() == 'да':
                            note.update({update_field: new_value})
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
                    return note
                else:
                    print('Некорректный ввод. Ответьте "да" или "нет".')
        else:
            print('Вы ввели некорректное имя поля, повторите ввод, используя предложенные имена полей.')
            continue


issue_date = timedelta(7) + datetime.today()
note = {'username' : 'username',
        'title' : 'title',
        'content' : 'content',
        'status' : 'status',
        'created_date' : datetime.today().date(),
        'issue_date' : issue_date.date()}
print(note)
update_note(note)
print(note)