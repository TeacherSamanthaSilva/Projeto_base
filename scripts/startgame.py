import pygame, sys
from scripts.scene import Scene

class StartGame:

    def __init__(self):
        
        self.display = pygame.display.set_mode([1280,720])

        self.current_scene = Scene()

    def run(self):
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.events(event)
            
            self.display.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()