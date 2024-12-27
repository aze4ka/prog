# Задача 1: Замыкание для получения очередной строки из файла
def line_reader(fname):
    try:
        f = open(fname, 'r')
    except FileNotFoundError:
        print(f"Ошибка: файл {fname} не найден.")
        return lambda: None  # Возвращаем заглушку, чтобы не было ошибок дальше

    def get_next_line():
        return f.readline().strip()

    return get_next_line


# Задача 2: Декоратор для логирования вызовов функций
def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__}({args=}) = {result}")
        return result
    return wrapper


# Применение декоратора к замыканию из задачи 1
@log
def get_next_line_logged(fname):
  return line_reader(fname)

# Пример использования:
if __name__ == "__main__":
    # Создание тестового файла
    with open("test.txt", "w") as f:
      f.write("Первая строка\n")
      f.write("Вторая строка\n")
      f.write("Третья строка\n")
    
    # Используем задекорированное замыкание
    file_reader = get_next_line_logged("test.txt")
    print(file_reader())
    print(file_reader())
    print(file_reader())
    print(file_reader())
    
    print('\n--- Пример ---')
    @log
    def add(x, y):
        return x + y
    
    print(add(5, 0))
    print(add(145, 564))