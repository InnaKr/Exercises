a = int(input('Введіть число: '))
k=1
s=0
while a<=0:
    a = int(input('Введіть число > 0: '))
for i in range(len(str(a))):
    b=a%10
    if b == 0:
        k=k*1
    else:
        k=k*b
    s=s+b
    a=a//10
print('Сума =', s, ' Добуток =' ,k)
