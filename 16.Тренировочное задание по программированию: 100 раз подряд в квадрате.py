#Заданное число N записали 100 раз подряд и затем возвели в квадрат. Что получилось?

# 1 Вариант 

A = int(input())
B = str(A)
C = (B * 100)
D = int(C)
E = (D ** 2)
print(E)

# 2 Вариант

A = int(input())
print(int(str(A*100))**2)