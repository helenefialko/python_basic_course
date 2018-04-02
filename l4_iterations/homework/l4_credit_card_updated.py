exc = 1
num = 1

while True:
    if exc == 4 and len(num) == 4:
        break
    num = input(str('Please, enter the number of your credit card in format XXXX XXXX XXXX XXXX: ')).split(' ')
    try:
        for i in num:
            n = int(i)
    except Exception as e:
        continue
    else:
        exc = 0

    for i in num:
        if len(i) != 4:
            continue      #optimized = to use here break and not check all other elements
        else:
            exc += 1

print('Number card is correct')

if num[0] == '5167':
    print('You use PrivatBank credit card')
elif num[0] == '5375':
    print('You use Monobank credit card')
else:
    print('You use credit card from the unknown bank')

date_0 = 0
date_1 = 0
exc_date = 0
while True:
    if date_0>0 and date_0<=12 and date_1>18 and exc_date == 1 and len(date) == 2:
        break
    date = input('Please, enter expiration date in format mm/yy: ').split('/')
    try:
        date_0 = int(date[0])
        date_1 = int(date[1])
    except Exception as e:
        continue
    else:
        exc_date = 1
print('Exp date is correct')

exc_cvv = 0
cvv = '0'
while True:
    if len(cvv) == 3 and exc_cvv == 1:
        break
    cvv = input('Please, enter CVV: ')
    try:
        cvv_temp = int(cvv)
    except Exception as e:
        print('555')
        exc_cvv = 0
        continue
    else:
        exc_cvv = 1
print('CVV is correct')
print('Everything is correct!')