'''
project : simple age calculator
author : Sreyeesh

'''

user_name = input(' What is your name ? ')

print(f'Hello, {user_name}')

user_age = input('What is your age: ')

user_age_number = int(user_age)

seconds = user_age_number * (365 * 24 * 60 * 60)

print(f'you have lived for {user_age_number * 12 } months.')

print(f' you lived for {seconds} seoncds so far.')

#
# name = input("Enter your name: ")
# print(f"Hello, {name}.")
#
# age = int(input("Enter your age: "))
#
# seconds = age * (365 * 24 * 60 * 60)
# print(f"You lived for {seconds} seconds so far.")