import pygame
import os

base_path = "data/images/"

def load_image(path):
    img = pygame.image.load(base_path + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_all_images(path):
    images = []
    for img_name in os.listdir(base_path + path):
        images.append(load_image(path + "/" + img_name))
    return images