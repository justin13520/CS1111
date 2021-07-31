import pygame
import gamebox
import random
# ================================================================================================
# Final Projects: Boggle by Patrick Bruns and Justin Liu (prb9hyg and jl8wf)
# Description: Mario and Bowser compete for coins on platforms that are slowly falling down
# toward lava. This game is a game of endurance, maneuverability, and luck.
# Optional Features:
#   1. scrolling
#   2. Two players at the same time
#   3. Enemies: Bowser (player 2) is able to push Mario (player 1) but Mario can not push Bowser. Criteria for enemy was able to move and hostile
#   4. Collectibles
#   5. Timer: once it hits a minute, whoever has the most points win
# ================================================================================================

camera = gamebox.Camera(900, 600)
player1 = gamebox.from_image(100,150,'Mario.png')
player2 = gamebox.from_image(200,250,'Bowser.png')
player1.yspeed = 0
player2.yspeed = 0
platforms = [
    gamebox.from_color(550, 250, 'black', 150, 15),
    gamebox.from_color(75, 200, "black", 150, 15), #mario on this one
    gamebox.from_color(300, 150, "black", 150, 15),
    gamebox.from_color(550, 25, "black", 150, 15),
    gamebox.from_color(300, 300, 'black', 150, 15),#bowser on this on
    gamebox.from_color(750,300,'black',150,15)
]
coins = [
    gamebox.from_color(600,15,'yellow',10,10),
    gamebox.from_color(240,200,'yellow',10,10)
]
lava = gamebox.from_color(0,600,'red',2000,40)
game_on = False
camera.clear("white")

#start screen
ID = gamebox.from_text(450,100,'Justin Liu: jl8wf and Patrick Bruns: prb9hyg', 50, 'red')

instructions = gamebox.from_text(450,200,'Player 1 uses W for up, A for left, and D for right.', 50, 'red')
instructions1 = gamebox.from_text(450,250,'Player 2 uses up, left, and right keys.', 50, 'red')
instructions2 = gamebox.from_text(450,300, 'Space when a player dies to restart.', 50, 'red')
instructions3 = gamebox.from_text(450,350,'There is a timer of one minute.',50,'red')
instructions4 = gamebox.from_text(450,400,'Most points win when time is up.',50,'red')
start = gamebox.from_text(450,450,'Press space to start',50,'red')

camera.draw(ID)
camera.draw(instructions)
camera.draw(instructions1)
camera.draw(instructions2)
camera.draw(instructions3)
camera.draw(instructions4)
camera.draw(start)
camera.display()

timer = 0
count = 0
score1 = 0
score2 = 0
#make coins and platform always move downward
for platform in platforms:
    platform.yspeed = 2
for coin in coins:
    coin.yspeed = 2

def tick(keys):
    # get access to the counter
    global score1
    global score2
    global game_on
    global timer
    global count
    if game_on == False:
        if pygame.K_SPACE in keys:
            # turns game on
            game_on = True
            #reset mechanic, positions everything to where they used to be
            player1.x = 120
            player1.y = 150
            player2.x = 200
            player2.y = 250
            player1.yspeed = 0
            player2.yspeed = 0
            score1 = 0
            score2 = 0
            platforms[0].x = 550
            platforms[0].y = 250

            platforms[1].x = 75
            platforms[1].y = 225

            platforms[2].x = 300
            platforms[2].y = 150

            platforms[3].x = 550
            platforms[3].y = 25

            platforms[4].x = 240
            platforms[4].y = 300

            platforms[5].x = 750
            platforms[5].y = 300

            coins[0].x = 600
            coins[0].y = 10
            coins[1].x = 270
            coins[1].y = 100

            timer = 0
    if game_on:
        #controls for left and right
        if pygame.K_d in keys:
            player1.x += 10
        if pygame.K_a in keys:
            player1.x -= 10
        if pygame.K_RIGHT in keys:
            player2.x += 10
        if pygame.K_LEFT in keys:
            player2.x -= 10

        #gravity
        player1.yspeed += 1
        player2.yspeed += 1
        player1.y = player1.y + player1.yspeed
        player2.y = player2.y + player2.yspeed
        camera.clear("green")
        camera.draw(player1)
        camera.draw(player2)

        #allows bowser to push mario
        player1.move_to_stop_overlapping(player2)

        for platform in platforms:
            #actually moves the platforms to make it look like scrolling screen
            platform.move_speed()
            if player1.bottom_touches(platform):
                #so it doesnt keep falling, no glitching
                player1.yspeed = 0
                if pygame.K_w in keys:
                    #makes it so can jump only when touching a platform
                    player1.yspeed = -20
            if player2.bottom_touches(platform):
                #so it doesnt keep falling, no glitching
                player2.yspeed = 0
                if pygame.K_UP in keys:
                    # makes it so can jump only when touching a platform
                    player2.yspeed = -20
            if player1.touches(platform):
                # so it doesn't fall through
                player1.move_to_stop_overlapping(platform)
            if player2.touches(platform):
                # so it doesn't fall through
                player2.move_to_stop_overlapping(platform)
            camera.draw(platform)

        #makes infinite platforms. Once it hits the lava, it'll respawn higher
            if platform.y > 600:
                platform.y -= random.randint(400,500)
        #coins
        for coin in coins:
            #actually moves the coins
            coin.move_speed()
            if player1.touches(coin):
                #mechanics of getting the coin. Once it touches it, the coin will move.
                score1 += 1
                coin.x = platforms[random.randint(0,5)].x + 25
                coin.y = platforms[random.randint(0,5)].y - 20
            if player2.touches(coin):
                # mechanics of getting the coin. Once it touches it, the coin will move.
                score2 += 1
                coin.x = platforms[random.randint(0,5)].x + 25
                coin.y = platforms[random.randint(0,5)].y - 20
            if coin.y > 600:
                #if a coin spawns and no one gets it, the coin will respawn on a new platform after it touches the lava
                coin.x = platforms[random.randint(0, 5)].x + 25
                coin.y = platforms[random.randint(0, 5)].y - 20
            camera.draw(coin)
        #scores
        camera.draw(gamebox.from_text(50, 50, str(score1), 40, 'black'))
        camera.draw(gamebox.from_text(800, 50, str(score2), 40, 'black'))
        #death mechanics
        if player2.y > 600:
            #turns game off
            game_on = False
            gg1 = gamebox.from_text(450,300,'Player 2 died',40,'red')
            camera.draw(gg1)
        if player1.y > 600:
            # turns game off
            game_on = False
            gg = gamebox.from_text(450,300,'Player 1 died',40,'red')
            camera.draw(gg)

        #timer
        count += 1
        camera.draw(gamebox.from_text(450, 50, 'timer: '+str(timer), 40, 'blue'))

        #timer mechanics
        #once it hits a minute, whoever has more point wins
        if count % 30 == 0:
            timer += 1
            if timer == 61:
                game_on = False
                if score1 > score2:
                    camera.draw(gamebox.from_text(450,300,'Player 1 wins',40,'red'))
                elif score1 < score2:
                    camera.draw(gamebox.from_text(450,300,'Player 2 wins',40,'red'))
                else:
                    camera.draw(gamebox.from_text(450, 300, 'Same points, huh? Well, the game wins I guess.', 40, 'red'))
        camera.draw(lava)
        camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
