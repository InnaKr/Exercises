y=int(input('Bведіть рік: '))

def Year(y):
    if y%4 == 0 and y%100>0:
        print ('Рік ',y,' високосний')
    elif y%4==0 and y%400==0 and y%100==0:
        print ('Рік ',y,' високосний')
    else:
        print ('Рік ',y,'не високосний')
Year(y)
