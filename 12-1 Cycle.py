def cycle(*iterable):
    for i in iterable:
        for l in i:
            yield l


while True:
    for i in cycle('AB', 'CD'):
        print(i)
