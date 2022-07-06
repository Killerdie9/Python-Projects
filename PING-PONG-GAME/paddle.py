import pygame as pg
class player(pg.sprite.Sprite):
    def __init__(self,color,width,height):
       super().__init__()
       self.image=pg.Surface([width,height])
       self.image.fill((0,0,0))
       self.image.set_colorkey((0,0,0))
       pg.draw.rect(self.image,color,[0,0,width,height])
       self.rect=self.image.get_rect()

    def m_up(self,pixels):
        self.rect.y=self.rect.y-pixels
        if self.rect.y < 0:
            self.rect.y=0
    def m_down(self,pixels):
        self.rect.y=self.rect.y+pixels
        if self.rect.y > 425:
            self.rect.y=425

