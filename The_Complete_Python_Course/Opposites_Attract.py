"""

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

"""

#picked a flower each
flower1 =  range(2,13)
flower2 =  range(1,10)

def lovefunc(flower1,flower2):
    
    # for petal in flower1:
                 
    #     if petal % 2 == 0:
    #         print('even petals on flower 1: ',petal)
    #     else: 
    #         print('odd petals in flower 1: ',petal)
    
           
    # for petal in flower2: 
        
    #     if petal % 2 == 0: 
    #         print('even list of petal on flower 2: ', petal)        
    #     else: 
    #         print('odd petals in flower 2: ', petal)
    
            
    # return (flower1 + flower2) % 2 == 1

    
            
            
    # flower_1 = flower1 % 2 == 0
    # flower_2 = flower2 % 2 == 0
    
    # if(flower_1 and not flower_2) or (not flower_1 and flower_2):
    #             return True  # They are in Love
      
    # return False  # They are not in False
    for petal1 in flower1:
        for petal2 in flower2:
            if petal1 % 2 == 0 and petal2 % 2 == 1  or petal2 % 2 == 0 and petal1 % 2 ==1: 
                return True
                # print('flower one petals picked ',petal1,' petals pick  ', petal2,'Timmy and Sarah are in love')
                
            # else:
            return False
            # print('flower one petals picked ',petal1,' petals pick  ', petal2,'Timmy and Sarah are not  in love')
                
    

            
  
      
print(lovefunc(flower1,flower2))     

