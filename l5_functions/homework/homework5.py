import l5_functions.homework.functions_hw as functions_hw
import os

os.environ['CARD_TYPE'] = 'China'

num = functions_hw.card_has_errors()
functions_hw.print_bank(num)
functions_hw.cvv_has_errors()





