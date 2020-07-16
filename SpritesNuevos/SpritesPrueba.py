import pygame
import sys
import random
from pygame.locals import*
import time

pygame.init()

win = pygame.display.set_mode((600,480))

#----Avatar1=avatar arquero---------------------------------------------------------------------------------------
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
                   pygame.image.load('Elf_01__IDLE_006.png'),
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
x = 50
y = 300
width = 40
height = 60


clock = pygame.time.Clock()


left = False
Die = False
Idle=False
Count = 0

def redrawGameWindow(x,y):
    global Count
    
    win.fill((0,0,0))  
    if Count + 1 >= 27:
        Count = 0
        
    if Attack:  
        win.blit(Avatar4attack[Count//3], (x,y))
        Count += 1                          
    elif Die:
        win.blit(Avatar4Die[Count//3], (x,y))
        Count += 1
    elif Idle:
        win.blit(Avatar4Char[Count//3], (x,y))
        Count += 1
       
        
        
    pygame.display.update() 
    


run = True

while run:
    tiempo =pygame.time.get_ticks()
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if (tiempo//1000)%10==0: 
      
        Attack = True
        Die = False
        Idle=False

    elif keys[pygame.K_RIGHT] :  
      
        Attack = False
        Die = True
        Idle=False
   

        
    else: 
        Attack = False
        Die = False
        Idle=True
        
        

    redrawGameWindow(x,50) 
    
    if (tiempo//1000)%15==0:
        x+=5
    
pygame.quit()
