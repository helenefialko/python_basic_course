import os

def card_has_errors():
    region = os.environ.get('CARD_TYPE', 'Europe')
    if region == 'China':
        num = card_has_errors_china()
    else:
        num = card_has_errors_europe()
    return num

def card_has_errors_china():
    temp_num = []
    while True:
        if len(temp_num) == 3:
            print('Your card number is correct!')
            return temp_num
        else:
            temp_num = []
            num = input(str('Please, enter the number of your credit card in format XXXX XXXX XXXX: ')).split(
                ' ')
            for i in num:
                if len(i) != 4:
                    temp_num = []
                    break
                try:
                    n = int(i)
                except Exception as e:
                    temp_num = []
                    break
                else:
                    temp_num.append(n)

def card_has_errors_europe():
    temp_num = []
    while True:
        if len(temp_num) == 4:
            print('Your card number is correct!')
            return temp_num
        else:
            temp_num = []
            num = input(str('Please, enter the number of your credit card in format XXXX XXXX XXXX XXXX: ')).split(' ')
            for i in num:
                if len(i) != 4:
                    temp_num = []
                    break
                try:
                    n = int(i)
                except Exception as e:
                    temp_num = []
                    break
                else:
                    temp_num.append(n)

def print_bank(num):
    if num[0] == 5167:
        print('You use PrivatBank credit card')
    elif num[0] == 5375:
        print('You use Monobank credit card')
    else:
        print('You use credit card from the unknown bank')

def cvv_has_errors():
    cvv = 0
    date = 0
    exc = 0
    while True:
        if exc == 1 and len(date) == 2 and len(cvv) == 3:
            print('Your exp_date and cvv is correct!')
            return False
        else:
            list_t = []
            date_without_split = input('Please, enter expiration date in format mm/yy: ')
            date = date_without_split.split('/')
            if len(date) != 2:
                continue
            cvv = input('Please, enter CVV: ')
            list_t.append(cvv)
            list_t.append(date[0])
            list_t.append(date[1])
            for i in list_t:
                try:
                    int_er = int(i)
                except Exception as e:
                    exc = 0
                    list_t = []
                    break
            if len(list_t) == 3:
                if int(list_t[1]) <= 0 or int(list_t[1]) > 12 or int(list_t[2]) <= 18:
                    break
                else:
                    exc = 1



