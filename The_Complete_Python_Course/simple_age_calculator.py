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

print(f' You have  lived for {seconds} seoncds so far.')

