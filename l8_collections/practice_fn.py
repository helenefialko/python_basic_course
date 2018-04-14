import random

def email_generator(max_value, companies):
    counter = 0
    new_list = []
    while True:
        if counter == 50:
            return new_list
        for i in companies:
            if counter != 50:
                r = random.randint(1, max_value)
                s = i + str(r) + '@' + i + '.com'
                new_list.append(s)
                counter += 1

def unique_numbers(ready_list):
    first_el = ready_list[0]
    unique_list = [first_el]
    for i in ready_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

def dict_creation(intersect_set):
    guest_dict = {}
    for i in intersect_set:
        elem = i.split('@')
        guest_dict[i] = elem[0]
    return guest_dict
