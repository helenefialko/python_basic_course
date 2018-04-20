from l8_collections.final_project.utils import *

alph_list = alph_list_creation()
name_list = name_list_creation(alph_list)
phone_list = phone_list_creation(alph_list)
exp_list = exp_list_creation()
card_list = card_list_creation(alph_list)
creation_of_headers_in_csv_file()
correct_csv_file_creation(name_list, phone_list, exp_list, card_list)



