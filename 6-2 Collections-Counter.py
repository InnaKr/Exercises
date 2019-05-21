S="Ти малий скажи малому хай малий малому скаже хай малий теля прив'яже"
S=S.split()
#print(S)
def dic(S):
    import collections
    c = collections.Counter()
    for i in S:
        c[i] += 1

    print(dict(c))
dic(S)
