""""
Project: Sorting Hat

Author: Sreyeesh Garimella

Date : 19/1/2020

"""



Howgwarts_Houses = ['Gryffindor','Slytherin','Hufflepuff','Ravenclaw']

students = []

Gryffindor = ['brave','daring','fire']
Slythern = ['cunning','ambitious','water']
Hufflepuff = ['just','loyal']
Ravenclaw = ['clever','witty', 'air']  

def sorting_hat_on_head():
    user_input =  input(" Enter you name to be added into the hat to be sorted: ")
    print("thank you for entering your name",user_input)

    #have student sorted to house by which characteristic they select
    
    while user_input !=  'm':
        if user_input == 'w':
            add_student_to_house()
        elif user_input == 't':
            teacher_can_sorted_students()

        
    


# def add_student_to_house():
    
    #append student to each house based on answer they give in pre-defined list

    #if correct answer is not provided they might be a muggle











# if __name__ == "__main__":
#     sorting_hat_on_head()



