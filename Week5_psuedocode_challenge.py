import random as rand


num_card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

type_card = ['c','s','d','h']

user_num = input()
user_type = input()

rand_num = rand.choice(num_card)
rand_type = rand.choice(type_card)

if (rand_type == user_type):
    print('Good try')

elif(rand_num == user_num):
    print('close but not quite')

elif((rand_type == user_type) & (rand_num == user_num)):
    print('You Win')

else:
    print('try again')