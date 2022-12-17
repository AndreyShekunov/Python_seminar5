#Задача 1. Посчитать наименьшее общее кратное (НОК) и наименьший общий делитель (НОД) числа

def factor(n, lst): # функция множитель
    num_f = 2
    while n > 1:
        if n % num_f == 0:
            lst.append(num_f)
            n = int(n / num_f)
        else:
            num_f += 1


n1 = int(input('Введите целое число n1: '))
n2 = int(input('Введите целое число n2: '))

lst1 = []
lst2 = []

factor(n1, lst1)
print(set(lst1))
factor(n2, lst2)
print(set(lst2))

nod_find = set(lst1).intersection(set(lst2))
nod = 1
for i in nod_find:
    nod = nod *i

nok = n1 * n2 // nod
print(f'Наименьшее общее кратное (НОК) = {nok}')
print(f'Наименьшей общий делитель (НОД) = {nod}')