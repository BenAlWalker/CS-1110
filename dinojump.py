# Ben Walker, baw3hg

import gamebox
import pygame
import random

camera = gamebox.Camera(800, 600)

score = 0

jump = False
dino_velocity = 10
ticker = 0
mass = 1
game_on = False
walls = [
    gamebox.from_color(400, 600, "green", 1000, 20)
]

sheet = gamebox.load_sprite_sheet(
    "https://offline-dino-game.firebaseapp.com/200-offline-sprite-bday.b5693bb4.png",
    1, 10)

dino = gamebox.from_image(50, 540, sheet[2])
dino.scale_by(0.6)

cactus1 = gamebox.from_image(900, 540,
                             "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd"
                             "/Carnegiea_gigantea_in_Saguaro_National_Park_near_Tucson%2C_Arizona_during_November_"
                             "%2858%29.jpg/1200px-Carnegiea_gigantea_in_Saguaro_National_Park_near_Tucson"
                             "%2C_Arizona_during_November_%2858%29.jpg")
cactus1.scale_by(0.05)
cactus2 = gamebox.from_image(1200, 565, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd"
                                        "/Carnegiea_gigantea_in_Saguaro_National_Park_near_Tucson"
                                        "%2C_Arizona_during_November_%2858%29.jpg/1200px"
                                        "-Carnegiea_gigantea_in_Saguaro_National_Park_near_Tucson"
                                        "%2C_Arizona_during_November_%2858%29.jpg")
cactus2.scale_by(0.03)


def tick(keys):
    global score
    global jump
    global dino_velocity
    global mass
    global game_on


    if game_on is not True:
        if pygame.K_SPACE in keys:
            score = 0
            cactus1.x = random.randint(900, 1200)
            cactus1.y = 540
            cactus2.x = random.randint(1200, 1500)
            cactus2.y = 565
            game_on = True


    if pygame.K_SPACE in keys:
        game_on = True
        gamebox.unpause()

    if game_on:
        if pygame.K_SPACE in keys and dino.y == 540:
            jump = True
        if jump:
            force = 0.5 * mass * dino_velocity ** 2
            dino.y -= force
            dino_velocity = dino_velocity - 1
            if dino_velocity < 0:
                mass = -1
            if dino.y == 540:
                jump = False
                dino_velocity = 10
                mass = 1

        number = random.randint(0, 2)
        if number == 1:
            dino.image = sheet[0]
        if number == 0:
            dino.image = sheet[2]

        cactus1.move(-15, 0)
        cactus2.move(-15, 0)

        if cactus1.contains(-50, 540):
            dist = random.randint(900, 1200)
            cactus1.move(dist, 0)

        if cactus2.contains(-20, 565):
            dist = random.randint(1200, 1500)
            cactus2.move(dist, 0)

        if cactus1.touches(cactus2):
            cactus1.move(500, 0)

        if cactus2.touches(cactus1):
            cactus2.move(500, 0)


        score += 1

    camera.clear("black")
    camera.draw(gamebox.from_text(400, 50, str('Score: ' + str(score)), 50, "Red", bold=True))

    # Draw all the walls
    for wall in walls:
        camera.draw(wall)


    camera.draw(dino)
    camera.draw(cactus1)
    camera.draw(cactus2)


    if dino.touches(cactus1) or dino.touches(cactus2):
        camera.draw(gamebox.from_text(400, 100, "You Lost!", 40, "Yellow", bold=False))
        game_on = False



    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
