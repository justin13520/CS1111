import turtle


charlie = turtle.Turtle()
charlie.shape('turtle')
turtle.colormode(255)
charlie.color('green', 'yellow')
charlie.speed(0)
i=1
while True:
    charlie.forward(i)
    charlie.left(60)
    charlie.color((4*i+100)%255,(2*i)%255,(7*i+50)%255)
    i=i+1

turtle.done()
