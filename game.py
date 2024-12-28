import pygame
from obj import object
from player import Player
from enemy import Enemy

class Game:


    def __init__(self):
        
        self.w = 700
        self.h = 700
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.gw = pygame.display.set_mode((self.w,self.h))
        self.clock = pygame.time.Clock()
        self.background = object(0,0,self.w,self.h,'zgaming/background.png')
        self.treasure = object(325,40,50,50,'zgaming/treasure.png')
        self.player = Player(325,620,50,50,'zgaming/player.png',8.75)
        self.enemy1 = Enemy(640,175,50,50,'zgaming/enemy.png',20)
        self.enemy2 = Enemy(640,350,60,60,'zgaming/enemy.png',15)
        self.enemy3 = Enemy(640,525,60,60,'zgaming/enemy.png',10)
        self.win = object(0,0,self.w,self.h,'zgaming/win.png')
        self.lose = object(0,0,self.w,self.h,'zgaming/lose.png')

    def draw_obj(self):

        self.gw.fill(self.white)
        self.gw.blit(self.background.image,(self.background.x,self.background.y))
        self.gw.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
        self.gw.blit(self.player.image,(self.player.x,self.player.y))
        self.gw.blit(self.enemy1.image,(self.enemy1.x,self.enemy1.y))
        self.gw.blit(self.enemy2.image,(self.enemy2.x,self.enemy2.y))
        self.gw.blit(self.enemy3.image,(self.enemy3.x,self.enemy3.y))

        

    def detect_collision(self,object1,object2):

        if(object1.y > object2.y + object2.height):
            return False
        elif(object1.y + object1.height < object2.y):
            return False

        if(object1.x + object1.width < object2.x):
            return False
        elif(object1.x > object2.x + object2.width):
            return False
        

        return True


    def game_loop(self):
        player_direction = 0
        while(1):

            events = pygame.event.get()


            for event in events:
                if(event.type == pygame.QUIT):
                    return
                elif(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_UP):
                        player_direction = -1
                    elif(event.key == pygame.K_DOWN):
                        player_direction = 1
                elif(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                        player_direction = 0
                

            

            
            if(self.detect_collision(self.player,self.enemy1) or self.detect_collision(self.player,self.enemy2) or self.detect_collision(self.player,self.enemy3)):
                    for event in events:
                        if(event.type == pygame.QUIT):
                            return
                    
                    self.gw.blit(self.lose.image,(self.lose.x,self.lose.y))
                    pygame.display.update()
                    continue
            

            if(self.detect_collision(self.player,self.treasure)):
                    for event in events:
                        if(event.type == pygame.QUIT):
                            return
                    
                    self.gw.blit(self.win.image,(self.lose.x,self.lose.y))
                    pygame.display.update()
                    continue
            
            self.player.move(player_direction,self.h)
            self.enemy1.move(self.w)
            self.enemy2.move(self.w)
            self.enemy3.move(self.w)
            
            
            self.draw_obj()
            pygame.display.update()


            self.clock.tick(60)