"""
project: making password checker
author: Sreyeesh Garimella

"""


user_name = input('please enter your name: ')
user_list = []

if user_name not in user_list:
    user_list.append(user_name)

enter_password = input('please enter your password : ')
user_password = []

if enter_password not in user_password:
    user_password.append(enter_password)

print(f'thank you for entering your name please set your password next')

show_password = input(f'would you like to see your password : yes or no ?  ')

if show_password == 'no':
    print('password will not be shown')
else:
    print('this is your password',enter_password)

show_user_list = input('would you like to view  list of users: yes or no ')

if show_user_list == 'no':
     print('not showing list of users')
else:
  print('will show users')

  for users  in user_list:
        print(f' this is the list of users {user_name},{user_list}')


show_user_password = input('would you like to view  list of users and the passwords : yes or no ')

if show_user_password == 'no':
    print('not showing list of users')
else:
    print('will show users')

    for passwords  in user_password:
        print(f' this is the list of users name and passwords  name :{user_name}, user name: {user_list},user password : {user_password}')




