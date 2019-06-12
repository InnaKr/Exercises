def cycle(*iterable):
    while True:
        for i in iterable:
            for l in i:
                yield l


for i in cycle('AB', 'CD'):
    print(i)
