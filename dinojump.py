import pygame
import gamebox
import random
camera = gamebox.Camera(1000,600)
dino = gamebox.from_color(100,500,'red',15,30)
game_on = False #to turn the game on or off at start and after touching cactus
game_end = False #condition to start next game
day_time = True #condition to make it day or night

cactuses = [
    gamebox.from_color(500,510,'green',20,40),
    gamebox.from_color(300,500,'green',20,60),
    gamebox.from_color(700,520,'green',20,20),
    gamebox.from_color(900,520,'green',40,25)
]

sun_or_moon = gamebox.from_color(1000,0,'yellow',100,100)

ground = gamebox.from_color(0,600,'brown',2000,140)

#counter starts as 0
counter = 0

#default speed of cactus is three
for cactus in cactuses:
    cactus.xspeed = -4
#How to play: Press space bar to start. Cactus move towards dino
#to make the illusion the dino and camera are moving.
#Everytime it turns night, it accelerates.
# Press space after touching a cactus to restart.

camera.clear('white')

def tick(keys):
    global dino
    global counter
    global game_on
    global game_end
    global day_time

    #Before the game starts, game_on is set to false, making the game appear to not be moving
    #When the dino touches a cactus, there will display a game over, and then pressing the space bar will
    #restart the game.
    if game_on == False:
        if pygame.K_SPACE in keys:
            #turns game on
            game_on = True
            game_end = False

    #draws the cactus so that it doesn't appear without them on the start screen
    for cactus in cactuses:
        camera.draw(cactus)

    #makes sure that the dino doesn't glitch through the ground after jump
    if dino.bottom_touches(ground):
        dino.yspeed = 0
        #jumps only when it is touching the ground
        if dino.bottom_touches(ground) and pygame.K_UP in keys or pygame.K_SPACE in keys :
            dino.yspeed = -18


    #once the game turns on, the cactuses move
    if game_on:
        #counter is for points
        counter += 1
        if counter%200 == 0:
            #everytime counter is divisible by 200 and equals to 0, it turns night by making day_time = False
            if day_time == True:
                day_time = False
                for cactus in cactuses:
                    cactus.xspeed -= 1
                    #cactus.x += cactus.xspeed
            else:
                day_time = True
        if day_time:
            #turning daytime
            camera.clear('white')
            # shows the points and moves it along the screen with dino
            points = gamebox.from_text(dino.x, dino.y - 50, str(counter), 16, 'black')
            camera.draw(points)
        else:
            #turning night
            camera.clear('black')
            # shows the points and moves it along the screen with dino
            points = gamebox.from_text(dino.x, dino.y - 50, str(counter), 16, 'white')
            camera.draw(points)
        for cactus in cactuses:
            #draws each cactus and moves them
            camera.draw(cactus)
            cactus.move_speed()
            if cactus.x < 0:
                #once the cactus moves past the left screen, it'll be reset pass 900
                cactus.x = random.randint(600,1200)
            if dino.touches(cactus):
                #end game mechanic

                #turns game off
                game_on = False

                #resets it to be day in the next play
                day_time = True

                #resets it so that the next play through, the cactus doesn't spawn where dino is
                for cactus1 in cactuses:
                    cactus1.x += 400
                    cactus1.speedx = -4
                game_end = True
    if game_end:
        #says game over on screen and resets points
        camera.draw(gamebox.from_text(500, 300, "Game Over", 70, "red"))
        counter = 0

    #keeps the dino from falling through ground
    dino.move_to_stop_overlapping(ground)

    #Gravity
    dino.speedy += 1
    dino.move_speed()

    #draw everything and displays it
    camera.draw(ground)
    camera.draw(sun_or_moon)
    camera.draw(dino)
    camera.display()

    #To see if the cactus do accelerate towards dino
    for cactus in cactuses:
        print(cactus.speedx)

gamebox.timer_loop(30,tick)


