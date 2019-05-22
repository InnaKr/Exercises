N = int(input("Введіть ціле число: "))

def K(a):
    P, R = [], []
    for _ in range(a):
        S = input("Введіть числовий ряд: ")
        G = [float(el) for el in S.split()]
        for k in G:
            if k.is_integer():
                P.append(k)
            else:
                R.append(k)
    P.sort()
    P=[int(el)for el in P]
    R.sort()
    P.extend(R)

    print(P)

K(N)
