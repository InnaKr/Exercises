a = int(input('Введіть ціле число: '))
for i in range(len(str(a))):
    print(a % 10, end='')
    a = a // 10
