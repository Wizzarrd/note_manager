#Объявление списка
titles = []
#Ввод первого заголовка
titles.append(input("Введите заголовок (или оставьте пустым для завершения): "))
#Цикл ввода заголовков
for title in titles:
    #Если пользователь оставит поле ввода пустым, то ввод заголовков закончится и пустой заголовок удалится
    if title == '':
        titles.remove(title)
        break
    titles.append(input("Введите заголовок (или оставьте пустым для завершения): "))
#Вывод заголовков в удобном для чтения формате
print('Заголовки заметки:')
for i in titles:
    print('-', i)

'''
Очень неудобно было выполнять это задание, т.к. я не нашел у себя в записях и в лекциях ни одного 
упоминания циклов и информации о том, как с ними работать, поэтому пришлось искать информацию о них на форумах
'''