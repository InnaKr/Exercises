a = int(input('Bведіть довжину 1-ї сторони: '))
b = int(input('Bведіть довжину 2-ї сторони: '))
c = int(input('Bведіть довжину 3-ї сторони: '))


def p(a, b, c):
    return (a + b + c) / 2

print (p(a,b,c))
def S(a, b, c):
    return ((p(a, b, c) * (p(a, b, c) - a) * (p(a, b, c) - b) * (p(a, b, c) - c)) ** 0.5)


print('Площа трикутника =', round(S(a, b, c), 2))
