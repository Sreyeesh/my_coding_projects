import turtle

a = 5 
print(a)

b = "hello"
print(b)

numbers = 45454545432
print(numbers)

sreyeesh_turtle = turtle.Turtle()

def square():
    sreyeesh_turtle.forward(100)
    sreyeesh_turtle.right(90)
    sreyeesh_turtle.forward(100)
    sreyeesh_turtle.right(90)
    sreyeesh_turtle.forward(100)
    sreyeesh_turtle.right(90)
    sreyeesh_turtle.forward(100)

# square()
# sreyeesh_turtle.forward(200)
# square()


# elephant_weight = 3000
# print(elephant_weight)

# ant_weight = 0.1 
# print(ant_weight)

# if elephant_weight < ant_weight:
#     square()
# else:
#     sreyeesh_turtle.forward(100)

# sreyeesh = "happy"
# while sreyeesh == 'sad':
    # sreyeesh_turtle.forward(10)

for count in range(4):
    sreyeesh_turtle.forward(4)
    square()

input()