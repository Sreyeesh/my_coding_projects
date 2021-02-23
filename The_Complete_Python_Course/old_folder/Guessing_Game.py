import random


print("Welcome to the Guessing Game")

target_number = random.randint(1,9)
guesses = []

# the_guess = 0 

while len(guesses) < 5:
    guess = int(input("Please type a number: "))
    guesses.append(guess)

    if guess > target_number:
        print("Too high! The number {} is too high!".format(guess))
    elif guess < target_number:
        print("Too low! The number {} is too low!".format(guess))
    else:
        print("You won! You guessed the number {} !".format(guess))
        break
else:
    print(f"You lost! The correct number was {target_number}.")


    
    # the_guess += 1

# if not the_guess < 5:
#     # print("You lost the game ! The correct number is {} ".format(target_number))
#     print(f"You lost! The correct number was {target_number}.")







