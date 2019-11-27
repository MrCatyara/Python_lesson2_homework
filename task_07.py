#Задача 7
#Найти произведение цифр числа.
integer_number = 2129
s = 1
for i in range(len(str(integer_number))):
    s *= int(str(integer_number)[i])
print(s)