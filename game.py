import pygame
from pygame. locals import*
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = 1
colors = {
    "fire": pygame.color('chartreuse4'),
    "white": (255,255,255)
}
letters_guessed_wrong = []
letters_guessed = []
input_text = ""
active = False



input_rect = pygame.Rect(200, 200, 140, 32)

def to_list(str:str):
    return list(str)

def render(object, loc =()):
    screen.blit(object, loc)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

            if event.type == pygame.KEYDOWN:

                #checking for backspace
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:                # if event.unicode.isalpha():
                    input_text += event.unicode


    print(colors["fire"])
    print(input_text)

screen.fill((120, 120, 120))
pygame.display.flip()

pygame.quit()