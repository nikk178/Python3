# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному
# в примере (важно в точности соблюдать вывод программы: обратите внимание на пробелы и на точки).
# Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.


a = int(input())

print('The next number for the number', str(a), 'is', str(a + 1) + '.')
print('The previous number for the number', str(a), 'is', str(a - 1) + '.')
