def line(fname):
    f = open(fname, 'r')
    
    def get_next_line():
        line = f.readline()
        if line == '':  # Если файл закончился
            f.close()  # Закрываем файл
            return None
        return line.strip()  # Убираем лишние пробелы и символы новой строки
    
    return get_next_line

# Пример использования
f = line('1.py')  # Убедитесь, что файл '1.py' существует в директории
print(f())
print(f())
print(f())
