#Задача 8
#Дать ответ на вопрос: есть ли среди цифр числа 5?
#'''
b5 = 'No'
integer_number = 213413
for i in range(len(str(integer_number))):
    if str(integer_number)[i]=='5':
       b5 = 'Yes'
print(b5)
