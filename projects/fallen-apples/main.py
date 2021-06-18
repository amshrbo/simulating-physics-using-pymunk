import pygame as pyg 
import pymunk as pyk 
import sys

# Initializing pygame
pyg.init()
window = pyg.display.set_mode((800, 800))
clock = pyg.time.Clock()

# Initializing pymunk
space = pyk.Space()
space.gravity = (0, 200) # adding horizontal and vertical gravity

# Creating static circles
def static_ball(space, pos):
    #specifing the type of the body and the shape of it
    body = pyk.Body(body_type = pyk.Body.STATIC)
    body.position = pos
    shape = pyk.Circle(body, 20)    

    space.add(body, shape)

    return shape

def draw_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)

        pyg.draw.circle(window, (0,0,0), (pos_x, pos_y), 20)


# Creating a list of balls
balls = []
balls.append(static_ball(space, (170, 300)))
balls.append(static_ball(space, (300, 450)))


# Creaing apples 
def create_apple(space, pos):
    body = pyk.Body(1, 1000, body_type = pyk.Body.DYNAMIC)
    body.position = pos
    shape = pyk.Circle(body, 20)

    space.add(body, shape)

    return shape

# creating the apple image
green_apple = pyg.image.load('assets/apple.svg')
def draw_apple(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)

        apple_rect = green_apple.get_rect(center = (pos_x, pos_y))
        window.blit(green_apple, apple_rect)

apples = []
apples.append(create_apple(space, (305, 0)))


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
    draw_apple(apples)

    # Updating pymunk space inside pygame
    space.step(0.02)

    #Basic setup for pygame
    pyg.display.update() #Rendring the frame
    clock.tick(120) # limiting the frame to 120 seconds

