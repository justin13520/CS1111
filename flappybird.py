import pygame
import gamebox
import random
camera = gamebox.Camera(600,600)
bird = gamebox.from_color(300,300,'red',15,15)
bird.yspeed = 0
pipes = [
    gamebox.from_color(0,0,'green',50,200),
    gamebox.from_color(300,300,'green',50,400),
    gamebox.from_color(450,0,'green',50,300),
]
counter = 0

def tick(keys):
    global counter
    """
    gets access from keyboard
    :param keys: input method
    """
    if pygame.K_RIGHT in keys:
        bird.x += 10
    if pygame.K_UP in keys or camera.mouseclick:
        bird.yspeed = -20

    bird.yspeed += 1
    bird.y += bird.yspeed
    camera.clear('white')
    camera.draw(bird)
    #makes the screen scroll
    camera.x += 3
    #counter is used to generate the walls
    counter +=1
    camera.display()
    if counter %50 == 0:
        new_pipe = gamebox.from_color(random.randint(200,600),camera.y-200,'green',random.randint(250,600),200)
        pipes.append(new_pipe)

    for pipe in pipes:
        if bird.bottom_touches(pipe):
            print('Game Over')
            gamebox.pause()
        if bird.touches(pipe):
            bird.move_to_stop_overlapping(pipe)
        camera.draw(pipe)

    camera.draw(pipe)

gamebox.timer_loop(30,tick)