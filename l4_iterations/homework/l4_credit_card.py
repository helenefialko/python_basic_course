num = input(str('Please, enter the number of your credit card in format XXXX XXXX XXXX XXXX: ')).split(' ')
date = input('Please, enter expiration date in format mm/yy: ').split('/')
cvv = input(str('Please, enter CVV: '))

exc = 0  # ввожу переменную, которую буду использовать в цикле while
try:     # проверяю каждый элемент списка на то что он численный
    for i in num:
        n = int(i)
except Exception as e:
    exc = 1        # присваиваю переменной единицу, чтобы while условие дало ошибку,
                   # таким образом здесь отдельную ошибку выводить не надо

while (len(num[0])!=4 or len(num[1])!=4 or len(num[2])!=4 or len(num[3])!=4 or exc==1 or len(num)!=4):
    # проверяю длину каждого элемента, количество элементов в списке, и так же переменную, которая выше из-за
    # ошибки int могла измениться с 0 на 1
    num = input(str('Error! Please, enter the number of your credit card in format XXXX XXXX XXXX XXXX: ')).split(' ')
    # вывожу ошибку и повторный ввод если хоть одно условие не было удовлетворено
    try:
        for i in num:
            n = int(i)
    except Exception as e:
        exc = 1
    # снова проверяю на int, так как повторный ввод мог допустить эту ошибку(и меняю переменную чтобы в while
    # выдало снова ошибку):
    else:
        exc = 0
    # переменная обнуляется, while условие не соблюдается, програма идет дальше

if num[0] == 5167:
    print('You use PrivatBank credit card')
elif num[0] == 5375:
    print('You use Monobank credit card')
else:
    print('You use credit card from the unknown bank')

# использую тот же подход с переменной что и выше для даты:
exc_date = 0
try:
    date_0 = int(date[0])
    date_1 = int(date[1])
except Exception as e:
    exc_date = 1
while (date_0<=0 or date_0>12 or date_1<=18 or exc_date==1):
    date = input('Error! Please, enter expiration date in format mm/yy: ').split('/')
    try:
        date_0 = int(date[0])
        date_1 = int(date[1])
    except Exception as e:
        exc_date = 1
    else:
        exc_date = 0

# использую тот же подход с переменной что и выше для cvv:
exc_cvv = 0
try:
    cvv_temp = int(cvv)
except Exception as e:
    exc_cvv = 1

while (len(cvv)!=3 or exc_cvv==1):
    cvv = input(str('Error! Please, enter CVV: '))
    try:
        cvv_temp = int(cvv)
    except Exception as e:
        exc_cvv = 1
    else:
        exc_cvv = 0

print('I knew it!')