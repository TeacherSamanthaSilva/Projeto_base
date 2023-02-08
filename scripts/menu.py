import pygame
from scripts.obj import Obj
from scripts.scene import Scene

class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/menu.png", [self.all_sprites])


class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/game.png", [self.all_sprites])
    
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.bg.rect.y += 1
        return super().events(event)
    

class GameOver(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/gameover.png", [self.all_sprites])
