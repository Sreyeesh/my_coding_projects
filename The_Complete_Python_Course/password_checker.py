"""
project: making password checker
author: Sreyeesh Garimella
"""

# user_name = input('Hello What is your name ? ')
# user_password = input('Please input your password')
#
# print('Thank you for inputting your user name and password ')
# show_password = input('would you like to show your password ? ')
# if show_password == 'yes':
#     print(show_password)
# for password in user_password:
#     print()
# if user_password in user_password:
#     password = []
#     print('password has been stored ')
#
# show_password = input('Would you like to see  your password? Please type yes or no')
#
# answer_one = 'yes'
# answer_no = 'no'
#
# if answer_one in show_password:
#     print(password)
# if answer_no in show_password:
#     print('password will not be shown')


user_list = ["Tom", "Jose", "Anna"]

username = input("Please enter your name: ")

if username in user_list:
    print(f"Hi {username}! Welcome back")
elif len(username) > 0:
    user_list.append(username)
    print(f"Hi {username}! Welcome to the club!")

print("\n\nHere's a list of our users:")

for user in user_list:
    print(user)