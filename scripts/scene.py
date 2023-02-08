import pygame
from scripts.obj import Obj

class Scene:

    def __init__(self):
        
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()

    def events(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.all_sprites.update()

