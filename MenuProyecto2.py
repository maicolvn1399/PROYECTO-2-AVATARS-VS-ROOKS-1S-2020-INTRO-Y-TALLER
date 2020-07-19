"""
Instituto Tecnológico de Costa Rica
Área de Ingeniería en Computadores
CE1102 - Taller de Programación
Profesor: Jason Leitón Jiménez
Estudiantes: Raquel Lizano y Michael Valverde
II Proyecto - I Semestre - 2020
"""


import pygame
import sys
import math
import os
import random
from pygame.locals import*
import time
pygame.init()
salir1=False

#----input box-------------------------------------
win = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = pygame.Color('chartreuse3')
COLOR_ACTIVE = pygame.Color('chartreuse1')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    def gettxt(self):
          return self.text
    def settxt(self,txt):
          self.text=txt
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, win):
        # Blit the text.
        win.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(win, self.color, self.rect, 4)
            


#----Fondos------------------------------------
fondo1= pygame.image.load("5.jpg")


#----constants--------------------------------
BLACK=(2, 22, 34)#RGB format
COLOR1=(255, 137, 3)
COLOR2=(118, 228, 0)
COLOR3=(242, 164, 0)
COLOR4=(169, 236, 12)
COLOR5=(253, 198, 28)
COLOR11=(255, 99, 3)
COLOR21=(103, 198, 0)
COLOR31=(217, 126, 0)
COLOR41=(156, 191, 0)
COLOR51=(222, 183, 27)
#---------------
WIDTH=1100
HEIGH=600
#---------------
buttonsize1=[320,45]#tamaño de nuestro boton(x,y)
button1=[375,300]#coordenadas de la poscicion de nuestro boton
buttoncolor1=[COLOR1,COLOR11]#colores que tendra nuestro boton

button2=[375,350]
buttoncolor2=[COLOR2,COLOR21]

button3=[375,400]
buttoncolor3=[COLOR3,COLOR31]

button4=[375,450]
buttoncolor4=[COLOR4,COLOR41]

button5=[375,500]
buttoncolor5=[COLOR5,COLOR51]



#------------------------------------------------
win= pygame.display.set_mode((WIDTH,HEIGH))
pygame.display.set_caption("")
clock=pygame.time.Clock()

#-----------------CONSTANTES PARA LA MATRIZ---------



#----font-------------------------------------
fontsize1=pygame.font.SysFont("Turtles",28)
fontsize2=pygame.font.SysFont("Turtles",48)
fontsize3=pygame.font.SysFont("Turtles",98)
fontsize4=pygame.font.SysFont("Turtles",120)
fontsize5=pygame.font.SysFont("Gloucester MT",55)
#fuentet6=pygame.font.SysFont("Gloucester MT",55)
#----Tamaño del texto----------------------------
def textObject(text,color,size):
     if size=="small":
          text=fontsize1.render(text,True, color)
     if size=="medium":
          text=fontsize2.render(text,True, color)
     if size=="big":
          text=fontsize3.render(text,True, color)
     if size=="giant":
          text=fontsize4.render(text,True, color)
     if size=="regular":
          text=fontsize5.render(text,True, color)
##     if tam=="normal2":
##          texto=fuentet5.render(text,True, color) 
     return text,text.get_rect()
#----Mensajes------------------------------------
def message(msg,color,desx=0,desy=0,size="small"):
     text,rect_text=textObject(msg,color,size)
     rect_text.center=int(WIDTH/2)+desx,int((HEIGH/2)+desy)
     win.blit(text,rect_text)
#----texto del boton-----------------------------
def buttontext(msg,color,buttonx,buttony,anchob,highb,size="small"):
     text,rect_text=textObject(msg,color,size)
     rect_text.center=int(buttonx+anchob/2),int((buttony+highb/2))
     win.blit(text,rect_text)     
#----Botones-------------------------------------
"""
entry=text,surface,state,position,size,ID 
return=buttons and their functions 
restraint:size, positions have to be part of a list
"""

def buttons(text,surface,state,position,size,ID=None,ms=None,ms2=None):
     cursor=pygame.mouse.get_pos()
     click=pygame.mouse.get_pressed()
     if position[0]+size[0] > cursor[0] > size[0] and position[1]+size[1]> cursor[1]>size[1] and position[1]+size[1]<cursor[1]+size[1]:
          button=pygame.draw.rect(surface,state[1],(position[0],position[1],size[0],size[1]))
          if click[0]==1:
               if ID=="start":
                    pygame.mixer.music.pause()
                    option()
               elif ID=="info":
                    pygame.mixer.music.pause()
                    instructions()
               elif ID=="point":
                    puntuations()
                    pygame.mixer.music.pause()
               elif ID=="credits":
                    pygame.mixer.music.pause()
                    Credits()
               elif ID=="exit":
                    Gameintro=False
                    quit()
               elif ID=="exit1":
                    introduction()
               elif ID=="level1":
                    pygame.mixer.music.stop()
                    StartCount(ms,ms2,1)
               elif ID=="level2":
                    startCount(ms,mas2,2)
               elif ID=="level3":
                    startCount(ms,ms2,3)
               elif ID=="pause":
                    pause()
               elif ID=="back":
                    pause=False
               elif ID=="ok":
                    levels(ms,ms2)
               
     else:
          
          button=pygame.draw.rect(surface,state[0],(position[0],position[1],size[0],size[1]))
     buttontext(text,BLACK,position[0],position[1],size[0],size[1])
     return button
    
#----pantalla creditos---------------------------
def Credits():
     entry = True
     while entry:
          
          for event in pygame.event.get():
               if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         quit()
               win.blit(fondo1,(0,0))
               buttons("volver",win,buttoncolor4,button5,buttonsize1,ID="exit1") 
               message("Creditos",COLOR4,0,-200,size="big")
               message("Desarrollado en Costa Rica",BLACK,0,-75,size="small")
               message("Tecnologico de Costa Rica, Ingenieria en Computadores",BLACK,0,-40,size="small")
               message("CE1102-Taller de Programacion, Grupo 4",BLACK,0,-5,size="small")
               message("Profesor Jason Leiton Jimenez",BLACK,0,+30,size="small")
               message("Version 1.0",BLACK,0,+65,size="small")
               message("Realizado por Raquel Lizano y Michael Valverde",BLACK,0,+100,size="small")
               message("II Proyecto - I Semestre - 2020",BLACK,0,+135,size="small")
               pygame.display.update()
               clock.tick(15) 
                     
#----pantallade inicio---------------------------
def  introduction():
     #pygame.mixer.music.load("cancion1.mp3")
     #pygame.mixer.music.set_volume(0.125) 
     Gameintro=True
     #pygame.mixer.music.play()
     
     while Gameintro:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    Gameintro=False
                    quit()  
               win.blit(fondo1,(0,0))
               buttons("Inicio",win,buttoncolor1,button1,buttonsize1,ID="start")
               buttons("Instrucciones",win,buttoncolor2,button2,buttonsize1,ID="info")
               buttons("Mejor puntaje",win,buttoncolor3,button3,buttonsize1,ID="point")
               buttons("Creditos",win,buttoncolor4,button4,buttonsize1,ID="credits")
               buttons("Salir",win,buttoncolor5,button5,buttonsize1,ID="exit") 
               message("Avatars VS Rooks",COLOR1,-15,-200,size="big")
               pygame.display.update()
               clock.tick(15)
#----Instrucciones--------------------------------
def instructions():
     instruccion=True
     while instruccion:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    instruccion=False
                    quit()
                    
               win.blit(fondo1,(0,0))
               
               buttons("Volver",win,buttoncolor2,button5,buttonsize1,ID="exit1") 
               message("Instrucciones",COLOR2,0,-200,size="big")
               message(" ",BLACK,-75,size="regular")
               message(" ",BLACK,-40,size="regular")
               message("",BLACK,-5,size="regular")
               message("",BLACK,+30,size="regular")
               pygame.display.update()
               clock.tick(15)
#----opciones-------------------------------------
def option():
    lock = pygame.time.Clock()
    input_box1 = InputBox(450,240, 360, 32)
    input_box2 = InputBox(450,325, 360, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RETURN:
                     if input_boxes[0].gettxt()!='' and input_boxes[1].gettxt()!='':
                         levels(input_boxes[0].gettxt(),input_boxes[1].gettxt())
                         input_boxes[0].settxt('')
                         input_boxes[1].settxt('')
                                
        for box in input_boxes:
            box.update()

        win.blit(fondo1,(0,0))
        for box in input_boxes:
            box.draw(win)     
        buttons("Volver",win,buttoncolor1,button4,buttonsize1,ID="exit1")
        message("Opciones del juego",COLOR1,-20,-200,size="big")
        message("Ingrese su nombre de usuario",COLOR11 ,+30,-80,size="regular")
        message("Ingrese la frecuencia de ataque(digitos)",COLOR11 ,+30,0,size="regular")
        message("presione 'ENTER' al finalizar.",COLOR11,+30,+90,size="regular")
        pygame.display.flip() 
        pygame.display.update()
        clock.tick(15)
#----niveles---------------------------------------
def levels(name, speed):
     
     level=True
     while level:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    level=False
                    pygame.quit()
               
                    
               win.blit(fondo1,(0,0))
               buttons("Volver",win,buttoncolor2,button5,buttonsize1,ID="exit1")
               buttons("Nivel 1",win,buttoncolor1,button2,buttonsize1,ID="level1",ms=str(name),ms2=str(speed))
               buttons("Nivel 2",win,buttoncolor3,button3,buttonsize1,ID="level2",ms=str(name),ms2=str(speed))
               buttons("Nivel 3",win,buttoncolor5,button4,buttonsize1,ID="level3",ms=str(name),ms2=str(speed))
               message("Hola"+" "+str(name),COLOR1,0,-100,size="big")
               message("Selecciona un nivel",COLOR1,0,0,size="regular")
                      
              
               pygame.display.update()
               clock.tick(15)               
#----Puntuaciones----------------------------------
def puntuations():
     entry= True
     while entry:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    entry=False
                    
               win.blit(fondo1,(0,0))
               buttons("Volver",win,buttoncolor3,button5,buttonsize1,ID="exit1")
               message("Puntuaciones",COLOR3,0,-200,size="big")
              # mensaje(contenido,BLANCO,tam="mediana")
               pygame.display.update()
               clock.tick(15)  


#----Cuenta inicial-------------------------------
"""               
entry=player name
return=count 
restraint=none
"""               
def StartCount(name,speed,n):
    count=True

    while count:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            if n==1:
                 win.blit(fondo1,(0,0))
                 message("READY",COLOR11,size="giant")            
                 pygame.display.update()
                 time.sleep(1)
                 win.blit(fondo1,(0,0))
                 message("GO!",COLOR11,size="giant")
                 pygame.display.update()
                 time.sleep(1)
                 Gameloop(name,speed)
            if n==2:
                 win.blit(fondo1,(0,0))
                 message("READY",COLOR11,size="giant")            
                 pygame.display.update()
                 time.sleep(1)
                 win.blit(fondo1,(0,0))
                 message("GO!",COLOR11,size="giant")
                 pygame.display.update()
                 time.sleep(1)
                 Gameloop1(name,speed)
            if n==3:
                 win.blit(fondo1,(0,0))
                 message("READY",COLOR11,size="giant")            
                 pygame.display.update()
                 time.sleep(1)
                 win.blit(fondo1,(0,0))
                 message("GO!",COLOR11,size="giant")
                 pygame.display.update()
                 time.sleep(1)
                 
                 Gameloop2(name,speed)






#----nivel1----------------------------------------
"""entry=player name 
return=surface with  the game 
restraint:none
"""
          
def Gameloop(name,speed):
#Constantes para iniciar la matriz--------
     FPSCLOCK = pygame.time.Clock()
     mousex = 0
     mousey = 0
     mouseClicked = False
#----------------------------------------
     exit1=False
     



#------bucle de inicio--------------------------
     while not exit1:
                  #ventana.fill(BGCOLOR)
         #ventana.blit(BG, (0, 0))




               #if mouseClicked and mousex>0 and mousex<80 and mousey>600 and mousey<700:
                   #print("NEW FIRE ROOK CREATED ")
               #if mouseClicked and mousex>80 and mousex<178 and mousey>600 and mousey<695:
                   #print("NEW ROCK ROOK CREATED")
               #if mouseClicked and mousex>172 and mousex<277 and mousey>600 and mousey<693:
                   #print("NEW WATER ROOK CREATED")
               #if mouseClicked and mousex>275 and mousex<385 and mousey>600 and mousey<695:
                   #print("NEW SAND ROOK CREATED")

               #ventana.blit(backgroundLevel1,(0,0))
         message("Nivel 1",COLOR3,-200,size="big")
         buttons("Pausa",win,buttoncolor5,button5,buttonsize1,ID="pause")
         pygame.display.update()
         clock.tick(60)
##-------condicion de game over--------------------
##          if vida<=0:
##                GameOver(nombre,puntos)
        
         pygame.display.update()
         clock.tick(60)
           
#----nivel2----------------------------------------
"""
entry=player name 
return=surface with  the game 
restraint:none
"""
def Gameloop1(name,speed):
     
##     pygame.mixer.music.load("cancion2.mp3")
##     pygame.mixer.music.play()
     exit1=False
     
#------bucle de inicio--------------------------
     while not exit1:
          #tiempo =pygame.mixer.music.get_pos()
     
          pygame.time.delay(100) 
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    exit1=True
               win.blit(fondo1,(0,0))
               message("Nivel 2",COLOR3,-200,size="big")
               buttons("Pausa",win,buttoncolor5,button5,buttonsize1,ID="pausa")
        
          pygame.display.update()
          clock.tick(60)

#----Nivel3----------------------------------------
"""          
entry=player name 
return=surface with  the game 
restraint:none
"""
def Gameloop2(name,speed):
     
##     pygame.mixer.music.load("cancion2.mp3")
##     pygame.mixer.music.play()
     exit1=False
     
#------bucle de inicio--------------------------
     while not exit1:
          #tiempo =pygame.mixer.music.get_pos()
     
          pygame.time.delay(100) 
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    exit1=True
               win.blit(fondo1,(0,0))
               message("Nivel 3",COLOR3,-200,size="big")
               buttons("Pausa",win,buttoncolor5,button5,buttonsize1,ID="pause")
          pygame.display.update()
          clock.tick(60)          
#----Game over-------------------------------------
def GameOver(name,points):
     exit1=False
     while not exit1:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    exit1=True
          
          win.blit(fondo1,(0,0))
          buttons("volver a jugar",win,buttoncolor5,button5,buttonsize1,ID="ok",ms=str(nombre))    
          message("tu puntuacion fue de:"+str(points),BLACK,90,size="small")
          message("",COLOR1,size="big")
          pygame.display.update()
          clock.tick(15)
#----Pausa------------------------------------------
def pause():
     pause=True
     while pausado:
          for event in pygame.event.get():

               buttons("volver",win,buttoncolor4,button4,buttonsize1,ID="back")
               buttons("salir",win,buttoncolor5,button5,buttonsize1,ID="exit1")
               buttons("menu principal",win,buttoncolor5,button5,buttonsize1,ID="exit")
               

          message("Juego en pausa",COLOR2,size="big")
          pygame.display.update()
          clock.tick(15)          
#---------------------------------------------------


#---------------------------------------------------

#----------------FUNCIONES PARA LEER Y ESCRIBIR EN ARCHIVOS------


#---------------------------------------------------------------------------------------------------
introduction()
Credits()
instruction()
option()
puntuations()
Gameloop()
Gameloop1()
Gameloop2()
pausa()


