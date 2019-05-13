S = "World Is Full Of Beautiful Things"
l = len(S.replace(' ',''))
print("Загальна кількість символів l=", l)

def Up(b):
    b = 0
    for i in S:
        if i.isupper():
            b=b+1
    return b
#print ("Кількісь великих літер = ", Up(S))

def L(sm):
    sm = 0
    for i in S:
        if i.islower():
            sm=sm+1
    return sm
#print("Кількісь маленьких літер = ", L(S))
print('Відсоток великих літер = ', round(Up(S)/l*100,2),'%')
print('Відсоток маленьких літер = ', round(L(S)/l*100,2),'%')

