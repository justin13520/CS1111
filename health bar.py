# basic platformer game w/ healthbar
# modified from example by Prof. Mark Sherriff
import pygame
import gamebox

camera = gamebox.Camera(800,600)

character = gamebox.from_color(50, 50, "green", 15, 40)
character.yspeed = 0

ground = gamebox.from_color(-100, 600, "black", 3000, 100)

walls = [
    ground,
    gamebox.from_color(500,500, "black", 50, 10),
    gamebox.from_color(450,450, "black", 50, 10)
]

coins = [
    gamebox.from_color(400, 400, "yellow", 12, 12),
    gamebox.from_color(200, 500, "yellow", 12, 12)
]

badguys = [
    gamebox.from_color(500,400, "red", 40, 40)
]

score = 0

# setup how much health you want to start with (it's all relative though)
current_health = 100

def tick(keys):
    global score
    # set it so you can access the health
    global current_health

    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    character.yspeed += 1
    character.y = character.y + character.yspeed
    camera.clear("blue")
    camera.draw(character)

    for badguy in badguys:
        badguy.yspeed += 1
        badguy.y += badguy.yspeed

        if character.x < badguy.x:
            badguy.x -= 3
        if character.x > badguy.x:
            badguy.x += 3

        if badguy.touches(character):
            # now when badguy touches you, decrease the healthbar
            current_health -= 1
            if current_health <= 0:
                camera.draw(gamebox.from_text(300, 300, "DEAD", 70, "red"))
                # this line will end the game
                gamebox.pause()


        # draw the health bar
        health_bar = gamebox.from_color(400, 50, "red", current_health*2, 30)
        camera.draw(health_bar)

        for wall in walls:
            if badguy.bottom_touches(wall):
                badguy.yspeed = 0
            if badguy.touches(wall):
                badguy.move_to_stop_overlapping(wall)
        camera.draw(badguy)


    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        camera.draw(coin)

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_UP in keys:
                character.yspeed = -15
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    score_display = gamebox.from_text(40, 40, str(score), 50, "red")
    camera.draw(score_display)

    camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
