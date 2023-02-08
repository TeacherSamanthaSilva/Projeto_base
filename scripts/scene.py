import pygame

class Scene:

    def __init__(self):
        pygame.display.set_caption("BeeHoney")

    def events(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    def draw(self):
        pass

    def update(self):
        pass

