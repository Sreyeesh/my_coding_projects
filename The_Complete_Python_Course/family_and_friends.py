"""
Project: Python Program to see whether family or friends

Author : Sreyeesh Garimella

Date: 6/14/21


"""

print(' Hello Harry Potter These are your family and friends: ')

friends = ["Ron" , "Hermione"]
family = ["Lilly","James"]

user_name = input("Enter your name: ")

if user_name in friends: 
    print(user_name)
else:
    print ("you are a death eater")


