def w_recursive(i):
    """
    Рекурсивная функция для расчета последовательности w.
    
    >>> w_recursive(1)
    0.3
    >>> w_recursive(2)
    -1.5
    >>> w_recursive(3)
    -0.225
    """
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    return w_recursive(i-1) * w_recursive(i-2) * (i-2)**2 / (i+1)**3
for i in range(1, 10):
    print(w_recursive(i))