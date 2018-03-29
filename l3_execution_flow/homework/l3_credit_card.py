num = input(str('Please, enter the number of your credit card: '))
date = input('Please, enter expiration date in format mm/yy: ')
cvv = input(str('Please, enter CVV: '))

if len(num) != 16:
    exit()

try:
    date=int(date)
except Exception as e:
    print('Ok')
else:
    exit()

if len(cvv)<3:
    print('CVV is not correct!')
    exit()

print('Ha-ha-ha.Now I will use your credit card!')

