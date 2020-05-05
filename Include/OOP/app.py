# from Student file import Student class
from Student import Student

import turtle

student1 = Student("Landy", "Business", 3.1, False)

print(student1.name)

qazi_turtle = turtle.Turtle()


def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)


square()
qazi_turtle.forward(200)
square()



