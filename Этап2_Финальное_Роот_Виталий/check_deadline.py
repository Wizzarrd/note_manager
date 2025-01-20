import datetime

# Вывод текущей даты.
current_date = datetime.date.today()
print('Текущая дата: ', current_date.strftime("%d-%m-%Y"))
# Запрос даты дедлайна и её анализ.
while True:
    issue_date_str = input('Введите дату дедлайна в формате ДД-ММ-ГГГГ: ')
    try:
        issue_date = datetime.datetime.strptime(issue_date_str, '%d-%m-%Y').date()
    except:
        print('Вы ввели дату неверно! Используйте предложенный формат. Пример: 10-12-2024')
    else:
        break
# Сравниваем даты.
if current_date < issue_date:
    print(f'До дедлайна осталось {(issue_date - current_date).days} дней.')
elif current_date == issue_date:
    print('Дедлайн сегодня! Поторопитесь!')
else:
    print(f'Дедлайн истёк {(current_date - issue_date).days} дней назад.')