# Создаём список заметок.
notes = [{'username' : 'Пользователь', 'title' : 'Заголовок', 'content' : 'Описание'},
         {'username' : 'Мария', 'title' : 'Список покупок', 'content' : 'Купить продукты на неделю'},
         {'username' : 'Мария', 'title' : 'Спорт', 'content' : 'Сходить в зал'},
         {'username' : 'Мария', 'title' : 'Конный', 'content' : 'Спорт'},
         {'username' : 'Мария', 'title' : 'Конный', 'content' : 'Спорт'}]
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