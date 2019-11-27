#Задача 6
#Найти сумму цифр числа.
integer_number = 2129
s = 0
for i in range(len(str(integer_number))):
    s += int(str(integer_number)[i])
print(s)