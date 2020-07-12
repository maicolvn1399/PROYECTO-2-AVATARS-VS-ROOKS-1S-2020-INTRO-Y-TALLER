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

salir1=False
avatar_knight_list = []
avatar_archer_list = []

sand_rook_list = []
rocks_bullet_list = []
fire_bullet_list = []
water_bullet_list = []

class SandRook(pygame.sprite.Sprite):
    def __init__(self,x,y,shootSeconds):
        self.live = True
        self.image = pygame.image.load("4.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 100
        self.attackPower = 4
        self.health = 14
        self.shootSeconds = shootSeconds
        self.shot_sand_count = 0

    def load_sand_rook(self):
        if hasattr(self,"image") and hasattr(self,"rect"):
            ventana.blit(self.image,self.rect)
        else:
            print("IMAGE SAND ROOK ERROR")

    def shoot_sand(self):
        should_fire_sand = False
        for avatar_knight in avatar_knight_list:#Un bucle por cada tipo de avatar
            if isColliding(avatar_knight.rect.x,avatar_knight.rect.y,self.rect.x,self.rect.y):
                should_fire_sand = True

        if self.live and should_fire_sand:
            self.shot_sand_count += 1
            if self.shot_sand_count == 25:
                sandBullet = SandBullet(self)
                ventana.sand_bullet_list.append(sandBullet)
                self.shot_sand_count = 0


class SandBullet(pygame.sprite.Sprite):
    def __init__(self,sandRook):
        self.live = True
        self.image = pygame.image.load("sandEffect.png")
        self.damage = 1
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.x = sandRook.rect.x + 60
        self.rect.y = sandRook.rect.y + 15

    def move_sand_bullet(self):
        if self.rect.x < WINDOWWIDTH:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_avatar(self):
        for avatar_knight in avatar_knight_list:#bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self,avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False

    def display_sand_bullet(self):
        ventana.blit(self.image,self.rect)

class AvatarKnight(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("avatarKnight.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.live = True
        self.stop = False
        self.damage = 3
        self.shoot_sword = False
        self.shoot_sword_seconds = 15
        self.health = 10
        self.seconds = 10

    def move_avatar_knight(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                salir1 = True

    def hit_rook(self):
        for sandrook in sand_rook_list: #hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

    def damage_rook(self,sandrook):
        sandrook.health -= self.damage
        if sandrook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_knight(self):
        ventana.blit(self.image,self.rect)

class RockRook(pygame.sprite.Sprite):
    def __init__(self,x,y,shootSeconds):
        self.live = True
        self.image = pygame.image.load("12.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.shootSeconds = shootSeconds
        self.price = 100
        self.attackPower = 4
        self.health = 14
        self.shot_rocks_count = 0

    def load_rock_rook(self):
        if hasattr(self,"image") and hasattr(self,"rect"):
            ventana.blit(self.image,self.rect)
        else:
            print("IMAGE ROCK ROOK ERROR")

    def shoot_rocks(self):
        should_fire_rocks = False
        for avatar_knight in avatar_knight_list:
            if isColliding(avatar_knight.rect.x,avatar_knight.rect.y,self.rect.x,self.rect.y):
                should_fire_rocks = True

        if self.live and should_fire_rocks:
            self.shot_rocks_count += 1
            if self.shot_rocks_count == 25:
                rocksBullet = RocksBullet(self)
                rocks_bullet_list.append(rocksBullet)
                self.shot_rocks_count = 0

class  RocksBullet(pygame.sprite.Sprite):
    def __init__(self,rockRook):
        self.live = True
        self.image = pygame.image.load("rockEffect.png")
        self.damage = 1
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.x = rockRook.rect.x + 60
        self.rect.y = rockRook.rect.y + 15

    def move_rock_bullet(self):
        if self.rect.x < WINDOWWIDTH:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_avatar(self):
        for avatar_knight in avatar_knight_list:
            if pygame.sprite.collide_rect(self,avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False

    def display_rock_bullet(self):
        ventana.blit(self.image,self.rect)


class FireRook(pygame.sprite.Sprite):
    def __init__(self,x,y,shootSeconds):
        self.live = True
        self.image = pygame.image.load("18.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 150
        self.attackPower = 8
        self.health = 16
        self.shootSeconds = shootSeconds
        self.shot_fire_count = 0

    def load_fire_rook(self):
        if hasattr(self,"image") and hasattr(self,"rect"):
            ventana.blit(self.image,self.rect)
        else:
            print("IMAGE FIRE ROOK ERROR")

    def shoot_rock(self):
        should_fire_fire = False
        for avatar_knight in avatar_knight_list:
            if isColliding(avatar_knight.rect.x,avatar_knight.rect.y,self.rect.x,self.rect.y):
                should_fire_fire = True

        if self.live and should_fire_fire:
            self.shot_fire_count += 1
            if self.shot_fire_count == 25:
                fireBullet = FireBullet(self)
                fire_bullet_list.append(fireBullet)
                self.shot_fire_count = 0

class FireBullet(pygame.sprite.Sprite):
    def __init__(self,fireRook):
        self.live = True
        self.image = pygame.image.load("fireEffect.png")
        self.damage = 1
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.x = fireRook.rect.x + 60
        self.rect.y = fireRook.rect.y + 15

    def move_rock_bullet(self):
        if self.rect.x < WINDOWWIDTH:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_avatar(self):
        for avatar_knight in avatar_knight_list:
            if pygame.sprite.collide_rect(self,avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False

    def display_rock_bullet(self):
        ventana.blit(self.image,self.rect)

class WaterRook(pygame.sprite.Sprite):
    def __init__(self,x,y,shootSeconds):
        self.live = True
        self.image = pygame.image.load("8.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 150
        self.attackPower = 8
        self.health = 16
        self.shootSeconds = shootSeconds
        self.shot_water_count = 0

    def load_water_rook(self):
        if hasattr(self, "image") and hasattr(self, "rect"):
            ventana.blit(self.image, self.rect)
        else:
            print("IMAGE WATER ROOK ERROR")

    def shoot_sand(self):
        should_fire_water = False
        for avatar_knight in avatar_knight_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_knight.rect.x, avatar_knight.rect.y, self.rect.x, self.rect.y):
                should_fire_water = True

        if self.live and should_fire_water:
            self.shot_water_count_count += 1
            if self.shot_water_count_count == 25:
                waterBullet = WaterBullet(self)
                ventana.sand_bullet_list.append(waterBullet)
                self.shot_water_count_count = 0


class WaterBullet(pygame.sprite.Sprite):
    def __init__(self,waterRook):
        self.live = True
        self.image = pygame.image.load("waterEffect.png")
        self.damage = 1
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.x = waterRook.rect.x + 60
        self.rect.y = waterRook.rect.y + 15

    def move_water_bullet(self):
        if self.rect.x < WINDOWWIDTH:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_avatar(self):
        for avatar_knight in avatar_knight_list:  # bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self, avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False

    def display_water_bullet(self):
        ventana.blit(self.image,self.rect)


class AvatarArcher(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("avatarArcher.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.live = True
        self.stop = False
        self.damage = 2
        self.shoot_arrow = False
        self.shoot_arrow_seconds = 10
        self.health = 5
        self.seconds = 12

    def move_avatar_archer(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                salir1 = True

    def hit_rook(self):
        for sandrook in sand_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

    def damage_rook(self, sandrook):
        sandrook.health -= self.damage
        if sandrook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_archer(self):
        ventana.blit(self.image, self.rect)


class AvatarLumberjack(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("avatarLumberjack.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.live = True
        self.stop = False
        self.damage = 9
        self.shoot_axe = False
        self.shoot_axe_seconds = 5
        self.health = 20
        self.seconds = 13

    def move_avatar_lumberjack(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                salir1 = True

    def hit_rook(self):
        for sandrook in sand_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

    def damage_rook(self, sandrook):
        sandrook.health -= self.damage
        if sandrook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_lumberjack(self):
        ventana.blit(self.image, self.rect)

class AvatarCannibal(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("avatarCannibal.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.live = True
        self.stop = False
        self.damage = 12
        self.shoot_stick = False
        self.shoot_stick_seconds = 3
        self.health = 25
        self.seconds = 14

    def move_avatar_cannibal(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                salir1 = True

    def hit_rook(self):
        for sandrook in sand_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

    def damage_rook(self, sandrook):
        sandrook.health -= self.damage
        if sandrook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_cannibal(self):
        ventana.blit(self.image, self.rect)

pygame.init()
#----Fondos------------------------------------
fondo1= pygame.image.load("5.png")

#----Fondos Niveles------------------------------------
backgroundLevel1 = pygame.image.load("backgroundLevel1.png")

#----constantes--------------------------------
NEGRO=(2, 22, 34)#formato RGB
COLOR1=(255, 137, 3)
COLOR2=(118, 228, 0 )
COLOR3=(242, 164, 0 )
COLOR4=(169, 236, 12   )
COLOR5=(253, 198, 28  )
COLOR11=(255, 99, 3)
COLOR21=(103, 198, 0)
COLOR31=(217, 126, 0)
COLOR41=(156, 191, 0)
COLOR51=(222, 183, 27)
#---------------
ANCHO=1050
ALTO=750
#---------------
tamboton1=[320,45]#tamaño de nuestro boton(x,y)
boton1=[360,450]#coordenadas de la poscicion de nuestro boton
colorboton1=[COLOR1,COLOR11]#colores que tendra nuestro boton

boton2=[360,500]
colorboton2=[COLOR2,COLOR21]

boton3=[360,550]
colorboton3=[COLOR3,COLOR31]

boton4=[360,600]
colorboton4=[COLOR4,COLOR41]

boton5=[360,650]
colorboton5=[COLOR5,COLOR51]



#------------------------------------------------
ventana= pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("")
clock=pygame.time.Clock()
#----fuentes-------------------------------------
fuentet1=pygame.font.SysFont("Turtles",28)
fuentet2=pygame.font.SysFont("Turtles",48)
fuentet3=pygame.font.SysFont("Turtles",98)
fuentet4=pygame.font.SysFont("Turtles",120)
fuentet5=pygame.font.SysFont("Gloucester MT",55)
#fuentet6=pygame.font.SysFont("Gloucester MT",55)
#----Tamaño del texto----------------------------

#-----------------CONSTANTES PARA LA MATRIZ---------
FLOOR = pygame.image.load('map.png')
GRIDSIZE = 16 #grid size of the map, eg. map will be 16 * 16, when GRIDSIZE = 16
BRIGHTBLUE = (0, 170, 255)
BGCOLOR = BRIGHTBLUE
FPS = 40 #frames per second, the speed rate of the prgram
WINDOWWIDTH = 1000 #window's width in pixel
WINDOWHEIGHT = 800 #window's height in pixel
BG = pygame.image.load("backgroundLevel1.png")

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
#---------------------------------------------------

rookFireCard = pygame.image.load("clickableFireRook.jpg")
rookWaterCard = pygame.image.load("clickableWaterRook.jpg")
rookSandCard = pygame.image.load("clickableSandRook.jpg")
rookRockRook = pygame.image.load("clickableRockRook.jpg")

rookFireCardRect = rookFireCard.get_rect()
rookWaterCardRect = rookWaterCard.get_rect()
rookSandCardRect = rookSandCard.get_rect()
rookRockRookRect = rookRockRook.get_rect()



#----------Fire animation for fire rook--------------
countSpritesFire = 0


def isColliding(enemyX, enemyY, rookXCoord, rookYCoord):
    """Determines the distance between two objects, gets the coordinates in x and y
    of the rook and the enemy"""
    """Code based on 
    https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint"""

    distance = math.sqrt((math.pow(enemyX - rookXCoord, 2)) + (math.pow(enemyY - rookYCoord, 2)))
    if distance < 41:
        return True
    else:
        return False

def objetotexto(text,color,tam):
     if tam=="peque":
          texto=fuentet1.render(text,True, color)
     if tam=="mediana":
          texto=fuentet2.render(text,True, color)
     if tam=="grande":
          texto=fuentet3.render(text,True, color)
     if tam=="gigante":
          texto=fuentet4.render(text,True, color)
     if tam=="normal":
          texto=fuentet5.render(text,True, color)
##     if tam=="normal2":
##          texto=fuentet5.render(text,True, color) 
     return texto,texto.get_rect()
#----Mensajes------------------------------------
def mensaje(msg,color,desy=0,tam="peque"):
     texto,textoRect=objetotexto(msg,color,tam)
     textoRect.center=int(ANCHO/2),int((ALTO/2)+desy)
     ventana.blit(texto,textoRect)
#----texto del boton-----------------------------
def txtboton(msg,color,botonx,botony,anchob,altob,tam="peque"):
     texto,textoRect=objetotexto(msg,color,tam)
     textoRect.center=int(botonx+anchob/2),int((botony+altob/2))
     ventana.blit(texto,textoRect)     
#----Botones-------------------------------------
"""
entrada=textodel boton,superficie,el color del boton(estado), el lugar,el tamaño, un identificador, un mensaje,un segundo mensaje
salida= coloca uun boton y le permite funcionar
restricciones= el tamaño y las posicion tiene que ser listas
"""

def botones(texto,superficie,estado,posicion,tam,ID=None,ms=None,ms2=None):
     cursor=pygame.mouse.get_pos()
     click=pygame.mouse.get_pressed()
     if posicion[0]+tam[0] > cursor[0] > tam[0] and posicion[1]+tam[1]> cursor[1]>tam[1] and posicion[1]+tam[1]<cursor[1]+tam[1]:
          boton=pygame.draw.rect(superficie,estado[1],(posicion[0],posicion[1],tam[0],tam[1]))
          if click[0]==1:
               if ID=="inicio":
                    pygame.mixer.music.pause()
                    opciones()
               elif ID=="info":
                    pygame.mixer.music.pause()
                    instruccion()
               elif ID=="puntajes":
                    puntuaciones()
                    pygame.mixer.music.pause()
               elif ID=="creditos":
                    pygame.mixer.music.pause()
                    Creditos()
               elif ID=="salir":
                    introjuego=False
                    quit()
               elif ID=="salir1":
                    introduccion()
               elif ID=="nivel1":
                    pygame.mixer.music.stop()
                    cuentainicio(ms,1)
               elif ID=="nivel2":
                    cuentainicio(ms,2)
               elif ID=="nivel3":
                    cuentainicio(ms,3)
               elif ID=="pausa":
                    pausa()
               elif ID=="volver":
                    pausado=False
               elif ID=="ok":
                    niveles(ms)
               
     else:
          
          boton=pygame.draw.rect(superficie,estado[0],(posicion[0],posicion[1],tam[0],tam[1]))
     txtboton(texto,NEGRO,posicion[0],posicion[1],tam[0],tam[1])
     return boton
    
#----pantalla creditos---------------------------
def Creditos():
     entrada = True
     while entrada:
          
          for event in pygame.event.get():
               if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         quit()
               ventana.blit(fondo1,(0,0))
               botones("volver",ventana,colorboton4,boton5,tamboton1,ID="salir1") 
               mensaje("Creditos",COLOR4,-200,tam="grande")
               mensaje("Desarrollado en Costa Rica",NEGRO,-75,tam="peque")
               mensaje("Tecnologico de Costa Rica, Ingenieria en Computadores",NEGRO,-40,tam="peque")
               mensaje("CE1102-Taller de Programacion, Grupo 4",NEGRO,-5,tam="peque")
               mensaje("Profesor Jason Leiton Jimenez",NEGRO,+30,tam="peque")
               mensaje("Version 1.0",NEGRO,+65,tam="peque")
               mensaje("Realizado por Raquel Lizano y Michael Valverde",NEGRO,+100,tam="peque")
               mensaje("II Proyecto - I Semestre - 2020",NEGRO,+135,tam="peque")
               pygame.display.update()
               clock.tick(15) 
                     
#----pantallade inicio---------------------------
def introduccion():
     #pygame.mixer.music.load("cancion1.mp3")
     #pygame.mixer.music.set_volume(0.125) 
     introjuego=True
     #pygame.mixer.music.play()
     
     while introjuego:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    introjuego=False
                    quit()  
               ventana.blit(fondo1,(0,0))
               botones("Inicio",ventana,colorboton1,boton1,tamboton1,ID="inicio")
               botones("Instrucciones",ventana,colorboton2,boton2,tamboton1,ID="info")
               botones("Mejor puntaje",ventana,colorboton3,boton3,tamboton1,ID="puntajes")
               botones("Creditos",ventana,colorboton4,boton4,tamboton1,ID="creditos")
               botones("Salir",ventana,colorboton5,boton5,tamboton1,ID="salir") 
               mensaje("Avatars VS Rooks",COLOR1,-100,tam="grande")
               pygame.display.update()
               clock.tick(15)
#----Instrucciones--------------------------------
def instruccion():
     instruccion=True
     while instruccion:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    instruccion=False
                    quit()
                    
               ventana.blit(fondo1,(0,0))
               
               botones("Volver",ventana,colorboton2,boton5,tamboton1,ID="salir1") 
               mensaje("Instrucciones",COLOR2,-200,tam="grande")
               mensaje(" ",NEGRO,-75,tam="normal")
               mensaje(" ",NEGRO,-40,tam="normal")
               mensaje("",NEGRO,-5,tam="normal")
               mensaje("",NEGRO,+30,tam="normal")
               pygame.display.update()
               clock.tick(15)
#----opciones-------------------------------------
def opciones():
    font = pygame.font.SysFont("normal", 40)

    input_box = pygame.Rect(boton2,tamboton1)
    color_inactive = pygame.Color('chartreuse3')
    color_active = pygame.Color('chartreuse1')
    color = color_inactive
    active = False
    text = ''
    atras=True
    while atras:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    atras=False
               if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                         active = not active
                    else:
                         active = False
                    color = color_active if active else color_inactive
               if event.type==pygame.KEYDOWN:
                    if active:
                         if event.key == pygame.K_RETURN:
                              print (text)
                              niveles(text)
                              text = ''
                              
                         elif event.key == pygame.K_BACKSPACE:
                              text = text[:-1]
                         else:
                              text += event.unicode
                    
               
               ventana.blit(fondo1,(0,0))
               txt_surface = font.render(text, True, color)
               width = max(320, txt_surface.get_width()+20)
               input_box.w = width
               ventana.blit(txt_surface, (input_box.x+5, input_box.y+5))
               pygame.draw.rect(ventana, color, input_box,4)
               botones("Volver",ventana,colorboton1,boton4,tamboton1,ID="salir1")
               mensaje("Opciones del juego",COLOR1,-100,tam="grande")
               mensaje("Ingrese su nombre de usuario",COLOR11 ,+30,tam="normal")
               mensaje("y presione 'ENTER' al finalizar.",COLOR11,+65,tam="normal")
               pygame.display.flip() 
               pygame.display.update()
               clock.tick(15)
#----niveles---------------------------------------
def niveles(text):
     atras=True
     while atras:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    atras=False
                    pygame.quit()
               
                    
               ventana.blit(fondo1,(0,0))
               botones("Volver",ventana,colorboton2,boton5,tamboton1,ID="salir1")
               botones("Nivel 1",ventana,colorboton1,boton2,tamboton1,ID="nivel1",ms=str(text))
               botones("Nivel 2",ventana,colorboton3,boton3,tamboton1,ID="nivel2",ms=str(text))
               botones("Nivel 3",ventana,colorboton5,boton4,tamboton1,ID="nivel3",ms=str(text))
               mensaje("Hola"+" "+str(text),COLOR1,-100,tam="grande")
               mensaje("Selecciona un nivel",COLOR1,+50,tam="normal")
              
               pygame.display.update()
               clock.tick(15)               
#----Puntuaciones----------------------------------
def puntuaciones():
     entrada = True
     while entrada:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    entrada=False
                    
               ventana.blit(fondo1,(0,0))
               botones("Volver",ventana,colorboton3,boton5,tamboton1,ID="salir1")
               mensaje("Puntuaciones",COLOR3,-200,tam="grande")
              # mensaje(contenido,BLANCO,tam="mediana")
               pygame.display.update()
               clock.tick(15)  


#----Cuenta inicial-------------------------------
"""               
entrada=nombre del jugador
salida=cuenta regresiva
restriccion=no tiene
"""               
def cuentainicio(nombre,n):
    cuenta=True

    while cuenta:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            if n==1:
                 ventana.blit(fondo1,(0,0))
                 mensaje("3",COLOR11,tam="gigante")            
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0))
                 mensaje("2",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0))
                 mensaje("1",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0)) 
                 mensaje("VAMOS",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 Gameloop(nombre)
            if n==2:
                 ventana.blit(fondo1,(0,0))
                 mensaje("3",COLOR11,tam="gigante")            
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0))
                 mensaje("2",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0))
                 mensaje("1",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0)) 
                 mensaje("VAMOS",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 Gameloop1(nombre)
            if n==3:
                 ventana.blit(fondo1,(0,0))
                 mensaje("3",COLOR11,tam="gigante")            
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0))
                 mensaje("2",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0))
                 mensaje("1",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 ventana.blit(fondo1,(0,0)) 
                 mensaje("VAMOS",COLOR11,tam="gigante")
                 pygame.display.update()
                 clock.tick(1)
                 Gameloop2(nombre)






#----nivel1----------------------------------------
#entrada= 
#salida=
          
def Gameloop(nombre):
#Constantes para iniciar la matriz--------
     FPSCLOCK = pygame.time.Clock()
     mousex = 0
     mousey = 0
     mouseClicked = False
#----------------------------------------
     salir1=False
     global avatar_knight_list
     avatar_knight_list = []

     global sand_rook_list
     sand_rook_list = []

     global rocks_bullet_list
     rocks_bullet_list = []

    
#------bucle de inicio--------------------------
     while not salir1:
          drawBoard()#Dibuja la matriz
          r = SandRook(100,100,10)
          r.load_sand_rook()

          a = AvatarKnight(500,200)
          a.display_avatar_knight()
          a.move_avatar_knight()

          archer = AvatarArcher(400,200)
          archer.display_avatar_archer()
          archer.move_avatar_archer()

          cannibal = AvatarCannibal(300,200)
          cannibal.display_avatar_cannibal()
          cannibal.move_avatar_cannibal()

          lumberjack = AvatarLumberjack(200,200)
          lumberjack.display_avatar_lumberjack()
          lumberjack.move_avatar_lumberjack()





          s = SandBullet(r)
          s.display_sand_bullet()
          s.move_sand_bullet()

          rw = WaterRook(500,300,60)
          rw.load_water_rook()
          rwb = WaterBullet(rw)
          rwb.display_water_bullet()
          rwb.move_water_bullet()

          rr = RockRook(500,380,60)
          rr.load_rock_rook()
          rrb = RocksBullet(rr)
          rrb.display_rock_bullet()
          rrb.move_rock_bullet()

          fr = FireRook(500,420,89)
          fr.load_fire_rook()
          frb = FireBullet(fr)
          frb.display_rock_bullet()
          frb.move_rock_bullet()

          pygame.time.delay(100) 
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    salir1=True
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   mouseClicked = True
                   mousex, mousey = pygame.mouse.get_pos()
               elif event.type == pygame.MOUSEBUTTONUP:
                   mouseClicked = False
               elif event.type == pygame.MOUSEMOTION:
                   mouse_position = pygame.mouse.get_pos()


               if mouseClicked and mousex>0 and mousex<80 and mousey>600 and mousey<700:
                   print("NEW FIRE ROOK CREATED ")
               if mouseClicked and mousex>80 and mousex<178 and mousey>600 and mousey<695:
                   print("NEW ROCK ROOK CREATED")
               if mouseClicked and mousex>172 and mousex<277 and mousey>600 and mousey<693:
                   print("NEW WATER ROOK CREATED")
               if mouseClicked and mousex>275 and mousex<385 and mousey>600 and mousey<695:
                   print("NEW SAND ROOK CREATED")






               #ventana.blit(backgroundLevel1,(0,0))
               mensaje("Nivel 1",COLOR3,-200,tam="grande")
               botones("Pausa",ventana,colorboton5,boton5,tamboton1,ID="pausa")
               pygame.display.update()
               clock.tick(60)
##-------condicion de game over--------------------
##          if vida<=0:
##                GameOver(nombre,puntos)
        
          pygame.display.update()
          clock.tick(60)
           
#----nivel2----------------------------------------
"""
entrada=nombre del jugador 
salida=pantalla de juego con enemigos y un jugado, tambien incluye marcador y tiempo
"""
def Gameloop1(nombre):
     
##     pygame.mixer.music.load("cancion2.mp3")
##     pygame.mixer.music.play()
     salir1=False
     
#------bucle de inicio--------------------------
     while not salir1:
          #tiempo =pygame.mixer.music.get_pos()
     
          pygame.time.delay(100) 
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    salir1=True
               ventana.blit(fondo1,(0,0))
               mensaje("Nivel 2",COLOR3,-200,tam="grande")
               botones("Pausa",ventana,colorboton5,boton5,tamboton1,ID="pausa")
        
          pygame.display.update()
          clock.tick(60)

#----Nivel3----------------------------------------
"""          
#entrada=nombre del jugador 
#salida=pantalla de juego con enemigos y un jugado, tambien incluye marcador y tiempo
"""
def Gameloop2(nombre):
     
##     pygame.mixer.music.load("cancion2.mp3")
##     pygame.mixer.music.play()
     salir1=False
     
#------bucle de inicio--------------------------
     while not salir1:
          #tiempo =pygame.mixer.music.get_pos()
     
          pygame.time.delay(100) 
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    salir1=True
               ventana.blit(fondo1,(0,0))
               mensaje("Nivel 3",COLOR3,-200,tam="grande")
               botones("Pausa",ventana,colorboton5,boton5,tamboton1,ID="pausa")
          pygame.display.update()
          clock.tick(60)          
#----Game over-------------------------------------
def GameOver(nombre,puntos):
     salir=False
     while not salir:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    salir=True
          
          ventana.blit(fondo1,(0,0))
          botones("volver a jugar",ventana,colorboton5,boton5,tamboton1,ID="ok",ms=str(nombre))    
          mensaje("tu puntuacion fue de:"+str(puntos),NEGRO,90,tam="peque")
          mensaje("",VERDE,tam="grande")
          pygame.display.update()
          clock.tick(15)
#----Pausa------------------------------------------
def pausa():
     pausado=True
     while pausado:
          for event in pygame.event.get():

               botones("volver",ventana,colorboton4,boton4,tamboton1,ID="volver") 
               botones("salir",ventana,colorboton5,boton5,tamboton1,ID="salir1")
               

          mensaje("Juego en pausa",COLOR2,tam="grande")
          pygame.display.update()
          clock.tick(15)          
#---------------------------------------------------

#-----------FUNCIONES PARA LA MATRIZ----------------
#initialize the map
def initialMap():
    map = []
    for i in range(5):
        column = []
        for j in range(9):
            column.append(0)
        map.append(column)
    return map



#draw the board and auxiliary settings
def drawBoard():
    ventana.fill(BGCOLOR)
    ventana.blit(BG, (0, 0))
    floory = 100
    for i in range(5):
        floorx =95
        ventana.blit(FLOOR, (floorx, floory))
        for j in range (9):
            ventana.blit(FLOOR, (floorx, floory))
            floorx += 95
        floory += 100

def getGridAtPixel(mouseX,mouseY):
    gridX = (mouseX-40)/50
    gridY = (mouseY-60)/40
    if gridX>= 0 and gridX<=15 and gridY>=0 and gridY <= 15:
        return gridX,gridY
    else:
        return None,None
#---------------------------------------------------

#----------------FUNCIONES PARA LEER Y ESCRIBIR EN ARCHIVOS------

def ReadFile():
    """This function reads the file of the scores
    and return the content in a list"""
    path = ""
    file = open(path)
    content = file.readlines()
    file.close()
    return content

def WriteInFile(score):
    """This function writes the score on the file"""
    path = ""
    file = open(path,"a")
    file.write(score+"\n")
    file.close()


def LoadImage(ImgName):
    """Loads and image"""
    path = os.path.join('media', ImgName)
    imageToLoad = PhotoImage(file=path)
    return imageToLoad
#---------------------------------------------------------------------------------------------------
introduccion()
creditos()
opciones()
puntuaciones()
Gameloop()
Gameloop1()
Gameloop2()
pausa()


