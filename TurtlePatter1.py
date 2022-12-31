import turtle
skk=turtle.Turtle()

def circle():
    skk.down()
    skk.fillcolor("Pink")
    skk.begin_fill()
    skk.circle(60)
    skk.end_fill()

# We find the 50% of the x axis is of length 700px and y axis is of 370px


skk.up()
skk.goto(0,-100)
circle()
skk.up()
skk.goto(0,100)
skk.goto(640,240)
circle()

skk.up()
skk.goto(0,100)
skk.goto(0,0)
skk.goto(-640,240)
skk.down()
circle()

skk.up()
skk.goto(0,100)
skk.goto(0,0)
skk.goto(-640,-350)
skk.down()
circle()

skk.up()
skk.goto(0,100)
skk.goto(0,0)
skk.goto(640,-350)
skk.down()
circle()

