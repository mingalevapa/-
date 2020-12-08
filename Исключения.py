#!/usr/bin/env python
# coding: utf-8

# 1) Напишите функцию, которая принимает имя файла. Если файла нет, то возвращает текст "404. File (filename) not found", иначе возвращает содержимое файла

# 2) Написать функцию умножения неограниченного количества чисел. Если аргумент не является число, то должна вызываться ошибка ValueError

# In[ ]:


def multiply(*args):
    res=1
    for i in args:
        if type(i) != int and type(i)!=float:
            raise ValueError
        res*=i
    return res


# 3) Написать калькулятор для строковых выражений вида '<число> <операция> <число>', где <число> - целое число, например 113, <арифмитическая операция> - одна из операций +,-,*,/(деление нацело),%(остаток от деления),^(возведение в степень). Пример calc('13 - 5') -> 8. Проверять переданную строку на корректность ввода и выводить отладочную ошибку

# In[ ]:


def string_calc(string):
    dict_signs={"+":lambda x,y:x+y
               "-":lambda x,y:x-y
               "*":lambda x,y:x*y
               "//":lambda x,y:x//y
               "%":lambda x,y:x%y
               "^":lambda x,y:x**y
              }
    string=string.split()
    assert len(string)==3, "Некорректно введено значение"
    assert string[0].isdigit(), "Первый знак не является числом"
    assert string[-1].isdigit(), "Последний знак не является числом"
    assert string[1] in dict_signs, "Данная операция не поддерживается"
    
    try:
        return dict_signs[string[1]](int(string[0]),int(string[-1]))
    except ZeroDivisionError:
        print("Деление на ноль")


# 4) Написать функцию подсчета сумма главной или побочной диагонали. Если матрица не является квадратной, должна вызываться ошибка

# In[ ]:


def matrix_diag_summ(matrix, main=True):
    length=len(matrix)
    for i in matrix:
        if len(i)!=length:
            raise ValueError
    diag_summ=0
    if main:
        for i,e in enumerate(matrix):
            diag_summ+=e[i]
    else:
        for i, e in enumerate(matrix):
            diag_summ+=e[-(i+1)]
    return diag_summ


# In[ ]:


matrix_diag_summ([[1,2,3],[4,5,6],[7,8,9]], True)


# 5) В функцию передаются 3 кортежа - координаты x,y точек. Необходимо найти площадь треугольника. Данные проверять в режиме отладки
