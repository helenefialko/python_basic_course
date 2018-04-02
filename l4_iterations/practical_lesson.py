low_digit_limit = 1
upper_digit_limit = 100
list_q = ['0']

while True:
    fav_num = input('What is your favorite number? ')
    try:
        fav_num = int(fav_num)
    except Exception as e:
        list_q.append(str(fav_num))
        continue
    else:
        list_q.append(fav_num)
        if fav_num < 1:
            print(f'Your input value {fav_num} is less than 1')
            continue
        elif fav_num > 100:
            print(f'Your input value {fav_num} is more than 100')
            continue
        else:
            print('Correct number!')
            break
list_q.pop(0)
print_list = [i for i in list_q if type(i) == str]
print(print_list)
