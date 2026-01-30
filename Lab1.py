#Базовый уровень 16 вариант
# size=int(input("Введите размер файла в байтах:"))
# result=size//1024
# print("Количество полных килобайтов:",result, " Кбайт")

#Средний уровень 16 вариант
# from math import *
# x=float(input("Введите x:"))
# c=9
# b=x+c**2
# a=(abs(b+c))**(1/3)
# y=cos(b)**2+b*cos(a**2)**4
# print("y=","{:7.2f}".format(y))

#Высокий уровень 16 вариант
from math import *
a=float(input("Введите a:"))
b=float(input("Введите b:"))
c=float(input("Введите c:"))
l=0.5*sqrt(2*b**2+2*c**2-a**2)
print("l=","{:7.2f}".format(l))