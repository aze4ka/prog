def line_reader(fname):
    try:
        f = open(fname, 'r')
    except FileNotFoundError:
        print(f"Ошибка: файл {fname} не найден.")
        return lambda: None  # Возвращаем заглушку, чтобы не было ошибок дальше

    def get_next_line():
        return f.readline().strip()

    return get_next_line


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__}({args=}) = {result}")
        return result
    return wrapper


@log
def get_next_line_logged(fname):
  return line_reader(fname)