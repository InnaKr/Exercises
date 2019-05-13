n=5
def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print (fib(n))

#---------------------------------

n=5
def fib(n):
    if n <= 2:
        return n
    else:
        return fib(n-1)+fib(n-2)
print (fib(n))

