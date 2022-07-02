# Ben Walker, baw3hg

import gamebox
import pygame

level_one = False
level_two = False
time1 = 900
time2 = 900
camera = gamebox.Camera(800, 600)
character = gamebox.from_image(325.25, 225.25, "https://freepngimg.com/thumb/mario_bros/91876-square-art-bros-mario"
                                               "-allstars-super.png")
character2 = gamebox.from_image(474.75, 404.5, "https://freepngimg.com/thumb/mario_bros/91876-square-art-bros-mario"
                                               "-allstars-super.png")
character.width = 30
character2.width = 30

box1 = gamebox.from_color(355.25, 225.25, "brown", 27, 27)
box2 = gamebox.from_color(385.25, 255.25, "brown", 27, 27)
box3 = gamebox.from_color(385.25, 285.25, "brown", 27, 27)
box4 = gamebox.from_color(385.25, 345.25, "brown", 27, 27)
box5 = gamebox.from_color(355.25, 345.25, "brown", 27, 27)
box6 = gamebox.from_color(415.25, 345.25, "brown", 27, 27)
box7 = gamebox.from_color(295.25, 345.25, "brown", 27, 27)

win1 = gamebox.from_color(295.25, 225.25, "green", 15, 15)
win2 = gamebox.from_color(415.25, 255.25, "green", 15, 15)
win3 = gamebox.from_color(385.25, 315.25, "green", 15, 15)
win4 = gamebox.from_color(385.25, 375.25, "green", 15, 15)
win5 = gamebox.from_color(355.25, 345.25, "green", 15, 15)
win6 = gamebox.from_color(445.25, 345.25, "green", 15, 15)
win7 = gamebox.from_color(295.25, 285.25, "green", 15, 15)

win8 = gamebox.from_color(714.25, 345.25, "orange", 15, 15)
win9 = gamebox.from_color(714.25, 375.25, "purple", 15, 15)
win10 = gamebox.from_color(714.25, 404.25, "green", 15, 15)
win11 = gamebox.from_color(264.5, 194.75, "cyan", 15, 15)
win12 = gamebox.from_color(324.75, 194.75, "white", 15, 15)
win13 = gamebox.from_color(145.25, 375.25, "red", 15, 15)

box8 = gamebox.from_color(264.25, 374.25, "orange", 27, 27)  # win is win8
box9 = gamebox.from_color(174.25, 374.25, "red", 27, 27)  # win is win13
box10 = gamebox.from_color(264.5, 284.75, "purple", 27, 27)  # win is win9
box11 = gamebox.from_color(264.5, 224.75, "cyan", 27, 27)  # win is win11
box12 = gamebox.from_color(324.75, 254.75, "white", 27, 27)  # win is win12
box13 = gamebox.from_color(354.25, 285.25, "green", 27, 27)  # win is win10

collectible = gamebox.from_color(415.25, 195.25, "yellow", 10, 10)
collectible2 = gamebox.from_color(324.25, 435.25, "yellow", 10, 10)

boundaries = [
    gamebox.from_color(384.5, 150, "black", 330, 60.5),
    gamebox.from_color(384.5, 420, "black", 330, 60.5),
    gamebox.from_color(250, 285, "black", 60.5, 300),
    gamebox.from_color(520, 285, "black", 60.5, 300),
    gamebox.from_color(310, 195, "black", 60.5, 30.5),
    gamebox.from_color(310, 255, "black", 60.5, 30.5),
    gamebox.from_color(325, 300, "black", 30.5, 60.5),
    gamebox.from_color(340, 285, "black", 60.5, 30.5),
    gamebox.from_color(460, 255, "black", 60.5, 150.5),
    gamebox.from_color(475, 360, "black", 30.5, 60.5),
]

boundariesnew = [
    gamebox.from_color(430, 150, "black", 720.5, 60.5),
    gamebox.from_color(430, 480, "black", 720.5, 60.5),
    gamebox.from_color(100, 285, "black", 60.5, 330),
    gamebox.from_color(760, 285, "black", 60.5, 330),
    gamebox.from_color(189.5, 420, "black", 120, 60.5),
    gamebox.from_color(189.5, 225, "black", 120, 90.5),
    gamebox.from_color(159.5, 300, "black", 60.5, 60.5),
    gamebox.from_color(234.5, 330, "black", 30.5, 60.5),
    gamebox.from_color(324.5, 330, "black", 90.5, 60.5),
    gamebox.from_color(339.5, 405, "black", 120.5, 30.5),
    gamebox.from_color(444.5, 420, "black", 30.5, 60.5),
    gamebox.from_color(475, 435, "black", 30.5, 30.5),
    gamebox.from_color(549.5, 420, "black", 120, 60.5),
    gamebox.from_color(669.5, 435, "black", 120, 30.5),
    gamebox.from_color(369.5, 225, "black", 60.5, 90.5),
    gamebox.from_color(505, 270, "black", 210.5, 180.5),
    gamebox.from_color(669.5, 255, "black", 120.5, 150.5),
]


def tick(keys):
    global level_one
    global level_two
    global time1
    global time2
    global boundaries
    global boundariesnew
    camera.draw(gamebox.from_text(400, 100, "Please-A Move-A Da Box", 50, "Red", bold=False))
    camera.draw(gamebox.from_text(400, 300, "Press Space to Start", 40, "Yellow", bold=False))
    camera.draw(gamebox.from_text(400, 200, "Created by Ben Walker (baw3hg)", 40, "Yellow", bold=False))
    camera.draw(gamebox.from_text(400, 400, "Controls:", 30, "Yellow", bold=False))
    camera.draw(gamebox.from_text(400, 450, "WASD", 30, "Yellow", bold=False))
    camera.draw(gamebox.from_text(400, 475, "Press R to restart", 30, "Yellow", bold=False))
    camera.draw(gamebox.from_text(400, 525, "Win by moving the boxes to the green squares!", 45, "Red", bold=False))

    if pygame.K_SPACE in keys:
        level_one = True

    if pygame.K_y in keys:
        level_two = True

    if level_one:
        camera.clear("pink")
        camera.draw(gamebox.from_text(400, 75, "Level 1", 50, "Black", bold=True))
        camera.draw(gamebox.from_text(400, 475, "Press R to restart", 50, "Black", bold=False))
        camera.draw(gamebox.from_text(400, 525, "Press Y to go to Level 2", 50, "Black", bold=False))
        camera.draw(gamebox.from_text(650, 125, "Time Left: " + str(int(time1 / 30)), 35, "Black", bold=False))

        for each in boundaries:
            character.move_to_stop_overlapping(each)

        if pygame.K_r in keys:
            character.x = 325.25
            character.y = 222.25
            box1.x = 355.25
            box2.x = 385.25
            box3.x = 385.25
            box4.x = 385.25
            box5.x = 355.25
            box6.x = 415.25
            box7.x = 295.25
            box1.y = 225.25
            box2.y = 255.25
            box3.y = 285.25
            box4.y = 345.25
            box5.y = 345.25
            box6.y = 345.25
            box7.y = 345.25
            time1 = 900
            collectible.x = 415.25
            collectible.y = 195.25
        if pygame.K_w in keys:
            character.y -= 15
        if pygame.K_s in keys:
            character.y += 15
        if pygame.K_a in keys:
            character.x -= 15
        if pygame.K_d in keys:
            character.x += 15

        if character.touches(collectible):
            time1 += 150
            collectible.x += 1000
            collectible.y += 1000

        if character.top_touches(box1):
            box1.y -= 15
        if character.right_touches(box1):
            box1.x += 15
        if character.left_touches(box1):
            box1.x -= 15
        if character.bottom_touches(box1):
            box1.y += 15
        if character.top_touches(box2):
            box2.y -= 15
        if character.right_touches(box2):
            box2.x += 15
        if character.left_touches(box2):
            box2.x -= 15
        if character.bottom_touches(box2):
            box2.y += 15
        if character.top_touches(box3):
            box3.y -= 15
        if character.right_touches(box3):
            box3.x += 15
        if character.left_touches(box3):
            box3.x -= 15
        if character.bottom_touches(box3):
            box3.y += 15
        if character.top_touches(box4):
            box4.y -= 15
        if character.right_touches(box4):
            box4.x += 15
        if character.left_touches(box4):
            box4.x -= 15
        if character.bottom_touches(box4):
            box4.y += 15
        if character.top_touches(box5):
            box5.y -= 15
        if character.right_touches(box5):
            box5.x += 15
        if character.left_touches(box5):
            box5.x -= 15
        if character.bottom_touches(box5):
            box5.y += 15
        if character.top_touches(box6):
            box6.y -= 15
        if character.right_touches(box6):
            box6.x += 15
        if character.left_touches(box6):
            box6.x -= 15
        if character.bottom_touches(box6):
            box6.y += 15
        if character.top_touches(box7):
            box7.y -= 15
        if character.right_touches(box7):
            box7.x += 15
        if character.left_touches(box7):
            box7.x -= 15
        if character.bottom_touches(box7):
            box7.y += 15

        for each in boundaries:
            box1.move_to_stop_overlapping(each)
            box2.move_to_stop_overlapping(each)
            box3.move_to_stop_overlapping(each)
            box4.move_to_stop_overlapping(each)
            box5.move_to_stop_overlapping(each)
            box6.move_to_stop_overlapping(each)
            box7.move_to_stop_overlapping(each)

        for boundary in boundaries:
            camera.draw(boundary)

        time1 -= 1
        camera.draw(character)
        camera.draw(box1)
        camera.draw(box2)
        camera.draw(box3)
        camera.draw(box4)
        camera.draw(box5)
        camera.draw(box6)
        camera.draw(box7)
        camera.draw(win1)
        camera.draw(win2)
        camera.draw(win3)
        camera.draw(win4)
        camera.draw(win5)
        camera.draw(win6)
        camera.draw(win7)
        camera.draw(collectible)

        if time1 == 0:
            camera.draw(gamebox.from_text(400, 100, "You Lose!", 40, "Red", bold=False))
            gamebox.pause()
        if box1.contains(295.25, 225.25) and box2.contains(415.25, 255.25) and box3.contains(385.25,
                                                                                             315.25) and box4.contains(
            385.25, 375.25) and box5.contains(355.25, 345.25) and box6.contains(445.25, 345.25) and box7.contains(
            295.25, 285.25):
            camera.draw(gamebox.from_text(400, 100, "You Win!", 40, "Red", bold=False))
            level_two = True

        if level_two:
            camera.clear('blue')
            camera.draw(gamebox.from_text(650, 50, "Time Left: " + str(int(time2 / 30)), 35, "Black", bold=False))
            for boundary in boundaries:
                boundary.x += 300
                boundary.y += 500
                camera.draw(boundary)
            box1.x += 500
            box2.x += 500
            box3.x += 500
            box4.x += 500
            box5.x += 500
            box6.x += 500
            box7.x += 500
            win1.x += 500
            win2.x += 500
            win3.x += 500
            win4.x += 500
            win5.x += 500
            win6.x += 500
            win7.x += 500
            collectible.x += 500
            time1 += 1
            time2 -= 1

            camera.draw(gamebox.from_text(400, 35, "Level 2", 50, "Black", bold=True))
            camera.draw(
                gamebox.from_text(400, 95, "Get the boxes of the same color to its corresponding square!", 30, "Black",
                                  bold=True))
            camera.draw(gamebox.from_text(400, 575, "Press R to restart", 50, "Black", bold=False))

            for each in boundariesnew:
                character2.move_to_stop_overlapping(each)
            if pygame.K_r in keys:
                character2.x = 474.75
                character2.y = 404.5
                box8.x = 264.25
                box9.x = 174.25
                box10.x = 264.5
                box11.x = 264.5
                box12.x = 324.75
                box13.x = 354.25

                box8.y = 374.25
                box9.y = 374.25
                box10.y = 284.75
                box11.y = 224.75
                box12.y = 254.75
                box13.y = 285.25

                collectible2.x = 324.25
                collectible2.y = 435.25

                time2 = 900

            if pygame.K_w in keys:
                character2.y -= 15
            if pygame.K_s in keys:
                character2.y += 15
            if pygame.K_a in keys:
                character2.x -= 15
            if pygame.K_d in keys:
                character2.x += 15

            if character2.top_touches(box8):
                box8.y -= 15
            if character2.right_touches(box8):
                box8.x += 15
            if character2.left_touches(box8):
                box8.x -= 15
            if character2.bottom_touches(box8):
                box8.y += 15
            if character2.top_touches(box9):
                box9.y -= 15
            if character2.right_touches(box9):
                box9.x += 15
            if character2.left_touches(box9):
                box9.x -= 15
            if character2.bottom_touches(box9):
                box9.y += 15
            if character2.top_touches(box10):
                box10.y -= 15
            if character2.right_touches(box10):
                box10.x += 15
            if character2.left_touches(box10):
                box10.x -= 15
            if character2.bottom_touches(box10):
                box10.y += 15
            if character2.top_touches(box11):
                box11.y -= 15
            if character2.right_touches(box11):
                box11.x += 15
            if character2.left_touches(box11):
                box11.x -= 15
            if character2.bottom_touches(box11):
                box11.y += 15
            if character2.top_touches(box12):
                box12.y -= 15
            if character2.right_touches(box12):
                box12.x += 15
            if character2.left_touches(box12):
                box12.x -= 15
            if character2.bottom_touches(box12):
                box12.y += 15
            if character2.top_touches(box13):
                box13.y -= 15
            if character2.right_touches(box13):
                box13.x += 15
            if character2.left_touches(box13):
                box13.x -= 15
            if character2.bottom_touches(box13):
                box13.y += 15

            if character2.touches(collectible2):
                time2 += 150
                collectible2.x += 1000
                collectible2.y += 1000

            for each in boundariesnew:
                box8.move_to_stop_overlapping(each)
                box9.move_to_stop_overlapping(each)
                box10.move_to_stop_overlapping(each)
                box11.move_to_stop_overlapping(each)
                box12.move_to_stop_overlapping(each)
                box13.move_to_stop_overlapping(each)

            for boundary in boundariesnew:
                camera.draw(boundary)

            camera.draw(box1)
            camera.draw(box2)
            camera.draw(box3)
            camera.draw(box4)
            camera.draw(box5)
            camera.draw(box6)
            camera.draw(box7)
            camera.draw(win1)
            camera.draw(win2)
            camera.draw(win3)
            camera.draw(win4)
            camera.draw(win5)
            camera.draw(win6)
            camera.draw(win7)
            camera.draw(collectible)
            camera.draw(character2)
            camera.draw(win8)
            camera.draw(win9)
            camera.draw(win10)
            camera.draw(win11)
            camera.draw(win12)
            camera.draw(win13)
            camera.draw(box8)
            camera.draw(box9)
            camera.draw(box10)
            camera.draw(box11)
            camera.draw(box12)
            camera.draw(box13)
            camera.draw(collectible2)

            if time2 == 0:
                camera.draw(gamebox.from_text(400, 300, "You Lose!", 150, "Red", bold=False))
                gamebox.pause()

            if box8.contains(714.25, 345.25) and box9.contains(145.25, 375.25) and box10.contains(714.25,
                                                                                                  375.25) and box11.contains(
                264.5, 194.75) and box12.contains(324.75, 194.75) and box13.contains(714.25, 404.25):
                camera.draw(gamebox.from_text(400, 300, "You Win!", 150, "Red", bold=False))
                gamebox.pause()

    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
