import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600),0,32)

pygame.display.set_caption("Mundo")

screen.fill((255,0,0))

pygame.display.update()

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.quit()


