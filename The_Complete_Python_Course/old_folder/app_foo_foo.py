friends = ["Harry","Ron","Hermione"]
family = ["James","Lily","Sirius"]

print(" Hello Welcome to the Potter's sotting list. ")

user_name = input("Enter your name: ")


while friends or family:
    if user_name not in friends:
    # print(" please add your friends to the friends list")
        answer = input(" Are you friend or family ? ")
        if answer == "friend":
            name = input(" Please enter your name to be added to the friends list : ")
            friends.append(name)
            print(friends)
            break
        if answer == "family":
            print("Please enter your name into the family list: ")
            name = input("Please enter your name to be added to the family list: ")
            family.append(name)
            print(family)
            break
print(" Thank you for entering your name  .")

       



# while friends:
#     if user_name not in friends:
#     # print(" please add your friends to the friends list")
#         answer = input(" Are you friend or family ? ")
#         if answer == "friend":
#             name = input(" Please enter your name to be added to the friends list : ")
#             friends.append(name)
#             print(friends)
#             print("You have been added to the friend list.")
#             # answer = input("Enter yes or no : ")
            

    # if user_name not in family:
    # # print(" please add your friends to the friends list")
    #     name = input(" Please enter your name to be added to the friends list : ")
    #     family.append(name)
    #     print(family)
    #     print("You have been added to the friends list.")

# while user_name  not in  friends:
#     question = input("Can you please enter your name if it's not on the list ? ")

#     if answer













    
    

    