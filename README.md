#Отчёт
```c
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



