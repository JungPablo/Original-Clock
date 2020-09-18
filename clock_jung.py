import turtle
import winsound
import time


# Variables declaration
title = 'Original Clock'
name = 'Clock by @jungyeunjae'
bgcolor = '#35682d' # Background color
width = 800 # Setup
height = 600 # Setup
font = 'Courier'
tracer = 0
speed = 0
color = 'white' # Text color

color_title = 'white'
color_big = 'yellow' # Big text color
synch = .98 # Clock synchronization
circle_size = 1 # Circle size (Reference)
small = 1 # Circle size (small)
medium = 1.5 # Circle size (medium)
large = 2 # Circle size (large)

wnds = turtle.Screen()
wnds.register_shape('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\cover.gif')
wnds.bgpic('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\cover.gif')
wnds.title(name)
wnds.bgcolor(bgcolor)
wnds.setup(width=width, height=height)
wnds.tracer(tracer)

# Pen
pen = turtle.Turtle()
pen.shape('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\cover.gif')
pen.speed(speed)
pen.color(color)
pen.penup()
pen.hideturtle()
pen.goto(0, 0) # start point

# x and y position for each number (0 to 9)
nbr_list = [[0, 100], [59, 81], [95, 31], [95, -31], [59, -81], [0, -100], [-59, -81], [-95, -31], [-95, 31], [-59, 81]]

# Print Title function
def print_title(text):
    pen.goto(0, 250)
    pen.color(color_title)
    pen.write(text, align='center', font = (font, 20, 'bold', 'underline'))

# Print number function
def print_nbr(nbr, x, y, font_name, font_size, font_type, font_color):
    pen.goto(x, y)
    pen.color(font_color)
    pen.write('{}'.format(nbr), align='center', font = (font_name, font_size, font_type))

# Print selector circle size function
def print_selector(nbr, ccl_size):
    itr = 0
    for i in nbr_list:
        if itr != nbr:
            print_nbr(itr, (nbr_list[itr][0]) * ccl_size, (nbr_list[itr][1]) * ccl_size, font, 20, 'normal', color)
        else:
            print_nbr(itr, (nbr_list[itr][0]) * ccl_size, (nbr_list[itr][1]) * ccl_size, font, 30, 'bold' , color_big)
        itr += 1


#--------------------------------
#               Main
#--------------------------------


#-------------------
#   Countdown
#-------------------
pen.goto(0, 250)
pen.color('white')
i = 5
while i > 0:
    pen.write('{}'.format(i), align='center', font = (font, 30, 'normal'))
    winsound.PlaySound('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\tick.wav', winsound.SND_ASYNC)
    time.sleep(synch)
    pen.clear()
    i -= 1

#-------------------
#   Start Clock
#-------------------
while True:
    nbr = 1
    while nbr < len(nbr_list):
        print_title(title)
        print_selector(nbr, circle_size * small)
        winsound.PlaySound('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\tick.wav', winsound.SND_ASYNC)
        time.sleep(synch)
        nbr += 1
        pen.clear()
    nbr = 10
    while nbr < len(nbr_list) * 10:
        print_title(title)
        tens = nbr // 10
        unit = nbr % 10
        print_selector(tens, circle_size * small)
        print_selector(unit, circle_size * medium)
        if unit == 0:
            winsound.PlaySound('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\bounce_wall.wav', winsound.SND_ASYNC)
        else:
            winsound.PlaySound('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\tick.wav', winsound.SND_ASYNC)
        time.sleep(synch)
        nbr += 1
        pen.clear()
    while nbr < len(nbr_list) * 100:
        print_title(title)
        hundreds = nbr // 100
        tens_x = nbr % 100
        tens = tens_x // 10
        unit = tens_x % 10
        print_selector(hundreds, circle_size * small)
        print_selector(tens, circle_size * medium)
        print_selector(unit, circle_size * large)
        if unit == 0:
            winsound.PlaySound('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\bounce_wall.wav', winsound.SND_ASYNC)
        else:
            winsound.PlaySound('C:\\Users\\acer\\Desktop\\Python Workspace\\Clock\\tick.wav', winsound.SND_ASYNC)
        time.sleep(synch)
        nbr += 1
        pen.clear()
wnds.update()