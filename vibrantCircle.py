import turtle as t

screen = t.Screen()
screen.bgcolor("black")

tim = t.Turtle()

tim.pencolor('silver')
a = 0
b = 0
tim.speed(0)
tim.penup()
tim.goto(0,200)
tim.pendown()
while True:
    tim.forward(a)
    tim.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle()


screen.exitonclick()