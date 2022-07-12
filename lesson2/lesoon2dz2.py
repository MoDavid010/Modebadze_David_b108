a = input("Введите чётные либо нечётные: ")
b = 'чётные'
c = 'нечётные'
if a == b:
    print("0 2 4 6 8 10 12 14 16 18 20")
elif a == c:
    print("1 3 5 7 9 11 13 15 17 19")
else:
    while a != b or a != c:
        print("Я не понимаю, что вы от меня хотите...")
        break








#a = 0
#while a < 7:
#    print ("A", a)
#    a +=1
#    print("the end")
#number = int(input('Введите целое число от 0 до 9'))
#while number < 10:
#    print(number)
#    number = number + 1
#print('программа завершина успешно')
#for i in  "hello, worl":
#    print(i)