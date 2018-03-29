# input method
a = int(input('Please, enter an integer: '))
b = input('Please, enter any type: ')
c = str(input('Please, enter your name: '))


# try...except
try:
    a/0
except ZeroDivisionError:
    print('You can not divide by zero')

try:
    b/'smth'
except Exception as e:
    print('Try something else')

try:
    c*0.5
except TypeError:
    print('You can try again')

