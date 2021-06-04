import pygame
import time
import random

# Initializing the working space before starting
pygame.init()

#crash_sound = pygame.mixer.Sound('C:\Users\Bertrand\PycharmProjects\Gametest\white knuckles.wav')
#pygame.mixer.music.load('C:\Users\Bertrand\PycharmProjects\Gametest\oklm.wav')

# Display width and height are for the window size
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

car_width = 155  # used for the crash when the car touches the boundary

pause = False

# Game display here is using pygame.display.set_mode which takes the variables declared before for the winddow size. Its basically defining the window
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Here we are defining the window name x)
pygame.display.set_caption('GAME')

# pygame.time.Clock() here is used to keep the window open
clock = pygame.time.Clock()

# We've got an image in the same folder as the python program and its loaded through pygame.image.load
carImg = pygame.image.load(r"sia.png")


# gameIcon = pygame.image.load("C:\Users\Bertrand\PycharmProjects\Gametest\icones.jpeg")

# pygame.display.set_icon(gameIcon)

def thing_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged : " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))
    # On the window GameDisplay we are placing the imported image which is carImg and positioning it on the screen (background) with parameter x and y
    # use update to make it appear on the screen(visible)


def crash():
    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)


    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Lost", largeText)
    TextRect.center = ((display_width / 2), (display_height) / 2.5)
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again !", 150, 450, 120, 50, green, bright_green, game_loop)

        button("Quit !", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(5)


def quitgame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac, action=None):  # IC = Inactive color, AC = active color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # This function has been copied and modified. The original function is under with the explanations
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        # click [0] == left click
        if click[0] == 1 and action != None:
            action()

            # if action == "play":
            #     game_loop()
            # elif action == "quit":
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))


        # The smalltext defines the style of the text that will be appearing on the green button
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)

    # We're placing the text right on the middle of the button.
    # 150 is the starting point and 100 is the length that's gotten divided by 2
    # 450 also == to starting point and 50 is the breadth which is gotten divided by 2 too

    textRect.center = ((x + (w / 2), (y + (h / 2))))
    gameDisplay.blit(textSurf, textRect)


# Text printed before the game starting
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                # The text is going to be black so we using .fill on the gameDisplay to make it white
        gameDisplay.fill(white)
        # The font style is freesansbold.ttf and the size is 115
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Dodger", largeText)
        TextRect.center = ((display_width / 2), (display_height) / 2.5)
        gameDisplay.blit(TextSurf, TextRect)

        button("Start !", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit !", 550, 450, 100, 50, red, bright_red, quitgame)

        # We are now drawing button to make them as buttons as there's no button in pygame

        # pygame.mouse.get_pos() is used to get the mouse postion in the variable named mouse and by looking in the terminal we see the values
        '''mouse = pygame.mouse.get_pos()'''
        # print(mouse)
        # The values we see in the terminal will be used to restrict the location of the button (rectangle)

        '''if 150+100 > mouse[0] > 150 and 450 + 50 > mouse [1] > 450:
#This -> IF <- is a little complicated but what we're doing here is basically taking
#Green rectangle coordinates which goes 150 and 100 on one side and 450 and 50 on the other
#so its like we're getting the length of the rectangle by doing 150 + 100 which normally greater than the mouse 1st element
#And the mouse should be greater than 150 which is the starting point of our rectangle
#We're also doing the same thing with the width of the rectangle with the and going 450+50 compared to 450
#And we need to put the normal red there otherwise it won't be display (not going into the else block)
            pygame.draw.rect(gameDisplay,bright_green,(150,450,100,50))
            #pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay,green,(150,450,100,50))
            #pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

#The smalltext defines the style of the text that will be appearing on the green button
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Start !", smallText)

        #We're placing the text right on the middle of the button.
        #150 is the starting point and 100 is the length that's gotten divided by 2
        #450 also == to starting point and 50 is the breadth which is gotten divided by 2 too

        textRect.center = ((150+(100/2),(450+(50/2))))
        gameDisplay.blit(textSurf, textRect)'''
        pygame.display.update()
        clock.tick(5)

        # pygame.display.update()
        # clock.tick(3)


def paused():
    # We are here pausing the music using the function pause and by clicking on continue after pressing the pause button the music should start again

    #pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height) / 2.5)
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                # The text is going to be black so we using .fill on the gameDisplay to make it white
        # gameDisplay.fill(white)
        # The font style is freesansbold.ttf and the size is 115


        button("Continue !", 150, 450, 100, 50, green, bright_green, unpause)

        button("Quit !", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(5)


def unpause():
    global pause
    # We unpause the music using the unpause function as the music should start playing back after the pause
    #pygame.mixer.music.unpause()
    pause = False


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    # Returns the text in black and places it in the windows which is a rectangle .get_rect()
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects(text, largeText)

    # TextRect.center is used to place the text right in the middle of the screen its takes 2 parameters width and height both /2
    TextRect.center = ((display_width / 2), (display_height) / 2)

    # Once everything is done we blit the text surface and the text rectangle and then we update it
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)  # 2 seconds sleep

    game_loop()  # This is to run the game again


def game_loop():
    #pygame.mixer.music.stop()
    #pygame.mixer.music.play(-1)

    global pause
    x = (display_width * 0.4)

    y = (display_height * 0.8)

    x_change = 0

    # --------Obstacle are being defined here-----------
    # For the obstable x we're using the random function to let it come from anywhere (shouldn't be predictable)
    thing_startx = random.randrange(0, display_width)

    # Here on the y dimension we're setting the object to -600 so that we don't see it coming
    thing_starty = -600

    # Then we're having the speed at which the obstacle will be coming and
    # their width and height
    thing_speed = 4
    thing_width = 80
    thing_height = 80

    dodged = 0

    gameExit = False  # This variable is used to stop the program

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7

                if event.key == pygame.K_KP_PLUS:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)  # Filling the work space with white then placing the image on it

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed  # the obstacle drops down at each loop by +7 speed
        car(x, y)
        thing_dodged(dodged)

        if x > display_width - car_width or x < 0:  # unless you - car_width the car will cross over on the right side
            crash()

        # We avoid obstacle to be generated outta the boundaries
        if thing_starty > display_height:
            thing_starty = 0 - thing_height

            # Obstacle would only be coming from one way if we don't also random the X dimension
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if thing_speed < 10:
                if dodged > 2 and dodged < 5:
                    thing_speed = 5
                if dodged > 5 and dodged < 10:
                    thing_speed = 7
                if dodged > 10 and dodged < 15:
                    thing_speed = 8
                if dodged > 15:
                    thing_speed = 10

                    # thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            # print('y cross over')


            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                # print('x cross over')
                crash()

        pygame.display.update()
        clock.tick(220)  # by variating the value in tick you can slow or speed up the game (frames/sec)


game_intro()
game_loop()
pygame.quit()
quit()
