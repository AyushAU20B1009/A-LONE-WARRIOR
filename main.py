#AYUSH D. JARIWALA
#AU20B1009
#Student at Avantika University


# Importing required modules.
import pygame
import random
import time

# activating pygame
pygame.init()

# setting heigth and width of the screen
display_heigth = 680
display_width = 895

button_start_x = 75
new_game_y = 400
quit_y = 460
button_width = 242
button_height = 50

# Colors  in hexa-decimal form
yellow = (233, 201, 29)
white = (255, 255, 255)
score_color = (157, 252, 33)
redLight = (255, 21, 21)
blue = (41, 140, 227)
green = (0, 255, 0)
greenLight = (51, 255, 51)
darkred = (196, 43, 43)

# loading png files.
heroimg = pygame.image.load("hero1.png")
backgroundleft = pygame.image.load("bgleft.png")
backgroundright = pygame.image.load("bgright.png")
mainbackground = pygame.image.load("mainbg1.png")
mainbackground2 = pygame.image.load("mainbg2.png")
logo = pygame.image.load("logo1.png")
introbackground = pygame.image.load("background1.jpg")

# hero's width
hero_width = 150

gamedisplay = pygame.display.set_mode((display_width, display_heigth))
pygame.display.set_caption("  A - LONE WARRIOR ")
pygame.display.set_icon(logo)
clock = pygame.time.Clock()


# defining function for main character
def hero(x, y):
    gamedisplay.blit(heroimg, (x, y))


# defining function for opponents
def opponent(op_startx, op_starty, op):  # Here used op in place of opponents.

    global op_image
    if op == 0:
        op_image = pygame.image.load("demon1.png")
    elif op == 1:
        op_image = pygame.image.load("demon3.png")
    elif op == 2:
        op_image = pygame.image.load("demon2.png")
    elif op == 3:
        op_image = pygame.image.load("demon3.png")

    # dispaly opponents using blit().
    gamedisplay.blit(op_image, (op_startx, op_starty))


# defining function to make background
def background():
    gamedisplay.blit(backgroundleft, (0, 0))

    gamedisplay.blit(backgroundright, (750, 0))

    gamedisplay.blit(mainbackground, (400, 0))
    gamedisplay.blit(mainbackground, (265, 0))
    gamedisplay.blit(mainbackground, (140, 0))
    gamedisplay.blit(mainbackground, (545, 0))
    gamedisplay.blit(mainbackground, (610, 0))


# defining function for using fonts
def text_object(text, font):
    textsurface = font.render(text, True, white)
    return textsurface, textsurface.get_rect()


# Function for create text size and style
def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 50)
    textsurf, textrect = text_object(text, largetext)
    textrect.center = ((display_width / 2), (display_heigth / 2 - 148))
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    main_loop()


# Making function create another text format for score
def message(size, msg, x_pos, y_pos):
    font = pygame.font.SysFont("Aial Black", size)
    render = font.render(msg, True, white)
    gamedisplay.blit(render, (x_pos, y_pos))


# Function for trap (gameover), to display text after character killed by traps.

def trap():
    message_display("OPPS..! HIDDEN TRAPS GOT YOU")


# Function to display text after killed by opponent.
def gameoveropponent():
    message_display("OPPS..! OPPONENT GOT YOU")


# Scoring function

def score(opponentpassed, score):
    font = pygame.font.SysFont("Arial Black", 25)
    text = font.render("Score : " + str(score), True, score_color)
    gamedisplay.blit(text, (630, 40))
    pygame.display.update()


# Making function for displaying instructions.
def instructions():
    instruction = False
    while instruction == False:

        # Defining font style and size for instructions.
        font = pygame.font.SysFont("Comic Sans MS", 30)
        font2 = pygame.font.SysFont("Comic Sans MS", 20)

        # Displaying instructions.
        text = font.render("Hello, welome to the game A -LONE WARRIOR.", True, redLight)
        text1 = font2.render("Attention player, the war has begun and you've only left from", True, redLight)
        text2 = font2.render("from your whole army, survive as much as possible and score ", True, redLight)
        text3 = font2.render(" as much possible by dodging the opponents.", True, redLight)
        text4 = font2.render(" --> Be aware of the traps on the left and right of the boundries..!!", True, blue)
        text5 = font2.render(" --> Move Your Hero using normal left and right keys from keyboard.", True, blue)
        text6 = font2.render(" ALL THE BEST ", True, darkred)
        gamedisplay.blit(introbackground, (0, 0))

        # Placing all the instructions in a proper line and manner.
        gamedisplay.blit(text, (145, 20))
        gamedisplay.blit(text1, (190, 100))
        gamedisplay.blit(text2, (190, 120))
        gamedisplay.blit(text3, (190, 140))
        gamedisplay.blit(text4, (170, 190))
        gamedisplay.blit(text5, (170, 220))
        gamedisplay.blit(text6, (300, 300))
        buttons(400, 500, "NEW GAME")  # calling button function
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    pygame.display.update()


# Making butttons and functioning it.
def buttons(x_button, y_button, message_button):
    pygame.draw.rect(gamedisplay, greenLight, [x_button, y_button, 250, 40])
    message(45, message_button, x_button, y_button)
    mouse = pygame.mouse.get_pos()  # getting position
    clicks = pygame.mouse.get_pressed(3)  # 3 buttons defined and press function

    # Conditions for clicks.
    if x_button < mouse[0] < x_button + 100 and y_button < mouse[1] < y_button + 40:
        if clicks == (1, 0, 0) and message_button == "NEW GAME":
            main_loop()

        elif clicks == (1, 0, 0) and message_button == "QUIT":
            pygame.quit()
            quit()

        elif clicks == (1, 0, 0) and message_button == "INSTRUCTIONS":
            instructions()

            if clicks == (1, 0, 0) and message_button == "NEW GAME":
                main_loop()


# Function for displaying intro with buttons.
def game_intro():
    intro = False
    while not intro:

        # Creating buttons by calling button function and adding it to the screen.
        gamedisplay.blit(introbackground, (0, 0))
        buttons(200, 300, "NEW GAME")
        buttons(400, 500, "QUIT")
        buttons(600, 300, "INSTRUCTIONS")

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()


# main loop of the game
def main_loop():
    global event
    # Setting position for main character
    x = (display_width * 0.44)
    y = (display_heigth * 0.7)
    x_change = 0
    # Speed of opponent
    opponent_speed = 10
    op = 0
    y_change = 0
    op_startx = random.randrange(200, (display_width - 200))  # Random opponent comings
    op_starty = -760

    opponent_passed = 0
    Score_a = 0

    # Height and width of the opponents
    op_width = 149
    op_heigth = 90
    bump = False
    while not bump:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bump = True

            # Key functioning
            # for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                if event.key == pygame.K_RIGHT:
                    x_change = 5

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            # If not pressed any keys there won't be any changes on the screen
            # for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # Calling functions..!
        gamedisplay.fill(yellow)
        background()
        op_starty -= (opponent_speed / 4)
        opponent(op_startx, op_starty, op)
        op_starty += opponent_speed
        hero(x, y)
        score(opponent_passed, Score_a)

        # Setting limits of the width
        if x > 819 - hero_width or x < 89:
            trap()
            bump = True

        # conditon opponents and hero
        if x > display_width - (hero_width + 10) or x < 10:
            gameoveropponent()
            bump = True

        if op_starty > display_heigth:
            op_starty = 0 - op_heigth
            op_startx = random.randrange(170, (display_width - 170))
            op = random.randrange(0, 3)  # Random opponents will come.
            opponent_passed = opponent_passed + 1
            Score_a = Score_a + 5
            if int(opponent_passed) % 10 == 0:
                opponent_speed = opponent_speed + 5
                pygame.display.update()
                time.sleep(2)

        # Condition if oppnent collide with the player.
        if y < op_starty + op_heigth:
            if x > op_startx and x < op_startx + op_width or x + hero_width > op_startx and x + hero_width < op_startx + op_width:
                gameoveropponent()
                bump = True

        pygame.display.update()  # Updating display.
        clock.tick(70)  # Overall Speed of the game.


game_intro()
main_loop()
pygame.quit()
quit()
#Closing all loops and quiting.
