import turtle

# if __name__ == '__main__':
#
#     turtle.title('Hi! I\'m Bob the turtle!')
#     turtle.setup(width=800, height=800)
#
#     bob = turtle.Turtle(shape='turtle')
#     bob.color('orange')
#
#     # Drawing a square
#     bob.forward(100)
#     bob.right(90)
#     bob.forward(100)
#     bob.right(90)
#     bob.forward(100)
#     bob.right(90)
#     bob.forward(100)
#
#     turtle.exitonclick()


# Python program to draw square
#   using Turtle Programming
#   import turtle

skk = turtle.Turtle()
for i in range(4):
    skk.forward(50)
    skk.left(90)
turtle.done()


# Python program to draw star
# using Turtle Programming
# import turtle

# star = turtle.Turtle()
# star.right(75)
# star.forward(100)
# for i in range(4):
#     star.right(144)
#     star.forward(100)
# turtle.done()




# ******************************    Info about this turtle Module    ******************************************

# help(turtle)          # This statement gives all info about turtle module
# help(turtle.shape)    # This statement gives all info about turtle shape

# help(turtle.color)    # gives all info about color of turle and line color

# turtle.color          # This statement display current color of (line, actual turtle)

# turtle.color("red")    # change the color of line as well as turtle

# turtle.color("red", "blue")     # This statement will make line color as red and turtle color as blue

# You can even use color by RGB i.e. turtle.color(50,60,120).....
# But before this we need to change our color mode
# Before our color mode was 1 .... For RGB we will make it as 255
# Hence type turtle.colormode(255)

# for changing background we will name the screeen of turtle... and then change bgcolor
# hh=turtle.Screen()
# hh.bgcolor("Black")


# Even we can change the name of the turtle tab
# If we run this code.... The new tab will open and the name of it will be "Python turtle graphic"
# So for changing the name of it...
# wn=turtle.Screen()      # WE will name that screen as wn stands for window
# wn.title("TITLE")

# For changing the color of background
# wn=turtle.Screen()     # WE will name that screen as wn stands for window
# wn.bgcolor("blue")
# WE can even change the color by RGB ... for that first set the color mode to 255
# turtle.colormode(255)
# turtle.color(50,60,120)

# For changing the background picture:
# wn.bgpic("sample.gif")
# Now here image must be in gif format...(can be done using paint... open image in paint and save as..and put "save as type" as "gif")
# and image must be in same folder
# For finding the current image on turtle tab...type:   wn.bgpic()



