import random as rand

def roll_dice():
    num = rand.randint(1,6)
    return num
    

roll = 1


while roll < 4:
    dice1 = roll_dice()
    dice2 = roll_dice()
    sum_di = dice1 + dice2

    print("dice 1 is " + str(dice1))
    print("dice 2 is " + str(dice2))
    print("Sum of di is " + str(sum_di))

    if dice1 == dice2:
        roll += 1
    elif (dice1 == dice2) and roll == 3:
        print("Go to jail")
    else:
        break