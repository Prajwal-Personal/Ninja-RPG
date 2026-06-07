import pygame

base_path = "data/images/"

def load_image(path):
    img = pygame.image.load(base_path + path).convert()
    img.set_colorkey((0,0,0))
    return img