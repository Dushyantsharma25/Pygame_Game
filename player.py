import pygame
from obj import object

class Player(object):


    def __init__(self,x,y,width,height,ip,speed):

        super().__init__(x,y,width,height,ip)
        self.speed = speed


    def move(self,direction,y_max):

        if(self.y >= y_max - self.height):
            self.y -= self.speed
            return
        elif(self.y <= 0):
            self.y += self.speed
            return

        self.y += direction*self.speed