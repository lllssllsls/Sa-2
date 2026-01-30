#Средний уровень 5 вариант
from math import *
t=float(input("Введите t:"))
p=3
k=sqrt(p*t)
x=p*t**2+sqrt(k)
y=tan(x)**2+k*t
print("y=","{:7.2f}".format(y))