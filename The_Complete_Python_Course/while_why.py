the_force = input('Do you believe you in the force ? (yes/no): ')


while the_force:
    print('May the force  be with you !')

    the_force = input('Do you believe in the force ? (yes/no): ')
     
    if the_force == "yes": 
        print("The force will guide you !")

    else:
        print('If Once You Start Down The Dark Path, Forever Will it Dominate Your Desitny!')

    if the_force == "no":
       print('Intiate Order 66 !')
    else:
        print('You were the chosen one !')

    break

print('The Force is strong in this one !')
    