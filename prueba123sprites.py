import pygame
import time
import random
from random import choice
pygame.init()

win = pygame.display.set_mode((1000,900))

pygame.display.set_caption("First Game")
bg  =  pygame.image.load( 'backgroundlevel1.jpg' ) 

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

##Rook1attack  =  [pygame.image.load('11.png'), pygame.image.load('13.png'),
##                 pygame.image.load('12.png')]
##
##Rook1Char = pygame.image.load('11.png')
#falta las bolas de ataque(cambiales el tamaño)
##
###----Rook2=rock rook----------------------------------------------------------------------------------------------
##
##Rook2attack  =  [pygame.image.load('2.png'), pygame.image.load('3.png'),
##                 pygame.image.load('4.png')]
##
##Rook2Char = pygame.image.load('2.png')
##
###----Rook3=fire rook-----------------------------------------------------------------------------------------------
##Rook3attack  =  [pygame.image.load('16.png'), pygame.image.load('17.png'),
##                 pygame.image.load('18.png')]
##
##Rook3Char = pygame.image.load('16.png')
##
###----Rook4=water rook-----------------------------------------------------------------------------------------------
##
##Rook4attack  =  [pygame.image.load('6.png'), pygame.image.load('7.png'),
##                   pygame.image.load('7.png')]
##
##Rook4Char = pygame.image.load('6.png')



clock = pygame.time.Clock()


class Avatar1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isDie = False
        self.Attack = False
        self.Idle = False
        self.Count = 0
        self.life=5
        
        

    def draw(self, win, time):
        if (time//1000)%15==0:
            avatar.x += avatar.vel
        elif (time//1000)%5==0:
           avatar.Attack = True
           avatar.Idle = False
           avatar.isDie= False
        elif self.life<=0:
           avatar.Attack = False
           avatar.Idle = False
           avatar.isDie= True
    
        else:
    
           avatar.Attack = False
           avatar.isDie= False
        
        if self.Count + 1 >= 27:
              self.Count = 0

        if self.Attack:
              win.blit(Avatar1attack[self.Count//3], (self.x,self.y))
              self.Count += 1
        elif self.isDie:
              win.blit(Avatar1Die[self.Count//3], (self.x,self.y))
              self.Count +=1
        else: 
              win.blit(Avatar1Char[self.Count//3], (self.x,self.y))
              self.Count +=1

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite): 
                return True
#---------------------------------------------------------------------------
class Avatar2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isDie = False
        self.Attack = False
        self.Idle = False
        self.Count = 0
        self.life=5
        
        

    def draw(self, win, time):
        if (time//1000)%15==0:
            avatar.x += avatar.vel
        elif (time//1000)%5==0:
           avatar.Attack = True
           avatar.Idle = False
           avatar.isDie= False
        elif self.life<=0:
           avatar.Attack = False
           avatar.Idle = False
           avatar.isDie= True
    
        else:
    
           avatar.Attack = False
           avatar.isDie= False
        
        if self.Count + 1 >= 27:
              self.Count = 0

        if self.Attack:
              win.blit(Avatar2attack[self.Count//3], (self.x,self.y))
              self.Count += 1
        elif self.isDie:
              win.blit(Avatar2Die[self.Count//3], (self.x,self.y))
              self.Count +=1
        else: 
              win.blit(Avatar2Char[self.Count//3], (self.x,self.y))
              self.Count +=1

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite): 
                return True
#---------------------------------------------------------------------------
class Avatar3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.vel = 5
##        self.isDie = False
        self.Attack = False
        self.Idle = False
        self.Count = 0
        self.life=5
        
        

    def draw(self, win, time):
        if (time//1000)%15==0:
            avatar.x += avatar.vel
        elif (time//1000)%5==0:
           avatar.Attack = True
           avatar.Idle = False
##           avatar.isDie= False
        elif self.life<=0:
           avatar.Attack = False
           avatar.Idle = False
           avatar.isDie= True
    
        else:
    
           avatar.Attack = False
           avatar.isDie= False
        
        if self.Count + 1 >= 27:
              self.Count = 0

        if self.Attack:
              win.blit(Avatar3attack[self.Count//3], (self.x,self.y))
              self.Count += 1
    
        else: 
              win.blit(Avatar3Char[self.Count//3], (self.x,self.y))
              self.Count +=1

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite): 
                return True
#---------------------------------------------------------------------------
class Avatar4(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.vel = 5
        self.isDie = False
        self.Attack = False
        self.Idle = False
        self.Count = 0
        self.life=5
        
        

    def draw(self, win, time):
        if (time//1000)%15==0:
            avatar.x += avatar.vel
        elif (time//1000)%5==0:
           avatar.Attack = True
           avatar.Idle = False
           avatar.isDie= False
        elif self.life<=0:
           avatar.Attack = False
           avatar.Idle = False
           avatar.isDie= True
    
        else:
    
           avatar.Attack = False
           avatar.isDie= False
        
        if self.Count + 1 >= 27:
              self.Count = 0

        if self.Attack:
              win.blit(Avatar4attack[self.Count//3], (self.x,self.y))
              self.Count += 1
        elif self.isDie:
              win.blit(Avatar4Die[self.Count//3], (self.x,self.y))
              self.Count +=1
        else: 
              win.blit(Avatar4Char[self.Count//3], (self.x,self.y))
              self.Count +=1

    def collide(self, sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self, sprite): 
                return True            
#---------------------------------------------------------------------------
def randomAvatar():
   
    lista=[Avatar1(100, 100),Avatar1(100,200),Avatar1(100, 300),Avatar1(100, 400),Avatar1(100,500),
           Avatar2(100, 100),Avatar2(100,200),Avatar2(100, 300),Avatar2(100, 400),Avatar2(100,500),
           Avatar3(100, 100),Avatar3(100,200),Avatar3(100, 300),Avatar3(100, 400),Avatar3(100,500),
           Avatar4(100, 100),Avatar4(100,200),Avatar4(100, 300),Avatar4(100, 400),Avatar4(100,500)]
    return (random.choice(lista))

def redrawGameWindow(time):
    
    win.blit(bg,(0,0))
    all_avatars.draw(win,time)
    
    pygame.display.update()
#---------------------------------------------------------------------------
cantidad_Avatars = 50    

def creaAvatars():
    cantidad_Avatars = 50 
    AvatarsList = []
    for i in range(cantidad_Avatars):
        Avatar = randomAvatar()
        AvatarsList.append(Avatar)
    return AvatarsList

#mainloop
all_sprites=pygame.sprite.Group()
all_avatars = pygame.sprite.Group()
##avatars = Avatar1(200, 410, 64,64)

all_avatars.add(creaAvatars())
num=5
run = True
while run:
    clock.tick(27)
    time =pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



            
    redrawGameWindow(time)
    num-=1

pygame.quit()
