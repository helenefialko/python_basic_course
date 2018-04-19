import random
import csv
import re

# creation of alphabet list
def alph_list_creation():
    alph_list = []
    for i in range(ord('a'), ord('z')+1):
        i = chr(i)
        alph_list.append(i)
    return alph_list

# creation of names list
def name_list_creation(alph_list):
    name_item = []
    for i in range(100):
        r_num_char = random.randint(3,8)
        for j in range(r_num_char):
            any_char = random.choice(alph_list)
            name_item.append(any_char)
        name_item.append('/')

    name_list = (''.join(name_item)).split('/')
    name_list.pop()
    return name_list

# creation of phone list
def phone_list_creation(alph_list):
    phone_item = []
    for i in range(100):
        chance = random.randint(1, 50)
        if chance == 9:
            ran_symbol = random.choice(['[', '-', ']', ' ', random.choice(alph_list)])
            ran_temp = '+38' + str(ran_symbol)
            phone_item.append(str(ran_temp))
            for k in range(8):
                r_num = random.randint(0, 9)
                phone_item.append(str(r_num))
        else:
            phone_item.append('+380')
            for k in range(8):
                r_num = random.randint(0,9)
                phone_item.append(str(r_num))
        phone_item.append('/')

    phone_list = (''.join(phone_item)).split('/')
    phone_list.pop()
    return phone_list

# creation of exp date
def exp_list_creation():
    exp_item = []
    for i in range(100):
        r_num = random.randint(1,12)
        if r_num < 10:
            r_num = '0'+ str(r_num)
        r_date = random.randint(19,30)
        exp_item.append(str(r_num))
        exp_item.append('/')
        exp_item.append(str(r_date))
        exp_item.append('//')

    exp_list = (''.join(exp_item)).split('//')
    exp_list.pop()
    return exp_list

# creation of card
def card_list_creation(alph_list):
    card_item = []
    for i in range(100):
        for j in range(4):
            chance = random.randint(1, 100)
            if chance == 9:
                ran_symbol = random.choice(['-', ' ', random.choice(alph_list)])
                card_item.append(str(ran_symbol))
                for l in range(3):
                    r_card_num = random.randint(0, 9)
                    card_item.append(str(r_card_num))
                card_item.append(' ')
            else:
                for l in range(4):
                    r_card_num = random.randint(0,9)
                    card_item.append(str(r_card_num))
                card_item.append(' ')
        card_item.append('/')

    card_list = (''.join(card_item)).split(' /')
    card_list.pop()
    return card_list

# checking the correctness of data
def tel_checking(phone):
    while True:
        checking = re.match(r'^\+[0-9]{11}$', phone)
        if checking is None:
            error = 'Present'
        else:
            error = 'Absent'
        return error

def card_checking(card_list):
    while True:
        checking = re.match(r'^[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}$', card_list)
        if checking is None:
            error = 'Present'
        else:
            error = 'Absent'
        return error

# creation of final dictionary and writing to the file if correct
def correct_csv_file_creation(name_list, phone_list, exp_list, card_list):
    with open('cardholders.csv', 'w') as csv_file:
        header = ['name', 'phone', 'exp_date', 'card']
        writer = csv.DictWriter(csv_file, fieldnames = header)
        writer.writeheader()
        ind = 0
        temp_dict = {}
        for i in range(100):
            ran_name = random.choice(name_list)
            temp_dict['name'] = name_list[ind] + ' ' + ran_name
            temp_dict['phone'] = phone_list[ind]
            temp_dict['exp_date'] = exp_list[ind]
            temp_dict['card'] = card_list[ind]
            error_tel = tel_checking(temp_dict['phone'])
            error_card = card_checking(temp_dict['card'])
            if error_tel == 'Absent' and error_card == 'Absent':
                writer.writerow(temp_dict)
            else:
                incorrect_csv_file_creation(temp_dict)
            ind += 1
    return temp_dict

# writing to the file if incorrect
def incorrect_csv_file_creation(temp_dict):
    with open('cardholders_errors.csv', 'a') as csv_file:
        header = ['name', 'phone', 'exp_date', 'card']
        writer = csv.DictWriter(csv_file, fieldnames = header)
        writer.writeheader()
        writer.writerow(temp_dict)
    return None
