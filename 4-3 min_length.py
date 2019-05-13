#S = input('Введіть будь яке речення:  ')
S='Live and learn'

def min_len(h):
    k = len(h)
    h = h.split()
    for i in h:
        if len(i) <= k:
            k = len(i)
    return k


print("Мінімальне слово має",min_len(S),'символа')
