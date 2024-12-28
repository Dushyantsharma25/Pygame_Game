import pygame


class object:

    def __init__(self,x,y,width,height,ip):
        image = pygame.image.load(ip)
        self.image = pygame.transform.scale(image,(width,height))
        self.x =x
        self.y = y
        self.width = width
        self.height = height