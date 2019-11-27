#Задача 10
#Найти количество цифр 5 в числе
integer_number = 2813574513
N5 = 0
for i in range(len(str(integer_number))):
    if str(integer_number)[i] == '5':
        N5 += 1
print(N5)