import turtle
# create a turtle
franklyn = turtle.Turtle()
franklyn.shape('turtle')
franklyn.speed('slowest')
# make the paint pink
franklyn.color('pink')

# Repeat for 4 times:
#   move forward by 200
#   turn left by 90 degrees

sides = 4

#square
for i in range(sides):  # repeat 4 times
    franklyn.forward(100)
    franklyn.left(360/sides)

sides = 5
# pentagon
for i in range(sides):  # repeat 5 times
    franklyn.forward(100)
    franklyn.left(360/sides)

# septagon
for i in range(7):  # repeat 3 times
    franklyn.forward(100)
    franklyn.left(360/7)

for i in range(10):
    for j in range(4):
        franklyn.forward(100)
        franklyn.left(90)


turtle.done()