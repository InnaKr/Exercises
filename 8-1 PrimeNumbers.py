k = 23


def is_prime(i):
    if i == 0:
        return False
    elif i == 2:
        return True
    for n in range(2, i):
        if i % n == 0:
            return False
    return True


def prime(n):
    G = [i for i in range(n + 1) if is_prime(i) == True]
    print(G)


prime(k)
