import time


def sleep():
    time.sleep(1)


start_game = input('So you want play quiz? ')
if start_game.lower() != 'yes':
    print('So good bay!')
    quit()

player_name = input('What is your nickname? ')
print(f"Let's start the game {player_name}")

points = 0
sleep()
first_question = {
    'a': 'Charles Leclerc',
    'b': 'Max Verstappen',
    'c': 'Lewis Hamilton',
    'd': 'Nikita Mazepin'
}
for q1, q1s in first_question.items():
    print(f"{q1} : {q1s}")
first_question_user = input('Who was the world champion in 2021?')
if first_question_user.lower() == 'b':
    print('Great that is correct answer')
    points += 10
else:
    print('Correct answer was b Max Verstappen')
sleep()
second_question = {
    'a': '18',
    'b': '20',
    'c': '15',
    'd': '22'
}
for q2, q2s in second_question.items():
    print(f"{q2} : {q2s}")
second_question_user = input('What size have wheels in 2022?')
if second_question_user == 'd':
    print('Yes, awsome it\'s correct answer')
    points += 10
else:
    print('Wrong, correct answer was d 22 inch')
print(f"Your points {points}")
