
import pygame, sys
import os
import time
import random
import json
from os import path
from pygame import mouse
from pygame.locals import *
pygame.font.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
pygame.mixer.init()
font_name = pygame.font.match_font('arial')
sound_folder = path.join(path.dirname(__file__), 'sounds')
width = screen.get_width()
height = screen.get_height()
# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "enemyBlack1.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "enemyBlue2.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "enemyGreen4.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "playerShip1_orange.png"))

# Item
HEART = pygame.image.load(os.path.join("assets", "pixel-heart.png"))
SPEED = pygame.image.load(os.path.join("assets", "bolt_gold.png"))
# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "laserRed02.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "laserGreen15.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "laserBlue11.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Logo
LOGO = pygame.image.load(os.path.join("assets", "logo5.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "starfield.png")), (WIDTH, HEIGHT))
# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#load sounds
die_sound = pygame.mixer.Sound(path.join(sound_folder, 'diesound.ogg'))
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'pew.wav'))
game_over_sound = pygame.mixer.Sound(path.join(sound_folder, 'gameover1.ogg'))
game_play_sound = pygame.mixer.Sound(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
menu_sound = pygame.mixer.Sound(path.join(sound_folder, 'menu.ogg'))
live_up_sound = pygame.mixer.Sound(path.join(sound_folder, 'liveup.ogg'))
speed_up_sound = pygame.mixer.Sound(path.join(sound_folder, 'speedup.ogg'))

class Button:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        #text
        self.text_surf = POKEFONT3.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, window):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(window,self.top_color, self.top_rect,border_radius = 12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    main()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

    def set_text(self, text):
        self.text = text

class Button1:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        #text
        self.text_surf = POKEFONT3.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, window):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(window,self.top_color, self.top_rect,border_radius = 12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    settings()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

    def set_text(self, text):
        self.text = text

class Button2:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        #text
        self.text_surf = POKEFONT3.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, window):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(window,self.top_color, self.top_rect,border_radius = 12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    tutorial()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

    def set_text(self, text):
        self.text = text

class Button3:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#354B5E'
        #text
        self.text_surf = POKEFONT3.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, window):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(window,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(window,self.top_color, self.top_rect,border_radius = 12)
        window.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    pygame.quit()
                    sys.exit()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'

    def set_text(self, text):
        self.text = text

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class LiveDrop:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = HEART
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class SpeedUp:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = SPEED
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                s = str(obj)
                if s[1:16] == "__main__.Player":
                    global lives
                    global power
                    lives = lives - 1
                die_sound.play()
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            shooting_sound.play()
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    global lives
    global power
    def __init__(self, x, y,):
        super().__init__(x, y)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.rect = self.ship_img.get_rect()
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            global score
                            score += 1

    def getX(self):
        return self.x
    def getY(self):
        return self.y
                        
    
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class VEnemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }          

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

class HEnemy(Ship):
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.x += vel

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1  

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def main():
    global button
    FPS = 60
    run = True
    level = 0
    global lives
    global highscore
    global score
    global game_count
    game_count += 1
    score = 0
    lives = 1
    liveDrop = []
    speedUp = []
    main_font = pygame.font.SysFont("comicsans", 30)
    lost_font = pygame.font.SysFont("comicsans", 40)
    Venemies = []
    Vwave_length = 5

    Henemies = []
    Hwave_length = 5
    remain = 0

    enemy_vel = 1
    player_vel = 5
    laser_vel = 5
    lost = False
    lost_count = 0

    player = Player(300,650)
    def redraw_window():
        WIN.blit(BG, (0,0))
        
        #text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        score_label = main_font.render(f"Score: {score}", 1, (255,255,255))
        highscore_label = main_font.render(f"High Score: {highscore}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        WIN.blit(score_label, (10, 50))
        WIN.blit(highscore_label, (WIDTH - highscore_label.get_width() - 10, 50))

        for Venemy in Venemies:
            Venemy.draw(WIN)

        for Henemy in Henemies:
            Henemy.draw(WIN)

        for liveD in liveDrop:
            liveD.draw(WIN) 

        for speedD in speedUp:
            speedD.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("Game Over", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
            game_over_sound.play()
        pygame.display.update()


    while run:
        redraw_window()
        if highscore < score:
            highscore = score

        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                lives = 2
                run = False
                button = Button('Play again',200,40,(WIN.get_width()/2-100,WIN.get_height()/2+38),5)
                button.draw(WIN)
            else:
                continue

        if len(Venemies) == 0:
            for i in range(Vwave_length):
                enemy = VEnemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                Venemies.append(enemy)


            if random.random() > 0.6 and random.random() < 0.9:
                  liveD = LiveDrop(random.randrange(50, WIDTH-100), -1000, HEART)
                  liveDrop.append(liveD)

            if random.random() > 0.3 and random.random() <= 0.8:
                speedD = SpeedUp(random.randrange(50, WIDTH-100), -1000, SPEED)
                speedUp.append(speedD)

            if level >= 3:
                if remain > 0:
                    for i in range (Hwave_length + remain):
                        enemy = HEnemy(random.randrange(-1500, -100), random.randrange(50, 350), random.choice(["red", "blue", "green"]))
                        Henemies.append(enemy)
                        remain = 0
                else:
                    for i in range (Hwave_length):
                        enemy = HEnemy(random.randrange(-1500, -100), random.randrange(50, 350), random.choice(["red", "blue", "green"]))
                        Henemies.append(enemy)
            level += 1
            lives += 1
            if level >= 3:
                enemy_vel += 0.2
            Vwave_length += 2
            Hwave_length += 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for liveD in liveDrop[:]:
            liveD.move(enemy_vel)
            if collide(liveD, player):
                liveDrop.remove(liveD)
                lives += 1
                live_up_sound.play()

        for speedD in speedUp[:]:
            speedD.move(enemy_vel)
            if collide(speedD, player):
                speedUp.remove(speedD)
                player_vel += 0.5
                speed_up_sound.play()

        for enemy in Venemies[:]:
            enemy.move(enemy_vel)
            if collide(enemy, player):
                Venemies.remove(enemy)
                lives -= 1
                die_sound.play()

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                die_sound.play()
                Venemies.remove(enemy)
        player.move_lasers(-laser_vel, Venemies)

        for enemy in Henemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if collide(enemy, player):
                Henemies.remove(enemy)
                lives -= 1
                die_sound.play()

            elif enemy.x + enemy.get_width() > WIDTH:
                Henemies.remove(enemy)
                remain += 1

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()
        player.move_lasers(-laser_vel, Henemies)

def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_text1(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


font = pygame.font.SysFont('comicsans', 50)

def settings():
    text4 = POKEFONT2.render('Music: On/Off', True, color)
    text5 = POKEFONT2.render('Volume', True, color)
    FPS = 60
    clock = pygame.time.Clock()
    running = True
    button4 = pygame.Rect(280, 300, 190, 40)
    button5 = pygame.Rect(280, 230, 190, 40)
    music_paused = False
    volume = False
    while running:
        mx, my = pygame.mouse.get_pos()
        WIN.blit(BG, (0,0))
        draw_text1('Settings', POKEFONT1, (255, 255, 255), screen, 20, 20)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if button4.collidepoint((mx, my)):
                if click:
                    music_paused = not music_paused
                    if music_paused:
                        game_play_sound.stop()
                    else:
                        game_play_sound.play()
            if button5.collidepoint((mx, my)):
                if click:
                     volume = not volume
                     if volume:
                         game_play_sound.set_volume(0.3)
                     else:
                         game_play_sound.set_volume(1.5)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.draw.rect(screen, color1, [280, 300, 190, 40])
        pygame.draw.rect(screen, color1, [280, 230, 190, 40])
        screen.blit(text4, (WIN.get_width() / 2 - 82, WIN.get_height() / 2 -62))
        screen.blit(text5, (WIN.get_width() / 2 - 38, WIN.get_height() / 2 -130))
        pygame.display.update()
        clock.tick(FPS)

POKEFONT1 = pygame.font.Font("Pokemon GB.ttf", 30)
POKEFONT2 = pygame.font.Font("Pokemon GB.ttf", 13)
POKEFONT3 = pygame.font.Font("Pokemon GB.ttf", 15)

def tutorial():
    FPS = 60
    clock = pygame.time.Clock()
    game_play_sound.stop()
    menu_sound.play(-1)
    running2 = True
    text6 = smallfont.render('-> Press A,W,S,D,SPACE to control the ship', True, color)
    text7 = smallfont.render('A: move left,D: move right,W: move up,S: move down and SPACE to shoot', True, color)
    text8 = smallfont.render('-> After each level,your lives will increase', True, color)
    text9 = smallfont.render('-> From level 5,enemies that move horizontally will appear', True, color)
    text10 = smallfont.render('Be carefull!.They can shoot you!!', True, color)
    text11 = smallfont.render('-> Any enemies that move vertically reach the bottom of the screen,', True, color)
    text12 = smallfont.render('your lives will decrease', True, color)
    text13 = smallfont.render('-> Try to destroy enemies as many as you can to get highscore.Good luck!', True, color)

    while running2:
        WIN.blit(BG, (0, 0))
        draw_text1('Tutorial', POKEFONT1, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running2 = False
                    menu_sound.stop()
                    game_play_sound.play()
        screen.blit(text6, (WIN.get_width() / 2 -370, WIN.get_height() / 2 -200))
        screen.blit(text7, (WIN.get_width() / 2 -370, WIN.get_height() / 2 - 165))
        screen.blit(text8, (WIN.get_width() / 2 -370, WIN.get_height() / 2 - 125))
        screen.blit(text9, (WIN.get_width() / 2 -370, WIN.get_height() / 2 - 85))
        screen.blit(text10, (WIN.get_width() / 2 -370, WIN.get_height() / 2 - 50))
        screen.blit(text11, (WIN.get_width() / 2 -370, WIN.get_height() / 2 - 10))
        screen.blit(text12, (WIN.get_width() / 2 -370, WIN.get_height() / 2 +25))
        screen.blit(text13, (WIN.get_width() / 2 -370, WIN.get_height() / 2 +65))

        pygame.display.update()
        clock.tick(FPS)

click = False
color1 = (71,95,119)
smallfont = pygame.font.SysFont('comicsans',30)
color = (255,255,255)
def main_menu():
    global game_count
    game_count = 0
    main_font = pygame.font.SysFont("comicsans", 30)
    FPS = 60
    clock = pygame.time.Clock()
    data = open('data.json', 'r')
    storage = json.loads(data.read())
    global highscore
    global score
    score = 0
    highscore = int(storage['highscore'])
    data.close()
    run = True
    text1 = POKEFONT3.render('Tutorial', True, color)
    text2 = POKEFONT3.render('Settings', True, color)
    game_play_sound.play()
    global button
    button = Button('Play',200,40,(WIN.get_width()/2-100,WIN.get_height()/2+40),5)
    button1 =Button1('Settings',200,40,(WIN.get_width()/2-100,WIN.get_height()/2+110),5)
    button2 =Button2('Tutorial',200,40,(WIN.get_width()/2-100,WIN.get_height()/2+180),5)
    button3 = Button3('Quit', 200, 40, (WIN.get_width() / 2 - 100, WIN.get_height() / 2 + 250), 5)
    while run:
        WIN.blit(BG, (0,0))
        if game_count != 0:
            score_label = main_font.render(f"Score: {score}", 1, (255,255,255))
            highscore_label = main_font.render(f"High Score: {highscore}", 1, (255,255,255))
            WIN.blit(score_label, (100, WIN.get_height()/2+30))
            WIN.blit(highscore_label, (WIDTH - highscore_label.get_width() - 30, WIN.get_height()/2+30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data = open('data.json', 'w+')
                storage['highscore'] = highscore
                data.write(json.dumps(storage))
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                  pygame.quit()
                  sys.exit()
        button.draw(WIN)
        button1.draw(WIN)
        button2.draw(WIN)
        button3.draw(WIN)
        WIN.blit(LOGO, (70, -100))
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

pygame.init()
main_menu()
