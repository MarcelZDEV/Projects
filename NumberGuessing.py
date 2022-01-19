import random

random_number = random.randint(1, 10)

user_answer = int(input('Type number to guess it: '))

if user_answer == random_number:
    print(f'Good the number was {user_answer}, try next!')
else:
    print(f'Not this time. Correct number was {random_number}')
