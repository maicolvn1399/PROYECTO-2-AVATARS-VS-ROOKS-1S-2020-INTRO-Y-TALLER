##############################
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
import os


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
        self.row = row
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

    def draw(self):
        Menu.ventana.blit(self,(self.row,self.column))

    def walk(self):
        Count = 0
        run = True
        Idle = False

        if Count + 1 >= 27:
            Count = 0
        elif Idle:
            Menu.ventana.blit(Avatar2Char[Count // 3], (self.row, self.column))
            Count += 1


        while run:
            if run:
                Idle = True


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
        self.type = type
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

    #Methods for this class
    """
    Attack()
    Delete()"""


