def unpack_iterative(n):
    """
    Итеративная функция для распаковки вложенного списка.
    
    >>> unpack_iterative([None, [1, ({2, 3}, {'foo': 'bar'})]])
    [None, 1, 2, 3, 'foo', 'bar']
    """
    r = []
    q = [n]
    
    while q:
        n = q.pop()
        match type(n).__name__:
            case 'list' | 'tuple' | 'set':
                q.extend(n)
            case 'dict':
                q.extend(list(n.keys()))
                q.extend(list(n.values()))
            case _:
                r.append(n)
    
    return r[::-1]

print(unpack_iterative([None, [1, ({2, 3}, {'foo': 'bar'})]]))
