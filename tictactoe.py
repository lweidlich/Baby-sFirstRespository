import pygame
from const.const import *
from sys import exit


pygame.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def map():
    pygame.draw.line(surface, (255,255,255), (300,0), (300,900))
    pygame.draw.line(surface, (255,255,255), (600,0), (600,900))
    pygame.draw.line(surface, (255,255,255), (0,300), (900,300))
    pygame.draw.line(surface, (255,255,255), (0,600), (900,600))

def draw_x(
        start_x_1, 
        start_y_1, 
        end_x_1, 
        end_y_1,
        start_x_2, 
        start_y_2, 
        end_x_2, 
        end_y_2
    ):
    pygame.draw.line(surface, (255,255,255), (start_x_1, start_y_1), (end_x_1, end_y_1,))
    pygame.draw.line(surface, (255,255,255), (0,600), (900,600))

def draw_o(x,y):
    pygame.draw.circle(surface, (255,255,255), (x,y), 5, width=2)

def pos_check(x,y):

    #tl corner
    if x <= 300 and y <= 300:
        draw_x(0, 0, 300, 300, 300, 0, 0, 300)

    #tc spot
    if x > 300 and x < 600 and y <= 300:
        draw_x(300, 0, 600, 300, 600, 0, 300, 300)

    #tr corner
    if x > 600 and y <= 300:
        draw_x(600, 0, 900, 300, 900, 0, 600, 300)

    #cl spot
    if x <= 300 and y > 300 and y <= 600:
        draw_x(0, 300, 300, 600, 300, 300, 0, 600)

    #cc
    if x > 300 and x <= 600 and y > 300 and y <= 600:
        draw_x(300, 300, 600, 600, 600, 300, 300, 600)

    #cr
    if x > 600 and y > 300 and y <= 600:
        draw_x(600, 300, 900, 600, 900, 300, 600, 600)

    #bl
    if x <= 300 and y > 600:
        draw_x(0, 600, 300, 900, 300, 600, 0, 900)

    #bc
    if x > 300 and x <= 600 and y > 600:
        draw_x(300, 600, 600, 900, 600, 600, 300, 900)

    #br
    if x > 600 and y > 600:
        draw_x(600, 600, 900, 900, 900, 600, 600, 900)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True


            if isPressed == True:
                mouse_x, mouse_y = pygame.mouse.get_pos()

            else: 
                pass

        #game code
        map()

        pos_check(mouse_x, mouse_y)

        pygame.display.update()
        clock.tick(60)