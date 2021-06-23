user_menu = input('please enter p or q: ')

while user_menu != 'q':  #run the code below as long as the user doesn't hit the letter q  that's what != means

    if user_menu == 'p':

        print('Hello')
    else:
        print('wrong selection')

    user_menu = input('please enter p or q to continue:')

print('quitting program')