import l8_collections.practice_fn as fn
import csv

companies = (input('Please, enter company names using <,> as a divider without spaces: ').split(','))

# function for email generator
old_year_list = fn.email_generator(11, companies)
new_year_list = fn.email_generator(30, companies)

# function for creation of unique lists
unique_old = fn.unique_numbers(old_year_list)
unique_new = fn.unique_numbers(new_year_list)

# common part for both lists
intersect_set = set(unique_old).intersection(set(unique_new))

# function for dictionary creation
new_dict = fn.dict_creation(intersect_set)

# creation of csv file
with open('new_dict.csv', 'w', newline = '') as csv_file:
    header = ['email', 'name']
    writer = csv.DictWriter(csv_file, fieldnames = header)
    writer.writeheader()
    for key, value in new_dict.items():
        writer.writerow({'email':key, 'name':value})



