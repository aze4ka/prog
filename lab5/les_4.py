import matplotlib.pyplot as plt
import numpy as np
from math import *

#Вариант №3

def f(x):
    return cos(x)*exp(-x**2)

x = np.linspace(-3, 3, 1000)
y1 = [f(i) for i in x]
y2 = [1 for i in x]

plt.title('Лабораторная работа 4, вариант 3')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y1, label='cos(x)*exp(-x**2)')
plt.plot(x, y2, 'r', label='Касательная')
plt.text(0.785, max(y1)+0.01, 'точка касания')
plt.legend()
plt.show()