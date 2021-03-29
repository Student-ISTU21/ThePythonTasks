# создаём массив.
# Он нужен, чтобы не вычислять одни и те же значения по несколько раз
chisla = [0] * 100


def fiboncci(n):
    # если ячейка массива пустая, то вычисляем значение
    # иначе - сразу переходим к return
    if chisla[n] == 0:
        if n == 1 or n == 2:
            chisla[n] = 1
        else:
            chisla[n] = fibo(n - 1) + fibo(n - 2)
    return chisla[n]


n = int(input())
print(fiboncci(n))
