number = int(input('Provide a number: '))

print('before if')

if number == 10 or number % 2 == 0:
    print('The number is 10. Yey!')
elif number == 20:
    print('The number is 20. Who ho!')
elif number == 30:
    print('The number is 30')
else:
    print('Else block.')

print('after if')
