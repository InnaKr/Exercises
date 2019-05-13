a=int(input('Введіть 1-е число: '))
b=int(input('Введіть 2-е число: '))
while True:
    c=input('Введіть дію (+, -, *, /): ')
    if c == "+":
        print ( a+b )
    elif c == "-":
        print ( a-b )1
    elif c == "*":
        print (a*b)
    elif c == "/":
        print (a/b)
    y = input ('Закінчити арифметичні дії (так/ні): ')
    if y == 'Так' or y == 'так':
        break
