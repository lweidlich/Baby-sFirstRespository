import pygame
from const.const import *
from sys import exit
import random


pygame.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
x_turn, o_turn = False, False
winner = {
    "x": False,
    "o": False
}

tiles = {
    "tl": {
        "x": 300,
        "y": 300
    }
}

# tiles['tl']['x']
# tiles['tl']['y']

x_placed = {
    "tl": False,
    "tc": False,
    "tr":  False,
    "cl": False,
    "cc": False,
    "cr": False,
    "bl": False,
    "bc": False,
    "br": False
}

o_placed = {
    "tl": False,
    "tc": False,
    "tr":  False,
    "cl": False,
    "cc": False,
    "cr": False,
    "bl": False,
    "bc": False,
    "br": False
}

def bot(randnum, o_turn):    
    try:

        if x_placed["tl"] == False and o_turn == True and randnum == 1:
              if x <= 300 and y <= 300:
                draw_o(150, 150)
                o_placed['tl'] = True
                o_turn = False
                x_turn = True
        else:
            return

        if x_placed["tc"] == False and o_turn == True and randnum == 2:
            if x > 300 and x < 600 and y <= 300:
                draw_o(450, 150)
                o_turn = False
                x_turn = True
                o_placed = True
        else:
            return

        if x_placed["tr"] == False and o_turn == True and randnum == 3:
            if x > 600 and y <= 300:
                draw_o(750, 150)
                o_placed = True
                o_turn = False
                x_turn = True
        else:
            return


        if x_placed["cl"] == False and o_turn == True and randnum == 4:
            if x <= 300 and y > 300 and y <= 600:
                draw_x(0, 300, 300, 600, 300, 300, 0, 600)
                x_placed['cl'] = True
                x_turn = False
                o_turn = True
        else:
            return


        if x_placed["cc"] == False and o_turn == True and randnum == 5:
            if x > 300 and x <= 600 and y > 300 and y <= 600:
                draw_o(450, 450)
                o_placed['cc'] = True
                o_turn = False
                x_turn = True
        else:
            return


        if x_placed["cr"] == False and o_turn == True and randnum == 6:
            if x > 600 and y > 300 and y <= 600:
                draw_o(750, 450)
                o_placed['cr'] = True
                o_turn = False
                x_turn = True
        else:
            return


        if x_placed["bl"] == False and o_turn == True and randnum == 7:
            if x <= 300 and y > 600:
                draw_o(150, 750)
                o_placed['bl'] = True
                o_turn = False
                x_turn = True
        else:
            return


        if x_placed["bc"] == False and o_turn == True and randnum == 8:
            if x > 300 and x <= 600 and y > 600:
                draw_o(450,750)
                o_placed['bc'] = True
                o_turn = False
                x_turn = True
        else:
            return


        if x_placed["br"] == False and o_turn == True and randnum == 9:
            if x > 600 and y > 600:
                draw_o(750,750)
                o_placed['br'] = True
                o_turn = False
                x_turn = True
        else:
            return

    except Exception as e:
        print(str(e))


# def bot():
#     global o_turn
#     randnum = random.randint(1,9)

#     try:
#         match randnum:
#             case 1: 
#                 if x_placed["tl"] == False and o_turn == True:
#                     draw_o(150, 150)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 2: 
#                 if x_placed["tc"] == False and o_turn == True:
#                     draw_o(450, 150)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 3: 
#                 if x_placed["tr"] == False and o_turn == True:
#                     draw_o(750, 150)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 4: 
#                 if x_placed["cl"] == False and o_turn == True:
#                     draw_o(150, 450)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 5: 
#                 if x_placed["cc"] == False and o_turn == True:
#                     draw_o(450, 450)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return
        
#             case 6: 
#                 if x_placed["cr"] == False and o_turn == True:
#                     draw_o(750, 450)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 7: 
#                 if x_placed["bl"] == False and o_turn == True:
#                     draw_o(150, 750)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 8: 
#                 if x_placed["bc"] == False and o_turn == True:
#                     draw_o(450, 750)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#             case 9: 
#                 if x_placed["br"] == False and o_turn == True:
#                     draw_o(750, 750)
#                     o_turn = False
#                     x_turn = True
#                     o_placed = True
#                 else:
#                     return

#     except Exception as e:
#         print(str(e))


def map():
    pygame.draw.line(surface, (255,255,255), (300,0), (300,900), width=6)
    pygame.draw.line(surface, (255,255,255), (600,0), (600,900), width=6)
    pygame.draw.line(surface, (255,255,255), (0,300), (900,300), width=6)
    pygame.draw.line(surface, (255,255,255), (0,600), (900,600), width=6)

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
    pygame.draw.line(surface, (255,255,255), (start_x_2, start_y_2), (end_x_2, end_y_2))

def draw_o(x,y):
    pygame.draw.circle(surface, (255,255,255), (x,y), 140, width=2)

def win_check(): # checks X: works
    if x_placed['tl'] and x_placed['tc'] and x_placed['tr'] == True:
        pygame.draw.line(surface, (255,255,255), (0,150), (900,150), width=4)
        winner["x"] == True

    if x_placed['cl'] and x_placed['cc'] and x_placed['cr'] == True:
        pygame.draw.line(surface, (255,255,255), (0,450), (900,450), width=4)
        winner["x"] == True

    if x_placed['bl'] and x_placed['bc'] and x_placed['br'] == True:
        pygame.draw.line(surface, (255,255,255), (0,750), (900,750), width=4)
        winner["x"] == True

    if x_placed['tl'] and x_placed['cl'] and x_placed['bl'] == True:
        pygame.draw.line(surface, (255,255,255), (150,0), (150,900), width=4)
        winner["x"] == True

    if x_placed['tc'] and x_placed['cc'] and x_placed['bc'] == True:
        pygame.draw.line(surface, (255,255,255), (450,0), (450,900), width=4)
        winner["x"] == True

    if x_placed['tr'] and x_placed['cr'] and x_placed['br'] == True:
        pygame.draw.line(surface, (255,255,255), (750,0), (750,900), width=4)
        winner["x"] == True

    if x_placed['tl'] and x_placed['cc'] and x_placed['br'] == True:
        pygame.draw.line(surface, (255,255,255), (0,0), (900,900), width=4)
        winner["x"] == True

    if x_placed['tr'] and x_placed['cc'] and x_placed['bl'] == True:
        pygame.draw.line(surface, (255,255,255), (900,900), (0,0), width=4)
        winner["x"] == True

def win_checko():
    if o_placed['tl'] and o_placed['tc'] and o_placed['tr'] == True:
        pygame.draw.line(surface, (255,255,255), (0,150), (900,150), width=4)
        winner["o"] == True

    if o_placed['cl'] and o_placed['cc'] and o_placed['cr'] == True:
        pygame.draw.line(surface, (255,255,255), (0,450), (900,450), width=4)
        winner["o"] == True

    if o_placed['bl'] and o_placed['bc'] and o_placed['br'] == True:
        pygame.draw.line(surface, (255,255,255), (0,750), (900,750), width=4)
        winner["o"] == True

    if o_placed['tl'] and o_placed['cl'] and o_placed['bl'] == True:
        pygame.draw.line(surface, (255,255,255), (150,0), (150,900), width=4)
        winner["o"] == True

    if o_placed['tc'] and o_placed['cc'] and o_placed['bc'] == True:
        pygame.draw.line(surface, (255,255,255), (450,0), (450,900), width=4)
        winner["o"] == True

    if o_placed['tr'] and o_placed['cr'] and o_placed['br'] == True:
        pygame.draw.line(surface, (255,255,255), (750,0), (750,900), width=4)
        winner["o"] == True

    if o_placed['tl'] and o_placed['cc'] and o_placed['br'] == True:
        pygame.draw.line(surface, (255,255,255), (0,0), (900,900), width=4)
        winner["o"] == True

    if o_placed['tr'] and o_placed['cc'] and o_placed['bl'] == True:
        pygame.draw.line(surface, (255,255,255), (900,900), (0,0), width=4)
        winner["o"] == True

def pos_check(x,y):
    global x_turn
    global o_turn

    #tl corner
    if x <= 300 and y <= 300:
        draw_x(0, 0, 300, 300, 300, 0, 0, 300)
        x_placed['tl'] = True
        x_turn = False
        o_turn = True

    #tc spot
    if x > 300 and x < 600 and y <= 300:
        draw_x(300, 0, 600, 300, 600, 0, 300, 300)
        x_placed['tc'] = True
        x_turn = False
        o_turn = True

    #tr corner
    if x > 600 and y <= 300:
        draw_x(600, 0, 900, 300, 900, 0, 600, 300)
        x_placed['tr'] = True
        x_turn = False
        o_turn = True

    #cl spot
    if x <= 300 and y > 300 and y <= 600:
        draw_x(0, 300, 300, 600, 300, 300, 0, 600)
        x_placed['cl'] = True
        x_turn = False
        o_turn = True

    #cc
    if x > 300 and x <= 600 and y > 300 and y <= 600:
        draw_x(300, 300, 600, 600, 600, 300, 300, 600)
        x_placed['cc'] = True
        x_turn = False
        o_turn = True

    #cr
    if x > 600 and y > 300 and y <= 600:
        draw_x(600, 300, 900, 600, 900, 300, 600, 600)
        x_placed['cr'] = True
        x_turn = False
        o_turn = True

    #bl
    if x <= 300 and y > 600:
        draw_x(0, 600, 300, 900, 300, 600, 0, 900)
        x_placed['bl'] = True
        x_turn = False
        o_turn = True

    #bc
    if x > 300 and x <= 600 and y > 600:
        draw_x(300, 600, 600, 900, 600, 600, 300, 900)
        x_placed['bc'] = True
        x_turn = False
        o_turn = True

    #br
    if x > 600 and y > 600:
        draw_x(600, 600, 900, 900, 900, 600, 600, 900)
        x_placed['br'] = True
        x_turn = False
        o_turn = True

def pos_checko(x,y): 
    global x_turn
    global o_turn
    
    #tl corner
    if x <= 300 and y <= 300:
        draw_o(150, 150)
        o_placed['tl'] = True
        o_turn = False
        x_turn = True

    #tc spot
    if x > 300 and x < 600 and y <= 300:
        draw_o(450, 150)
        o_placed['tc'] = True
        o_turn = False
        x_turn = True

    #tr corner
    if x > 600 and y <= 300:
        draw_o(750, 150)
        o_placed['tr'] = True
        o_turn = False
        x_turn = True

    #cl spot
    if x <= 300 and y > 300 and y <= 600:
        draw_o(150, 450)
        o_placed['cl'] = True
        o_turn = False
        x_turn = True

    #cc
    if x > 300 and x <= 600 and y > 300 and y <= 600:
        draw_o(450, 450)
        o_placed['cc'] = True
        o_turn = False
        x_turn = True

    #cr
    if x > 600 and y > 300 and y <= 600:
        draw_o(750, 450)
        o_placed['cr'] = True
        o_turn = False
        x_turn = True

    #bl
    if x <= 300 and y > 600:
        draw_o(150, 750)
        o_placed['bl'] = True
        o_turn = False
        x_turn = True

    #bc
    if x > 300 and x <= 600 and y > 600:
        draw_o(450,750)
        o_placed['bc'] = True
        o_turn = False
        x_turn = True

    #br
    if x > 600 and y > 600:
        draw_o(750,750)
        o_placed['br'] = True
        o_turn = False
        x_turn = True

def main():
    while winner["x"] != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True


            #game code
                if isPressed == True:
                    mouse_pos = pygame.mouse.get_pos()
                    pos_check(mouse_pos[0], mouse_pos[1])

                else: 
                    pass

            # print(x_placed)
            # print(o_placed)

            num = random.randint(1,9)

            map()
            win_check()
            win_checko()
            # bot(num, o_turn)
            pos_checko(x, y)

            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    x_turn = True
    main()