from pygame.locals import *
from random import randint
from PIL import ImageTk, Image 
import pygame
import time
import tkinter
from tkinter import *



class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 

class Poison:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))  
 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0

    
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
            
           
 
 
 
    def moveRight(self):
        self.direction = 0     
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
       

class App:
    
    player = 0
    apple = 0
    poison = 5 
    score = 0
    canvasWidth=700
    canvasHeight=600
    
    
    
   
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self._poison_surf = None 
        self.game = Game()
        self.player = Player(3) 
        self.apple = Apple(3,5)
        self.poison = Poison(6,10)
        self.score = 0 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.canvasWidth,self.canvasHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Slithery snek')
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()
        self._apple_surf = pygame.image.load("block.jpg").convert()
        self._poison_surf = pygame.image.load("apple2.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
 
        # This is what adds length to the snake when it eats and apple
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.poison.x = randint (2,9) * 40
                self.poison.y = randint (2,9) * 40
                self.player.length = self.player.length + 1
                score = self.player.length / 2 
                
        #this is the code for the posin apple which decreases the size     
        for i in range(0,self.player.length):
            if self.game.isCollision(self.poison.x,self.poison.y,self.player.x[i], self.player.y[i],44):
                self.poison.x = randint(2,9) * 44
                self.poison.y = randint(2,9) * 44
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44 
                self.player.length = self.player.length - 2
                score = self.player.length 
                if score < 2:
                    self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40)
                    final_score = self.game.isCollision
                    final_score = self.player.length / 2 
                    root = Tk()
                    T = Text(root, width = 20, height = 5)
                    T.pack()
                    T.insert(END, "TOO SMALL-")
                    T.insert(END,  final_score)
                    mainloop()
                    exit(0)   
                    
                        
 
 
        # This is what causes the snake to die if it touches itself
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                final_score = self.game.isCollision
                final_score = self.player.length / 2 
                root = Tk()
                T = Text(root, width = 20, height = 5)
                T.pack()
                T.insert(END, "CRASHED-")
                T.insert(END,  final_score)
                mainloop()
                exit(0)        
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        self.poison.draw(self._display_surf, self._poison_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0);
        self.on_cleanup()
        
        
 
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()