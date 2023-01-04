import pygame
from pygame. locals import*

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = 1
letters_guessed_wrong = []
letters_guessed = []

def to_list(str:str):
    return list(str)

def render(object, loc =()):
    screen.blit(object, loc)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        

screen.fill((120, 120, 120))
pygame.display.flip()

pygame.quit()