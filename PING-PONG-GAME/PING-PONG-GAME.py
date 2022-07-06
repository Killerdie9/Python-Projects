import pygame as pg
import random as rd
pg.init()
screen = pg.display.set_mode((500,500))
import os
import sys
from paddle import player
from ball import ball
score1=0
score2=0
white=(255,255,255)
clock = pg.time.Clock()
pg.display.set_caption('Ping-Pong-Game!')
done = False
p1 = player(white,10,85)
p1.rect.x=5
p1.rect.y=200
p2 = player(white,10,85)
p2.rect.x=485
p2.rect.y=200
b=ball(white,10,10)
b.rect.x=245
b.rect.y=255
alls = pg.sprite.Group()
alls.add(p1)
alls.add(p2)
alls.add(b)
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    prd=pg.key.get_pressed()
    if prd[pg.K_UP]:
        p1.m_up(5)
    if prd[pg.K_DOWN]:
        p1.m_down(5)
    if prd[pg.K_w]:
        p2.m_up(5)
    if prd[pg.K_s]:
        p2.m_down(5)
    if prd[pg.K_r]:
        score1=0
        score2=0
    alls.update()
    screen.fill((0,0,0))
    pg.draw.line(screen, (255,0,0) , (249,0), (249,500), 2)

    
    if b.rect.x >= 490:
        score1 += 1
        b.velocity[0]=-b.velocity[0]
    if b.rect.x <= 0:
        score2 += 1
        b.velocity[0]=-b.velocity[0]
    if b.rect.y >= 490:
        b.velocity[1]=-b.velocity[1]
    if b.rect.y <= 0:
        b.velocity[1]=-b.velocity[1]
    if score1 >= 10 and score2 >= 10:
        b.velocity[0]+=5
        b.velocity[1]+=5
 
    if pg.sprite.collide_mask(p1,b) or pg.sprite.collide_mask(p2,b):
        b.bounce()
    if score1 >= 20:
        font1 = pg.font.Font('freesansbold.ttf', 100)
        p1w = font.render("GAME OVER, Player 1 wins(Left paddle player)!", True, (255,255,255))
        screen.blit(p1w,(12,250))
        done=True
        
    if score2 >= 20:
        p2w = font.render("GAME OVER, Player 2 wins(Right paddle player)!", True, (255,255,255))
        screen.blit(p2w,(12,250))
        done=True
        
    font = pg.font.Font('freesansbold.ttf', 25)
    text = font.render(str(score1), True, (255,0,0))
    screen.blit(text,(10,10))

    text1 = font.render(str(score2), True, (255,0,0))
    screen.blit(text1,(460,10))
        
        
    alls.draw(screen)
    pg.display.flip()
    clock.tick(40)
