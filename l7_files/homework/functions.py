import re

def checking_the_name():
    while True:
        first_name = input('Please, enter your first and second names: ')
        checking = re.match(r'^[A-Za-z]+\s[A-Za-z]+$', first_name)
        if checking is None:
            continue
        else:
            return first_name

def card_has_errors_china():
    while True:
        num = input(str('Please, enter the number of your credit card in format XXXX XXXX XXXX: '))
        checking = re.match(r'^[0-9]{4}\s[0-9]{4}\s[0-9]{4}$', num)
        if checking is None:
            continue
        else:
            return num

def card_has_errors_europe():
    while True:
        num = input(str('Please, enter the number of your credit card in format XXXX XXXX XXXX XXXX: '))
        checking = re.match(r'^[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}$', num)
        if checking is None:
            continue
        else:
            return num

def print_bank(num):
    if num.startswith('5167'):
        bank = 'You use PrivatBank credit card'
    elif num.startswith('5375'):
        bank = 'You use Monobank credit card'
    else:
        bank = 'You use credit card from the unknown bank'
    return bank

def cvv_has_errors():
    while True:
        exp = input('Please, enter expiration date in format mm/yy: ')
        checking = re.match(r'^0*[1-12]+\/[19-99]+$', exp)
        if checking is None:
            continue
        else:
            return exp

def exp_has_errors():
    while True:
        cvv = input(str('Please, enter CVV: '))
        checking = re.match(r'^[0-9]{3}$', cvv)
        if checking is None:
            continue
        else:
            return cvv




