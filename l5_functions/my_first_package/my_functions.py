def profile(name, surname, age):
    if age < 25:
        print (f'Hello {name} {surname}. You are young enough')
    if age >= 25:
        print (f'Hello {name} {surname}. You are old')

def birth_year(age):
    print (2018 - age)
