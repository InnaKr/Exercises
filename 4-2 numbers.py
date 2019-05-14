s="ds0df123ds d4fs5d 6s7d sd89sd"

def num(a):
    k=''
    for i in range(len(a)):
        if a[i].isdigit():
            k=k+a[i]
        else:
            k=k+' '
    k=k.split()
    return k
print(num(s))