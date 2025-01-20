# Создаём словарь со значениями статуса заметок и объявляем текущий статус.
status_list = {'1' : 'Выполнено', '2' : 'В процессе', '3' : 'Отложено'}
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