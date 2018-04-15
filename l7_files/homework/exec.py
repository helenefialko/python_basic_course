import l7_files.homework.functions as fn
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

# print correct information in .txt file
with open('homework.txt', 'w') as file:
    file.writelines([first_name.upper(), '\n', num, ' : ', bank, '\n', cvv, '\n', exp])

with open('homework.txt', 'r') as file:
    s = file.read()
    print(s)

