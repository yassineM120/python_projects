from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.backward(10)


def move_left():
    tom.left(10)

def move_right():
    tom.right(10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
