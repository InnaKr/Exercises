import re

#---№1-----------------------------------------------------------------------
time1 = '01:39'

pattern1 = re.compile(r'(([01][0-2])\:([0-5][0-9]))')
print('№1: ', pattern1.match(time1).group())
#---№2-----------------------------------------------------------------------
time2 = '23:27'

pattern2 = re.compile(r'(([0-1][0-9])|[2][0-3]):([0-5][0-9])')
print('№2: ',pattern2.match(time2).group())
#---№3-----------------------------------------------------------------------
email1='khD-0214@outlook.com'
email2='khD-0214@example.com'
#   умова @example.com - не проходить

pattern3=r'[\w.-]+@(?!example\.com)[A-Za-z]+\.[\w.]+'
print('№3: ',re.findall(pattern3,email1))
print('№3: ',re.findall(pattern3,email2))
#---№4-----------------------------------------------------------------------
date='27/06/2019'   # валідація такого формату

pattern4=re.compile(r'([0-2][0-9]|[3][01])+/([0][0-9]|[1][0-2])+/[0-2][0-9]{3}')
print('№4: ', pattern4.match(date).group())





