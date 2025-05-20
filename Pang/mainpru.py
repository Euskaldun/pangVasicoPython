import pygame
import player
import balls
import SmallBubble
import proyectil

pygame.init()

ancho_ventana = 1240
alto_ventana = 720
proyectiles = []  # Lista para almacenar los disparos
bubbles = []  # Lista de burbujas

screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Pang 2D")
clock = pygame.time.Clock()
player = player.Kate((ancho_ventana / 2, alto_ventana - 76))

bubbles = pygame.sprite.Group()
#pum = balls.Ball((0, 0), 4, 4, 0.8, 200)
bubbles.add(balls.Ball((0, 0), 4, 10, 0.4, 200))
bubbles.add(balls.Ball((ancho_ventana - 200, 0), -4, 10, 0.4, 200))
#bubbles.add(pum)


game_over = False

fondo = pygame.image.load("../Img/playa_de_gorliz.jpg")
fondo = pygame.transform.scale(fondo, (ancho_ventana, alto_ventana))

game_Over_Sprite = pygame.image.load("../Img_Sprite/game_over.png")
game_Over_Sprite = pygame.transform.scale(game_Over_Sprite, (ancho_ventana/5, alto_ventana/5))

while not game_over:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Manejar disparo al presionar ESPACIO
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            nuevo_proyectil = proyectil.Proyectil(player.rect.centerx, player.rect.top, fondo.get_height())  # Crear nuevo proyectil
            proyectiles.append(nuevo_proyectil)  # Agregarlo a la lista

    # Dibujar elementos en pantalla
    player.handle_event(event)  # Mover jugador
    screen.blit(fondo, (0, 0))  # Dibujar fondo
    screen.blit(player.image, player.rect)  # Dibujar jugador

    for proj in proyectiles:
        proj.update()
        screen.blit(proj.image, proj.rect)
        if proj.height >= alto_ventana:  # Si el proyectil alcanzó el límite, lo eliminamos
            proyectiles.remove(proj)
        for bubble in bubbles:
            if proj.rect.colliderect(bubble.rect):  # Si el ataque toca la burbuja
                nuevos_bubbles = bubble.explode()  # Explota la burbuja y crea 2 mas peques
                bubbles.remove(bubble)  # Elimina la burbuja original
                bubbles.add(*nuevos_bubbles)
                if proj in proyectiles:
                    proyectiles.remove(proj)
    # Dibujar burbujas
    for bubble in bubbles:
        bubble.update()
        screen.blit(bubble.image, bubble.rect)
        if pygame.sprite.collide_mask(bubble, player):
            game_over = True

    pygame.display.flip()  # Actualizar pantalla
    clock.tick(20)  # Controlar velocidad del bucle

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
    screen.blit(game_Over_Sprite, ((ancho_ventana / 2) - (game_Over_Sprite.get_width() / 2),
                                        (alto_ventana / 2) - (game_Over_Sprite.get_height() / 2)))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()