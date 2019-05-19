d1={'a': 2,'b': 3,'c': 4,'e': 5}
d2={'b': 3,'f': 7,'e': 9}

def merge(d1,d2):
    d3,d4 = {},{}
    d1s,d2s = set(d1), set(d2)
    for k in (d1s & d2s):
        d3[k]=d1[k]+d2[k]
    for k in ((d1s-d2s)):
        d4[k]=d1[k]
    for k in ((d2s-d1s)):
        d4[k]=d2[k]
    d4.update(d3)
    print(d4)


merge (d1,d2)
