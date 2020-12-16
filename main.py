# This program uses Turtle GUI to mimic Hirst painting.
# Written on: Dec 15, 2020

"""
You can draw any type you like by tweaking position, distance and direction.
"""

import colorgram
import turtle as t
import random

# Create an empty list to store extracted (r, g, b) colors.
rgb_colors = []
# Use cologram extract function to get desired number of color combinations.
colors = colorgram.extract('image.jpg', 40)
# Using for loop, add combinations to color list.
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
# print(rgb_colors)

t.colormode(255)
jack = t.Turtle()
jack.speed("fastest")

# If you want to see how it is drawn, comment out penup() and hideturtle().
jack.penup()
jack.hideturtle()
# color_list = [(246, 240, 227), (249, 237, 244), (233, 247, 239), (235, 240, 248), (203, 150, 113), (57, 97, 134),
#               (144, 68, 89), (228, 217, 107), (150, 78, 64), (132, 166, 190), (192, 143, 159), (34, 20, 14),
#               (19, 26, 43), (205, 89, 74), (202, 77, 97), (130, 178, 149), (47, 23, 33), (49, 125, 94), (12, 24, 17),
#               (73, 162, 112), (229, 169, 183), (171, 166, 53), (233, 171, 162), (115, 39, 60), (47, 55, 102),
#               (228, 221, 9), (164, 210, 184), (50, 159, 183), (110, 122, 158), (103, 47, 41)]

# Get to the starting position.
jack.setheading(225)
jack.fd(250)
jack.setheading(0)

# Desire drawing style is 10 dots per line for 10 lines.
number_of_dots = 100

# Add 1 to number_of_dots so that last dot will be drawn.
for dot_count in range(1, number_of_dots+1):
    # Get random color for each dot.
    jack.dot(20, random.choice(rgb_colors))
    # This is the distance between each dot.
    jack.fd(50)
    # After drawing 10 dots, get turtle or cursor to starting position one line above.
    if dot_count % 10 == 0:
        jack.setheading(90)
        jack.fd(50)
        jack.setheading(180)
        jack.fd(500)
        jack.setheading(0)

screen = t.Screen()
screen.exitonclick()
