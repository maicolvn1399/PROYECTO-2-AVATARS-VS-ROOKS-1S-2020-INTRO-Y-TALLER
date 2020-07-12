import pygame
import random

IMAGEPATH = "imgs/"
screen_width = 800
screen_height = 560

GAMEOVER = False

LOG = "File: Method in {}: {}Error".format(__file__,__name__)

class Map:
    map_names_list = [IMAGEPATH + "map1.png",IMAGEPATH + "map2.png"]
    def __init__(self,x,y,img_index):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x,y)
        #Can be placed
        self.can_be_placed = True

    def load_map(self):
        MainGame.window.blit(self.image,self.position)

class Rook(pygame.sprite.Sprite):
    def __init__(self):
        super(Rook,self).__init__()
        self.live = True

    def load_image(self):
        if hasattr(self,"image") and hasattr(self,"rect"):
            MainGame.window.blit(self.image,self.rect)
        else:
            print(LOG)


class Diamond(Rook):
    def __init__(self,x,y):
        super(Diamond,self).__init__()
        self.image = pygame.image.load("imgs/diamond2.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.health = 100
        self.time_count = 0

    def produce_money(self):
        self.time_count += 1
        if self.time_count == 25:
            MainGame.money += 5
            self.time_count = 0

    def display_diamond(self):
        MainGame.window.blit(self.image,self.rect)


class FireRook(Rook):
    def __init__(self,x,y):
        super(FireRook,self).__init__()
        self.image = pygame.image.load("imgs/fireRook.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.health = 200
        self.shot_count = 0

    def shot(self):
        should_fire = False

        for avatar in MainGame.avatar_list:
            if avatar.rect.y == self.rect.y and avatar.rect.x < 800 and avatar.rect.x > self.rect.x:
                should_fire = True

        if self.live and should_fire:
            self.shot_count += 1

            if self.shot_count == 25:

                bullet = Bullet(self)
                MainGame.bullet_list.append(bullet)
                self.shot_count = 0

    def display_fireRook(self):
        MainGame.window.blit(self.image,self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,firerook):
        self.live = True
        self.image = pygame.image.load("imgs/fire.png")
        self.damage = 50
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.x = firerook.rect.x+ 60
        self.rect.y = firerook.rect.y + 15

    def move_bullet(self):
        if self.rect.x < screen_width:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_avatar(self):
        for avatar in MainGame.avatar_list:
            if pygame.sprite.collide_rect(self,avatar):
                self.live = False
                avatar.health -= self.damage
                if avatar.health <= 0:
                    avatar.live = False
                    self.nextLevel()

    def nextLevel(self):
        MainGame.score += 20
        MainGame.remnant_score -= 20
        for i in range(1,100):
            if MainGame.score == 100*i and MainGame.remnant_score == 0:
                MainGame.remnant_score = 100*i
                MainGame.c += 1
                MainGame.produce_avatar += 50

    def display_bullet(self):
        MainGame.window.blit(self.image,self.rect)

class Avatar(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Avatar,self).__init__()
        self.image = pygame.image.load("imgs/elf.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 1000
        self.damage = 2
        self.speed = 1
        self.live = True
        self.stop = False

    def move_avatar(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                MainGame.gameOver()

    def hit_rook(self):
        for rook in MainGame.rook_list:
            if pygame.sprite.collide_rect(self,rook):
                self.stop = True
                self.attack_rook(rook)

    def attack_rook(self,rook):
        rook.health -= self.damage

        if rook.health <= 0:
            a = rook.rect.y // 80 - 1
            b = rook.rect.x // 80
            map = MainGame.map_list[a][b]
            map.can_be_placed = True
            rook.live = False
            self.stop = False

    def display_avatar(self):
        MainGame.window.blit(self.image,self.rect)

class MainGame():
    c = 1
    score = 0
    remnant_score = 100
    money = 200

    map_points_list = []

    map_list = []

    rook_list = []

    bullet_list = []

    avatar_list = []

    avatarCount = 0
    produceAvatar = 100

    def init_window(self):
        pygame.display.init()
        MainGame.window = pygame.display.set_mode([screen_width,screen_height])

    def draw_text(self,content,size,color):
        pygame.font.init()
        font = pygame.font.SysFont('arial', size)
        text = font.render(content, True, color)
        return text

    def load_help_text(self):
        text1 = self.draw_text("Press the right button"
                               "to create a rook",26,(255, 0, 0))
        MainGame.window.blit(text1,(5,5))

    def init_rook_points(self):
        for y in range(1,7):
            points = []
            for x in range(10):
                point = (x,y)
                points.append(point)
        MainGame.map_points_list.append(points)
        print("MainGame.map_points_list",MainGame.map_points_list)


    def init_map(self):
        for points in MainGame.map_points_list:
            temp_map_list = list()
            for point in points:
                if (point[0] + point[1]) %2 == 0:
                    map = Map(point[0] * 80, point[1] * 80,0)
                else:
                    map = Map(point[0] * 80, point[1] * 80,1)

                temp_map_list.append(map)
                print("temp_map_list",temp_map_list)

            MainGame.map_list.append(temp_map_list)
        print("MainGame.map_list",MainGame.map_list)

    def load_map(self):
        for temp_map_list in MainGame.map_list:
            for map in temp_map_list:
                map.load_map()

    def load_rooks(self):
        for rook in MainGame.rook_list:
            if rook.live:
                if isinstance(rook,Diamond):
                    rook.display_diamond()
                    rook.produce_money()
                elif isinstance(rook,FireRook):
                    rook.display_fireRook()
                    rook.shot()
            else:
                MainGame.rook_list.remove(rook)

    def load_bullets(self):
        for b in MainGame.bullet_list:
            if b.live:
                b.display_bullet()
                b.move_bullet()
                b.hit_avatar()
            else:
                MainGame.bullet_list.remove(b)

    def deal_events(self):
        eventList = pygame.event.get()
        for e in eventList:
            if e.type == pygame.QUIT:
                self.gameOver()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                print(e.pos)
                x = e.pos[0] // 80
                y = e.pos[1] // 80
                print(x,y)
                map = MainGame.map_list[y - 3][x]
                print(map.position)
                if e.button == 1:
                    if map.can_be_placed and MainGame.money >= 50:
                        diamond = Diamond(map.position[0],map.position[1])
                        MainGame.rook_list.append(diamond)
                        map.can_be_placed = False
                        MainGame.money -=50
                elif e.button == 3:
                    if map.can_be_placed and MainGame.money >= 50:
                        firerook = FireRook(map.position[0],map.position[1])
                        MainGame.rook_list.append(firerook)
                        print("Current avatar list length: {}".format(len(MainGame.rook_list)))
                        map.can_be_placed = False
                        MainGame.money -= 50

    def init_avatars(self):
        for i in range(1,7):
            dis = random.randint(1,5) * 200
            avatar = Avatar(800+ dis,i*80)
            MainGame.avatar_list.append(avatar)

    def load_avatars(self):
        for avatar in MainGame.avatar_list:
            if avatar.live:
                avatar.display_avatar()
                avatar.move_avatar()
                avatar.hit_rook()
            else:
                MainGame.avatar_list.remove(avatar)

    def start_game(self):
        self.init_window()
        self.init_rook_points()
        self.init_map()
        self.init_avatars()

        while not GAMEOVER:

            MainGame.window.fill((255,255,255))
            #MainGame.init_window(self.draw_text('Current money: $: {}'.format(MainGame.money),26,(255,0,0)),(500,40))
            MainGame.window.blit(self.draw_text(
                "Current levels {}, score {}, "
                "less than {} points from Xiaguan".format(MainGame.c,MainGame.score,MainGame.remnant_score),26,(255,0,0)),(5,40
            ))
            self.load_help_text()
            self.load_map()
            self.load_avatars()
            self.load_bullets()
            self.deal_events()
            self.load_rooks()
            MainGame.avatarCount += 1
            if MainGame.avatarCount == MainGame.produceAvatar:
                self.init_avatars()
                MainGame.avatarCount = 0

            pygame.time.wait(10)
            pygame.display.update()

    def gameOver(self):
        MainGame.window.blit(self.draw_text("Game Over",50,(255,0,0)),(300,200))
        print("Game Over")
        pygame.time.wait(400)
        global GAMEOVER
        GAMEOVER = True

if __name__ == "__main__":
    game = MainGame()
    game.start_game()




























