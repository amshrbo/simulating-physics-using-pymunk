import pygame as pyg 
import pymunk as pyk 
import sys

# Initializing pygame
pyg.init()
window = pyg.display.set_mode((600, 600))
clock = pyg.time.Clock()

# Initializing pymunk
space = pyk.Space()
space.gravity = (0, 100) # adding horizontal and vertical gravity

# Creating static circles
def static_ball(space, pos):
    #specifing the type of the body and the shape of it
    body = pyk.Body(body_type = pyk.Body.STATIC)
    body.position = pos
    shape = pyk.Circle(body, 50)    

    space.add(body, shape)

    return shape

def draw_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)

        pyg.draw.circle(window, (0,0,0), (pos_x, pos_y), 30)


# Creating a list of balls
balls = []
balls.append(static_ball(space, (170, 300)))
balls.append(static_ball(space, (300, 450)))


while True:
    # Chking for user inputs 
    for event in pyg.event.get(): 
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()

    # Filling the window back ground colour
    window.fill((217, 217, 217))


    # Drawing two static balls 
    draw_ball(balls)

    # Updating pymunk space inside pygame
    space.step(0.02)

    #Basic setup for pygame
    pyg.display.update() #Rendring the frame
    clock.tick(120) # limiting the frame to 120 seconds

