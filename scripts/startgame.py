import pygame, sys
from scripts.menu import Menu, Game, GameOver

class StartGame:

    def __init__(self):
        
        self.display = pygame.display.set_mode([1280,720])
        self.scene = "menu"
        self.current_scene = Menu()
    
    def run(self):
        
        while True:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.current_scene = Game()
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.events(event)
            
            self.display.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()