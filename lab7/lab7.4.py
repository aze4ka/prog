def w_iterative(i):
    """
    Итеративная функция для расчета последовательности w.
    
    >>> w_iterative(1)
    0.3
    >>> w_iterative(2)
    -1.5
    >>> w_iterative(3)
    -0.225
    """
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    
    p = -1.5
    pp = 0.3
    
    for j in range(3, i + 1):
        t = p * pp * (j - 2)**2 / (j + 1)**3
        pp = p
        p = t
    
    return p
for i in range(1, 10):
    print(w_iterative(i))
