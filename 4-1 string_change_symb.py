#S = input('Введіть будь яке речення:  ')
S='Actions speak louder than words '

def change(a):
    d = a.split()
    k = ''
    for i in range(len(d)):
        if i == len(d) - 1:
            k = k + d[i]
        else:
            k = k + d[i] + '*'
    return k


print(change(S))
