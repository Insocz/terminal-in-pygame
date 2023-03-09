import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, write, group,xy,color = (250,250,250)) -> None:
        super().__init__(group)

        self.screen = pygame.display.get_surface()

        self.write = write
        self.color = color
        self.xy = xy

        self.font = pygame.font.Font(None,20)
        self.image = self.font.render(self.write, True, self.color)
        self.rect = self.image.get_rect(topleft=self.xy)

    def update(self):

        self.image = self.font.render(self.write, True,self.color)

        self.screen.blit(self.image,self.rect)