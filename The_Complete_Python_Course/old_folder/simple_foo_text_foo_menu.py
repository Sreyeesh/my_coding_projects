# Ask the user to choose one of two options:

# if they type 'p', our program should prin "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.

# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()

user_choice = input("Please type either p or type q to exit program:")

while user_choice != "q":
    if user_choice == "p":
        print('Hello')
    # else:
    #     print(" You didn't type p or q ")

    user_choice = input(" Please enter q or p : ")