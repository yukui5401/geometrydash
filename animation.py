# Brooke Yang - Culminating - Animation
# Input:        N/A.
# Processing:   N/A.
# Output:       Animation of Geometry Dash.

# Declaration Section
import pygame, time
from pygame import KEYDOWN, K_ESCAPE, K_q, RESIZABLE
delay = 0.001
scene = 1
sgiGray16 = (40, 40, 40)
sgiGray96 = (244, 244, 244)
aquamarine1 = (127, 255, 212)
aquamarine4 = (69, 139, 116)
coral1 = (255, 114, 86)
darkOrange = (255, 140, 0)
darkOliveGreen1 = (202, 255, 112)
springGreen = (0, 255, 127)
slateBlue4 = (71, 60, 139)
oliveDrab3 = (154, 205, 50)
cyan2 = (0, 238, 238)
gold1 = (255, 215, 0)
x = 1
x2 = -770
x3 = 1
x4 = 0
x5 = 0
y = 200
y2 = -200
y3 = 1
y4 = 1
y5 = 0
y6 = -40
y7 = 0
y8 = 0
r = 1
trigger = True

# Step 1: Setup Game
pygame.init()
window = pygame.display.set_mode([1300, 700], RESIZABLE)
pygame.display.set_caption("Brooke Yang - Geometry Dash UltraLite (Battery Issues)")
pygame.mixer.music.load("stereo_madness.mp3")
pygame.mixer.music.play()
font = pygame.font.SysFont("inkfree", 70, True, 1)
font2 = pygame.font.SysFont("inkfree", 30, True, 1)
font3 = pygame.font.SysFont("Arial", 60, False, 0)
font4 = pygame.font.SysFont("inkfree", 25, True, 1)
title = font.render("Geometry Dash UltraLite", True, coral1)
title2 = font.render("(Battery Issues)", True, coral1)
text1 = font4.render("This is easy...", True, [4, 4, 4])
text2 = font4.render("Let me try firebird. I bet I can complete it!", True, [4, 4, 4])
text3 = font4.render("WHY DOES THE BATTERY ALWAYS RUN OUT!!", True, [4, 4, 4])
level = font2.render("Level 1 Complete!", True, coral1)
nxt_level = font2.render("Next Level: 2", False, coral1)
shutdown = font3.render("Shutting down", False, (252, 252, 252))
end = font.render("The End", True, coral1)
green_background = pygame.transform.scale(pygame.image.load("green_background.png"), [1300, 700])
homeScreen = pygame.transform.scale(pygame.image.load("stereo_madness_map.jpg"), [1300, 700])
homeScreen2 = pygame.transform.scale(pygame.image.load("firebird.jpg"), [1300, 700])
map2 = pygame.transform.scale(pygame.image.load("map2.jpg"), [1300, 700])

# Step 2: Poll for Events
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.mixer.music.stop()
        break
    elif event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q):
        pygame.mixer.music.stop()
        break

# Step 3: Update Game
    x += 1
    if x == 1300:
        x = 1
        scene += 1
    if scene == 2 and y > 0:
        y *= 0.985
    elif scene == 3:
        if 840 <= x <= 940:
            y -= 0.8
        elif 940 <= x < 960 or 1020 <= x < 1085:
            y += 1
    elif scene == 4:
        if y2 < 80:
            y2 += 2
        if x2 < 0:
            x2 += 6
        elif x3 < 30 and 550 > x > 500:
            pygame.mixer.music.load("DJVI - Back On Track.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
            x3 += 2
            y3 += 2
        elif x3 > 1 and x > 550:
            pygame.mixer.music.set_volume(0.4)
            x3 -= 2
            y3 -= 2
        elif x > 600:
            scene += 1
            pygame.mixer.music.set_volume(0.8)
    elif scene == 5 and y4 <= 701:
        pygame.mixer.music.set_volume(0.5)
        y4 += 6
    elif scene == 5 and y6 < 550:
        pygame.mixer.music.set_volume(0.4)
        y6 += 2
    elif scene == 6 and x4 < 1300:
        pygame.mixer.music.set_volume(0.3)
        x4 += 65
    elif scene == 6 and x5 < 600:
        pygame.mixer.music.set_volume(0.2)
        x5 += 5
    elif scene == 7 and y5 < 700:
        pygame.mixer.music.load("DJVI - Dry Out.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()
        y5 += 7
        y7 += 0.9
    elif scene == 7 and 450 < x < 600:
        y8 += 0.8
    elif scene == 7 and 600 <= x < 670:
        y8 -= 0.8
    elif scene == 7 and 670 <= x < 860:
        y8 += 0.8
    elif scene == 7 and 860 <= x < 880:
        y8 -= 1
    elif scene == 7 and 960 <= x < 1025:
        y8 -= 2
    elif scene == 7 and 1030 <= x < 1150:
        y8 += 1
    elif scene == 7 and 1150 <= x < 1290:
        y8 -= 0.4
    elif scene == 8 and 60 < x < 125:
        y8 -= 2
    elif scene == 8 and x > 400:
        scene = 9
    elif 11 > scene >= 9:
        if r > 0:
            r -= 0.01
        else:
            r = 1

# Step 4: Draw Surface
    if scene < 7 or scene > 10:
        window.blit(green_background, [0 - x, 0])
        window.blit(green_background, [1300 - x, 0])
    elif scene < 9:
        window.blit(map2, [0 - x, 0])
        window.blit(map2, [1300 - x, 0])
    if scene == 1:
        window.blit(title, [200, 430])
        window.blit(title2, [300, 510])
    elif scene == 2:
        window.blit(title, [200 - x, 430])
        window.blit(title2, [300 - x, 510])
        pygame.draw.rect(window, coral1, [300, 460 + y, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [300, 460 + y, 40, 40], 12, 4)
    elif scene == 3:
        pygame.draw.rect(window, coral1, [300, 460 + y, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [300, 460 + y, 40, 40], 12, 4)
        pygame.draw.rect(window, aquamarine4, [1280 - x, 440, 60, 60], 8, 2)
    elif scene == 4:
        pygame.draw.rect(window, coral1, [300, 460 + y, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [300, 460 + y, 40, 40], 12, 4)
        pygame.draw.rect(window, springGreen, [400, 100 + y2, 400, 150], 0, 4)
        pygame.draw.circle(window, gold1, [6.25 * y2, 280], 30)
        pygame.draw.circle(window, gold1, [7.5 * y2, 280], 30)
        pygame.draw.circle(window, gold1, [8.75 * y2, 280], 30)
        window.blit(level, [450, 105 + y2])
        pygame.draw.rect(window, oliveDrab3, [430 + x2 - x3, 380 - y3, 350 + 2 * x3, 50 + 2 * y3], 0, 7)
        window.blit(nxt_level, [485 + x2, 385])
    elif scene == 5:
        window.blit(homeScreen, [0, 701 - y4])
        pygame.draw.rect(window, coral1, [900, y6, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [900, y6, 40, 40], 12, 4)
        if y6 >= 550:
            pygame.draw.ellipse(window, sgiGray96, [1000, 550, 250, 70])
            pygame.draw.circle(window, sgiGray96, [980, 555], 7)
            pygame.draw.circle(window, sgiGray96, [960, 553], 4)
            window.blit(text1, [1050, 570])
    elif scene == 6:
        window.blit(homeScreen, [0 - x4, 701 - y4])
        window.blit(homeScreen2, [1300 - x4, 0])
        pygame.draw.rect(window, coral1, [900 - x5, 550, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [900 - x5, 550, 40, 40], 12, 4)
        if x5 >= 600:
            pygame.draw.ellipse(window, sgiGray96, [120, 335, 680, 100])
            pygame.draw.circle(window, sgiGray96, [350, 460], 10)
            pygame.draw.circle(window, sgiGray96, [340, 490], 7)
            pygame.draw.circle(window, sgiGray96, [330, 515], 5)
            window.blit(text2, [155, 375])
    elif scene == 7 and y8 == 0:
        window.blit(homeScreen2, [0, 0 + y5])
        pygame.draw.rect(window, coral1, [300, 554 - y7, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [300, 554 - y7, 40, 40], 12, 4)
    elif scene == 7 or scene == 8:
        pygame.draw.rect(window, coral1, [300, 464 - y8, 40, 40], 0, 4)
        pygame.draw.rect(window, darkOliveGreen1, [300, 464 - y8, 40, 40], 12, 4)
    elif 11 > scene >= 9:
        window.fill([4, 4, 4])
        window.blit(shutdown, [400, 320])
        pygame.draw.circle(window, [255, 255, 255], [730, 370], 5 * r)
        pygame.draw.circle(window, [255, 255, 255], [765, 370], 3 * r)
        pygame.draw.circle(window, [255, 255, 255], [800, 370], 2 * r)
        pygame.draw.ellipse(window, sgiGray96, [560, 65, 665, 100])
        pygame.draw.circle(window, sgiGray96, [1230, 75], 8)
        pygame.draw.circle(window, sgiGray96, [1270, 50], 5)
        pygame.draw.circle(window, sgiGray96, [1290, 30], 3)
        window.blit(text3, [600, 100])
        if trigger:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("StayInsideMe.mp3")
            pygame.mixer.music.play()
            trigger = False
    elif scene < 13:
        window.blit(end, [200, 430])
    else:
        scene = 1
        x = 1
        x2 = -770
        x3 = 1
        x4 = 0
        x5 = 0
        y = 200
        y2 = -200
        y3 = 1
        y4 = 1
        y5 = 0
        y6 = -40
        y7 = 0
        y8 = 0
        r = 1
        trigger = True
        pygame.mixer.music.stop()
        pygame.mixer.music.load("stereo_madness.mp3")
        pygame.mixer.music.play()

# Step 5: Display Surface
    pygame.display.update()
    time.sleep(delay)
pygame.quit()
quit()