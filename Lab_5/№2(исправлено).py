# Задача 2: Минимумы
# Напишите программу, на вход которой подаётся прямоугольная матрица в
# виде последовательности строк (числа пишем через пробел). Используйте
# метод split() строки. После последней строки матрицы идёт строка,
# содержащая только end.
# После того, как пользователь ввел end, программа должна найти в каждой
# строке матрицы минимальное значение и вывести его на экран.
import sys

a = []
b = input()
min = sys. maxsize
while b != "end":
    a.append(b.split())
    b = input()
for i in range(len(a)):
    for j in range(len(a[i])):
        if(int(a[i][j]) < min):
            min = int(a[i][j])
    print(min)
    min = sys. maxsize


