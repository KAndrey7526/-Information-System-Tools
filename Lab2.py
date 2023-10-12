# Задание 15

import tkinter
import time
from tkinter import *
from tkinter import messagebox


while True:
    if __name__ == '__main__':
        messagebox.showinfo('Useful Python', 'Вы долго смотрели в монитор, теперь посмотрите в окно.')
    time.sleep(10)

# Задание 3
a = 3
print(type(a))
a = 3.5
print(type(a))
a = 'qwerty'
print(type(a))
a = True
print(type(a))
a = '123'
print(type(a))

# Задание 4

print(int(5.7))
print(int(-5.7))
print(3 ** 39 - int(float(3 ** 39)))

# Задание 5

name = input('Введите свое имя:')
print('Привет,' + name)

# Задание 6

x, y = input().split()
x = int(x)
y = int(y)
sum = (60*x)+y
print(2*sum)

# Задание 7

a = False
b = True
c = False
print((not a or b) and c)

# Задание 8

year = int(input('Введите год:'))
if(year < 1900 or year > 3000):
   print('Год не входит в выборку')
elif(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 ==0)):
  print('С днём рождения!')
else:
   print('Год обычный')

#Задание 9

a = 1
while(a <= 20):
   if(a % 2 == 0):
       print(a, end=' ')
   a += 1

#Задание 10
x = 0
a = 1
while(a != 0):
   x += a
   a = int(input())

print(x - 1)

#Задание 11

x = int(input('Введите X:'))
y = int(input('Введите Y:'))
n = 1
while (n % x != 0) or (n % y != 0):
    n += 1
print('Нужно кусков: ', n)
print('Пицца порезана!')

# Задание 12

for i in range(1,20):
    if(i % 2 == 0):
        print(i, end=' ')

# Задание 13

a, b, c, d = [int(input('Введите значение: ')) for i in range(4)] # инпут значений
print('', end='\t') # отступ чтобы все было ровно
for j in range(c, d + 1):
    print(j, end='\t') # вывод горизонтальной строки чисел ( множителей)
print()# перенос строки
for i in range(a, b + 1):
    print(i, end='\t') # вывод вертикальной строки чисел ( множителей)
    for j in range(c, d + 1):
        print(i * j, end='\t') # вывод произведений
    print()# перенос строки

# Задание 14

n = int(input())
a = [[0] * n for i in range(n)]
count = 0
for i in range(n):
    count += 1
    a[0][i] = count
j = 0
i = n-1
n -= 1
while len(a)**2 != count:
    for k in range(n):
        j += 1
        count += 1
        a[j][i] = count
    for k in range(n):
        i -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):
        i += 1
        count += 1
        a[j][i] = count
    n -= 2
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# Задание 16



def clicked():
    window.quit()
def ok():
    time.sleep(5)

window = Tk() #создание окна
window.title('Напоминалка') #заголовок окна
window.geometry('1500x250') #размеры окна
lbl = Label(window, text='Вы долго смотрели в монитор, теперь посмотрите в окно', font=('Arial Bold', 30))
lbl.grid(column=0, row=0)
btn = Button(window, text='ОК', command=ok)
btn2 = Button(window, text='ЗАКРЫТЬ', command=clicked)
btn.grid(column=0, row=4)
btn2.grid(column=0, row=6)
window.mainloop() #бесконечный цикл окна, окно ждёт нажатий

