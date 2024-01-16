# falling blocks game
# 12/20/23
__author__ = 'Harrison Beck'


pygame.init()

textfont = pygame.font.SysFont("arial", 40)
textfontsmall = pygame.font.SysFont("arial", 30)

windowheight = 500
windowwidth = 500

window = pygame.display.set_mode((windowwidth, windowheight))


def mainmenu():  # creates the main menu
    purple = (125, 61, 168)
    window.fill(purple)
    text1 = 'Start Game'
    textd1 = textfont.render(text1, 1, (255, 255, 255))
    text_w = textd1.get_rect().width
    text_h = textd1.get_rect().height
    window.blit(textd1, [windowwidth / 2 - text_w / 2, windowheight / 2 - text_h / 2 - 50])
    button_rect = pygame.Rect(windowwidth / 2 - text_w / 2, windowheight / 2 - text_h / 2 - 50, text_w, text_h)
    text2 = 'Quit'
    textd2 = textfont.render(text2, 1, (255, 255, 255))
    text_w2 = textd2.get_rect().width
    text_h2 = textd2.get_rect().height
    window.blit(textd2, [windowwidth / 2 - text_w2 / 2, windowheight / 2 - text_h2 / 2])
    button_rect2 = pygame.Rect(windowwidth / 2 - text_w2 / 2, windowheight / 2 - text_h2 / 2, text_w2, text_h2)

    def on_mouse_button_down(event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_rect.collidepoint(event.pos):
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_rect2.collidepoint(event.pos):
            pygame.quit()
            exit()
        else:
            return True

    pygame.display.update()

    running = True

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                running = on_mouse_button_down(event)

        pygame.display.update()


def checkcollision(box1y, box1x, box2y, box2x, dead, x, y):  # checks to see if the player is in the hazard
    if x >= box1x and x <= box1x + 50:
        if y >= box1y and y <= box1y + 50:
            dead = True
    if x >= box2x and x <= box2x + 50:
        if y >= box2y and y <= box2y + 50:
            dead = True
    if x + 20 >= box1x and x + 20 <= box1x + 50:
        if y + 20 >= box1y and y + 20 <= box1y + 50:
            dead = True
    if x + 20 >= box2x and x + 20 <= box2x + 50:
        if y + 20 >= box2y and y + 20 <= box2y + 50:
            dead = True
    if x + 20 >= box1x and x + 20 <= box1x + 50:
        if y >= box1y and y <= box1y + 50:
            dead = True
    if x + 20 >= box2x and x + 20 <= box2x + 50:
        if y >= box2y and y <= box2y + 50:
            dead = True
    if x >= box1x and x <= box1x + 50:
        if y + 20 >= box1y and y + 20 <= box1y + 50:
            dead = True
    if x >= box2x and x <= box2x + 50:
        if y + 20 >= box2y and y + 20 <= box2y + 50:
            dead = True
    return dead


def main():  # runs everything
    global windowheight, windowwidth, textfont, textfontsmall

    highest = 0

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    boxwidth = 50
    boxheight = 50
    fallspeed = 0.1

    box1spawn = True
    box2spawn = True
    box1y = 0
    box1x = 0
    box2y = 0
    box2x = 0

    width = 20
    height = 20
    x = windowwidth / 2 - width / 2
    y = windowheight - width
    vel = 0.1

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    dead = False

    mainmenu()

    start_ticks = pygame.time.get_ticks()

    running = True

    while running:
        clock.tick()
        if dead == False:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        window.fill(white)
        dead = checkcollision(box1y, box1x, box2y, box2x, dead, x, y)
        if dead == True:
            f = open('highscore.txt', 'r')
            score = []
            for line in f:
                line = line.strip('\n')
                if line != score:
                    score.append(line)
            done = True
            f.close()
            f = open('highscore.txt', 'w')
            for i in score:
                i = float(i)
                highest = float(highest)
                if i > highest:
                    highest = i
            seconds = float(seconds)
            highest = float(highest)
            if seconds > highest:
                seconds = str(seconds)
                f.write(seconds)
            else:
                highest = str(highest)
                f.write(highest)
            f.close()
        if dead == True:
            text1 = 'You Survived:'
            textd1 = textfont.render(text1, 1, (255, 0, 0))
            text_w = textd1.get_rect().width
            text_h = textd1.get_rect().height
            window.blit(textd1, [windowwidth / 2 - text_w / 2, windowheight / 2 - text_h / 2 - 150])
            text_w2 = textd3.get_rect().width
            text_h2 = textd3.get_rect().height
            window.blit(textd3, [windowwidth / 2 - text_w2 / 2, windowheight / 2 - text_h2 / 2 - 50])
            text6 = 'Highscore:'
            textd6 = textfont.render(text6, 1, (255, 0, 0))
            text_w6 = textd6.get_rect().width
            text_h6 = textd6.get_rect().height
            window.blit(textd6, [windowwidth / 2 - text_w6 / 2, windowheight / 2 - text_h6 / 2 + 50])
            highest = str(highest)
            text9 = highest
            textd9 = textfontsmall.render(text9, 1, (0, 0, 0))
            text_w9 = textd9.get_rect().width
            text_h9 = textd9.get_rect().height
            window.blit(textd9, [windowwidth / 2 - text_w9 / 2, windowheight / 2 - text_h9 / 2 + 150])
        if dead == False:
            v = random.randint(1, 2500)
            text3 = str(seconds)
            textd3 = textfontsmall.render(text3, 1, (0, 0, 0))
            window.blit(textd3, [10, 10])
            if box1spawn == True and v == 1:
                box1x = random.randint(0, windowwidth - boxwidth)
                box1y = 0
                box1spawn = False
            if box2spawn == True and v == 2:
                box2x = random.randint(0, windowwidth - boxwidth)
                box2y = 0
                box2spawn = False
        if box1y > 500:
            box1spawn = True
        if box2y > 500:
            box2spawn = True
        if dead == False:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if dead == False:
            pygame.draw.rect(window, (0, 0, 0), (x, y, width, height))
            pygame.draw.rect(window, (blue), (box1x, box1y, boxwidth, boxheight))
            pygame.draw.rect(window, (blue), (box2x, box2y, boxwidth, boxheight))
            box1y += fallspeed
            box2y += fallspeed
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x += vel
        if dead == True:
            time.sleep(3)
            main()
        if x < 0:
            x = 0
        if x + width > windowwidth:
            x = windowwidth - width
        fallspeed += 0.0000015


if __name__ == '__main__':
    main()
