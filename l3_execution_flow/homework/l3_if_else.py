# If...else 1
d = int(input('Enter d: '))
f = int(input('Enter f: '))
e = int(input('Enter e: '))
if d==f and e<(d+f):
    print ('Everything is correct')
elif e>(d+f):
    print ('Try other numbers')
else:
    print ('Something is going wrong')

# If...else 2
g = int(input('Try some number: '))
p = g//2
if p==1:
    print('You number is odd!')
else:
    print('You number is even!')

# If...else 3
g = ''
p = int(input('Try...: '))
if g is not True:
    print('Good')
else:
    print('Error')
