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

enter_password = input(str('please enter your password : '))
user_password = []

if enter_password in user_password:
    user_password.append(enter_password)
print(f'thank you for entering your password ')

show_password = input(str(f'would you like to see your password : yes or no ?  '))
answer_no = 'no'
answer_yes = 'yes'

if answer_no in show_password:
    print('password will not be shown')

if answer_yes in show_password:
    if enter_password not in user_password:
        print('this is your password',enter_password)



