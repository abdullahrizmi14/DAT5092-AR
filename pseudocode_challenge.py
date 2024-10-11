import random
import unittest


N_min = 1
N_max = 10

N_rand = random.randint(N_min,N_max)

i = 1
y = 1

while (y == 1):
    N_guess = int(input("Guess a number "))
    if (N_guess > N_rand):
        print("Too high")
        i += 1
    
    elif (N_guess < N_rand):
        print("Too Low")
        i += 1
    
    else:
        print("Success! Guessed in " + str(i) + " attempts")
        y = 0
    
