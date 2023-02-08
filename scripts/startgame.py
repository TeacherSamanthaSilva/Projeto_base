import pygame, sys

class StartGame:

    def __init__(self):
        
        self.display = pygame.display.set_mode([1280,720])

    def run(self):
        
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.display.fill("black")
            pygame.display.flip()