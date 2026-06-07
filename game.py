import pygame
import sys

class Game:
    def __init__(self):
        pygame.init() # initilizes the game
        pygame.display.set_caption("Ninja Role Playing Game")

        self.screen = pygame.display.set_mode((640,480)) # passing tuple to initilze width, height
        self.clock = pygame.time.Clock() # running at constant 60 FPS

        self.cloud1_img = pygame.image.load("data/images/clouds/cloud_1.png") # loading the backgroung image of cloud
        self.cloud1_img_position = [100,200]

        self.movement = [False,False]

    def run(self):
        while(1):
            self.screen.fill((135,206,235)) # fills entire screen with sky blue

            self.cloud1_img_position[1] += self.movement[1] - self.movement[0] # moves the cloud when only 1 key is pressed
            self.screen.blit(self.cloud1_img,self.cloud1_img_position) # places cloud img at 100px from left and 200 px from right

            for event in pygame.event.get(): # process all pending event from prev frame one by one
                if (event.type==pygame.QUIT) :
                    pygame.quit() # exits when closes using x button
                    sys.exit() # exits application

                if (event.type==pygame.KEYDOWN): # when key is pressed
                    if (event.key == pygame.K_UP):
                        self.movement[0] = True
                    if (event.key == pygame.K_DOWN):
                        self.movement[1] = True

                if (event.type==pygame.KEYUP): # when key is released 
                    if (event.key == pygame.K_UP):
                        self.movement[0] = False
                    if (event.key == pygame.K_DOWN):
                        self.movement[1] = False

            pygame.display.update() # updates the screen
            self.clock.tick(60) # sleep until it achieve 60 FPS 

if (__name__ == "__main__"): # main is the starting point of function this only runs if executed directly but not in imported
    Game().run()