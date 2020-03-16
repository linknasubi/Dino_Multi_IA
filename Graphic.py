from graphics import *
import time
from random import randint

WIDTH, HEIGHT = 900, 800





#        
class General():
    
    def __init__(self, number_dinos):
        self.dino_dic = {}
        self.number_dinos = number_dinos
        self.speed = 1
        self.distance = 2.01
        
    
    def dinosCreation(self):
        
        for i in range (self.number_dinos):
            
            dino_position = randint(50,100)
            dino_location_x = (WIDTH//2)+dino_position
            dino_location_y = HEIGHT//2
            self.dino = Rectangle(Point(dino_location_x , dino_location_y), Point(dino_location_x+50, dino_location_y+50))
            self.dino.setFill(color_rgb(randint(0,255), randint(0,255), randint(0,255)))
            
            self.dino_dic[i] = [self.dino, dino_location_x, dino_location_y]
    
    def cactusCreation(self):
        
        self.cactus = Rectangle(Point(WIDTH-50, (HEIGHT//2)+50), Point(WIDTH, ((HEIGHT//2)-randint(1, 200))))
        self.cactus.setFill('green')
        
        return self.cactus

    def worldGen(self):
        
        self.dinosCreation()
        self.cactusCreation()
        
        self.win = GraphWin('Dino Evolution', WIDTH, HEIGHT)
        
        self.floor = Rectangle(Point(0, (HEIGHT//2)+51), Point(WIDTH, (HEIGHT//2)+60))
        self.floor.setFill('brown')
        
        self.floor.draw(self.win)
        self.cactus.draw(self.win)
        
        for i in range(self.number_dinos):    
            self.dino_dic[i][0].draw(self.win)
        
        time.sleep(0.3)
#       
    
    def moving(self):
        
        self.worldGen() 
        while self.speed <= 30:
            self.distance += self.speed*0.02
            print(self.distance)
            time.sleep(0.02)
            self.speed += 0.005
            self.cactus.move(-self.speed, 0)
            
            if int(self.distance)%22 == 1:

                self.cactus.undraw()
                self.cactus = self.cactusCreation()
                self.cactus.draw(self.win)
            
            if any(self.dino_dic[1]) ==
        
        while self.speed > 30:
            time.sleep(0.02)
            print(self.distance)
            self.distance += self.speed*0.02
            self.cactus.move(-self.speed, 0)  
            if int(self.distance)%22 == 1:
                
                self.cactus.undraw()
                self.cactus = self.cactusCreation()
                self.cactus.draw(self.win)
    
#        


#            self.distance += self.speed
#            self.gen_controller(self.speed)
#            time.sleep(0.05)
#            self.speed += 0.01
#            self.player.move(self.speed, self.gravity)
#            if self.jump == True:
#                self.player.move(self.speed, self.jump_force + self.gravity)
    
        

#din = Dino(4)
a = General(15)
#a.worldGen()
a.moving()

#getattr(Dino, 'dino_size')





#for i in range (number_of_dinos):
#    
#    dino = Rectangle(Point(50, HEIGHT//2), Point(100, (HEIGHT//2)+50))
#    dino.setFill(color_rgb(randint(0,255), randint(0,255), randint(0,255)))
#    
#    self.dinos_dic[i] = dino



#
#class Dinos(object):
#    
#    def __init__(self):
#        
#
#        self.gravity = 2
#        self.jump_force = -10
#        self.speed = 1
#        self.distance = 0
#        
#        self.win = GraphWin('Lab Four', WIDTH, HEIGHT)
#    
#        self.player = Rectangle(Point(50, HEIGHT//2), Point(100, (HEIGHT//2)+50))
#        self.player.setFill('blue')
#        self.floor = Rectangle(Point(0, (HEIGHT//2)+51), Point(WIDTH, (HEIGHT//2)+60))
#        self.floor.setFill('brown')
#
#    
#        self.player.draw(self.win)
#        self.floor.draw(self.win)
#        
#        
#    
#    def gen_controller(self, distance):
#        self.jump = False
#        if (distance%60) == 1:
#            self.cactus = Rectangle(Point(WIDTH-50, HEIGHT//2), Point(WIDTH, (HEIGHT//2)+randint(1, 200)))
#            self.cactus.setFill('green')
#            self.cactus.draw(self.win)
#
#    def moving_controller(self):
#        self.gen_controller()
#        
#        
#
#    def moving(self):
#        
#        while self.distance < (WIDTH//2) - 50:
#
#            self.distance += self.speed
#            self.gen_controller(self.speed)
#            time.sleep(0.05)
#            self.speed += 0.01
#            self.player.move(self.speed, self.gravity)
#            if self.jump == True:
#                self.player.move(self.speed, self.jump_force + self.gravity)


#
#Din = Dinos()
#Din.moving()