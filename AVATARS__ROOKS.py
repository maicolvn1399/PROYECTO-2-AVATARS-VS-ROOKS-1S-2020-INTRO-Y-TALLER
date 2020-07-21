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


"""Code based on 
https://www.youtube.com/watch?v=PVY46hUp2EM
https://www.youtube.com/watch?v=giskNuBHPsU&t=17s
https://inventwithpython.com/pygame/
https://books.google.co.cr/books/about/Code_This_Game.html?id=EsLkDwAAQBAJ&source=kp_book_description&redir_esc=y
https://www.youtube.com/watch?v=HHQV3ifJopo&t=51s"""

#Initialize pygame
pygame.init()
font.init()
#constants for gui
display_width = 800
display_height = 600

avatarsDead = []

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
startingMoney = 50
moneyRate = 120
startingMoneyBooster = 20

#Set up win/lose conditions
ENEMIES_PASSED = 5 #cantidad de avatars que pasan
WIN_TIME = FRAME_RATE * 60 * 3

#Speeds
REG_SPEED = 2
SLOW_SPEED = 1

#lists for locations
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
background_img1 = image.load("backgroundlevel1.png")
background_surf1 = Surface.convert_alpha(background_img1)

background_img2 = image.load("backgroundlevel2.png")
background_surf2 = Surface.convert_alpha(background_img2)

background_img3 = image.load("backgroundlevel3.png")
background_surf3 = Surface.convert_alpha(background_img3)

BACKGROUND = transform.scale(background_surf1,WINDOW_RES)
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

axe_bullet_img = image.load("axe_bullet.png")
axe_bullet_surf = Surface.convert_alpha(axe_bullet_img)
AXE = transform.scale(arrow_bullet_surf,(65,25))

shield_bullet_img = image.load("shield_bullet.png")
shield_bullet_surf = Surface.convert_alpha(shield_bullet_img)
SHIELD = transform.scale(shield_bullet_surf,(40,40))

stick_bullet_img = image.load("stick_bullet.png")
stick_bullet_surf = Surface.convert_alpha(stick_bullet_img)
STICK = transform.scale(stick_bullet_surf,(70,25))


#image for explosion
explosion_img = image.load("explosion.png")
EXPLOSION = explosion_img
welcomeWindow = Tk()

#player name
playerName = ""

def WelcomeWindow():
    """This is the first window the player sees on screen, it allows the player to enter their name and select a level,
    or see the scores from previous games as well as the instructions and credits  """
    global welcomeWindow
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

    secondsLabel = Label(welcomeWindow, text="Enter the seconds", font="Fixedsys 16", bg=COLOR2, fg="black")
    secondsLabel.place(x=50, y=210)

    secondsEntry = Entry(welcomeWindow, width=25, bg=COLOR2, fg="black")
    secondsEntry.place(x=250, y=210)

    levelLabel = Label(welcomeWindow, text="Select a level", font="Fixedsys 16", bg=COLOR3, fg="black")
    levelLabel.place(x=50, y=260)

    buttonLevel1 = Button(welcomeWindow,font = "Fixedsys 16", text="Level 1",bg=COLOR3,fg="black",command = lambda: ValidateInputs(str(nameEntry.get()),int(secondsEntry.get()),"LEVEL1"))
    buttonLevel1.place(x=250,y=260)

    buttonLevel2 = Button(welcomeWindow,font = "Fixedsys 16", text="Level 2",bg=COLOR4,fg="black",command = lambda: ValidateInputs(str(nameEntry.get()),int(secondsEntry.get()),"LEVEL2"))
    buttonLevel2.place(x=250,y=290)

    buttonLevel3 = Button(welcomeWindow,font = "Fixedsys 16", text="Level 3",bg=COLOR5,fg="black",command = lambda: ValidateInputs(str(nameEntry.get()),int(secondsEntry.get()),"LEVEL3"))
    buttonLevel3.place(x=250,y=330)

    instructionsButton = Button(welcomeWindow, font="Fixedsys 16", text="Instructions", bg=COLOR3, fg="black",
                                command=Instructions)
    instructionsButton.place(x=250, y=360)

    previousScoresButton = Button(welcomeWindow, font="Fixedsys 16", text="Best Scores", bg=COLOR4, fg="black",
                                  command=lambda: TopScoresWindow())
    previousScoresButton.place(x=250, y=390)

    creditsButton = Button(welcomeWindow, font="Fixedsys 16", text="Credits", bg=COLOR5, fg="black", command=Credits)
    creditsButton.place(x=250, y=420)

    welcomeWindow.mainloop()

def TopScoresWindow():
    """"GUI to show the scores of the game"""
    ScoresWindow = Toplevel()
    COLOR1 = "#FF8903"
    COLOR2 = "#76E400"
    COLOR3 = "#F2A400"
    COLOR4 = "#A9EC0C"
    COLOR5 = "#FDC61C"
    ScoresWindow.minsize(450, 400)
    ScoresWindow.resizable(width=NO, height=NO)
    ScoresWindow.title("Top Best Scores")
    scores = GetScores()

    backgroundImageScore = LoadImage("background.gif")
    labelBGScores = Label(ScoresWindow, image=backgroundImageScore)
    labelBGScores.image = backgroundImageScore
    labelBGScores.place(x=0, y=0, relwidth=1, relheight=1)

    labelScores = Label(ScoresWindow,text="Scores",font = "Fixedsys 17",bg=COLOR3)
    labelScores.place(x=65,y=30)
    messageScores = Message(ScoresWindow,
                      text=str(scores),
                      bg=COLOR4, justify="left", relief="ridge", font="Fixedsys 16")
    messageScores.place(x=50, y=150)
    ScoresWindow.mainloop()


def Instructions():
    """GUI  to show the instructions of the game to the players"""
    instructionsWindow = Toplevel()
    COLOR1 = "#FF8903"
    COLOR2 = "#76E400"
    COLOR3 = "#F2A400"
    COLOR4 = "#A9EC0C"
    COLOR5 = "#FDC61C"
    instructionsWindow.minsize(450, 500)
    instructionsWindow.resizable(width=NO, height=NO)
    instructionsWindow.title("Instructions")

    backgroundImage = LoadImage("background.gif")
    labelBackground = Label(instructionsWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0, relwidth=1, relheight=1)
    labelBackground.image = backgroundImage
    message = Message(instructionsWindow, text="The objective of the game is to kill the avatars appearing in the "
                                               "right side of the screen, to do so, you have to select one rook"
                                               "from the bottom of the screen,you have to select the rook with your mouse, if you have enough money to get it the rook will be placed, there are four types of rooks:"
                                               "\nWater rook: shoots water to the enemies "
                                               "\nRock rook: shoots rocks to the enemies "
                                               "\nSand rook: throws sand to the opponents "
                                               "\nFire rook: throws fire balls to the opponents, then you have to and place it to the game board "
                                               "once the rook is set, it will begin to shoot the enemies, be careful because "
                                               "the avatars will appear constantly and they will fight back.\n\n Good luck!", bg=COLOR5, justify="left", relief="ridge", font="Fixedsys 13")
    message.place(x=20, y=50)
    instructionsWindow.mainloop()

def Credits():
    """GUI for the credits of the game"""
    creditsWindow = Toplevel()
    COLOR1 = "#FF8903"
    COLOR2 = "#76E400"
    COLOR3 = "#F2A400"
    COLOR4 = "#A9EC0C"
    COLOR5 = "#FDC61C"
    creditsWindow.minsize(450, 500)
    creditsWindow.resizable(width=NO, height=NO)
    creditsWindow.title("Credits")


    backgroundImage = LoadImage("background.gif")
    labelBackground = Label(creditsWindow, image=backgroundImage)
    labelBackground.place(x=0, y=0, relwidth=1, relheight=1)
    labelBackground.image = backgroundImage

    img_raquel = LoadImage("raquel.gif")
    labelRaquel = Label(creditsWindow, image=img_raquel)
    labelRaquel.place(x=50, y=300)
    labelRaquel.image = img_raquel

    img_michael = LoadImage("michael.gif")
    labelMichael = Label(creditsWindow, image=img_michael)
    labelMichael.place(x=300,y=300)
    labelMichael.image = img_michael


    message = Message(creditsWindow, text="Desarrollado en Costa Rica\n\n"
                                          "Tecnológico de Costa Rica, Ingeniería en Computadores\n\n"
                                          "CE1102-Taller de Programación, Grupo 4\n\n"
                                          "Profesor Jason Leitón Jiménez\n\n"
                                          "Version 1.0\n\n"
                                          "Realizado por Raquel Lizano y Michael Valverde\n\n"
                                          "II Proyecto - I Semestre - 2020\n\n", bg=COLOR2, justify="left", relief="ridge", font="Fixedsys 16")

    message.place(x=50, y=40)

    creditsWindow.mainloop()


def ValidateInputs(name, secondsToShoot,level):
    """Function that validates the inputs before running the game, the name should be an string and the level should be a integer,
otherwise it won't run and will ask the user to type or click valid value"""
    if isinstance(name, str) and not name.isspace() and not len(name) == 0 and isinstance(secondsToShoot,int) and level == "LEVEL1":
        print("SECONDS TO SHOOT "+str(secondsToShoot))
        return MainloopLevel1(name,secondsToShoot)
    elif isinstance(name, str) and not name.isspace() and not len(name) == 0 and isinstance(secondsToShoot,int) and level == "LEVEL2":
        return MainloopLevel2(name,secondsToShoot)
    elif isinstance(name, str) and not name.isspace() and not len(name) == 0 and isinstance(secondsToShoot,int) and level == "LEVEL3":
        return MainloopLevel3(name,secondsToShoot)
    else:
        return messagebox.showerror("Error", "You have to enter a valid player name or a valid amount of seconds")


def LoadImage(ImgName):
    """Loads and image"""
    path = os.path.join('media', ImgName)
    imageToLoad = PhotoImage(file=path)
    return imageToLoad

#set up classes
class Avatar(sprite.Sprite):
    """Create avatars with specific features, the object created will be the enemy of the game"""
    def __init__(self,type,image,attackPower,health,walkSeconds):
        super().__init__()
        self.type = type
        if self.type == "AVATAR_ARCHER":
            all_avatars_archers.add(self)
        elif self.type == "AVATAR_KNIGHT":
            all_avatars_knights.add(self)
        elif self.type == "AVATAR_CANNIBAL":
            all_avatars_cannibals.add(self)
        elif self.type == "AVATAR_LUMBERJACK":
            all_avatars_lumberjacks.add(self)

        self.speed = REG_SPEED
        self.lane = randint(0,4)
        all_avatars.add(self)
        self.image = image
        y = 50 + self.lane * 100
        self.health = health
        self.attackPower = attackPower
        self.walkSeconds = walkSeconds
        self.stop = False
        self.rect = self.image.get_rect(center=(1100,y))
        self.despawn_wait = None
        self.avatars_killed_count = 0

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def setSpeed(self,newSpeed):
        self.speed = newSpeed

    def getAvatarsKilledCount(self):
        return self.avatars_killed_count

    def update(self,game_window,counters):
        """this method makes the avatar move"""
        game_window.blit(BACKGROUND,
                         (self.rect.x, self.rect.y), self.rect)

        timer = pygame.time.get_ticks()
        timerWalk = int(timer/1000)
        """Avatars move """
        if timerWalk%self.walkSeconds == 0 and not self.stop:
            self.rect.x -= self.speed*1
            self.stop = True
        else:
            self.stop = False


        """Check for collisions with bullets"""
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

        """When an avatar cross the board"""
        if self.rect.x <= 100:
            counters.enemies_passed += 1
            self.despawn_wait = 0

        """Check for when the avatar is dead"""
        if self.despawn_wait is None:
            if self.health <= 0:
                self.image = EXPLOSION
                self.speed = 0
                self.despawn_wait = 20
            game_window.blit(self.image,(self.rect.x,self.rect.y))
        elif self.despawn_wait <= 0:
            self.avatars_killed_count = 1
            avatarsDead.append(1)
            self.kill()

        else:
            self.despawn_wait -= 1
        game_window.blit(self.image,(self.rect.x,self.rect.y))

    def attack(self,tile):
        """Avatar attacks when is close to a rook"""
        if tile.rook == WATERrook:
            self.speed = SLOW_SPEED
        elif tile.rook == FIRErook:
            self.health -= 1
        elif tile.rook == ROCKrook:
            self.health = 0

globalTimer = 0
class Counters(object):
    """Class for counters on the screen"""
    def __init__(self,enemy_money,money_rate,money_booster,timer,enemies_passed,fire_rate,gameTimerSeconds,name):
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
        self.gameTimerSeconds = gameTimerSeconds
        self.gameTimerSeconds_rect = None
        self.name = name
        self.name_rect = None

    def setFIRE_RATE(self,NEW_FIRE_RATE):
        self.fire_rate = NEW_FIRE_RATE

    def getFIRE_RATE(self):
        return self.fire_rate

    def increment_money(self):
        """Increment money"""
        if self.loop_count % self.money_rate == 0:
            self.enemy_money += self.money_booster

    def draw_money(self,game_window):
        """Display money on screen"""
        if self.money_rect:
            game_window.blit(BACKGROUND,(self.money_rect.x,self.money_rect.y),self.money_rect)
        money_surface = self.display_font.render("$"+str(self.enemy_money),True,WHITE)
        self.money_rect = money_surface.get_rect()
        self.money_rect.x = WINDOW_WIDTH - 80
        self.money_rect.y = WINDOW_HEIGHT - 60
        game_window.blit(money_surface,self.money_rect)

    def draw_enemies_passed(self,game_window):
        """Display the amount of avatars that have crossed the game board """
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
        timerGame = int(pygame.time.get_ticks()/1000)
        globalTimer = timerGame
        #timer_surf = self.display_font.render(str(WIN_TIME - self.loop_count // FRAME_RATE),True,WHITE)
        timer_surf = self.display_font.render(str(timerGame)+"s",True,WHITE)
        self.timer_rect = timer_surf.get_rect()
        self.timer_rect.x = WINDOW_WIDTH - 250
        self.timer_rect.y = WINDOW_HEIGHT - 50
        game_window.blit(timer_surf,self.timer_rect)

    def draw_name(self,game_window):
        if self.name_rect:
            game_window.blit(BACKGROUND,
                             (self.timer_rect.x, self.timer_rect.y), self.name_rect)
        name_surface = self.display_font.render(str(self.name),True,WHITE)
        self.name_rect = name_surface.get_rect()
        self.name_rect.x = WINDOW_WIDTH - 400
        self.name_rect.y = WINDOW_HEIGHT - 400
        game_window.blit(name_surface, self.name_rect)

    def update(self,game_window):
        """Update all the methods of this class"""
        self.loop_count += 1
        self.increment_money()
        self.draw_money(game_window)
        self.draw_enemies_passed(game_window)
        self.draw_timer(game_window)
        self.update_rock_rook()
        self.update_fire_rook()
        self.update_water_rook()
        self.update_sand_rook()
        self.update_avatar_archer_objects()
        #self.update_rook_damage()
        self.update_avatar_cannibal_objects()
        self.update_avatar_knights_objects()
        self.update_avatar_lumberjack_objects()
        self.draw_name(game_window)

    def update_rock_rook(self):
        """Create a new bullet given the coordinates of a rook"""
        for location in rock_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"ROCK_ROOK")

    def update_fire_rook(self):
        """Create a new bullet given the coordinates of a rook"""
        for location in fire_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"FIRE_ROOK")

    def update_water_rook(self):
        """Create a new bullet given the coordinates of a rook"""
        for location in water_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"WATER_ROOK")

    def update_sand_rook(self):
        """Create a new bullet given the coordinates of a rook"""
        for location in sand_rook_coordinates:
            if self.loop_count%self.fire_rate == 0:
                Bullets(location,"SAND_ROOK")

    def update_avatar_archer_objects(self):
        """Create a new bullet given the coordinates of a rook"""
        for i in all_avatars_archers:
            if self.loop_count % 600 == 0:
                AvatarObject(i.getX(),i.getY(),"ARROW",ARROW)

    def update_avatar_knights_objects(self):
        """Create a new bullet given the coordinates of a rook"""
        for i in all_avatars_knights:
            if self.loop_count%900 == 0:
                AvatarObject(i.getX(), i.getY(), "SHIELD",SHIELD)

    def update_avatar_cannibal_objects(self):
        """Create a new object for the avatars given the coordinates each avatar"""
        for i in all_avatars_cannibals:
            if self.loop_count % 180 == 0:
                AvatarObject(i.getX(), i.getY(), "STICK",STICK)

    def update_avatar_lumberjack_objects(self):
        """Create a new object for the avatars given the coordinates each avatar"""
        for i in all_avatars_lumberjacks:
            if self.loop_count % 300 == 0:
                AvatarObject(i.getX(), i.getY(), "AXE",AXE)

    def update_rook_damage(self):
        for pos in sand_rook_coordinates:
            sand_rookX,sand_rookY = pos
            if isColliding(sand_rookX,sand_rookY):
                print("IS COLLIDING")

class Rook(sprite.Sprite):
    """Class to create a rook"""
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
        self.bullet_stop = False #Atribute to shoot objects to the avatars

class RookApplicator(object):
    """Class to make a rook appear and function on screen"""
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
    """Draw invisibles tiles for the matrix on the screen"""
    def __init__(self,rect):
        super().__init__()
        self.rook = None
        self.rect = rect

class PlayTile(BackgroundTile):
    """Make tiles interactive for when a tile gets clicked"""
    def set_rook(self,rook,counters):
        """Sets the rook in the position the player chose"""
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
        """Draw a rook """
        if bool(self.rook):
            game_window.blit(self.rook.type_img,(self.rect.x,self.rect.y))

    def unset_rook(self,rook,counters):
            if rook == ROCKrook:
                rook.kill()

    def attack_rook(self):
        """Method for when a rook is being attacked"""
        for i in all_arrows:
            if isColliding(self.rect.x,self.rect.y,i.getX(),i.getY()):
                #print("ROOK HEALTH DECREASES -2")
                self.rook.health -= 2
                i.kill()


        for i in all_sticks:
            if isColliding(self.rect.x,self.rect.y,i.getX(),i.getY()):
                #print("ROOK HEALTH DECREASES -12")
                self.rook.health -= 12
                i.kill()


        for i in all_axes:
            if isColliding(self.rect.x,self.rect.y,i.getX(),i.getY()):
                print("ROOK HEALTH DECREASES -9")
                self.rook.health -= 9
                i.kill()
            else:
                print("NO COLLISION DETECTED")

        for i in all_shields:
            if isColliding(self.rect.x,self.rect.y,i.getX(),i.getY()):
                #print("ROOK HEALTH DECREASES -3")
                self.rook.health -= 3
                i.kill()


        #if self.rook.health <= 0:
            #print("ROOK GOT KILLED")



class ButtonTile(BackgroundTile):
    """Make tiles as a button so it can be responsive when the user wants to select a rook"""
    def set_rook(self,rook,counters):
        if counters.enemy_money >= self.rook.cost:
            return self.rook
        else:
            return None

    def draw_rook(self,game_window,rook_applicator):
        """Draw the buttons at the bottom of the screen"""
        if bool(rook_applicator.selected):
            if rook_applicator.selected == self.rook:
                draw.rect(game_window,(238,190,47),
                          (self.rect.x,self.rect.y,WIDTH,HEIGHT),5)

    def undraw(self,game_window,rook_remover):
        pass

class InactiveTiles(BackgroundTile):
    """Inactive tiles to prevent the player to place a rook outside the game board"""
    def set_rook(self,rook,counters):
        return None

    def draw_rook(self,game_window,rook_applicator ):
        pass

    def undraw(self,game_window,rook_remover):
        pass

class Bullets(sprite.Sprite):
    """Class for the objects that the rooks throw to the avatars"""
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
        """Updates the bullets """
        game_window.blit(BACKGROUND,(self.rect.x,self.rect.y),self.rect)
        timer = pygame.time.get_ticks()
        timerBullets = timer/1000
        self.rect.x += self.speed
        if self.rect.x > 1200:
            self.kill()
        else:
            game_window.blit(self.image_bullet,(self.rect.x,self.rect.y))


class AvatarObject(sprite.Sprite):
    """Class for the objects that the avatars throw to the rooks"""
    def __init__(self,x,y,object_type,image):
        super().__init__()
        #self.x = x
        #self.y = y+40
        self.image = image
        self.object_type = object_type
        if self.object_type == "ARROW":
            all_arrows.add(self)
        elif self.object_type == "STICK":
            all_sticks.add(self)
        elif self.object_type == "SHIELD":
            all_shields.add(self)
        elif self.object_type == "AXE":
            all_axes.add(self)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y+40
        self.speed = 1

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def update_object(self,game_window):
        """Update the object """
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
    path = "gameScores.txt"
    file = open(path)
    content = file.readlines()
    file.close()
    return content

def WriteInFile(score):
    """This function writes the score on the file"""
    path = "gameScores.txt"
    file = open(path,"a")
    file.write(score+"\n")
    file.close()

def SaveScore(playerName,score,time):
    """This function gathers information from the player, it gets the player name,
    the score they got, and the time they played and then writes the information in a .txt file"""
    player = playerName
    scoreToSave = str(score)
    timePlayed = str(time)
    data = player+","+timePlayed+","+scoreToSave
    WriteInFile(data)

def isColliding(rookX, rookY,objectX,objectY):
    """Determines the distance between two objects, gets the coordinates in x and y
    of the main car and the enemy"""
    """Code based on 
    https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint"""
    distance = math.sqrt((math.pow(rookX - objectX, 2)) + (math.pow(rookY - objectY, 2)))
    if distance < 80:
        return True
    else:
        return False

def GetScores():
    """Gets the scores of the file that stores values of the players"""
    return TopScores(sortList(getScoresAux(ReadFile(),[])),"",0)

def TopScores(list,topScores,num):
    """returns the scores and concatenates those values in a string"""
    non_blank_count = 0

    with open('gameScores.txt') as infp:
        for line in infp:
            if line.strip():
                non_blank_count += 1
    if num == non_blank_count:
        return topScores
    else:
        if num == 0:
            playerSc , playerNm, enemies = list[0]
            global firstBestScore
            firstBestScore = playerSc
        playerScore,playerName , avatarsKilled = list[0]
        return TopScores(list[1:],topScores+str(num+1)+"."+playerName+" - "+str(playerScore)+" Seconds"+" - "+avatarsKilled.replace("\n","")+" Dead Avatars"+"\n",num+1)

def getScoresAux(list,newList):
    """Gets the scores in a list"""
    if list == []:
        return newList
    else:
        return getScoresAux(list[1:],newList+[(int(list[0].split(",")[1]),str(list[0].split(",")[0]),str(list[0].split(",")[2]))])

def sortList(list):
    """"Sorts the list in ascending order, this way it keeps the lowest time as a score always on the top"""
    sortedList = sorted(list,key=itemgetter(0))
    return sortedList

def SortScores(list):
     """Returns a list of scores in ascending order"""
     list.sort()
     return list

def TimePlaying(secs):
    """Function that displays the player time in seconds"""
    font = pygame.font.SysFont(None, 25)
    text = font.render("Time: " + str(secs) + "s", True, (255,255,255))
    GAME_WINDOW.blit(text, (0, 55))

def PlayerName(name):
    """Function that displays the player's name or chosen nickname"""
    font = pygame.font.Font("font.ttf",25)
    text = font.render("Player: " + str(name), True,(255,255,255))
    GAME_WINDOW.blit(text, (0, 550))

def LevelDisplay(currentLevel):
    """Function that shows the current level an user is playing"""
    font = pygame.font.Font("font.ttf",25)
    text = font.render(str(currentLevel), True,(255,255,255))
    GAME_WINDOW.blit(text, (0, 25))

def DisplayAvatarsDead(num):
    font = pygame.font.Font("font.ttf", 25)
    text = font.render("Dead Avatars: "+str(num), True, (255, 255, 255))
    GAME_WINDOW.blit(text, (0, 50))





#create group for all avatars instances and bullets instances
all_avatars = sprite.Group()
all_avatars_archers = sprite.Group()
all_avatars_cannibals = sprite.Group()
all_avatars_knights = sprite.Group()
all_avatars_lumberjacks = sprite.Group()

all_bullets = sprite.Group()
all_water_bullets = sprite.Group()
all_rock_bullets = sprite.Group()
all_sand_bullets = sprite.Group()
all_fire_bullets = sprite.Group()

all_arrows = sprite.Group()
all_sticks = sprite.Group()
all_shields = sprite.Group()
all_axes = sprite.Group()

all_rooks_sprite = sprite.Group()
#Creation of timer
timer = pygame.time.get_ticks()
gameTimerSeconds = int(timer/1000)

#create an instance of counters

counters = Counters(startingMoney,moneyRate,startingMoneyBooster,WIN_TIME,ENEMIES_PASSED,FIRE_RATE,gameTimerSeconds,playerName)

#rook initialization
WATERrook = Rook("WATER_ROOK",150,WATER_ROOK)
FIRErook = Rook("FIRE_ROOK",150,FIRE_ROOK)
SANDrook = Rook("SAND_ROOK",50,SAND_ROOK)
ROCKrook = Rook("ROCK_ROOK",100,ROCK_ROOK)

rook_applicator = RookApplicator() #Create an instance of the rook applicator class

def MainloopLevel1(name,secondsToShoot):
    """First level of the game"""

    global BACKGROUND
    BACKGROUND = transform.scale(background_surf1,WINDOW_RES)
    GAME_WINDOW.blit(BACKGROUND, (0, 0))

    global avatarsDead
    avatarsDead = [] #Stores the amount of avatars that have been killed on screen

    counters.setFIRE_RATE(secondsToShoot*60)

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

    #Mainloop
    game_running = True
    program_running = True
    PlayMainMusic()

    while game_running:
        #Check for events
        for event in pygame.event.get():
            #Exit the game
            if event.type == QUIT:
                game_running = False
                program_running = False
            elif event.type == MOUSEBUTTONDOWN: #event for when the left button of the mouse is pressed
                if event.button == 1:
                    coordinates = mouse.get_pos() #gets the coordinates of the mouse
                    x = coordinates[0] #store the coordinates in a list
                    y = coordinates[1]
                    tile_y = y // 100 #get the column
                    tile_x = x // 100 #get the row
                    #print(tile_y,tile_x)
                    print(x,y)
                    rook_applicator.select_tile(tile_grid[tile_y][tile_x],counters) #Applies the rook to the game board
                elif event.button == 3:
                    coordinates = mouse.get_pos()
                    x = coordinates[0]
                    y = coordinates[1]
                    tile_y = y // 100
                    tile_x = x // 100
                    print(tile_y, tile_x)
                    print("SHOULD REMOVE THE ROOK")
                    print((x//100*100,y//100*100))
                    #rook_remover.select_tile(tile_grid[tile_y][tile_x],counters)
            elif event.type == MOUSEMOTION:
                position = mouse.get_pos()
                #print(position)

        PlayerName(name) #displays the player name
        timerSecs = int(pygame.time.get_ticks()//1000) #timer for the screen
        print(timerSecs)
        print("AVATARS KILLED "+str(len(avatarsDead)))

        LevelDisplay("Level 1")

        #spawn sprites
        if randint(1,SPAWN_RATE) == 1:
            Avatar("AVATAR_KNIGHT",AVATAR_KNIGHT,3,10,10)
        elif randint(1,SPAWN_RATE) == 5:
            Avatar("AVATAR_ARCHER",AVATAR_ARCHER,2,5,12)
        elif randint(1,SPAWN_RATE) == 10:
            Avatar("AVATAR_CANNIBAL",AVATAR_CANNIBAL,12,25,14)
        elif randint(1,SPAWN_RATE) == 15:
            Avatar("AVATAR_lUMBERJACK",AVATAR_lUMBERJACK,9,20,13)

        #set up collision detection
        #Draw the background grid
        for tile_row in tile_grid:
            for tile in tile_row:
                if bool(tile.rook):
                    GAME_WINDOW.blit(GAME_WINDOW,(tile.rect.x,tile.rect.y),tile.rect)

        #Set up detection for collision with background tiles
        for avatar_archer in all_avatars:
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

        #if counters.loop_count > WIN_TIME:
            #game_running = False

        #Update enemies
        for avatar in all_avatars:
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

        for object in all_shields:
            object.update_object(GAME_WINDOW)

        for object in all_sticks:
            object.update_object(GAME_WINDOW)

        for object in all_axes:
            object.update_object(GAME_WINDOW)

        #for object in all_arrows:
            #object.attack()

        for object in playTilesList:
            object.attack_rook()
            object.kill()

        #Wining or losing the game
        if len(avatarsDead) >= 10 and counters.enemies_passed < 8:#winning condition
            MainloopLevel2(name,secondsToShoot) #next level
        elif len(avatarsDead) < 10 and counters.enemies_passed >= 8: #losing condition
            SaveScore(name,len(avatarsDead),timerSecs)
            pygame.quit()
            welcomeWindow.destroy()
            GameOverAnimation() #show animation if the player has lost the game

        counters.update(GAME_WINDOW)

        display.update()
        clock.tick(FRAME_RATE)

    #End of mainloop



def MainloopLevel2(name,secondsToShoot):
    """Level 2"""
    global BACKGROUND
    BACKGROUND = transform.scale(background_surf2, WINDOW_RES)
    GAME_WINDOW.blit(BACKGROUND, (0, 0))

    global avatarsDead
    avatarsDead = [] #list that contains the number of avatars killed

    counters.setFIRE_RATE(secondsToShoot * 60)

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
    PlayMainMusic() #plays the music of the game

    while game_running:
        for event in pygame.event.get():
            #Exit the game
            if event.type == QUIT:
                game_running = False
                program_running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    coordinates = mouse.get_pos()#event for when the left button of the mouse is pressed
                    x = coordinates[0] #store the coordinates in a list
                    y = coordinates[1]
                    tile_y = y // 100 #column
                    tile_x = x // 100 #row
                    #print(tile_y,tile_x)
                    #print(x,y)
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
                    #rook_remover.select_tile(tile_grid[tile_y][tile_x],counters)
            elif event.type == MOUSEMOTION:
                position = mouse.get_pos()
                #print(position)

        PlayerName(name)
        LevelDisplay("Level 2")

        #spawn sprites
        if randint(1,SPAWN_RATE) == 1:
            Avatar("AVATAR_KNIGHT",AVATAR_KNIGHT,3,10,10)
        elif randint(1,SPAWN_RATE) == 5:
            Avatar("AVATAR_ARCHER",AVATAR_ARCHER,2,5,12)
        elif randint(1,SPAWN_RATE) == 10:
            Avatar("AVATAR_CANNIBAL",AVATAR_CANNIBAL,12,25,14)
        elif randint(1,SPAWN_RATE) == 15:
            Avatar("AVATAR_lUMBERJACK",AVATAR_lUMBERJACK,9,20,13)

        #set up collision detection
        #Draw the background grid
        for tile_row in tile_grid:
            for tile in tile_row:
                if bool(tile.rook):
                    GAME_WINDOW.blit(GAME_WINDOW,(tile.rect.x,tile.rect.y),tile.rect)

        #Set up detection for collision with background tiles
        for avatar_archer in all_avatars:
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

        #if counters.loop_count > WIN_TIME:
            #game_running = False

        #Update enemies


        for avatar in all_avatars:
            avatar.setSpeed(2)

        for avatar in all_avatars:
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

        for object in all_shields:
            object.update_object(GAME_WINDOW)

        for object in all_sticks:
            object.update_object(GAME_WINDOW)

        for object in all_axes:
            object.update_object(GAME_WINDOW)




        #for object in all_arrows:
            #object.attack()

        for object in playTilesList:
            object.attack_rook()
            object.kill()

        #Winning or losing the game
        if len(avatarsDead) >= 20 and counters.enemies_passed < 6:
            MainloopLevel3(name,secondsToShoot) #level 3
        elif len(avatarsDead) < 20 and counters.enemies_passed >= 6:
            pygame.quit()
            welcomeWindow.destroy()
            GameOverAnimation() #shows the animation if the player has lost the game

        counters.update(GAME_WINDOW)

        display.update()
        clock.tick(FRAME_RATE)

    #End of mainloop



def MainloopLevel3(name,secondsToShoot):
    """Level 3"""
    global BACKGROUND
    BACKGROUND = transform.scale(background_surf3, WINDOW_RES)
    GAME_WINDOW.blit(BACKGROUND, (0, 0))
    global avatarsDead
    avatarsDead = [] #store the amount of avatars that have been killed

    counters.setFIRE_RATE(secondsToShoot * 60)

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
    PlayMainMusic() #plays the music of the game

    while game_running:

        #print(all_rooks_sprite)
        #print(len(all_rooks_created))
        #print(len(playTilesList))
        #check for events
        for event in pygame.event.get():
            #Exit the game
            if event.type == QUIT:
                game_running = False
                program_running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    coordinates = mouse.get_pos() #gets the coordinates when the mouse is clicked
                    x = coordinates[0] #store the value in a list
                    y = coordinates[1] #store the value in a list
                    tile_y = y // 100 #column
                    tile_x = x // 100 #row
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
                    #rook_remover.select_tile(tile_grid[tile_y][tile_x],counters)
            elif event.type == MOUSEMOTION:
                position = mouse.get_pos()
                #print(position)

        PlayerName(name)
        LevelDisplay("Level 3")

        #spawn sprites
        if randint(1,SPAWN_RATE) == 1:
            Avatar("AVATAR_KNIGHT",AVATAR_KNIGHT,3,10,10)
        elif randint(1,SPAWN_RATE) == 5:
            Avatar("AVATAR_ARCHER",AVATAR_ARCHER,2,5,12)
        elif randint(1,SPAWN_RATE) == 10:
            Avatar("AVATAR_CANNIBAL",AVATAR_CANNIBAL,12,25,14)
        elif randint(1,SPAWN_RATE) == 15:
            Avatar("AVATAR_lUMBERJACK",AVATAR_lUMBERJACK,9,20,13)

        #set up collision detection
        #Draw the background grid
        for tile_row in tile_grid:
            for tile in tile_row:
                if bool(tile.rook):
                    GAME_WINDOW.blit(GAME_WINDOW,(tile.rect.x,tile.rect.y),tile.rect)

        #Set up detection for collision with background tiles
        for avatar_archer in all_avatars:
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

        #f counters.loop_count > WIN_TIME:
            #game_running = False

        for avatar in all_avatars:
            avatar.setSpeed(2.3)

        #Update enemies
        for avatar in all_avatars:
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

        for object in all_shields:
            object.update_object(GAME_WINDOW)

        for object in all_sticks:
            object.update_object(GAME_WINDOW)

        for object in all_axes:
            object.update_object(GAME_WINDOW)

        #for object in all_arrows:
            #object.attack()

        for object in playTilesList:
            object.attack_rook()
            object.kill()

        if len(avatarsDead) >= 30 and counters.enemies_passed < 5:#winning condition
            pygame.quit()
            welcomeWindow.destroy()
            WinningAnimation() #shuts down pygame and tkinter and shows the winning animation
        elif len(avatarsDead) < 30 and counters.enemies_passed >= 5:
            pygame.quit()
            welcomeWindow.destroy()
            GameOverAnimation() #show animation when the game is over

        counters.update(GAME_WINDOW)

        display.update()
        clock.tick(FRAME_RATE)

    #End of mainloop

#_____ANIMATIONS______________________
#ANIMATION FOR WHEN THE PLAYER WINS
def GameOverAnimation():
    WindowAnimation = turtle.Screen() #create screen for animation
    WindowAnimation.bgcolor("black")
    WindowAnimation.bgpic("5.png")
    WindowAnimation.title("Game Over")
    WindowAnimation.tracer(0)

    # Create the avatars and store them in a list
    avatars = []

    #adds a new turtle to the empty list previously created
    for i in range(15):
        avatars.append(turtle.Turtle())

    #load the images for animation
    WindowAnimation.register_shape("avatarKnight.gif")
    WindowAnimation.register_shape("avatarCannibal.gif")
    WindowAnimation.register_shape("avatarLumberjack.gif")
    WindowAnimation.register_shape("avatarArcher.gif")

    imgs = ["avatarLumberjack.gif", "avatarCannibal.gif", "avatarKnight.gif", "avatarArcher.gif"] #store images in a list
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.goto(0, 150)
    font = ("Fixedsys", 80, "normal")
    pen.write("YOU LOST ! :(", font=font, align="center")

    for avatar in avatars:
        avatar.shape(choice(imgs))#chooses an image randomly from the list
        avatar.penup()
        avatar.speed(0)  # speed of the movement
        X = randint(-290, 290)#gets a coordinate for x
        Y = randint(200, 400)#gets a coordinate for y
        avatar.goto(X, Y)  # place the turtle in the x y coordinates starts
        avatar.dy = 0
        avatar.dx = randint(-3, 3)  # to move from left to right
        avatar.da = randint(-5, 5)
        gravity = 0.1 #gravity to make avatars fall

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
def WinningAnimation():
    #Variables for display
    animationWindow = turtle.Screen() #create a display
    animationWindow.title("You Won!! :) ")
    animationWindow.bgcolor("green")
    animationWindow.bgpic("5.png")
    animationWindow.setup(width=800,height=600)
    animationWindow.tracer(0)
    #load images
    animationWindow.register_shape("diamond1.gif")
    animationWindow.register_shape("diamond2.gif")
    animationWindow.register_shape("diamond3.gif")

    #add the images to a list
    diamondShapes = ["diamond1.gif","diamond2.gif","diamond3.gif"]

    #Create a list of diamonds
    diamonds = []

    #Add the diamonds
    for i in range(50):
        diamond = turtle.Turtle()
        diamond.speed(0)
        diamond.shape(choice(diamondShapes)) #randomly chooses an image of the list previously created
        diamond.color("blue")
        diamond.penup()
        diamond.goto(0,250) #Starting point in x and y
        diamond.speed = randint(1,4) #randonmly chooses a speed so the diamonds can fall
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
    pen.write("YOU WON!!! :)",font=font,align="center")

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




