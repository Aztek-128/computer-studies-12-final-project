import pygame , sys
import time
import sqlite3
import os
import random

from pygame.constants import KEYDOWN, KEYUP

#Constants 
WIDTH, HEIGHT = 300,500
TITLE = "Shooter game"

#pygame start up
pygame.init()
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

class Player():

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x,self.y,32,32)
        self.color = (250,120,60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 2

    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self,win):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x),int(self.y),32,32) 

#Player start up
player = Player(WIDTH/2,HEIGHT/2)

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

    win.fill((12,24,36))
    player.draw(win)

    #update the display
    player.update(win)
    pygame.display.flip()

    clock.tick(120)
'''class main(): #This is a shooter game like survivor.io

    def __init__(self) -> None:
        pygame.init()
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists playerscore (
            id integer primary key autoincrement,
            killscore int,
            time_spent_alive int);
        """
        self.cursor.execute(query)
        
        self.screen = pygame.display.set_mode((500,500))
        self.screen.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.deltaTime = 0
        pygame.display.flip()
        self.running = True
        self.vel = 5
        self.stats = {"hp": 5,"dp": 1,"movement": self.vel}
        self.start()
    def start(self):
        x = 250
        y = 250
        #timestart = time.time()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        

                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    x -= 30 * self.deltaTime * self.vel
                    print("left")
                if keys[pygame.K_d]:
                    x += 30 * self.deltaTime * self.vel
                    print("right")
                if keys[pygame.K_w]:
                    y -= 30 * self.deltaTime * self.vel
                    print("up")
                if keys[pygame.K_s]:
                    y += 30 * self.deltaTime * self.vel
                    print("down")
                self.deltaTime = self.clock.tick(60)/1000
                pygame.draw.circle(self.screen,(0,0,255),(x,y),6,20)
            pygame.display.update()
        

    
main()'''