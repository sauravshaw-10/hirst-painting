# import colorgram
import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)

# colors = colorgram.extract("image.jpg",30)

# def extract_color():
#     image_color = []
#     for i in range(30):
#         color_list = colors[i]
#         rgb_color= color_list.rgb
#         r = rgb_color.r
#         g = rgb_color.g
#         b = rgb_color.b
#         t = (r, g, b)
#         image_color.append(t)
#     print(image_color)
#
# extract_color()

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]



# tim.color(random.choice(color_list))
# tim.dot(20)
# tim.penup()
x = -250
y = -250
pacing = 50
instance = 0
climb = 0
steps = int(500/pacing)

tim.hideturtle()
tim.penup()
tim.setposition(x, y)


def x_move():
    global instance
    for x_position in range(steps):
        tim.color(random.choice(color_list))
        tim.setx(x+(pacing*instance))
        tim.dot(20)
        instance += 1
    instance = 0
    tim.setx(x)


def y_move():
    global climb
    tim.sety(y+(pacing*climb))
    climb +=1


while climb < 10:
    y_move()
    x_move()


# tim.showturtle()
# tim.color(random.choice(color_list))
# tim.setposition(0,50)
# tim.dot(20)








my_screen = Screen()
my_screen.exitonclick()



