#Задача 9
#Найти максимальную цифру в числе
integer_number = 28137413
Max = 0
for i in range(len(str(integer_number))):
    if int(str(integer_number)[i]) > Max:
        Max = int(str(integer_number)[i])
print(Max)