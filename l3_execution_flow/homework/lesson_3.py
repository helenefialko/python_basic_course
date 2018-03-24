name = input('Please, enter your name: ')
age = input('Please, enter your age: ')

email = f'{name}{age}@itea.ua'
print(email)

surname = 'Noob'
try:
    p_error = name / 'sometext'
except Exception as e:
    surname = 'Fialko'

print('\nDeveloping with Python...\n')
if surname == 'Noob':
    print('Ti dopustil oshibku!')
else:
    print('Molodec!')
