import pygame
import random
import math
from pygame import mixer

# intializes constants/assets needed
WIDTH = 500
HEIGHT = 500
run = True
WHITE = (255,255,255)
BLACK = (0,0,0)
RADIUS = 30
y = 350
lst_choices = ["Rock", "Paper", "Scissors"]
lst_settings = ['Back', 'Music', 'Quit']
lst_menu = ['Play', 'Settings', 'My Profile']
lst_coordinates = [50, 250, 450]
lst_places = [50, 250, 450]
previous_choices = []
rock_count = 0
scissors_count = 0
paper_count = 0

pygame.init()
LETTER_FONT = pygame.font.SysFont('courier', 10)
TITLE_FONT = pygame.font.SysFont('courier', 15)
SETTINGS_FONT = pygame.font.SysFont('courier', 15)

mixer.music.load('assets/bg_sound.wav')
settings_image = pygame.image.load("assets/rps_settings.png")
profile_pic = pygame.image.load("assets/selfie.png")


# Check whether the computer or the player won
def check_winner(player_choice):
    previous_choices.append(player_choice)
    rock_count = previous_choices.count("Rock")
    paper_count = previous_choices.count("Paper")
    scissors_count = previous_choices.count("Scissors")
    most_used = max(rock_count, scissors_count, paper_count)
    if most_used == rock_count:
        computer_choice = "Paper"
    elif most_used == scissors_count:
        computer_choice = "Rock"
    elif most_used == paper_count:
        computer_choice = "Scissors"
    else:
        computer_choice = random.choice(lst_choices)
    combined_choices = player_choice + computer_choice
    if combined_choices in ('RockScissors', 'PaperRock', 'ScissorsPaper'):
        result = "Player won"
    elif combined_choices in ('ScissorsRock', 'RockPaper', 'PaperScissors'):
        result = "Computer won"
    else:
        result = "It was a tie.."

    text = TITLE_FONT.render(result, 1, BLACK)
    win.blit(text, (250 - text.get_width() / 2, 175 - text.get_height() / 2))
    text = TITLE_FONT.render("Your choice: "+player_choice + " -- Computer choice: "+computer_choice, 1, BLACK)
    win.blit(text, (270 - text.get_width() / 2, 250 - text.get_height() / 2))

    pygame.display.update()
    pygame.time.delay(3000)
    start(win)

# creates the main menu display
def main_menu(win):
    while True:
        win.fill((WHITE))
        text = TITLE_FONT.render('Main Menu', 1, BLACK)
        win.blit(text, (235 - text.get_width() / 2, 30 - text.get_height() / 2))
        for i in range(3):
            pygame.draw.rect(win, BLACK, (70, lst_coordinates[i]/2 +50, 150, 50),3)
            text = SETTINGS_FONT.render(lst_menu[i], 1, BLACK)
            win.blit(text, (150 - text.get_width() / 2, lst_coordinates[i]/2+77 - text.get_height() / 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for i in range(3):
                    if m_x > 70 and m_x < 220:
                        if m_y > lst_coordinates[i]/2 +50 and m_y < lst_coordinates[i]/2 +100:
                            if (lst_menu[i] == 'Play'):
                                start(win)
                            if (lst_menu[i] == 'Settings'):
                                settings(win)
                            if (lst_menu[i] == "My Profile"):
                                profile(win)

# creates menu bar (back)
def top_menu_bar(win, i, y, phrase):
    pygame.draw.circle(win, BLACK, (lst_coordinates[i], y), RADIUS, 3)
    text = LETTER_FONT.render(phrase, 1, BLACK)
    win.blit(text, (lst_coordinates[i] - text.get_width() / 2, y - text.get_height() / 2))

#shows my picture and I made the code
def profile(win):
    win.fill((WHITE))
    win.blit(pygame.transform.scale(profile_pic, (240, 240)), (10,100))
    descrip = SETTINGS_FONT.render('Hi, my name is Alykhan and I made this code!', 1, BLACK)
    win.blit(descrip, (10, 355))
    top_menu_bar(win, 0, 50, "Back")
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for i in range(3):
                    dis = math.sqrt((lst_coordinates[i] - int(m_x)) ** 2 + (50 - int(m_y)) ** 2)
                    if dis < RADIUS:
                        if (lst_settings[i] == "Back"):
                            main_menu(win)

#settings to turn music on/off shows image of rock paper scissors and how to play
def settings(win):
    win.fill((WHITE))
    win.blit(pygame.transform.scale(settings_image, (350, 380)), (75,100))
    run = True
    for i in range(3):
        top_menu_bar(win, i, 50, lst_settings[i])

    pygame.display.update()
    click = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for i in range(3):
                    dis = math.sqrt((lst_coordinates[i] - int(m_x))**2 + (50-int(m_y))**2)
                    if dis < RADIUS:
                        if (lst_settings[i] == 'Quit'):
                            run = False
                            pygame.quit()
                        if (lst_settings[i] == 'Music'):
                            if click:
                                mixer.music.stop()
                                click = False
                            else:
                                mixer.music.play(-1)
                                click = True
                        if (lst_settings[i] == "Back"):
                            main_menu(win)

# play the game
def start(win):
    win.fill((WHITE))
    run = True
    for i in range(3):
        top_menu_bar(win, i, y, lst_choices[i])
    top_menu_bar(win, 0, 50, "Back")

    text2 = TITLE_FONT.render('Rock Paper Scissors', 1, BLACK)
    win.blit(text2, (235 - text2.get_width() / 2, 50 - text2.get_height() / 2))
    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for i in range(3):
                    dis = math.sqrt((lst_places[i] - int(m_x))**2 + (y-int(m_y))**2)
                    if dis < RADIUS:
                        check_winner(lst_choices[i])
                    top_dis = math.sqrt((lst_coordinates[0] - int(m_x))**2 + (50-int(m_y))**2)
                    if top_dis < RADIUS:
                        main_menu(win)

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((WHITE))
pygame.display.set_caption("Rock Paper Scissors Game")
pygame.display.update()
main_menu(win)