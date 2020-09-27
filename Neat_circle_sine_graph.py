import turtle
import math
import time

frequency = 0

step = 0
repeat = 1
wave_y = 0
xpos = 0
ypos = 0
radius = 200
amplitude = 100
stepsize = math.pi / 180

#First step size: 0.00872664625 (2 pi / 720)
#Second stepsize: 0.00436332312 (2 pi / 1440)


#This messy shit here is just to fix the problem that the program starts drawing from the center, so I don't want a line from center to step 1

turtle.penup()

#Basically, the radius of the circle constantly changes according the the y value of a cosine graph, creating a circular cosine wave

#Scale is the base radius
#Wave_intensity is the scale of the wave (so I can have a more or less pronounced wave)
#Frequency is the number of oscillations in a revolution
wave_y  = radius + (math.cos((step - 180) * frequency) * amplitude)

#The stepsize should be self-explanitory
step = step + stepsize

#For some reason, zero is the fastest speed (I guess zero means zero intentional delay)
turtle.speed(0)

#These 2 commands prevents the screen from refreshing, so the program doesn't have to refresh the whole screen every time for one movement
turtle.tracer(0)
#I defined the x and y values as variables cause I need to implement the circle formula, which I don't think python would like in the turtle.goto statement itself
xpos = wave_y * math.cos(step)
ypos = wave_y * math.sin(step)
turtle.goto(xpos, ypos)

turtle.update()

turtle.pendown()

while step <= math.pi * 2:

    #Basically, the radius of the circle constantly changes according the the y value of a cosine graph, creating a circular cosine wave

    #Scale is the base radius
    #Wave_intensity is the scale of the wave (so I can have a more or less pronounced wave)
    #Frequency is the number of oscillations in a revolution
    wave_y  = radius + (math.cos((step - 180) * frequency) * amplitude)

    #The stepsize should be self-explanitory
    step = step + stepsize

    turtle.speed(0)

    #These 2 commands prevents the screen from refreshing, so the program doesn't have to refresh the whole screen every time for one movement
    turtle.tracer(0)
    #I defined the x and y values as variables cause I need to implement the circle formula, which I don't think python would like in the turtle.goto statement itself
    xpos = wave_y * math.cos(step)
    ypos = wave_y * math.sin(step)
    turtle.goto(xpos, ypos)

#This command updates the screen, otherwise it'll draw nothing
turtle.update()
