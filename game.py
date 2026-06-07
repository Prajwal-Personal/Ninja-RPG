import pygame
import sys
from scripts.entities import PhysicsEntities
from scripts.utils import load_image, load_all_images

class Game:
    def __init__(self):
        pygame.init() # initilizes the game
        pygame.display.set_caption("Ninja Role Playing Game")

        self.screen = pygame.display.set_mode((640,480)) # passing tuple to initilze width, height
        self.clock = pygame.time.Clock() # running at constant 60 FPS

        self.display = pygame.Surface((self.screen.get_width()//2, self.screen.get_height()//2))

        self.movement = [False,False] # up and down movement
        self.assets = {
            "decor" : load_all_images("tiles/decor"),
            "grass" : load_all_images("tiles/grass"),
            "large_decor" : load_all_images("tiles/large_decor"),
            "stone" : load_all_images("tiles/stone"),
            "player" : load_image("entities/player.png")
        }
        self.player = PhysicsEntities(self, "player", (50,50), (8,15))

    def run(self):
        while(1):
            self.display.fill((135,206,235)) # fills entire screen with sky blue

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get(): # process all pending event from prev frame one by one
                if (event.type==pygame.QUIT) :
                    pygame.quit() # exits when closes using x button
                    sys.exit() # exits application

                if (event.type==pygame.KEYDOWN): # when key is pressed
                    if (event.key == pygame.K_LEFT):
                        self.movement[0] = True
                    if (event.key == pygame.K_RIGHT):
                        self.movement[1] = True

                if (event.type==pygame.KEYUP): # when key is released 
                    if (event.key == pygame.K_LEFT):
                        self.movement[0] = False
                    if (event.key == pygame.K_RIGHT):
                        self.movement[1] = False
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update() # updates the screen
            self.clock.tick(60) # sleep until it achieve 60 FPS 

if (__name__ == "__main__"): # main is the starting point of function this only runs if executed directly but not in imported
    Game().run()