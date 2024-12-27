from itertools import chain

def unpack_recursive(x):
    """
    Рекурсивная функция для распаковки вложенного списка.
    
    >>> unpack_recursive([None, [1, ({2, 3}, {'foo': 'bar'})]])
    [None, 1, 2, 3, 'foo', 'bar']
    """
    def f(z):
        if isinstance(z, (list, tuple, set)):
            return list(chain.from_iterable(f(i) for i in z))
        return [z]

    match type(x).__name__:
        case 'list' | 'tuple' | 'set':
            return f([unpack_recursive(i) for i in x])
        case 'dict':
            return [key for key in x.keys()] + [unpack_recursive(x[key]) for key in x.keys()]
        case _:
            return [x]