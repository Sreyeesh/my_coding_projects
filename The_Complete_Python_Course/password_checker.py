"""
project: making password checker
author: Sreyeesh Garimella

"""

user_name = input('please enter your name: ')
user_list = []


if user_name not in user_list:
    print(f'Hello {user_name},welcome!')
elif len(user_name) > 0: # this is to calculate the length  of the list when users get added
    user_list.append(user_name)

print(f'thank you for entering your name please set your password next')

enter_password = input('please enter your password : ')
user_password = []

if enter_password  in user_password:
    user_password.append(enter_password)

print(f'thank you for entering your password ')


show_password = input(f'would you like to see your password : yes or no ?  ')

if show_password == 'no':
    print('password will not be shown')
else:
    print('this is your password',enter_password)


