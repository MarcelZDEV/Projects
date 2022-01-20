import random

dice_roll_d4 = random.randint(1, 4)
dice_roll_d6 = random.randint(1, 6)
dice_roll_d10 = random.randint(1, 10)
dice_roll_d12 = random.randint(1, 12)
dice_roll_d20 = random.randint(1, 20)

ask_user_dice = input('what dice you want chose? (d4/d6/d10/d12/d20): ')
if ask_user_dice == 'd4':
    print(dice_roll_d4)
elif ask_user_dice == 'd6':
    print(dice_roll_d6)
elif ask_user_dice == 'd10':
    print(dice_roll_d10)
elif ask_user_dice == 'd12':
    print(dice_roll_d12)
elif ask_user_dice == 'd20':
    print(dice_roll_d20)
else:
    print('something gone wrong')
