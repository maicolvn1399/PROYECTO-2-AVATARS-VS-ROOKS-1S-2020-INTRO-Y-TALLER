import pygame
from pygame import *
from random import *
from tkinter import *
from tkinter import messagebox
import math
from pygame.locals import*
from operator import itemgetter
import turtle
import time
import sys
import os

"""
Instituto Tecnológico de Costa Rica
Área de Ingeniería en Computadores
CE1102 - Taller de Programación
Profesor: Jason Leitón Jiménez
Estudiantes: Raquel Lizano y Michael Valverde
II Proyecto - I Semestre - 2020
"""

#Initialize pygame
pygame.init()
font.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height)) #The display in which the game runs
pygame.display.set_caption("Road Fighter")

#set up a clock
clock = pygame.time.Clock()

#CONSTANT VARIABLES
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH,WINDOW_HEIGHT)

#Define tile parameters
WIDTH = 100
HEIGHT = 100

#define color
WHITE = (255,255,255)

#set up rates
SPAWN_RATE = 1000
FRAME_RATE = 60

#Set up counters
startingMoney = 15
moneyRate = 120
startingMoneyBooster = 1

#Set up win/lose conditions
ENEMIES_PASSED = 8 #cantidad de avatars que pasan
WIN_TIME = FRAME_RATE * 60 * 3

#Speeds
REG_SPEED = 2
SLOW_SPEED = 1

rock_rook_coordinates = []
sand_rook_coordinates = []
fire_rook_coordinates = []
water_rook_coordinates = []

all_rooks_created = []
new_rooks = []
playTilesList = []

FIRE_RATE = 600

#____________load assets__________________

#Window to display the game
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption("AVATARS VS ROOKS")

#Background
background_img = image.load("backgroundlevel3.png")
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf,WINDOW_RES)
GAME_WINDOW.blit(BACKGROUND,(0,0))

tile_color = WHITE


#set up enemies
avatar_archer_img = image.load("avatarArcher.png")
#avatar_archer_surf = Surface.convert_alpha(avatar_archer_img)
AVATAR_ARCHER = avatar_archer_img

avatar_cannibal_img = image.load("avatarCannibal.png")
AVATAR_CANNIBAL = avatar_cannibal_img

avatar_knight_img = image.load("avatarKnight.png")
AVATAR_KNIGHT = avatar_knight_img

avatar_lumberjack_img = image.load("avatarLumberjack.png")
AVATAR_lUMBERJACK = avatar_lumberjack_img

#transform.scale(avatar_archer_surf,(60,75))

#set up rooks
water_rook = image.load("waterRook.png")
water_rook_surf = Surface.convert_alpha(water_rook)
WATER_ROOK = transform.scale(water_rook_surf,(WIDTH,HEIGHT))

fire_rook = image.load("fireRook.png")
fire_rook_surf = Surface.convert_alpha(fire_rook)
FIRE_ROOK = transform.scale(fire_rook_surf,(WIDTH,HEIGHT))

sand_rook = image.load("sandRook.png")
sand_rook_surf = Surface.convert_alpha(sand_rook)
SAND_ROOK = transform.scale(sand_rook_surf, (WIDTH,HEIGHT))

rock_rook = image.load("rockRook.png")
rock_rook_surf = Surface.convert_alpha(rock_rook)
ROCK_ROOK = transform.scale(rock_rook_surf,(WIDTH,HEIGHT))

#set up bullets
sand_bullet_img = image.load("sandEffect.png")
sand_bullet_surf = Surface.convert_alpha(sand_bullet_img)
SAND_BULLET = transform.scale(sand_bullet_surf,(30,30))

water_bullet_img = image.load("waterEffect.png")
water_bullet_surf = Surface.convert_alpha(water_bullet_img)
WATER_BULLET = transform.scale(water_bullet_surf,(30,30))

rock_bullet_img = image.load("rockEffect.png")
rock_bullet_surf = Surface.convert_alpha(rock_bullet_img)
ROCK_BULLET = transform.scale(rock_bullet_surf,(30,30))

fire_bullet_img = image.load("fireEffect.png")
fire_bullet_surf = Surface.convert_alpha(fire_bullet_img)
FIRE_BULLET = transform.scale(fire_bullet_surf,(30,30))

#attacks from avatars images
arrow_bullet_img = image.load("arrow_bullet.png")
arrow_bullet_surf = Surface.convert_alpha(arrow_bullet_img)
ARROW = transform.scale(arrow_bullet_surf,(75,15))

#image for explosion
explosion_img = image.load("explosion.png")
EXPLOSION = explosion_img


def WelcomeWindow():
    """This is the first window the player sees on screen, it allows the player to type in their name and select a level,
    or see the scores from previous games as well as the instructions and credits  """
    welcomeWindow = Tk()
    COLOR1 = "#FF8903"
    COLOR2 = "#76E400"
    COLOR3 = "#F2A400"
    COLOR4 = "#A9EC0C"
    COLOR5 = "#FDC61C"
    welcomeWindow.title("Avatars Vs Rooks")
    welcomeWindow.minsize(450, 500)
    welcomeWindow.resizable(width=NO, height=NO)
    backgroundImage = LoadImage("background.gif")
    labelBackground = Label(welcomeWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0)
    welcomeLabel = Label(welcomeWindow, text="Avatars Vs Rooks", font="Fixedsys 18", bg=COLOR1, fg="black")
    welcomeLabel.place(x=50, y=100)
    nameLabel = Label(welcomeWindow, text="Enter your name", font="Fixedsys 16", bg=COLOR2, fg="black")
    nameLabel.place(x=50, y=180)

    nameEntry = Entry(welcomeWindow, width=25, bg=COLOR2, fg="black")
    nameEntry.place(x=250, y=180)

    levelLabel = Label(welcomeWindow, text="Select a level", font="Fixedsys 16", bg=COLOR3, fg="black")
    levelLabel.place(x=50, y=230)

    buttonLevel1 = Button(welcomeWindow,font = "Fixedsys 16", text="Level 1",bg=COLOR3,fg="black")
    buttonLevel1.place(x=250,y=230)

    buttonLevel2 = Button(welcomeWindow,font = "Fixedsys 16", text="Level 2",bg=COLOR4,fg="black")
    buttonLevel2.place(x=250,y=260)

    buttonLevel3 = Button(welcomeWindow,font = "Fixedsys 16", text="Level 3",bg=COLOR5,fg="black")
    buttonLevel3.place(x=250,y=290)

    instructionsButton = Button(welcomeWindow, font="Fixedsys 16", text="Instructions", bg=COLOR3, fg="black",
                                command=Instructions)
    instructionsButton.place(x=250, y=330)

    previousScoresButton = Button(welcomeWindow, font="Fixedsys 16", text="Best Scores", bg=COLOR4, fg="black",
                                  command=lambda: TopScoresWindow())
    previousScoresButton.place(x=250, y=360)

    creditsButton = Button(welcomeWindow, font="Fixedsys 16", text="Credits", bg=COLOR5, fg="black", command=Credits)
    creditsButton.place(x=250, y=390)

    welcomeWindow.mainloop()

def TopScoresWindow():
    """"GUI to show the top best scores of the game"""
    ScoresWindow = Toplevel()
    ScoresWindow.minsize(400, 400)
    ScoresWindow.resizable(width=NO, height=NO)
    ScoresWindow.title("Top Best Scores")
    #scores = GetScores()

    backgroundImageScore = LoadImage("bgScores.gif")
    labelBGScores = Label(ScoresWindow, image=backgroundImageScore)
    labelBGScores.image = backgroundImageScore
    labelBGScores.place(x=0, y=0, relwidth=1, relheight=1)

    labelScores = Label(ScoresWindow,text="Top 7 Best Scores",font = "Fixedsys 17",bg="#f59042")
    labelScores.place(x=65,y=30)
    messageScores = Message(ScoresWindow,
                      text=str("scores"),
                      bg="#f59042", justify="left", relief="ridge", font="Fixedsys 16")
    messageScores.place(x=100, y=150)
    ScoresWindow.mainloop()


def Instructions():
    """GUI  to show the instructions of the game to the players"""
    instructionsWindow = Toplevel()
    instructionsWindow.minsize(450, 500)
    instructionsWindow.resizable(width=NO, height=NO)
    instructionsWindow.title("Instructions")

    backgroundImage = LoadImage("background.gif")
    labelBackground = Label(instructionsWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0, relwidth=1, relheight=1)
    labelBackground.image = backgroundImage
    message = Message(instructionsWindow, text="The objective of the game is to kill the avatars appearing in the "
                                               "right side of the screen, to do so, you have to select one rook"
                                               " from the bottom of the screen, there are four types of rooks:"
                                               "\nWater rook: shoots water to the enemies "
                                               "\nRock rook: shoots rocks to the enemies "
                                               "\nSand rook: throws sand to the opponents "
                                               "\nFire rook: throws fire balls to the opponents, then you have to and place it to the game board "
                                               "once the rook is set, it will begin to shoot the enemies, be careful because "
                                               "the avatars will fight back.\n\n Good luck!", bg="#f59042", justify="left", relief="ridge", font="Fixedsys 13")
    message.place(x=50, y=50)
    instructionsWindow.mainloop()

def Credits():
    """GUI for the credits of the game"""
    creditsWindow = Toplevel()
    creditsWindow.minsize(600, 500)
    creditsWindow.resizable(width=NO, height=NO)
    creditsWindow.title("Credits")
    backgroundImage = LoadImage("background.gif")
    labelBackground = Label(creditsWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0, relwidth=1, relheight=1)
    labelBackground.image = backgroundImage

    message = Message(creditsWindow, text="Desarrollado en Costa Rica\n"
                                          "Tecnologico de Costa Rica, Ingenieria en Computadores\n"
                                          "", bg="#f59042", justify="left", relief="ridge", font="Fixedsys 16")

    message.place(x=100, y=100)

    creditsWindow.mainloop()


#def ValidateInputs(name, currentLevel):
    """Function that validates the inputs before running the game, the name should be an string and the level should be a integer,
otherwise it won't run and will ask the user to type or click valid values"""
    #if isinstance(name, str) and not name.isspace() and not len(name) == 0:
        #return GameWindow(name, currentLevel)
    #else:
        #return messagebox.showerror("Error", "You have to enter a valid player name")

def LoadImage(ImgName):
    """Loads and image"""
    path = os.path.join('media', ImgName)
    imageToLoad = PhotoImage(file=path)
    return imageToLoad

#set up classes
class Avatar(sprite.Sprite):
    def __init__(self,image,attackPower,health,walkSeconds):
        super().__init__()
        self.speed = REG_SPEED
        self.lane = randint(0,4)
        all_avatars_archers.add(self)
        self.image = image
        #AVATAR_ARCHER.copy()
        y = 50 + self.lane * 100
        self.health = health
        self.attackPower = attackPower
        self.walkSeconds = walkSeconds
        self.stop = False
        self.rect = self.image.get_rect(center=(1100,y))
        self.despawn_wait = None

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def update(self,game_window,counters):
        game_window.blit(BACKGROUND,
                         (self.rect.x, self.rect.y), self.rect)

        timer = pygame.time.get_ticks()
        timerWalk = int(timer/1000)

        if timerWalk%self.walkSeconds == 0 and not self.stop:
            self.rect.x -= self.speed*2.1
            self.stop = True
        else:
            self.stop = False

        #isColliding = sprite.spritecollide(self,all_bullets,True)
        #if isColliding is not None:
            #for bullet in isColliding:
                #self.health -= -1

        isCollidingWithFireBullet = sprite.spritecollide(self,all_fire_bullets,True)
        if isCollidingWithFireBullet is not None:
            for bullet in isCollidingWithFireBullet:
                self.health -= 8
                PlayHitSound(2)

        isCollidingWithWaterBullet = sprite.spritecollide(self,all_water_bullets,True)
        if isCollidingWithWaterBullet is not None:
            for bullet in isCollidingWithWaterBullet:
                PlayHitSound(3)
                self.health -= 8

        isCollidingWithRockBullet = sprite.spritecollide(self,all_rock_bullets,True)
        if isCollidingWithRockBullet is not None:
            for bullet in isCollidingWithRockBullet:
                PlayHitSound(4)
                self.health -= 4

        isCollidingWithSandBullet = sprite.spritecollide(self,all_sand_bullets,True)
        if isCollidingWithSandBullet is not None:
            for bullet in isCollidingWithSandBullet:
                PlayHitSound(5)
                self.health -= 2

        if self.rect.x <= 100:
            counters.enemies_passed += 1
            self.despawn_wait = 0

        if self.despawn_wait is None:
            if self.health <= 0:
                self.image = EXPLOSION
                self.speed = 0
                self.despawn_wait = 20
            game_window.blit(self.image,(self.rect.x,self.rect.y))
        elif self.despawn_wait <= 0:
            self.kill()
        else:
            self.despawn_wait -= 1
        game_window.blit(self.image,(self.rect.x,self.rect.y))

    def attack(self,tile):
        if tile.rook == WATERrook:
            self.speed = SLOW_SPEED
        elif tile.rook == FIRErook:
            self.health -= 1
        elif tile.rook == ROCKrook:
            self.health = 0


class Counters(object):
    def __init__(self,enemy_money,money_rate,money_booster,timer,enemies_passed,fire_rate):
        self.loop_count = 0
        self.display_font = font.Font("font.ttf",25)
        self.enemy_money = enemy_money
        self.money_rate = money_rate
        self.money_booster = money_booster
        self.money_rect = None
        self.timer = timer
        self.timer_rect = None
        self.enemies_passed = 0
        self.enemies_passed_rect = None
        self.fire_rate = fire_rate

    def increment_money(self):
        if self.loop_count % self.money_rate == 0:
            self.enemy_money += self.money_booster

    def draw_money(self,game_window):
        if self.money_rect:
            game_window.blit(BACKGROUND,(self.money_rect.x,self.money_rect.y),self.money_rect)
        money_surface = self.display_font.render(str(self.enemy_money),True,WHITE)
        self.money_rect = money_surface.get_rect()
        self.money_rect.x = WINDOW_WIDTH - 50
        self.money_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(money_surface,self.money_rect)

    def draw_enemies_passed(self,game_window):
        if bool(self.enemies_passed_rect):
            game_window.blit(BACKGROUND,(self.enemies_passed_rect.x,self.enemies_passed_rect.y),self.enemies_passed_rect)

        enemies_passed_surf = self.display_font.render(str(self.enemies_passed),True,WHITE)
        self.enemies_passed_rect = enemies_passed_surf.get_rect()

        self.enemies_passed_rect.x = WINDOW_WIDTH - 150
        self.enemies_passed_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(enemies_passed_surf,self.enemies_passed_rect)

    def draw_timer(self,game_window):
        if bool(self.timer_rect):
            game_window.blit(BACKGROUND,
                             (self.timer_rect.x, self.timer_rect.y),self.timer_rect)
        #timerGame = int(time.get_ticks()/1000)
        timer_surf = self.display_font.render(str(WIN_TIME - self.loop_count // FRAME_RATE),True,WHITE)
        #timer_surf = self.display_font.render(str(timerGame),True,WHITE)
        self.timer_rect = timer_surf.get_rect()
        self.timer_rect.x = WINDOW_WIDTH - 250
        self.timer_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(timer_surf,self.timer_rect)

    def update(self,game_window):
        self.loop_count += 1
        self.increment_money()
        self.draw_money(game_window)
        self.draw_enemies_passed(game_window)
        self.draw_timer(game_window)
        self.update_rock_rook()
        self.update_fire_rook()
        self.update_water_rook()
        self.update_sand_rook()
        self.update_avatar_objects()
        #self.update_rook_damage()

    def update_rock_rook(self):
        for location in rock_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"ROCK_ROOK")

    def update_fire_rook(self):
        for location in fire_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"FIRE_ROOK")

    def update_water_rook(self):
        for location in water_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"WATER_ROOK")

    def update_sand_rook(self):
        for location in sand_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"SAND_ROOK")

    def update_avatar_objects(self):
        for i in all_avatars_archers:
            if self.loop_count % self.fire_rate == 0:
                AvatarObject(i.getX(),i.getY(),"ARROW")

    def update_rook_damage(self):
        for pos in sand_rook_coordinates:
            sand_rookX,sand_rookY = pos
            if isColliding(sand_rookX,sand_rookY):
                print("IS COLLIDING")

class Rook(sprite.Sprite):
    def __init__(self,type,cost,type_img):
        self.type = type
        if type == "WATER_ROOK":
            self.health = 16
        elif type == "FIRE_ROOK":
            self.health = 16
        elif type == "ROCK_ROOK":
            self.health = 14
        else:
            self.health = 2

        self.cost = cost
        self.type_img = type_img
        self.rect = self.type_img.get_rect()
        self.bullet_speed = 1
        self.bullet_stop = False

class RookApplicator(object):
    def __init__(self):
        self.selected = None

    def select_rook(self,rook):
        if rook.cost <= counters.enemy_money:
            self.selected = rook

    def select_tile(self,tile,counters):
        self.selected = tile.set_rook(self.selected,counters)

class RookRemover(object):
    def __init__(self):
        self.selected = None

    def select_tile(self,tile,counters):
        self.selected = tile.unset_rook(self.selected,counters)

class BackgroundTile(sprite.Sprite):
    def __init__(self,rect):
        super().__init__()
        self.rook = None
        self.rect = rect
        self.health = 0

class PlayTile(BackgroundTile):
    def set_rook(self,rook,counters):
        if bool(rook) and not bool(self.rook):
            counters.enemy_money -= rook.cost
            self.rook = rook
            playTilesList.append(self)
            if rook == SANDrook:
                self.health = 14
                counters.money_booster += 1
                sand_rook_coordinates.append((self.rect.x,self.rect.y))
                all_rooks_created.append((self.rect.x,self.rect.y))
            if rook == ROCKrook:
                self.health = 14
                rock_rook_coordinates.append((self.rect.x,self.rect.y))
                all_rooks_created.append((self.rect.x, self.rect.y))
            if rook == WATERrook:
                self.health = 16
                water_rook_coordinates.append((self.rect.x,self.rect.y))
                all_rooks_created.append((self.rect.x, self.rect.y))
            if rook == FIRErook:
                self.health = 16
                fire_rook_coordinates.append((self.rect.x,self.rect.y))
                all_rooks_created.append((self.rect.x, self.rect.y))
        return None

    def draw_rook(self,game_window,rook_applicator):
        if bool(self.rook):
            game_window.blit(self.rook.type_img,(self.rect.x,self.rect.y))

    def unset_rook(self,rook,counters):
            if rook == ROCKrook:
                rook.kill()

    def attack_rook(self):
        for i in all_arrows:
            if isColliding(self.rect.x,self.rect.y,i.getX(),i.getY()):
                print("ROOK HEALTH DECREASES -2")
                self.rook.health -= 2
            else:
                print("NO COLLISION DETECTED")

class ButtonTile(BackgroundTile):
    def set_rook(self,rook,counters):
        if counters.enemy_money >= self.rook.cost:
            return self.rook
        else:
            return None

    def draw_rook(self,game_window,rook_applicator):
        if bool(rook_applicator.selected):
            if rook_applicator.selected == self.rook:
                draw.rect(game_window,(238,190,47),
                          (self.rect.x,self.rect.y,WIDTH,HEIGHT),5)

    def undraw(self,game_window,rook_remover):
        pass

class InactiveTiles(BackgroundTile):
    def set_rook(self,rook,counters):
        return None

    def draw_rook(self,game_window,rook_applicator ):
        pass

    def undraw(self,game_window,rook_remover):
        pass

class Bullets(sprite.Sprite):
    def __init__(self,coordinates,bullet_type):
        super().__init__()
        self.bullet_type = bullet_type
        if self.bullet_type == "ROCK_ROOK":
            self.image_bullet = ROCK_BULLET
            all_rock_bullets.add(self)
        elif self.bullet_type == "WATER_ROOK":
            self.image_bullet = WATER_BULLET
            all_water_bullets.add(self)
        elif self.bullet_type == "SAND_ROOK":
            self.image_bullet = SAND_BULLET
            all_sand_bullets.add(self)
        elif self.bullet_type == "FIRE_ROOK":
            self.image_bullet = FIRE_BULLET
            all_fire_bullets.add(self)

        self.speed = 2
        all_bullets.add(self)
        self.rect = self.image_bullet.get_rect()
        self.rect.x = coordinates[0] + 40
        self.rect.y = coordinates[1] + 40

    def update(self,game_window):
        game_window.blit(BACKGROUND,(self.rect.x,self.rect.y),self.rect)
        timer = pygame.time.get_ticks()
        timerBullets = timer/1000
        self.rect.x += self.speed
        if self.rect.x > 1200:
            self.kill()
        else:
            game_window.blit(self.image_bullet,(self.rect.x,self.rect.y))


class AvatarObject(sprite.Sprite):
    def __init__(self,x,y,object_type):
        super().__init__()
        #self.x = x
        #self.y = y+40
        self.object_type = object_type
        if object_type == "ARROW":
            self.image = ARROW

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y+40
        self.speed = 1
        all_arrows.add(self)

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def update_object(self,game_window):
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y),self.rect)
        self.rect.x -= self.speed
        if self.rect.x < 100:
            print("COORDINATES FOR ARROW"+str(self.rect.x)+" - "+ str(self.rect.y))
            self.kill()
        else:
            game_window.blit(self.image,(self.rect.x, self.rect.y))

    def attack(self):
        for COORDS in all_rooks_created:
            x,y = COORDS
            if isColliding(x,y,self.rect.x,self.rect.y):
                print("ARROW COLLIDES WITH ROOK****")
            else:
                print("NOT COLLIDING")

def PlayMainMusic():
    """Plays game music"""
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("mainTheme.wav"),-1)

def PlayExplosionSound():
    """Plays sound effect"""
    pygame.mixer.init()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("explosion.wav"))

def PlayHitSound(channel):
    """Plays sound effect"""
    pygame.mixer.init()
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound("hit1.wav"))

def ReadFile():
    """This function reads the file of the scores
    and return the content in a list"""
    path = "TopScores.txt"
    file = open(path)
    content = file.readlines()
    file.close()
    return content

def WriteInFile(score):
    """This function writes the score on the file"""
    path = "TopScores.txt"
    file = open(path,"a")
    file.write(score+"\n")
    file.close()

def SaveScore(playerName,score,time):
    """This function gathers information from the player, it gets the player name,
    the score they got, and the time they played and then writes the information in a .txt file"""
    player = playerName
    scoreToSave = str(score)
    timePlayed = str(time)
    #data =
    #WriteInFile(data)


def isColliding(rookX, rookY,objectX,objectY):
    """Determines the distance between two objects, gets the coordinates in x and y
    of the main car and the enemy"""
    """Code based on 
    https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint"""
    distance = math.sqrt((math.pow(rookX - objectX, 2)) + (math.pow(rookY - objectY, 2)))
    if distance < 150:
        return True
    else:
        return False


#create group for all avatars instances and bullets instances
all_avatars_archers = sprite.Group()
all_bullets = sprite.Group()
all_water_bullets = sprite.Group()
all_rock_bullets = sprite.Group()
all_sand_bullets = sprite.Group()
all_fire_bullets = sprite.Group()
all_arrows = sprite.Group()
all_rooks_sprite = sprite.Group()

#create an instance of counters
counters = Counters(startingMoney,moneyRate,startingMoneyBooster,WIN_TIME,ENEMIES_PASSED,FIRE_RATE)

#rook initialization
WATERrook = Rook("WATER_ROOK",5,WATER_ROOK)
FIRErook = Rook("FIRE_ROOK",3,FIRE_ROOK)
SANDrook = Rook("SAND_ROOK",7,SAND_ROOK)
ROCKrook = Rook("ROCK_ROOK",8,ROCK_ROOK)

rook_applicator = RookApplicator()
rook_remover = RookRemover()
def MainloopLevel1():
    #initialize and draw the background grid
    #create an empty list to hold the tile grid
    tile_grid = []
    #define color of grid outline
    tile_color = WHITE
    #populate the background grid
    for row in range(6):
        row_of_tiles = []
        tile_grid.append(row_of_tiles)
        for column in range(11):
            tile_rect = Rect(WIDTH*column,HEIGHT*row,WIDTH,HEIGHT)
            if column <= 1:
                new_tile = InactiveTiles(tile_rect)
            else:
                if row == 5:
                    if 2 <= column <= 5:
                        new_tile = ButtonTile(tile_rect)
                        new_tile.rook = [WATERrook,FIRErook,SANDrook,ROCKrook][column-2]
                    else:
                        new_tile = InactiveTiles(tile_rect)
                else:
                    new_tile = PlayTile(tile_rect)
            row_of_tiles.append(new_tile)
            if row == 5 and 2 <= column <= 5:
                GAME_WINDOW.blit(new_tile.rook.type_img,
                                 (new_tile.rect.x,new_tile.rect.y))

            if column != 0 and row != 5:
                if column != 1:
                    draw.rect(GAME_WINDOW,tile_color,
                              (WIDTH*column,HEIGHT*row,WIDTH,HEIGHT),1)

    GAME_WINDOW.blit(GAME_WINDOW,(0,0))

    #Mainloop
    game_running = True
    program_running = True
    PlayMainMusic()

    while game_running:

        #print(all_rooks_sprite)
        #print(len(all_rooks_created))
        print(len(playTilesList))
        #check for events
        for event in pygame.event.get():
            #Exit the game
            if event.type == QUIT:
                game_running = False
                program_running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    coordinates = mouse.get_pos()
                    x = coordinates[0]
                    y = coordinates[1]
                    tile_y = y // 100
                    tile_x = x // 100
                    #print(tile_y,tile_x)
                    print(x,y)
                    rook_applicator.select_tile(tile_grid[tile_y][tile_x],counters)
                elif event.button == 3:
                    coordinates = mouse.get_pos()
                    x = coordinates[0]
                    y = coordinates[1]
                    tile_y = y // 100
                    tile_x = x // 100
                    print(tile_y, tile_x)
                    print("SHOULD REMOVE THE ROOK")
                    print((x//100*100,y//100*100))
                    rook_remover.select_tile(tile_grid[tile_y][tile_x],counters)
            elif event.type == MOUSEMOTION:
                position = mouse.get_pos()
                #print(position)


        #spawn sprites
        if randint(1,SPAWN_RATE) == 1:
            Avatar(AVATAR_KNIGHT,3,10,10)
        elif randint(1,SPAWN_RATE) == 5:
            Avatar(AVATAR_ARCHER,2,5,12)
        elif randint(1,SPAWN_RATE) == 10:
            Avatar(AVATAR_CANNIBAL,12,25,14)
        elif randint(1,SPAWN_RATE) == 15:
            Avatar(AVATAR_lUMBERJACK,9,20,13)

        #set up collision detection
        #Draw the background grid
        for tile_row in tile_grid:
            for tile in tile_row:
                if bool(tile.rook):
                    GAME_WINDOW.blit(GAME_WINDOW,(tile.rect.x,tile.rect.y),tile.rect)

        #Set up detection for collision with background tiles
        for avatar_archer in all_avatars_archers:
            tile_row = tile_grid[avatar_archer.rect.y//100]
            avatar_archer_left_side = avatar_archer.rect.x // 100
            avatar_archer_right_side = (avatar_archer.rect.x + avatar_archer.rect.width)//100

            if 0 <= avatar_archer_left_side <= 10:
                left_tile = tile_row[avatar_archer_left_side]
            else:
                left_tile = None
            if 0 <= avatar_archer_right_side <= 10:
                right_tile = tile_row[avatar_archer_right_side]
            else:
                right_tile = None

            if bool(left_tile):
                avatar_archer.attack(left_tile)
            if bool(right_tile):
                if right_tile != left_tile:
                    avatar_archer.attack(right_tile)

        #set win or lose conditions
        if counters.enemies_passed >= ENEMIES_PASSED:
            game_running = False

        if counters.loop_count > WIN_TIME:
            game_running = False

        #Update enemies
        for avatar in all_avatars_archers:
            avatar.update(GAME_WINDOW,counters)

        #update rooks that have been set
        for tile_row in tile_grid:
            for tile in tile_row:
                tile.draw_rook(GAME_WINDOW,rook_applicator)

        #for bullet in all_bullets:
            #bullet.update(GAME_WINDOW)

        for bullet in all_fire_bullets:
            bullet.update(GAME_WINDOW)

        for bullet in all_rock_bullets:
            bullet.update(GAME_WINDOW)

        for bullet in all_sand_bullets:
            bullet.update(GAME_WINDOW)

        for bullet in all_water_bullets:
            bullet.update(GAME_WINDOW)

        for object in all_arrows:
            object.update_object(GAME_WINDOW)

        #for object in all_arrows:
            #object.attack()

        for object in playTilesList:
            object.attack_rook()
            object.kill()

        counters.update(GAME_WINDOW)

        display.update()
        clock.tick(FRAME_RATE)

    #End of mainloop

    end_font = font.SysFont(None,50)
    if program_running:
        if counters.enemies_passed >= ENEMIES_PASSED:
            end_surf = end_font.render("GAME OVER",True,WHITE)
        else:
            end_surf = end_font.render("YOU WIN!!",True,WHITE)
            GAME_WINDOW.blit(end_surf,(350,200))
            display.update()

    while program_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                program_running = False
        clock.tick(FRAME_RATE)


#_____ANIMATIONS______________________
#ANIMATION FOR WHEN THE PLAYER WINS
def WinningAnimation():
    WindowAnimation = turtle.Screen()
    WindowAnimation.bgcolor("black")
    WindowAnimation.bgpic("5.png")
    WindowAnimation.title("You Won Animation")
    WindowAnimation.tracer(0)

    # Create the avatars and store them in a list
    avatars = []

    for i in range(15):
        avatars.append(turtle.Turtle())

    WindowAnimation.register_shape("avatarKnight.gif")
    WindowAnimation.register_shape("avatarCannibal.gif")
    WindowAnimation.register_shape("avatarLumberjack.gif")
    WindowAnimation.register_shape("avatarArcher.gif")

    imgs = ["avatarLumberjack.gif", "avatarCannibal.gif", "avatarKnight.gif", "avatarArcher.gif"]
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.goto(0, 150)
    font = ("Fixedsys", 80, "normal")
    pen.write("YOU WON! :)", font=font, align="center")

    for avatar in avatars:
        avatar.shape(choice(imgs))
        avatar.penup()
        avatar.speed(0)  # speed of the movement
        X = randint(-290, 290)
        Y = randint(200, 400)
        avatar.goto(X, Y)  # place where it starts
        avatar.dy = 0
        avatar.dx = randint(-3, 3)  # to move from left to right
        avatar.da = randint(-5, 5)
        gravity = 0.1

    while True:
        time.sleep(0.01)

        WindowAnimation.update()

        for avatar in avatars:
            avatar.rt(avatar.da)
            avatar.dy -= gravity
            avatar.sety(avatar.ycor() + avatar.dy)

            avatar.setx(avatar.xcor() + avatar.dx)
            # check for borderlines
            if avatar.xcor() > 330:
                avatar.dx *= -1
            if avatar.xcor() < -330:
                avatar.dx *= -1
            # bounces
            if avatar.ycor() < -330:
                avatar.dy *= -1

    WindowAnimation.mainloop()

#ANIMATION FOR WHEN THE PLAYER HAS LOST THE GAME
def GameOverAnimation():
    #Variables for display
    animationWindow = turtle.Screen()
    animationWindow.title("You Lost Animation")
    animationWindow.bgcolor("green")
    animationWindow.bgpic("5.png")
    animationWindow.setup(width=800,height=600)
    animationWindow.tracer(0)
    animationWindow.register_shape("diamond1.gif")
    animationWindow.register_shape("diamond2.gif")
    animationWindow.register_shape("diamond3.gif")

    diamondShapes = ["diamond1.gif","diamond2.gif","diamond3.gif"]

    #Create a list of diamonds
    diamonds = []

    #Add the diamonds
    for i in range(50):
        diamond = turtle.Turtle()
        diamond.speed(0)
        diamond.shape(choice(diamondShapes))
        diamond.color("blue")
        diamond.penup()
        diamond.goto(0,250)
        diamond.speed = randint(1,4)
        diamonds.append(diamond)


    #Pen to write on screen
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.goto(0,150)
    font = ("Fixedsys",80,"normal")
    pen.write("YOU LOST! :(",font=font,align="center")

    #Mainloop for the animation
    while True:
        animationWindow.update()
        #Move the diamond
        for diamond in diamonds:
            y = diamond.ycor()
            y -= diamond.speed
            diamond.sety(y)
            #Check if off the screen
            if y < -300:
                x = randint(-380,380)
                y = randint(300,400)
                diamond.goto(x,y)

    animationWindow.mainloop()


#MainloopLevel1()
#WinningAnimation()
#GameOverAnimation()
WelcomeWindow()

pygame.quit()




