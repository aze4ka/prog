def log(level='INFO'):
    def decorator(f):
        def d(*args, **kwargs):
            r = f(*args, **kwargs)
            print(f'[{level}] LOG: {f.__name__}({", ".join(map(str, args))}) = {r}')
            return r
        return d
    return decorator

@log()  # Используем декоратор без параметров
def add(x, y): 
    return x + y

# Пример использования
print(add(1, 2))
print(add(3, 4))
print(add(128, 256))
