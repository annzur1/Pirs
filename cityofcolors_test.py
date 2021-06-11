import pygame, sys, random
from pygame import surface
from pygame import image
from pygame.math import Vector2

pygame.init()

#### KLASA GRACZA ####
class Player:
    def __init__ (self):
        self.pos = Vector2(1,5)
        self.speed = 2
        self.direction = Vector2(1,0)
        self.stored_direction=None
        self.color = (pygame.Color("white"))
        self.pix_pos = self.get_pix_pos()
        self.can_move = True
    def update(self):
        if self.can_move:
            self.pix_pos += self.direction * self.speed
        if self.time_of_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
        self.pos[0]=(self.pix_pos[0]+cell_size//2)//cell_size
        self.pos[1]=(self.pix_pos[1]+cell_number//2)//cell_number
    def draw_player(self):
        pygame.draw.rect(screen, (self.color), (int(self.pix_pos.x), int(self.pix_pos.y), 10, 10))
    def move(self, direction):
        self.stored_direction = direction
    def get_pix_pos(self):
        return Vector2((self.pos.x * cell_size)//2 + cell_number//2, (self.pos.y * cell_number)//2 + cell_number//2)
    def time_of_move(self):
        if int(self.pix_pos.x//2) % cell_size == 0:
            if self.direction == Vector2(1, 0) or self.direction ==  Vector2(-1, 0) or self.direction ==  Vector2(0, 0):
                return True
        if int(self.pix_pos.y//2) % cell_number == 0:
            if self.direction ==  Vector2(0, 1) or self.direction ==  Vector2(0, -1) or self.direction == Vector2(0, 0):
                return True
    def collision(self):
        if Vector2(self.pos + self.direction) in buildings:
            print(self.pos)

#### KLASA PRZECIWNIKA ####
class Enemy:
    def __init__ (self):
        self.x = 25.5
        self.y= 25.5
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
        self.speed = 0.1
        self.direction = Vector2(0,0)
        self.color = (pygame.Color("red"))
    def update(self):
        self.pos = self.pos + (self.direction * self.speed)
    def draw_enemy(self):
        pygame.draw.rect(screen, (self.color), (int(self.pos.x), int(self.pos.y), 10, 10),)
    def move(self, direction):
        self.direction = direction
    def randmove(self, movecounter):
        if (movecounter % 120 == 0):
            self.randomizer = (random.randint(1, 4))
        if self.randomizer == 1:
            self.move(Vector2(-1 * cell_size, 0))
        elif self.randomizer == 2:
            self.move(Vector2(1 * cell_size, 0))
        elif self.randomizer == 3:
            self.move(Vector2(0, -1 * cell_size))
        else:
            self.move(Vector2(0, 1 * cell_size))

#### KLASA BYTU NEUTRALNEGO ####
class Stranger:
    def __init__ (self):
        self.x = 15.5
        self.y= 15.5
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
        self.speed = 0.1
        self.direction = Vector2(0,0)
        self.color = (pygame.Color("green"))
    def update(self):
        self.pos = self.pos + (self.direction * self.speed)
    def draw_stranger(self):
        pygame.draw.rect(screen, (self.color), (int(self.pos.x), int(self.pos.y), 10, 10),)
    def move(self, direction):
        self.direction = direction
    def randmove(self, movecounter):

        if (movecounter % 120 == 0):
            self.randomizer = (random.randint(1, 4))
        if self.randomizer == 1:
            self.move(Vector2(-1 * cell_size, 0))
        elif self.randomizer == 2:
            self.move(Vector2(1 * cell_size, 0))
        elif self.randomizer == 3:
            self.move(Vector2(0, -1 * cell_size))
        else:
            self.move(Vector2(0, 1 * cell_size))
### KLASA ELEMENT EKWIPUNKU ###
#jeszcze nie zaczęta


### ZDEFINIOWANIE ISTOTNYCH WARTOŚCI ###

width = 616
height = 660
cell_size = width//28
cell_number = height//30
screen = pygame.display.set_mode((width, height))
background = pygame.image.load('C:/Users/robal/Desktop/programowanie/img/miasto.png')
background = pygame.transform.scale(background, (width, height))
clock = pygame.time.Clock()
buildings = []
with open('C:/Users/robal/Desktop/programowanie/img/grid.txt') as file:
    for yidx, line in enumerate(file):
        for xidx, char in enumerate(line):
            if char == '1':
                buildings.append([xidx, yidx])

### ZMIENNE POTRZEBNE DO DZIAŁANIA MENU I OBRAZKI ###                
run = True
menu = True
ingame = False
credits = False
controls = False
menuimage = pygame.image.load('C:/Users/robal/Desktop/programowanie/img/menu2.jpg')
creditsimage = pygame.image.load('C:/Users/robal/Desktop/programowanie/img/credits.jpg')
ingameimage = pygame.image.load('C:/Users/robal/Desktop/programowanie/img/menuingame.jpg')
controlsimage = pygame.image.load('C:/Users/robal/Desktop/programowanie/img/controls.jpg')
imagerect = menuimage.get_rect()

### EKWIPUNEK ###
inventorysurface = pygame.Surface((width, 2*cell_size))
inventorysurface2 = pygame.Surface((16*cell_size, cell_size))
inventorysurface.fill('black')
inventorysurface2.fill('white')
inventoryrect = inventorysurface.get_rect(topleft = (0, height))
inventoryrect2 = inventorysurface.get_rect(topleft = (6*cell_size, height + cell_size/2))
inventory = []
for i in range (8):
    inventory.append(0)
print(inventory)
### TWORZENIE BYTÓW ###

player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
stranger = Stranger()
movecounter = 0


### GŁÓWNA CZĘŚĆ ###

while run:
    if menu == True: ####menu główne
        
        if credits == True: ####poszczególne plansze menu
            screen.fill((255,255,255))
            screen.blit(creditsimage, imagerect)
        elif ingame == True:
            screen.fill((255,255,255))
            screen.blit(ingameimage, imagerect)
        elif controls == True:
            screen.fill((255,255,255))
            screen.blit(controlsimage, imagerect)
        else:
            screen.fill((255,255,255))
            screen.blit(menuimage, imagerect)
        
        for event in pygame.event.get(): ####wywoływanie plansz
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        menu = False
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        pygame.quit()
                        sys.exit()
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_4:
                        if controls == True:
                            if (controls == True) and (ingame == False):
                                controls = False
                            else:
                                controls = True
                        else:    
                            if (credits == False) and (ingame == False):
                                credits = True
                            elif (credits == True) and (ingame == False):
                                credits = False
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_5:
                        if (controls == False) and (ingame == False):
                            controls = True
                        elif (controls == True) and (ingame == False):
                            controls = False

    else:
        screen = pygame.display.set_mode((width, height + cell_size*2)) ####dorysowanie paska ekwipunku
        for event in pygame.event.get(): ####wyjście z gry krzyżykiem
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:     ####poruszanie graczem
                if event.key == pygame.K_LEFT:
                    player.move(Vector2(-1, 0))
                if event.key == pygame.K_RIGHT:
                    player.move(Vector2(1, 0))
                if event.key == pygame.K_UP:
                    player.move(Vector2(0, -1))
                if event.key == pygame.K_DOWN:
                    player.move(Vector2(0, 1))
                if event.key == pygame.K_1:
                    player.move(Vector2(0, 0))

                if event.key == pygame.K_2: ####pauza i wyjście przyciskiem
                    menu = True
                    ingame = True
                if event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

        enemy1.randmove(movecounter) ####ruch bytów
        enemy2.randmove(movecounter)
        enemy3.randmove(movecounter)
        stranger.randmove(movecounter)
        movecounter += 1

        screen.fill((0,0,0)) ###rysowanie
        screen.blit(background, (0,0))
        player.draw_player()
        player.update()
        player.collision()
        enemy1.draw_enemy()
        enemy1.update()
        enemy2.draw_enemy()
        enemy2.update()
        enemy3.draw_enemy()
        enemy3.update()
        stranger.draw_stranger()
        stranger.update()
        screen.blit(inventorysurface, (inventoryrect))
        screen.blit(inventorysurface2, (inventoryrect2))

        #### INTERAKCJE POMIĘDZY GRACZEM A BYTAMI (testowo)####
        if ((abs(player.pix_pos.x - enemy1.pos.x) < cell_size) and (abs(player.pix_pos.y - enemy1.pos.y) < cell_size)):
            enemy1.color = (pygame.Color("blue"))
        if ((abs(player.pix_pos.x - enemy2.pos.x) < cell_size) and (abs(player.pix_pos.y - enemy2.pos.y) < cell_size)):
            enemy2.color = (pygame.Color("blue"))
        if ((abs(player.pix_pos.x - enemy1.pos.x) < cell_size) and (abs(player.pix_pos.y - enemy3.pos.y) < cell_size)):
            enemy3.color = (pygame.Color("blue"))
        if ((abs(player.pix_pos.x - stranger.pos.x) < cell_size) and (abs(player.pix_pos.y - stranger.pos.y) < cell_size)):
            player.color = (pygame.Color("yellow"))

        #### RYSUJE SIATKĘ W TLE (testowo)####
        for x in range((width//cell_number)):
            pygame.draw.line(screen, (0,0,90), (x*cell_number, 0), (x*cell_number, height))
        for x in range((height//cell_size)):
            pygame.draw.line(screen, (0,0,90), (0, x*cell_size),(width, x*cell_size))

    pygame.display.update()
    pygame.display.set_caption("PIRS")
    clock.tick(60)
