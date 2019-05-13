a = int(input('Bведіть довжину 1-ї сторони: '))
b = int(input('Bведіть довжину 2-ї сторони: '))
c = int(input('Bведіть довжину 3-ї сторони: '))


def T(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


print(T(a, b, c))
