# Задача 2. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число и внесите исправление в файл.

path = 'seminar5/5.txt' # путь к файлу

with open(path, 'r') as numbers: # считываем данные из файла в переменную numbers
    numbers_list = list(map(int, numbers.read().split())) # преобразовываем данные в список интовых значений numbers_list из переменной numbers
print(f'Исходный список: {numbers_list}')

for i in range(1, len(numbers_list)): # пробегаемся по списку numbers_list
    if numbers_list[i] - numbers_list [i-1] > 1: # если разность элемента и предыдущего элемента > 1
        numbers_list.insert(i, numbers_list[i-1]+1) # то на место i вставляем элемент со значением [i-1]+1
        print(f'Потерянное число в списке - {numbers_list[i-1]+1}') # выводим элемент который потерян

print(f'Откорректированный список: {numbers_list}')

# первый вариант записи в файл
# with open(path, 'w') as data: # перезаписываем данные в файл
#     data.write(' '.join(list(map(str, numbers_list)))) # соединяем список и преобразуем в строку (str)

# второй вариант записи в файл
with open(path, 'w') as date:
    print(*numbers_list, file=date, sep=' ')