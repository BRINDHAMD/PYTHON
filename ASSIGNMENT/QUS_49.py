#Build a Mini-Project: Write a command-line "Number Guessing Game". The computer randomly selects a number between 1 and 100. The user gets 7 attempts to guess it. After each guess, the computer tells them if the guess is "too high" or "too low".
import numpy as np

c = np.random.randint(1, 101)
d = 0

while d < 7:
    user = int(input("Guess the number: "))

    if user == c:
        print("Your guess is right!")
        break
    else:
        d += 1
        print("Please, try again")

if d == 7:
    print("No more attempts.")


ANS:
Guess the number:  34
Please, try again
Guess the number:  56
Please, try again
Guess the number:  78
Please, try again
Guess the number:  34
Please, try again
Guess the number:  89
Please, try again
Guess the number:  32
Please, try again
Guess the number:  11
Please, try again
No more attempts.
