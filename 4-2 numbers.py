S="ds0df123ds d4fs5d 6s7d sd89sd"   # not ready
#S=S.split()
print(S)
def Num(S):
    N=[]
    for i in S:
        if i.isdigit():
            N=N+i
            print (N)
    return (N)
print(Num(S))
