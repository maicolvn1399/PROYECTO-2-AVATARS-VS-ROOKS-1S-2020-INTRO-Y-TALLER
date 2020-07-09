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
import random
from pygame.locals import*
import time

#----Avatar1=avatar arquero---------------------------------------------------------------------------------------
from AvatarsRooks import Rooks

Avatar1Die =       [pygame.image.load('Elf_01__DIE_000.png'), pygame.image.load('Elf_01__DIE_001.png'),
                    pygame.image.load('Elf_01__DIE_002.png'), pygame.image.load('Elf_01__DIE_003.png'),
                    pygame.image.load('Elf_01__DIE_004.png'), pygame.image.load('Elf_01__DIE_005.png'),
                    pygame.image.load('Elf_01__DIE_006.png'), pygame.image.load('Elf_01__DIE_007.png'),
                    pygame.image.load('Elf_01__DIE_008.png'), pygame.image.load('Elf_01__DIE_009.png')]

Avatar1attack  =  [pygame.image.load('Elf_01__ATTACK_000.png'), pygame.image.load('Elf_01__ATTACK_001.png'),
                   pygame.image.load('Elf_01__ATTACK_002.png'), pygame.image.load('Elf_01__ATTACK_003.png'),
                   pygame.image.load('Elf_01__ATTACK_004.png'), pygame.image.load('Elf_01__ATTACK_005.png'),
                   pygame.image.load('Elf_01__ATTACK_006.png'), pygame.image.load('Elf_01__ATTACK_007.png'),
                   pygame.image.load('Elf_01__ATTACK_008.png'), pygame.image.load('Elf_01__ATTACK_009.png')]

Avatar1Char =     [pygame.image.load('Elf_01__IDLE_000.png'), pygame.image.load('Elf_01__IDLE_001.png'),
                   pygame.image.load('Elf_01__IDLE_002.png'), pygame.image.load('Elf_01__IDLE_003.png'),
                   pygame.image.load('Elf_01__IDLE_004.png'), pygame.image.load('Elf_01__IDLE_005.png'),
                   pygame.image.load('Elf_01__IDLE_006.png'), pygame.image.load('Elf_01__IDLE_007.png'),
                   pygame.image.load('Elf_01__IDLE_008.png'), pygame.image.load('Elf_01__IDLE_009.png')]


#-----Avatar2=avatar escudero--------------------------------------------------------------------------------------
Avatar2Die =      [pygame.image.load('Knight_03__DIE_000.png'), pygame.image.load('Knight_03__DIE_001.png'),
                    pygame.image.load('Knight_03__DIE_002.png'), pygame.image.load('Knight_03__DIE_003.png'),
                    pygame.image.load('Knight_03__DIE_004.png'), pygame.image.load('Knight_03__DIE_005.png'),
                    pygame.image.load('Knight_03__DIE_006.png'), pygame.image.load('Knight_03__DIE_007.png'),
                    pygame.image.load('Knight_03__DIE_008.png'), pygame.image.load('Knight_03__DIE_009.png')]

Avatar2attack  =  [pygame.image.load('Knight_03__ATTACK_000.png'), pygame.image.load('Knight_03__ATTACK_001.png'),
                   pygame.image.load('Knight_03__ATTACK_002.png'), pygame.image.load('Knight_03__ATTACK_003.png'),
                   pygame.image.load('Knight_03__ATTACK_004.png'), pygame.image.load('Knight_03__ATTACK_005.png'),
                   pygame.image.load('Knight_03__ATTACK_006.png'), pygame.image.load('Knight_03__ATTACK_007.png'),
                   pygame.image.load('Knight_03__ATTACK_008.png'), pygame.image.load('Knight_03__ATTACK_009.png')]

Avatar2Char =     [pygame.image.load('Knight_03__IDLE_000.png'), pygame.image.load('Knight_03__IDLE_001.png'),
                   pygame.image.load('Knight_03__IDLE_002.png'), pygame.image.load('Knight_03__IDLE_003.png'),
                   pygame.image.load('Knight_03__IDLE_004.png'), pygame.image.load('Knight_03__IDLE_005.png'),
                   pygame.image.load('Knight_03__IDLE_006.png'), pygame.image.load('Knight_03__IDLE_007.png'),
                   pygame.image.load('Knight_03__IDLE_008.png'), pygame.image.load('Knight_03__IDLE_009.png')]

#----Avatar3=avatar lenador---------------------------------------------------------------------------------------
#este no tenia imagenes para morir y cada lista tiene 12 elementos en vez de 10 como las otras

Avatar3attack  =  [pygame.image.load('Golem_02_Attacking_000.png'), pygame.image.load('Golem_02_Attacking_000.png'),
                   pygame.image.load('Golem_02_Attacking_002.png'), pygame.image.load('Golem_02_Attacking_003.png'),
                   pygame.image.load('Golem_02_Attacking_004.png'), pygame.image.load('Golem_02_Attacking_005.png'),
                   pygame.image.load('Golem_02_Attacking_006.png'), pygame.image.load('Golem_02_Attacking_007.png'),
                   pygame.image.load('Golem_02_Attacking_008.png'), pygame.image.load('Golem_02_Attacking_009.png'),
                   pygame.image.load('Golem_02_Attacking_010.png'), pygame.image.load('Golem_02_Attacking_011.png')]

Avatar3Char =     [pygame.image.load('Golem_02_Idle_000.png'), pygame.image.load('Golem_02_Idle_001.png'),
                   pygame.image.load('Golem_02_Idle_002.png'), pygame.image.load('Golem_02_Idle_003.png'),
                   pygame.image.load('Golem_02_Idle_004.png'), pygame.image.load('Golem_02_Idle_005.png'),
                   pygame.image.load('Golem_02_Idle_006.png'), pygame.image.load('Golem_02_Idle_007.png'),
                   pygame.image.load('Golem_02_Idle_008.png'), pygame.image.load('Golem_02_Idle_009.png'),
                   pygame.image.load('Golem_02_Idle_010.png'), pygame.image.load('Golem_02_Idle_011.png')]


#----Avatar4=avatar canibal---------------------------------------------------------------------------------------
Avatar4Die =       [pygame.image.load('Troll_01_1_DIE_000.png'), pygame.image.load('Troll_01_1_DIE_001.png'),
                    pygame.image.load('Troll_01_1_DIE_002.png'), pygame.image.load('Troll_01_1_DIE_003.png'),
                    pygame.image.load('Troll_01_1_DIE_004.png'), pygame.image.load('Troll_01_1_DIE_005.png'),
                    pygame.image.load('Troll_01_1_DIE_006.png'), pygame.image.load('Troll_01_1_DIE_007.png'),
                    pygame.image.load('Troll_01_1_DIE_008.png'), pygame.image.load('Troll_01_1_DIE_009.png')]

Avatar4attack  =   [pygame.image.load('Troll_01_1_ATTACK_000.png'), pygame.image.load('Troll_01_1_ATTACK_001.png'),
                    pygame.image.load('Troll_01_1_ATTACK_002.png'), pygame.image.load('Troll_01_1_ATTACK_003.png'),
                    pygame.image.load('Troll_01_1_ATTACK_004.png'), pygame.image.load('Troll_01_1_ATTACK_005.png'),
                    pygame.image.load('Troll_01_1_ATTACK_006.png'), pygame.image.load('Troll_01_1_ATTACK_007.png'),
                    pygame.image.load('Troll_01_1_ATTACK_008.png'), pygame.image.load('Troll_01_1_ATTACK_009.png')]

Avatar4Char =      [pygame.image.load('Troll_01_1_IDLE_000.png'), pygame.image.load('Troll_01_1_IDLE_001.png'),
                    pygame.image.load('Troll_01_1_IDLE_002.png'), pygame.image.load('Troll_01_1_IDLE_003.png'),
                    pygame.image.load('Troll_01_1_IDLE_004.png'), pygame.image.load('Troll_01_1_IDLE_005.png'),
                    pygame.image.load('Troll_01_1_IDLE_006.png'), pygame.image.load('Troll_01_1_IDLE_007.png'),
                    pygame.image.load('Troll_01_1_IDLE_008.png'), pygame.image.load('Troll_01_1_IDLE_009.png')]
#----Rook1=sand rook----------------------------------------------------------------------------------------------

Rook1attack  =  [pygame.image.load('11.png'), pygame.image.load('13.png'),
                 pygame.image.load('12.png')]

Rook1Char = pygame.image.load('11.png')
#falta las bolas de ataque(cambiales el tamaño)

#----Rook2=rock rook----------------------------------------------------------------------------------------------

Rook2attack  =  [pygame.image.load('2.png'), pygame.image.load('3.png'),
                 pygame.image.load('4.png')]

Rook2Char = pygame.image.load('2.png')

#----Rook3=fire rook-----------------------------------------------------------------------------------------------
Rook3attack  =  [pygame.image.load('16.png'), pygame.image.load('17.png'),
                 pygame.image.load('18.png')]

Rook3Char = pygame.image.load('16.png')

#----Rook4=water rook-----------------------------------------------------------------------------------------------

Rook4attack  =  [pygame.image.load('6.png'), pygame.image.load('7.png'),
                   pygame.image.load('7.png')]

Rook4Char = pygame.image.load('6.png')


#-------------------------------------------------------------------------------------------------------------------



class Avatar():
    def __init__(self,type,row,column,attackPower,health,hit):
        if type == "avatar1":
            self.type = Avatar1Char
        elif type == "avatar2":
            self.type = Avatar2Char
        elif type == "avatar3":
            self.type = Avatar3Char
        else:
            self.type = Avatar4Char
        self.row = 0
        self.column = column
        self.attackPower = attackPower
        self.health = health
        self.hit = hit

    def GetType(self):
        return self.type

    def SetType(self,type):
        self.type = type

    def GetRow(self):
        return self.row

    def SetRow(self,row):
        self.row = row

    def GetColumn(self):
        return self.column

    def SetColumn(self,column):
        self.column = column

    def GetAttackPower(self):
        return self.attackPower

    def SetAttackPower(self,attackPower):
        self.attackPower = attackPower

    def GetHealth(self):
        return self.health

    def SetHealth(self,health):
        self.health = health

    def GetHit(self):
        return self.hit

    def SetHit(self,hit):
        self.hit = hit

    def walk(self):
        Count = 0
        ventana.blit(self.type[Count // 31],(self.row,self.column))
        Count += 1


    def GetInitialMap(self):
        map = []
        for i in range(5):
            column = []
            for j in range(9):
                column.append(0)
            map.append(column)
        return map

class Rooks:
    def __init__(self,type,row,column,attackPower,cost,health,damage):
        if type == "rook1":
             self.type = Rook1attack
        elif type == "rook2":
             self.type = Rook2attack
        elif type == "rook3":
             self.type = Rook3attack
        else:
             self.type = Rook4attack

        self.row = row
        self.column = column
        self.attackPower = attackPower
        self.cost = cost
        self.health = health
        self.damage = damage

    def GetType(self):
        return self.type

    def SetType(self,type):
        self.type = type

    def GetRow(self):
        return self.row

    def SetRow(self,row):
        self.row = row

    def GetColumn(self):
        return self.column

    def SetColumn(self,column):
        self.column = column

    def GetAttackPower(self):
        return self.attackPower

    def SetAttackPower(self,attackPower):
        self.attackPower = attackPower

    def GetCost(self):
        return self.cost

    def SetCost(self,cost):
        self.cost = cost

    def GetHealth(self):
        return self.health

    def SetHealth(self,health):
        self.health = health

    def GetDamage(self,damage):
        self.damage = damage

    def attack(self):
        Count = 0
        ventana.blit(self.type[Count // 3], (self.row, self.column))
        Count += 1


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


#-----Crea matriz---------------------------------



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
     row = 0
    
#------bucle de inicio--------------------------
     while not salir1:
          drawBoard()#Dibuja la matriz
          a = Avatar("avatar2",400,400,10,10,10)
          a.walk()
          r = Rooks("rook2",200,200,34,23,12,10)
          r.attack()


          pygame.time.delay(100) 
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    salir1=True
               elif event.type == pygame.MOUSEMOTION:
                    mousex, mousey = event.pos
               elif event.type == pygame.MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True


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


