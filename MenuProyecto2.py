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
avatar_cannibal_list = []
avatar_lumberjack_list = []



sand_rook_list = []
rock_rook_list = []
water_rook_list = []
fire_rook_list = []

rocks_bullet_list = []
fire_bullet_list = []
water_bullet_list = []
sand_bullet_list = []

points = []
point = []
map_list = []
map_points_list = []

temp_map_list = list()





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
            win.blit(self.image,self.rect)
        else:
            print("IMAGE SAND ROOK ERROR")

    def shoot_sand(self):
        should_fire_sand = False
        for avatar_knight in avatar_knight_list:#loop for every type of avatar
            if isColliding(avatar_knight.rect.x,avatar_knight.rect.y,self.rect.x,self.rect.y):
                should_fire_sand = True

        if self.live and should_fire_sand:
            self.shot_sand_count += 1
            if self.shot_sand_count == 25:
                sandBullet = SandBullet(self)
                ventana.sand_bullet_list.append(sandBullet)
                self.shot_sand_count = 0

        for avatar_archer in avatar_archer_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_archer.rect.x, avatar_archer.rect.y, self.rect.x, self.rect.y):
                should_fire_sand = True

        if self.live and should_fire_sand:
            self.shot_sand_count += 1
            if self.shot_sand_count == 25:
                sandBullet = SandBullet(self)
                ventana.sand_bullet_list.append(sandBullet)
                self.shot_sand_count = 0

        for avatar_cannibal in avatar_cannibal_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_cannibal.rect.x, avatar_cannibal.rect.y, self.rect.x, self.rect.y):
                should_fire_sand = True

        if self.live and should_fire_sand:
            self.shot_sand_count += 1
            if self.shot_sand_count == 25:
                sandBullet = SandBullet(self)
                ventana.sand_bullet_list.append(sandBullet)
                self.shot_sand_count = 0

        for avatar_lumberjack in avatar_lumberjack_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_lumberjack.rect.x, avatar_lumberjack.rect.y, self.rect.x, self.rect.y):
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

    def hit_avatar1(self):
        for avatar_knight in avatar_knight_list:#bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self,avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False

        for avatar_archer in avatar_archer_list:#bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self,avatar_archer):
                self.live = False
                avatar_archer.health -= self.damage

                if avatar_archer.health <= 0:
                    avatar_knight.live = False

        for avatar_cannibal in avatar_cannibal_list:#bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self,avatar_cannibal):
                self.live = False
                avatar_cannibal.health -= self.damage

                if avatar_cannibal.health <= 0:
                    avatar_cannibal.live = False

        for avatar_lumberjack in avatar_lumberjack_list:#bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self,avatar_lumberjack):
                self.live = False
                avatar_lumberjack.health -= self.damage

                if avatar_lumberjack.health <= 0:
                    avatar_lumberjack.live = False

    def display_sand_bullet(self):
        win.blit(self.image,self.rect)

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

    def hit_rook1(self):
        for sandrook in sand_rook_list: #hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

        for rockrook in rock_rook_list: #hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, rockrook):
                self.stop = True
                self.damage_rook(rockrook)

        for waterrook in water_rook_list: #hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, waterrook):
                self.stop = True
                self.damage_rook(waterrook)

        for firerook in fire_rook_list:
            if pygame.sprite.collide_rect(self, firerook):
                self.stop = True
                self.damage_rook(firerook)

    def damage_rook(self,rook):
        rook.health -= self.damage
        if rook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_knight(self):
        win.blit(self.image,self.rect)

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
            win.blit(self.image,self.rect)
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

        for avatar_archer in avatar_archer_list:
            if isColliding(avatar_archer.rect.x,avatar_archer.rect.y,self.rect.x,self.rect.y):
                should_fire_rocks = True

        if self.live and should_fire_rocks:
            self.shot_rocks_count += 1
            if self.shot_rocks_count == 25:
                rocksBullet = RocksBullet(self)
                rocks_bullet_list.append(rocksBullet)
                self.shot_rocks_count = 0

        for avatar_lumberjack in avatar_lumberjack_list:
            if isColliding(avatar_lumberjack.rect.x,avatar_lumberjack.rect.y,self.rect.x,self.rect.y):
                should_fire_rocks = True

        if self.live and should_fire_rocks:
            self.shot_rocks_count += 1
            if self.shot_rocks_count == 25:
                rocksBullet = RocksBullet(self)
                rocks_bullet_list.append(rocksBullet)
                self.shot_rocks_count = 0


        for avatar_cannibal in avatar_cannibal_list:
            if isColliding(avatar_cannibal.rect.x,avatar_cannibal.rect.y,self.rect.x,self.rect.y):
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

    def hit_avatar2(self):
        for avatar_knight in avatar_knight_list:
            if pygame.sprite.collide_rect(self,avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False


        for avatar_archer in avatar_archer_list:
            if pygame.sprite.collide_rect(self,avatar_archer):
                self.live = False
                avatar_archer.health -= self.damage

                if avatar_archer.health <= 0:
                    avatar_archer.live = False


        for avatar_cannibal in avatar_cannibal_list:
            if pygame.sprite.collide_rect(self,avatar_cannibal):
                self.live = False
                avatar_cannibal.health -= self.damage

                if avatar_cannibal.health <= 0:
                    avatar_cannibal.live = False


        for avatar_lumberjack in avatar_lumberjack_list:
            if pygame.sprite.collide_rect(self,avatar_lumberjack):
                self.live = False
                avatar_lumberjack.health -= self.damage

                if avatar_lumberjack.health <= 0:
                    avatar_lumberjack.live = False

    def display_rock_bullet(self):
        win.blit(self.image,self.rect)


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
            win.blit(self.image,self.rect)
        else:
            print("IMAGE FIRE ROOK ERROR")

    def shoot_fire(self):
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

        for avatar_cannibal in avatar_cannibal_list:
            if isColliding(avatar_cannibal.rect.x,avatar_cannibal.rect.y,self.rect.x,self.rect.y):
                should_fire_fire = True

        if self.live and should_fire_fire:
            self.shot_fire_count += 1
            if self.shot_fire_count == 25:
                fireBullet = FireBullet(self)
                fire_bullet_list.append(fireBullet)
                self.shot_fire_count = 0

        for avatar_archer in avatar_archer_list:
            if isColliding(avatar_archer.rect.x,avatar_archer.rect.y,self.rect.x,self.rect.y):
                should_fire_fire = True

        if self.live and should_fire_fire:
            self.shot_fire_count += 1
            if self.shot_fire_count == 25:
                fireBullet = FireBullet(self)
                fire_bullet_list.append(fireBullet)
                self.shot_fire_count = 0

        for avatar_lumberjack in avatar_lumberjack_list:
            if isColliding(avatar_lumberjack.rect.x,avatar_lumberjack.rect.y,self.rect.x,self.rect.y):
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

    def move_fire_bullet(self):
        if self.rect.x < WINDOWWIDTH:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_avatar3(self):
        for avatar_knight in avatar_knight_list:
            if pygame.sprite.collide_rect(self,avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage

                if avatar_knight.health <= 0:
                    avatar_knight.live = False

        for avatar_archer in avatar_archer_list:
            if pygame.sprite.collide_rect(self,avatar_archer):
                self.live = False
                avatar_archer.health -= self.damage

                if avatar_archer.health <= 0:
                    avatar_archer.live = False

        for avatar_cannibal in avatar_cannibal_list:
            if pygame.sprite.collide_rect(self,avatar_cannibal):
                self.live = False
                avatar_cannibal.health -= self.damage

                if avatar_cannibal.health <= 0:
                    avatar_cannibal.live = False


        for avatar_lumberjack in avatar_lumberjack_list:
            if pygame.sprite.collide_rect(self,avatar_lumberjack):
                self.live = False
                avatar_lumberjack.health -= self.damage

                if avatar_lumberjack.health <= 0:
                    avatar_lumberjack.live = False

    def display_fire_bullet(self):
        win.blit(self.image,self.rect)

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
            win.blit(self.image, self.rect)
        else:
            print("IMAGE WATER ROOK ERROR")

    def shoot_water(self):
        should_fire_water = False
        for avatar_knight in avatar_knight_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_knight.rect.x, avatar_knight.rect.y, self.rect.x, self.rect.y):
                should_fire_water = True

        if self.live and should_fire_water:
            self.shot_water_count_count += 1
            if self.shot_water_count_count == 25:
                waterBullet = WaterBullet(self)
                win.sand_bullet_list.append(waterBullet)
                self.shot_water_count_count = 0


        for avatar_cannibal in avatar_cannibal_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_cannibal.rect.x, avatar_cannibal.rect.y, self.rect.x, self.rect.y):
                should_fire_water = True

        if self.live and should_fire_water:
            self.shot_water_count_count += 1
            if self.shot_water_count_count == 25:
                waterBullet = WaterBullet(self)
                win.sand_bullet_list.append(waterBullet)
                self.shot_water_count_count = 0


        for avatar_archer in avatar_archer_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_archer.rect.x, avatar_archer.rect.y, self.rect.x, self.rect.y):
                should_fire_water = True

        if self.live and should_fire_water:
            self.shot_water_count_count += 1
            if self.shot_water_count_count == 25:
                waterBullet = WaterBullet(self)
                win.sand_bullet_list.append(waterBullet)
                self.shot_water_count_count = 0


        for avatar_lumberjack in avatar_lumberjack_list:  # Un bucle por cada tipo de avatar
            if isColliding(avatar_lumberjack.rect.x, avatar_lumberjack.rect.y, self.rect.x, self.rect.y):
                should_fire_water = True

        if self.live and should_fire_water:
            self.shot_water_count_count += 1
            if self.shot_water_count_count == 25:
                waterBullet = WaterBullet(self)
                win.sand_bullet_list.append(waterBullet)
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

    def hit_avatar4(self):
        for avatar_knight in avatar_knight_list:  # bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self, avatar_knight):
                self.live = False
                avatar_knight.health -= self.damage
                if avatar_knight.health <= 0:
                    avatar_knight.live = False

        for avatar_archer in avatar_knight_list:  # bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self, avatar_archer):
                self.live = False
                avatar_archer.health -= self.damage
                if avatar_archer.health <= 0:
                    avatar_archer.live = False


        for avatar_cannibal in avatar_cannibal_list:  # bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self, avatar_cannibal):
                self.live = False
                avatar_cannibal.health -= self.damage
                if avatar_cannibal.health <= 0:
                    avatar_cannibal.live = False


        for avatar_lumberjack in avatar_lumberjack_list:  # bucle para cada tipo de avatar
            if pygame.sprite.collide_rect(self, avatar_lumberjack):
                self.live = False
                avatar_lumberjack.health -= self.damage
                if avatar_lumberjack.health <= 0:
                    avatar_lumberjack.live = False

    def display_water_bullet(self):
        win.blit(self.image,self.rect)


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

    def hit_rook2(self):
        for sandrook in sand_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

        for rockrook in rock_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, rockrook):
                self.stop = True
                self.damage_rook(rockrook)


        for water_rook in water_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, water_rook):
                self.stop = True
                self.damage_rook(water_rook)

        for firerook in fire_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, firerook):
                self.stop = True
                self.damage_rook(firerook)

    def damage_rook(self, rook):
        rook.health -= self.damage
        if rook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_archer(self):
        win.blit(self.image, self.rect)


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

    def hit_rook3(self):
        for sandrook in sand_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

        for rockrook in rock_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, rockrook):
                self.stop = True
                self.damage_rook(rockrook)

        for waterrook in water_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, waterrook):
                self.stop = True
                self.damage_rook(waterrook)

        for firerook in fire_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, firerook):
                self.stop = True
                self.damage_rook(firerook)

    def damage_rook(self, rook):
        rook.health -= self.damage
        if rook.health <= 0:
            print("eliminar sand rook")

    def display_avatar_lumberjack(self):
        win.blit(self.image, self.rect)

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

    def hit_rook4(self):
        for sandrook in sand_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, sandrook):
                self.stop = True
                self.damage_rook(sandrook)

        for rockrook in rock_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, rockrook):
                self.stop = True
                self.damage_rook(rockrook)

        for waterrook in water_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, waterrook):
                self.stop = True
                self.damage_rook(waterrook)

        for firerook in fire_rook_list:  # hacer un bucle por cada rook
            if pygame.sprite.collide_rect(self, firerook):
                self.stop = True
                self.damage_rook(firerook)


    def damage_rook(self, rook):
        rook.health -= self.damage
        if rook.health <= 0:
            print("eliminar sand rook")
            rook.stop = True

    def display_avatar_cannibal(self):
        win.blit(self.image, self.rect)


class Map():

    map_names_list = ["map1.png","map2.png"]

    def __init__(self,x,y,img_index):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x,y)

        self.rook_can_be_placed = True

    def load_map(self):
        win.blit(self.image,self.position)


def init_rook_points():
    for y in range(1,6):
        points = []
        for x in range(9):
            point = (x,y)
            points.append(point)
        map_points_list.append(points)

def init_map():
    global temp_map_list
    for points in map_points_list:
        temp_map_list = list()
        for point in points:
            if (point[0] + point[1])%2 == 0:
                map = Map(point[0] * 100,point[1] * 100,0)
            else:
                map = Map(point[0] * 100,point[1] * 100,1)
            temp_map_list.append(map)
        map_list.append(temp_map_list)

def load_map():
    for temp_map_list in map_list:
        for map in temp_map_list:
            map.load_map()

def load_rooks():
    for sandrook in sand_rook_list:
        if sandrook.live:
            if isinstance(sandrook,SandRook):
                sandrook.load_sand_rook()
                sandrook.shoot_sand()
        else:
            sand_rook_list.remove(sandrook)

    for rockrook in rock_rook_list:
        if rockrook.live:
            if isinstance(rockrook,RockRook):
                rockrook.load_rock_rook()
                rockrook.shoot_rocks()
            else:
                rock_rook_list.remove(rockrook)

    for waterrook in water_rook_list:
        if waterrook.live:
            if isinstance(waterrook,WaterRook):
                waterrook.load_water_rook()
                waterrook.shoot_water()
            else:
                water_rook_list.remove(waterrook)

    for firerook in fire_rook_list:
        if firerook.live:
            if isinstance(firerook,FireRook):
                firerook.load_fire_rook()
                firerook.shoot_fire()
            else:
                fire_rook_list.remove(firerook)


def load_bullets():
    for sb in sand_bullet_list:
        if sb.live:
            sb.display_sand_bullet()
            sb.move_sand_bullet()
            sb.hit_avatar1()
        else:
            sand_bullet_list.remove(sb)

    for rb in rocks_bullet_list:
        if rb.live:
            rb.display_rock_bullet()
            rb.move_rock_bullet()
            rb.hit_avatar2()
        else:
            rocks_bullet_list.remove(rb)

    for wb in water_bullet_list:
        if wb.live:
            wb.display_water_bullet()
            wb.move_water_bullet()
            wb.hit_avatar4()
        else:
            water_bullet_list.remove(wb)

    for fb in fire_bullet_list:
        if fb.live:
            fb.display_fire_bullet()
            fb.move_fire_bullet()
            fb.hit_avatar3()

        else:
            fire_bullet_list.remove(fb)

def init_avatar_knight():
    for i in range(1,6):
        dis = random.randint(1,5) * 200
        newAvatarKnight = AvatarKnight(800+dis,i*80)
        avatar_knight_list.append(newAvatarKnight)

def init_avatar_cannibal():
    for i in range(1,6):
        dis = random.randint(1, 5) * 200
        newAvatarCannibal = AvatarCannibal(800 + dis, i * 80)
        avatar_cannibal_list.append(newAvatarCannibal)


def init_avatar_archer():
    for i in range(1,6):
        dis = random.randint(1, 5) * 200
        newAvatarArcher = AvatarArcher(800 + dis, i * 80)
        avatar_archer_list.append(newAvatarArcher)


def init_avatar_lumberjack():
    for i in range(1,6):
        dis = random.randint(1, 5) * 200
        newAvatarLumberjack = AvatarLumberjack(800 + dis, i * 80)
        avatar_lumberjack_list.append(newAvatarLumberjack)

def load_avatars_knights():
    for av in avatar_knight_list:
        if av.live:
            av.display_avatar_knight()
            av.move_avatar_knight()
            av.hit_rook1()
        else:
            avatar_knight_list.remove(av)

def load_avatars_cannibals():
    for a in avatar_cannibal_list:
        if a.live:
            a.display_avatar_cannibal()
            a.move_avatar_cannibal()
            a.hit_rook4()
        else:
            avatar_cannibal_list.remove(a)

def load_avatars_archers():
    for a in avatar_archer_list:
        if a.live:
            a.display_avatar_archer()
            a.move_avatar_archer()
            a.hit_rook2()
        else:
            avatar_archer_list.remove(a)

def load_avatars_lumberjacks():
    for a in avatar_lumberjack_list:
        if a.live:
            a.display_avatar_lumberjack()
            a.move_avatar_lumberjack()
            a.hit_rook3()
        else:
            avatar_lumberjack_list.remove(a)


pygame.init()
#----Fondos------------------------------------
fondo1= pygame.image.load("5.jpg")

#----Fondos Niveles------------------------------------
backgroundLevel1 = pygame.image.load("backgroundLevel1.png")

#----constantes--------------------------------
BLACK=(2, 22, 34)#formato RGB
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
FLOOR = pygame.image.load('map.png')
GRIDSIZE = 16 #grid size of the map, eg. map will be 16 * 16, when GRIDSIZE = 16
BRIGHTBLUE = (0, 170, 255)
BGCOLOR = BRIGHTBLUE
FPS = 40 #frames per second, the speed rate of the prgram
WINDOWWIDTH = 1100 #window's width in pixel
WINDOWHEIGHT = 600 #window's height in pixel
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
entry=button text,surface,button color(state), position,size,ID, un mensaje,un segundo mensaje
return= Button.
restriction= size y position==list
"""

def buttons(text,surface,state,position,size,ID=None,ms=None,ms2=None):
     cursor=pygame.mouse.get_pos()
     click=pygame.mouse.get_pressed()
     if position[0]+size[0] > cursor[0] > size[0] and position[1]+size[1]> cursor[1]>size[1] and position[1]+size[1]<cursor[1]+size[1]:
          button=pygame.draw.rect(surface,state[1],(position[0],position[1],size[0],size[1]))
          if click[0]==1:
               if ID=="start":
                    pygame.mixer.music.pause()
                    Options()
               elif ID=="info":
                    pygame.mixer.music.pause()
                    instructions()
               elif ID=="puntuation":
                    puntuation()
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
                    StartCount(ms,1)
               elif ID=="level2":
                    startCount(ms,2)
               elif ID=="level3":
                    startCount(ms,3)
               elif ID=="pause":
                    pause()
               elif ID=="back":
                    pause=False
               elif ID=="ok":
                    levels(ms)
               
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
def introduction():
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
               buttons("Mejor puntaje",win,buttoncolor3,button3,buttonsize1,ID="puntuation")
               buttons("Creditos",win,buttoncolor4,button4,buttonsize1,ID="credits")
               buttons("Salir",win,buttoncolor5,button5,buttonsize1,ID="exit") 
               message("Avatars VS Rooks",COLOR1,-15,-200,size="big")
               pygame.display.update()
               clock.tick(15)
#----Instrucciones--------------------------------
def instructions():
     instruction=True
     while instruction:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    instruction=False
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
def Options():
    font = pygame.font.SysFont("normal", 40)

    input_box = pygame.Rect(button2,buttonsize1)
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
                              levels(text)
                              text = ''
                              
                         elif event.key == pygame.K_BACKSPACE:
                              text = text[:-1]
                         else:
                              text += event.unicode
                    
               
               win.blit(fondo1,(0,0))
               txt_surface = font.render(text, True, color)
               width = max(320, txt_surface.get_width()+20)
               input_box.w = width
               win.blit(txt_surface, (input_box.x+5, input_box.y+5))
               pygame.draw.rect(win, color, input_box,4)
               buttons("Volver",win,buttoncolor1,button4,buttonsize1,ID="exit1")
               message("Opciones del juego",COLOR1,-20,-200,size="big")
               message("Ingrese su nombre de usuario",COLOR11 ,+30,-30,size="regular")
               message("y presione 'ENTER' al finalizar.",COLOR11,+30,size="regular")
               pygame.display.flip() 
               pygame.display.update()
               clock.tick(15)
#----niveles---------------------------------------
def levels(text):
     level=True
     while level:
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    level=False
                    pygame.quit()
               
                    
               win.blit(fondo1,(0,0))
               buttons("Volver",win,buttoncolor2,button5,buttonsize1,ID="exit1")
               buttons("Nivel 1",win,buttoncolor1,button2,buttonsize1,ID="level1",ms=str(text))
               buttons("Nivel 2",win,buttoncolor3,button3,buttonsize1,ID="level2",ms=str(text))
               buttons("Nivel 3",win,buttoncolor5,button4,buttonsize1,ID="level3",ms=str(text))
               message("Hola"+" "+str(text),COLOR1,0,-100,size="big")
               message("Selecciona un nivel",COLOR1,0,+50,size="regular")
              
               pygame.display.update()
               clock.tick(15)               
#----Puntuaciones----------------------------------
def puntuation():
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
entrada=nombre del jugador
salida=cuenta regresiva
restriccion=no tiene
"""               
def StartCount(name,n):
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
                 Gameloop(name)
            if n==2:
                 win.blit(fondo1,(0,0))
                 message("READY",COLOR11,size="giant")            
                 pygame.display.update()
                 time.sleep(1)
                 win.blit(fondo1,(0,0))
                 message("GO!",COLOR11,size="giant")
                 pygame.display.update()
                 time.sleep(1)
                 Gameloop1(name)
            if n==3:
                 win.blit(fondo1,(0,0))
                 message("READY",COLOR11,size="giant")            
                 pygame.display.update()
                 time.sleep(1)
                 win.blit(fondo1,(0,0))
                 message("GO!",COLOR11,size="giant")
                 pygame.display.update()
                 time.sleep(1)
                 
                 Gameloop2(name)






#----nivel1----------------------------------------
#entrada= 
#salida=
          
def Gameloop(name):
#Constantes para iniciar la matriz--------
     FPSCLOCK = pygame.time.Clock()
     mousex = 0
     mousey = 0
     mouseClicked = False
#----------------------------------------
     exit1=False
     global avatar_knight_list,avatar_lumberjack_list,avatar_archer_list,avatar_cannibal_list
     aK = AvatarKnight(300,200)
     bK = AvatarKnight(350,250)
     avatar_knight_list = [aK,bK]
     avatar_archer_list = []
     avatar_lumberjack_list = []
     avatar_cannibal_list = []

     global sand_rook_list,rock_rook_list,water_rook_list,fire_rook_list
     sand_rook_list = []
     rock_rook_list = []
     water_rook_list = []
     fire_rook_list = []

     global rocks_bullet_list,sand_bullet_list,water_bullet_list,fire_bullet_list
     rocks_bullet_list = []
     sand_bullet_list = []
     water_bullet_list = []
     fire_bullet_list = []

     #init_avatar_knight()
     print(avatar_knight_list)



#------bucle de inicio--------------------------
     while not exit1:
         drawBoard()
         pygame.time.delay(100)

         load_avatars_knights()


         for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    exit1=True
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   x = event.pos[0] // 90
                   y = event.pos[1] // 90
                   map = map_list[y-1][x]
                   print(map.position)

                   if event.button == 1:
                       if map.rook_can_be_placed:
                           rook = SandRook(map.position[0],map.position[1],5)
                           sand_rook_list.append(rook)
                           bullet = SandBullet(rook)
                           sand_bullet_list.append()
                           map.rook_can_be_placed = False
                   elif event.button == 3:
                       if map.rook_can_be_placed:
                           waterRook = WaterRook(map.position[0],map.position[1],5)
                           water_rook_list.append(waterRook)
                           waterBullet = WaterBullet(waterRook)
                           water_bullet_list.append(waterBullet)
                           map.rook_can_be_placed = False

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
entrada=nombre del jugador 
salida=pantalla de juego con enemigos y un jugado, tambien incluye marcador y tiempo
"""
def Gameloop1(name):
     
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
               ventana.blit(fondo1,(0,0))
               message("Nivel 2",COLOR3,-200,size="big")
               buttons("Pausa",win,buttoncolor5,button5,buttonsize1,ID="pause")
        
          pygame.display.update()
          clock.tick(60)

#----Nivel3----------------------------------------
"""          
#entrada=nombre del jugador 
#salida=pantalla de juego con enemigos y un jugado, tambien incluye marcador y tiempo
"""
def Gameloop2(name):
     
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
               ventana.blit(fondo1,(0,0))
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
     while pause:
          for event in pygame.event.get():

               buttons("volver",ventana,buttoncolor4,button4,buttonsize1,ID="back") 
               buttons("salir",ventana,buttoncolor5,button5,buttonsize1,ID="exit1")
               

          message("Juego en pausa",COLOR2,size="big")
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
introduction()
Credits()
Options()
puntuations()
Gameloop()
Gameloop1()
Gameloop2()
pausa()


