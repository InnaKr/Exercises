a=int(input('Введіть число: '))
if a < 0:
    a=a*-1
p=0
np=0
for i in range(len(str(a))):
    if (a%10)%2==0:
        p=p+1
    else:
        np=np+1
    a=a//10
print("Кількість парних чисел =", p)
print("Кількість непарних чисел =", np)
