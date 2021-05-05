"""

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

"""

flower1 =list(range(10))

#don't have two lists  with identical numbers try to use one list 

flower2 = list(range(1,11))


def lovefunc( flower1, flower2 ):
    for p in flower1 and flower2: #fix the for loop 
        # print(f'this the number of even petals in flower 1:',p)
        
        if(p %2 ) == 0:
            print(f'petal in flower1 is even',p)
            print('they are in love')
            # return True
            
        else:
            print(f'petal in flower2  is odd',p) 
            # return False
           
               
        if(p %2 )  != 0:
            print(f'they are not in love',p)
            # return False

lovefunc(flower1,flower2)


