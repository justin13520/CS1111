# Example of doing an animated sprite with a sprite sheet.
# Mark Sherriff animated sprite using a sprite sheet

import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# load a sprite sheet of 1 row and 22 columns
sheet = gamebox.load_sprite_sheet("http://estelle.github.io/10/files/sprite.png", 1, 22)
# sheet = gamebox.load_sprite_sheet("spiffy_dancer_from_estelle-github-io.png", 1, 22)

frame = 0
direction = 0
counter = 0
character = gamebox.from_image(200, 200, sheet[frame])  # gamebox image is first pic in sprite sheet


def tick(keys):
    global frame
    global direction
    global counter

    frame += 1
    counter += 1
    if frame == 10:
        frame = 0
    if counter % 2 == 0:  # control dancer speed by changing 1
        # character.image = sheet[frame+direction*10]
        character.image = sheet[frame]

    camera.clear("cyan")
    camera.draw(character)
    camera.display()


ticks_per_second = 10

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
