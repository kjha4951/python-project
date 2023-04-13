import turtle
turtle.bgcolor("light blue")
turtle.pensize(4.5)
turtle.speed(0.5)
# turtle.bgpic("mod.gif")
color=["orange","white","green"]
for x in range(19):
    for i in color:
        turtle.color(i)
        turtle.circle(500)
        turtle.left(10)