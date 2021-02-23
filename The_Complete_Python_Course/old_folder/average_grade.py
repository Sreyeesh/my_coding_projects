"""
Project: Calulate Averag Grade

Author : Sreyeesh Garimella 
Date: 11/5/2020

"""


# my_student = {
#     'name': ' Harry Potter',
#     'grades': [70, 88, 90, 99],
#     'average': None
# }


# def average_grade(student):
#     return sum(student['grades']) / len(student['grades'])

# print(average_grade(my_student))


# class Student: 
#     def __init__(self,new_name, new_grades):  #dunder init method
#         self.name = new_name
#         self.grades = new_grades

#     def average(self): 
#         return  sum(self.grades) / len(self.grades)


# student_one = Student('Harry Potter', [70, 88, 90, 99])  

# print(student_one.name)

# my_student = {  #  this is a dictinoary
#     'name': ' Harry Potter', #name is the key,  #Harry Potter is the value
#     'grades': [70, 88, 90, 99] #grades is the key,  #numbers are the value

# }

# # average_vals = [grade for grade in my_student.items() if grade != 0] # average values has a list comphriension
 
# print(average_vals)
# average = sum(average_vals) / len(average_vals)
# print(average)

# # print(str(average))

my_student = {  #  this is a dictinoary
    'name': ' Harry Potter',
    'grades': [70, 88, 90, 99] 
}

def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

print(average_grade(my_student))

# average_vals = [grade for grade in my_student["grades"]if grade = grades]
# average_vals = [grade for grade in my_student["grades"]]

# print(str(average_vals))

# # print(average)
