import re
import l6_strings.homework.functions as fn
import os

region = os.environ['CARD_TYPE'] = 'China'

# checking the name
first_name = fn.checking_the_name()

# ask the number of the card due to region
region = os.environ.get('CARD_TYPE', 'Europe')
if region == 'China':
    num = fn.card_has_errors_china()
else:
    num = fn.card_has_errors_europe()

# checking the bank
bank = fn.print_bank(num)

# checking CVV and exp date and expiration date
cvv = fn.cvv_has_errors()
exp = fn.exp_has_errors()

# print correct information
print(first_name.upper())
print(num, ':', bank)
print(cvv)
print(exp)


