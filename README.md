#Отчёт
```c
Вариант 3
Задание:
1.Разберите код программы из примера.
2.Составьте блок-схему алгоритма для своего варианта.
3.Напишите программу, решающую задачу по своему варианту.
вариант:Вывести значение наименьшего из трёх параметров a, b, c если оно меньше или равно x и кратно 7, и частное наименьшего параметра и суммы двух оставшихся иначе.
#include <stdio.h>

int min(int a, int b, int c) 
{
  if (a <= b && a <= c)
  {
    return a;
  }
  else if (b <= a && b <= c) 
  {
    return b;
  }
  else
    return c;
}

int oper(int a, int b, int c) 
{
  float z = (float)a / b / c;
  float oper = z;
  if (z - oper != 0.0)
      return z;
  else
      return oper;
}

int main() 
{
  int x;

  printf("Введите x: ");
  scanf("%d", &x);

  int a,b,c;

  printf("Введите a: ");
  scanf("%d", &a);
  printf("Введите b: ");
  scanf("%d", &b);
  printf("Введите c: ");
  scanf("%d", &c);

  if (min(a,b,c) <= x && (min(a,b,c) % 7) == 0)
  {
    printf("Самое маленькое число: %d\n", min(a,b,c));
  }
  else 
  {
    printf("Частное чисел: %d \n", oper(a,b,c));
    printf("Сумма двух оставшихся: %d\n", a + b + c - min(a,b,c));
  }
}

скриншот:
file:///home/user/Desktop/students/601-41/abdullina/prog/lab1/pics)/lab1.png


