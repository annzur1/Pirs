import pygame, sys, random
from pygame.math import Vector2

pygame.init()


#### KLASA GRACZA ####
class Player:
    def __init__ (self):
        self.x = 5.5
        self.y= 5.5
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
        self.speed = 0.1
        self.direction = Vector2(0,0)
        self.color = (pygame.Color("white"))
    def update(self):
        self.pos = self.pos + (self.direction * self.speed)
    def draw_player(self):
        pygame.draw.circle(screen, (self.color), (int(self.pos.x), int(self.pos.y)), cell_size//3)
    def move(self, direction):
        self.direction = direction

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
        


    


width = 616
height = 660
cell_size = width//28
cell_number = height//30
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()




player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
stranger = Stranger()
movecounter = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:     ####poruszanie graczem
            if event.key == pygame.K_LEFT:
                player.move(Vector2(-1 * cell_size, 0))
            if event.key == pygame.K_RIGHT:
                player.move(Vector2(1 * cell_size, 0))
            if event.key == pygame.K_UP:
                player.move(Vector2(0, -1 * cell_size))
            if event.key == pygame.K_DOWN:
                player.move(Vector2(0, 1 * cell_size))
            if event.key == pygame.K_1:
                player.move(Vector2(0, 0))
    
    enemy1.randmove(movecounter) ####ruch bytów
    enemy2.randmove(movecounter)
    enemy3.randmove(movecounter)
    stranger.randmove(movecounter)
    movecounter += 1
    
    screen.fill((0,0,0))
    player.draw_player()
    player.update()
    enemy1.draw_enemy()
    enemy1.update()
    enemy2.draw_enemy()
    enemy2.update()
    enemy3.draw_enemy()
    enemy3.update()
    stranger.draw_stranger()
    stranger.update()
    
    #### INTERAKCJE POMIĘDZY GRACZEM A BYTAMI (testowo)####
    if ((abs(player.pos.x - enemy1.pos.x) < cell_size) and (abs(player.pos.y - enemy1.pos.y) < cell_size)):
        enemy1.color = (pygame.Color("blue"))
    if ((abs(player.pos.x - enemy2.pos.x) < cell_size) and (abs(player.pos.y - enemy2.pos.y) < cell_size)):
        enemy2.color = (pygame.Color("blue"))
    if ((abs(player.pos.x - enemy1.pos.x) < cell_size) and (abs(player.pos.y - enemy3.pos.y) < cell_size)):
        enemy3.color = (pygame.Color("blue"))
    if ((abs(player.pos.x - stranger.pos.x) < cell_size) and (abs(player.pos.y - stranger.pos.y) < cell_size)):
        player.color = (pygame.Color("yellow"))
    #### RYSUJE SIATKĘ W TLE (testowo)####
    for x in range(width//cell_number):
        pygame.draw.line(screen, (0,0,90), (x*cell_number, 0),
                                 (x*cell_number, height))
    for x in range(height//cell_size):
        pygame.draw.line(screen, (0,0,90), (0, x*cell_size),(width, x*cell_size))    
    pygame.display.update()
    pygame.display.set_caption("PIRS")
    clock.tick(60)
