import pygame
from obj import object

class Enemy(object):

    def __init__(self,x,y,width,height,ip,speed):

        super().__init__(x,y,width,height,ip)

        self.speed = speed
    

    def move(self,x_max):

        if(self.x >= x_max - self.width):
            self.x -= self.speed
            self.speed = -1*self.speed
            return 
        elif(self.x <= 0):
            self.x -= self.speed
            self.speed = -1*self.speed
            return


        self.x += self.speed