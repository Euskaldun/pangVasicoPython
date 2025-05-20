import pygame

class SmallBubble(pygame.sprite.Sprite):
    def __init__(self, position, speed_x, speed_y, gravity, size):
        super().__init__()
        self.sheet = pygame.image.load('../Img_Sprite/bals-pang-t (1).png')
        self.sheet.set_clip(pygame.Rect(50, 63, 250, 260))  # Recorta el sprite
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image = pygame.transform.scale(self.image, (size, size))  # Ajustar tamaño
        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.mask = pygame.mask.from_surface(self.image)

        # Movimiento
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = gravity
        self.size = size


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y -= self.speed_y
        self.speed_y -= self.gravity

        if self.rect.left < 0 or self.rect.right > 1240:
            self.speed_x = -self.speed_x

        if self.rect.bottom >= 720:
            self.rect.bottom = 720
            self.speed_y = max(-self.speed_y, -5)
            self.speed_y = min(self.speed_y, 19)

    def explode(self):
        if self.size > 30:  # Evitar burbujas infinitamente pequeñas
            new_size = self.size // 2  # Reducir tamaño dinámicamente

            from SmallBubble import SmallBubble  # Importar aquí para evitar el ciclo

            return [
                SmallBubble((self.rect.centerx - new_size // 2, self.rect.centery), self.speed_x * 1.1,
                            self.speed_y * 0.9, self.gravity + 0.3, new_size),
                SmallBubble((self.rect.centerx + new_size // 2, self.rect.centery), self.speed_x * -1.1,
                            self.speed_y * 0.9, self.gravity + 0.3, new_size)
            ]
        return []
