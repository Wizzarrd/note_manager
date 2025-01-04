username = input('Имя пользователя: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = input('Дата создания в формате ДД-ММ-ГГГГ: ')
issue_date = input('Дата истечения в формате ДД-ММ-ГГГГ: ')
title1 = input('Первый заголовок: ')
title2 = input('Второй заголовок: ')
title3 = input('Третий заголовок: ')
titles = [title1, title2, title3]
note = [username, content, status, created_date, issue_date, titles]
print(note)