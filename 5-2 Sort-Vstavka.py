S=[4,9,6,12,5,3,1,8,2,10,7,11]

def sort(S):
    for i in range(len(S)):
        j = i - 1
        N = S[i]
        while j >= 0 and S[j] > N:
            S[j+1] = S[j]
            j = j-1
        S[j+1]=N
    print(S)

sort(S)

