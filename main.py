from sys import stdin

first = []
# первый список
for s in stdin:
    # если строка непустая, то присоединяем ее содержимое к кортежу, иначе - выходим из циклв
    if len(s) > 1:
        first.append(tuple(map(int, s.split())))
    else:
        break
# количество следующих списков можно не запоминать - нам нужен только самый первый подходящий по условия список
input()

# функция для проверки соответствия списка заданным условиям
def check(a, b):
    # проверка на схожесть формы строк списков
    if len(a) != len(b):
        return False
    # проверка на то, отличаются ли соответствующие элементы друг на друга на 7
    for i, j in zip(a, b):
        if not all(abs(x - y) == 7 for x, y in zip(i, j)):
            return False
    return True

# ищем нужный список
second = []
for s in stdin:
    # если строка непустая, то присоединяем ее содержимое к кортежу second
    # иначе - проверяем кортеж на соответствие условиям
    if len(s) > 1:
        second.append(tuple(map(int, s.split())))
    else:
        result = check(first, second)
        # если second соответствует условиям, то выходим из цикла
        # иначе - обнуляем second
        if result:
            break
        else:
            second = []
else:
    result = check(first, second)

if result:
    for row in second:
        print('Вывод:')
        print(*row)
else:
    print('Матрица уникальна')
