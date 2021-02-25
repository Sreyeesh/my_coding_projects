"""
project: making password checker
author: Sreyeesh Garimella

"""

user_name = input('please enter your name: ')
user_list = []

enter_password = input('please enter your password : ')
user_password = []

if enter_password  in user_password:
    user_password.append(enter_password)

print(f'thank you for entering your name please set your password next')

show_password = input(f'would you like to see your password : yes or no ?  ')

if show_password == 'no':
    print('password will not be shown')
else:
    print('this is your password',enter_password)




#TODO: Iterate through the user list to show users that have signed up


#TODO: have users reset password

