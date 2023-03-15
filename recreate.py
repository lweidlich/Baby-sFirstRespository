import pygame
from sys import exit

WIDTH, HEIGHT = 1000, 1000

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def projectOne():
    pygame.draw.line(surface, (255,255,255), (600,400), (600,600))
    pygame.draw.line(surface, (255,255,255), (600,600), (400,600))
    pygame.draw.line(surface, (255,255,255), (400,600), (400,400))
    pygame.draw.line(surface, (255,255,255), (400,400), (600,400))
    pygame.draw.line(surface, (255,255,255), (600,400), (700,500))
    pygame.draw.line(surface, (255,255,255), (700,500), (600,600))
    pygame.draw.line(surface, (255,255,255), (600,600), (500,700))
    pygame.draw.line(surface, (255,255,255), (500,700), (400,600))
    pygame.draw.line(surface, (255,255,255), (400,600), (300,500))
    pygame.draw.line(surface, (255,255,255), (300,500), (400,400))
    pygame.draw.line(surface, (255,255,255), (400,400), (500,300))
    pygame.draw.line(surface, (255,255,255), (500,300), (700,500))
    pygame.draw.line(surface, (255,255,255), (700,500), (700,700))
    pygame.draw.line(surface, (255,255,255), (700,700), (300,700))
    pygame.draw.line(surface, (255,255,255), (300,700), (300,300))
    pygame.draw.line(surface, (255,255,255), (300,300), (700,300))
    pygame.draw.line(surface, (255,255,255), (700,300), (700,700))
    pygame.draw.line(surface, (255,255,255), (700,700), (500,900))
    pygame.draw.line(surface, (255,255,255), (500,900), (300,700))
    pygame.draw.line(surface, (255,255,255), (300,700), (100,500))
    pygame.draw.line(surface, (255,255,255), (100,500), (300,300))
    pygame.draw.line(surface, (255,255,255), (300,300), (500,100))
    pygame.draw.line(surface, (255,255,255), (500,100), (700,300))
    pygame.draw.line(surface, (255,255,255), (700,300), (900,500))
    pygame.draw.line(surface, (255,255,255), (900,500), (700,700))
    
    
    pygame.draw.circle(surface, (255,255,255), (500,500), (10), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (20), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (30), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (40), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (50), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (60), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (70), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (80), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (90), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (100), width=2)
    pygame.draw.circle(surface, (255,255,255), (500,500), (400), width=2)

def circlefunc():
    init = 0
    end = 200
    while init <= end:
        pygame.draw.circle(surface, (255,255,255), (500,500), init, width=1)
        init += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
        pygame.draw.line(surface, (255,255,255), (0,1000), (500,500))
        # circlefunc()
        pygame.draw.arc(surface, (255,255,255), [500,0,50,50], 70, 70)
        
        


        pygame.display.update()
        clock.tick(60)