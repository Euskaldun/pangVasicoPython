import pygame

class Proyectil(pygame.sprite.Sprite):  # Ahora hereda de Sprite
    def __init__(self, x, y, z):
        super().__init__()  # Inicializar correctamente la clase Sprite
        self.x = x
        self.y = y
        self.z = z
        self.height = 10  # Tamaño inicial
        self.speed = 5  # Velocidad de crecimiento

        self.sheet = pygame.image.load('../Img_Sprite/pang-hook.png')
        self.sheet.set_clip(pygame.Rect(123, 121, 280, 900))
        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.image = pygame.transform.scale(self.image, (30, self.height))
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))  # Mantener alineación

    def update(self):
        if self.height < self.z:  # Establecer límite de crecimiento
            self.height += self.speed
            self.image = pygame.transform.scale(self.image, (30, self.height))
            self.rect = self.image.get_rect(midbottom=(self.x, self.y))  # Mantener posición de base
        else:
            self.kill()  # Eliminar del grupo de sprites cuando alcance su tamaño máximo
