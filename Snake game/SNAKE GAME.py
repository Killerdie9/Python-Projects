import pygame as pg
import os
import sys
import random as rd
pg.init()
randomx = rd.randint(100,400)
randomy = rd.randint(100,400)
screen=pg.display.set_mode((500,500))
clock=pg.time.Clock()
pg.display.set_caption('Snake Game!')
red=(255,0,0)
snake_block=15
snake_position = [100, 50]
snake_body = [[10,10]]
#a class to create snake and food sprites for using collidemask
class SpriteCreate(pg.sprite.Sprite):
    def __init__ (self,x,y,w,h,color):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color=color
        self.image=pg.Surface((self.w,self.h))
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.mask=pg.mask.from_surface(self.image)
       
    def update(self):
        self.rect=pg.Rect(self.x,self.y,self.w,self.h)
        screen.blit(self.image,(self.x,self.y))

#creating snake    
def snake(snake_block,snake_list,x ,y):
    global sc

    for each in snake_list:
        sc=SpriteCreate(each[0],each[1],10,10,(255,0,0))
     
        sc.update()
        #pg.display.update()
        
        
score = 0

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pg.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	screen.blit(score_surface, score_rect)

	
#main game loop
def gameloop():
    global score
    global sc
    snake_list=[]
    done=False
    x=250
    y=250
    y_change=0
    x_change=0
    lenth_s=2
    fx=rd.randint(20,480)
    fy=rd.randint(20,480)

   
    im=pg.image.load("bg.png").convert()
    while not done:
        screen.blit(im,[0,0])
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done=True
            if event.type == pg.KEYDOWN:
               
       
                if event.key == pg.K_UP:
                    y_change=-2
                    x_change = 0
                if event.key == pg.K_DOWN:
                    y_change=2
                    x_change= 0
                if event.key == pg.K_LEFT:
                    x_change=-2
                    y_change = 0
                if event.key == pg.K_RIGHT:
                    x_change=2
                    y_change = 0
        y +=y_change
        x +=x_change
       
        screen.fill((0,0,0))
        screen.blit(im,(0,0))
        snakehead=[]
        snakehead.append(x)
        snakehead.append(y)
        snake_list.append(snakehead)
        
        if len(snake_list) > lenth_s:
            del snake_list[0]
        
        snake(snake_block,snake_list,x,y)
        fc=SpriteCreate(fx,fy,10,10,(254,234,198))
        sc.update()
        fc.update()
        pg.display.update()
        if x >= 499 or x <= 1 or y >= 499 or y <= 1:
            font = pg.font.Font('freesansbold.ttf', 50)
            gmor = font.render("GAME OVER", True, (255,255,255))
            screen.blit(gmor,(12,250))
            done=True
           
        if pg.sprite.collide_mask(sc,fc):
            snake_body.insert(0, list(snake_position))
            fx=rd.randint(0,490)
            fy=rd.randint(0,490)
            fc=SpriteCreate(fx,fy,10,10,(254,234,198))
            lenth_s+=5
            score+=1

        #update score
        show_score(1, red, 'Agency FB', 15)
        pg.display.update()
        clock.tick(30)
gameloop()
        
