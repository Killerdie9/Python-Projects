import pygame as pg
import random as rd
class ball(pg.sprite.Sprite):
    def __init__(self,color,width,height):
       super().__init__()
       self.image=pg.Surface([width,height])
       self.image.fill((0,0,0))
       self.image.set_colorkey((0,0,0))
       pg.draw.rect(self.image,color,[0,0,width,height])
       self.rect=self.image.get_rect()
       self.velocity = [rd.randint(1,8),rd.randint(-8,8)]

    def update(self):
        self.rect.x=self.rect.x+self.velocity[0]
        self.rect.y=self.rect.y+self.velocity[1]
    def bounce(self):
        self.velocity[0]=-self.velocity[0]
        self.velocity[1] = rd.randint(-8,8)
        
