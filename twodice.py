import random

dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)

if dice_1 + dice_2 == 6 or dice_1 + dice_2 == 7 or dice_1 + dice_2 == 8:
    print("win")
else:
    print("lose")
print (dice_1 + dice_2)