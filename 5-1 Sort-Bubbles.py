S=[14,9,26,12,5,3,11,48,2,10,7,13]

def Bubble(S):
    for i in range(len(S)):
        for k in range(len(S)-1):
            if S[k] > S[k+1]:
                S[k], S[k+1] = S[k+1], S[k]
    print(S)


Bubble(S)
