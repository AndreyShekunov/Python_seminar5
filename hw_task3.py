# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Например:
# Ввод: AABBBCCCC, Вывод: 2A3B4C

def compression(txt): # функция сжатия
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def expansion(txt): # функция разжатия
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите данные для сжатия: ")
print(f"Данные после сжатия: {compression(s)}")
print(f"Данные после восстановления: {expansion(compression(s))}")