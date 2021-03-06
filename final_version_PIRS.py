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
        self.healcounter = 0
    def update(self):
        if self.can_move:
            self.pix_pos += self.direction * self.speed
        if self.time_of_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
        # self.pos[0]=(self.pix_pos[0]+cell_size//2)//cell_size
        # self.pos[1]=(self.pix_pos[1]+cell_number//2)//cell_number
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
    # def collision(self):
    #     if Vector2(self.pos + self.direction) in buildings:
    #         print(self.pos)
    def encounter(self):
        self.speed = 0
    def heal(self):
        if self.speed != 1:
            self.healcounter += 1
            if self.healcounter == 120:
                self.speed += 0.25
                self.healcounter = 0
        else:
            self.healcounter = 0

#### KLASA PRZECIWNIKA ####
class Enemy:
    def __init__ (self):
        self.x = 25.5
        self.y= 25.5
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
        self.speed = 0.075
        self.direction = Vector2(0,0)
        self.color = (pygame.Color("purple"))
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
        self.speed = 0.025
        self.direction = Vector2(0,0)
        self.color = (pygame.Color("pink"))
    def update(self):
        self.pos = self.pos + (self.direction * self.speed)
    def draw_stranger(self):
        pygame.draw.rect(screen, (self.color), (int(self.pos.x), int(self.pos.y), 10, 10),)
    def move(self, direction):
        self.direction = direction
    def resetpos(self):
        self.x = random.randint(1,28)
        self.y= random.randint(1,28)
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
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

### KLASA ZNAJD??KI ###
class Treasure():
    def __init__ (self):
        self.x = random.randint(1,28)
        self.y= random.randint(1,28)
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
        self.color1 = random.randint(1,4)
        if self.color1 == 1:
            self.color = (pygame.Color("orange"))
        if self.color1 == 2:
            self.color = (pygame.Color("green"))
        if self.color1 == 3:
            self.color = (pygame.Color("red"))
        if self.color1 == 4:
            self.color = (pygame.Color("yellow"))
    def draw_treasure(self):
        if self.color1 == 1:
            self.color = (pygame.Color("orange"))
        if self.color1 == 2:
            self.color = (pygame.Color("green"))
        if self.color1 == 3:
            self.color = (pygame.Color("red"))
        if self.color1 == 4:
            self.color = (pygame.Color("yellow"))
        pygame.draw.rect(screen, (self.color), (int(self.pos.x), int(self.pos.y), 10, 10),)
    def resetpos(self):
        self.x = random.randint(1,28)
        self.y= random.randint(1,28)
        self.pos = Vector2(self.x * cell_size, self.y * cell_size)
    def givecolor(self):
        return self.color1
    def resetcolor(self):
        self.color1 = random.randint(1,4)

class Ending:
    def write_text(self, my_text, screen, pos, size, colour, my_font):
        font = pygame.font.SysFont(my_font, size)
        text = font.render(my_text, False, colour)
        text_size = text.get_size()
        screen.blit(text, pos)
    def win(self):
        screen.fill((0,0,0))
        self.write_text("WYGRA??E??",screen,(70,100),100,(211,27,232),"arial")
        self.write_text("TW??J WYNIK:{}".format(self.player.score),self.screen,(190,250),35,(211,27,232),"arial")
        self.write_text("Aby zagra?? jeszcze raz naci??nij SPACJ??",self.screen,(90,400),30,(211,27,232),"arial")
        self.write_text("Aby zako??czy?? gr?? naci??nij klawisz ESCAPE",self.screen,(70,500),30,(211,27,232),"arial")
### ZDEFINIOWANIE ISTOTNYCH WARTO??CI ###
width = 616
height = 660
cell_size = width//28
cell_number = height//30
screen = pygame.display.set_mode((width, height))
background = pygame.image.load('miasto.png')
background = pygame.transform.scale(background, (width, height))
clock = pygame.time.Clock()
# buildings = []
# with open('grid.txt') as file:
#     for yidx, line in enumerate(file):
#         for xidx, char in enumerate(line):
#             if char == '1':
#                 buildings.append([xidx, yidx])

### ZMIENNE POTRZEBNE DO DZIA??ANIA MENU I OBRAZKI ###
run = True
menu = True
ingame = False
credits = False
controls = False
puzzle = False
puzzle1 = False
done = False
menuimage = pygame.image.load('menu2.jpg')
creditsimage = pygame.image.load('credits.jpg')
ingameimage = pygame.image.load('menuingame.jpg')
controlsimage = pygame.image.load('controls.jpg')
imagerect = menuimage.get_rect()

### EKWIPUNEK ###
inventorysurface = pygame.Surface((width, 2*cell_size))
inventorysurface2 = pygame.Surface((16*cell_size, cell_size))
inventorysurface.fill((0,0,0))
inventorysurface2.fill((255,255,255))
inventoryrect = inventorysurface.get_rect(topleft = (0, height))
inventoryrect2 = inventorysurface.get_rect(topleft = (6*cell_size, height + cell_size/2))

slotsurface0 = pygame.Surface((cell_size*2, cell_size))
slotsurface0.fill(pygame.Color("green"))
slotrect0 = slotsurface0.get_rect(topleft = (6*cell_size, height + cell_size/2))

slotsurface1 = pygame.Surface((cell_size*2, cell_size))
slotsurface1.fill(pygame.Color("red"))
slotrect1 = slotsurface1.get_rect(topleft = (8*cell_size, height + cell_size/2))

slotsurface2 = pygame.Surface((cell_size*2, cell_size))
slotsurface2.fill(pygame.Color("yellow"))
slotrect2 = slotsurface2.get_rect(topleft = (10*cell_size, height + cell_size/2))

slotsurface3 = pygame.Surface((cell_size*2, cell_size))
slotsurface3.fill(pygame.Color("blue"))
slotrect3 = slotsurface3.get_rect(topleft = (12*cell_size, height + cell_size/2))

slotsurface4 = pygame.Surface((cell_size*2, cell_size))
slotsurface4.fill(pygame.Color("green"))
slotrect4 = slotsurface4.get_rect(topleft = (14*cell_size, height + cell_size/2))

slotsurface5 = pygame.Surface((cell_size*2, cell_size))
slotsurface5.fill(pygame.Color("red"))
slotrect5 = slotsurface5.get_rect(topleft = (16*cell_size, height + cell_size/2))

slotsurface6 = pygame.Surface((cell_size*2, cell_size))
slotsurface6.fill(pygame.Color("yellow"))
slotrect6 = slotsurface6.get_rect(topleft = (18*cell_size, height + cell_size/2))

slotsurface7 = pygame.Surface((cell_size*2, cell_size))
slotsurface7.fill(pygame.Color("blue"))
slotrect7 = slotsurface7.get_rect(topleft = (20*cell_size, height + cell_size/2))

inventorybase = [slotsurface0, slotsurface1, slotsurface2, slotsurface3, slotsurface4, slotsurface5, slotsurface6, slotsurface7]
inventory = []
for i in range (8):
    inventory.append(0)

### TWORZENIE BYT??W ###

player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
stranger = Stranger()
treasure1 = Treasure()
treasure2 = Treasure()
treasure3 = Treasure()
ending = Ending()
movecounter = 0


### G????WNA CZ?????? ###

while run:
    if menu == True: ####menu g????wne + pauza i zagadki

        if credits == True: ####poszczeg??lne plansze menu
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


        for event in pygame.event.get(): ####wywo??ywanie plansz
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
        for event in pygame.event.get(): ####wyj??cie z gry krzy??ykiem
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
                if event.key == pygame.K_BACKSPACE:
                    i = 7
                    condition = True
                    while condition:
                        if inventory[i] != 0:
                            inventory[i] = 0
                            condition = False
                        i -= 1

                if event.key == pygame.K_2: ####pauza i wyj??cie przyciskiem
                    menu = True
                    ingame = True
                if event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

        enemy1.randmove(movecounter) ####ruch byt??w
        enemy2.randmove(movecounter)
        enemy3.randmove(movecounter)
        stranger.randmove(movecounter)
        movecounter += 1

        screen.fill((0,0,0)) ###rysowanie
        screen.blit(background, (0,0))

        player.draw_player()
        player.heal()
        player.update()
        # player.collision()

        enemy1.draw_enemy()
        enemy1.update()
        enemy2.draw_enemy()
        enemy2.update()
        enemy3.draw_enemy()
        enemy3.update()

        stranger.draw_stranger()
        stranger.update()

        treasure1.draw_treasure()
        treasure2.draw_treasure()
        treasure3.draw_treasure()

        screen.blit(inventorysurface, (inventoryrect))
        screen.blit(inventorysurface2, (inventoryrect2))
        screen.blit(slotsurface0, (slotrect0))
        screen.blit(slotsurface1, (slotrect1))
        screen.blit(slotsurface2, (slotrect2))
        screen.blit(slotsurface3, (slotrect3))
        screen.blit(slotsurface4, (slotrect4))
        screen.blit(slotsurface5, (slotrect5))
        screen.blit(slotsurface6, (slotrect6))
        screen.blit(slotsurface7, (slotrect7))

        for i in range (8):
            if inventory[i] == 1:
                inventorybase[i].fill(pygame.Color("orange"))
            elif inventory[i] == 2:
                inventorybase[i].fill(pygame.Color("green"))
            elif inventory[i] == 3:
                inventorybase[i].fill(pygame.Color("red"))
            elif inventory[i] == 4:
                inventorybase[i].fill(pygame.Color("yellow"))
            else:
                inventorybase[i].fill(pygame.Color("white"))

        if enemy1.pos.x >= width: ### przeciwnik1 nie wychodzi poza mape###
            enemy1.speed *= -1
        if enemy1.pos.x <= 0:
            enemy1.speed *= -1
        if enemy1.pos.y <= 0:
            enemy1.speed *= -1
        if enemy1.pos.y >= height:
            enemy1.speed *= -1

        if enemy2.pos.x >= width: ### przeciwnik2 nie wychodzi poza mape###
            enemy2.speed *= -1
        if enemy2.pos.x <= 0:
            enemy2.speed *= -1
        if enemy2.pos.y <= 0:
            enemy2.speed *= -1
        if enemy2.pos.y >= height:
            enemy2.speed *= -1

        if enemy3.pos.x >= width: ### przeciwnik3 nie wychodzi poza mape###
            enemy3.speed *= -1
        if enemy3.pos.x <= 0:
            enemy3.speed *= -1
        if enemy3.pos.y <= 0:
            enemy3.speed *= -1
        if enemy3.pos.y >= height:
            enemy3.speed *= -1

        if stranger.pos.x >= width: ### neutralny nie wychodzi poza mape###
            stranger.speed *= -1
        if stranger.pos.x <= 0:
            stranger.speed *= -1
        if stranger.pos.y <= 0:
            stranger.speed *= -1
        if stranger.pos.y >= height:
            stranger.speed *= -1

        #### INTERAKCJE POMI??DZY GRACZEM A BYTAMI (testowo)####
        if ((abs(player.pix_pos.x - enemy1.pos.x) < cell_size*2) and (abs(player.pix_pos.y - enemy1.pos.y) < cell_size*2)):
            player.encounter()

        if ((abs(player.pix_pos.x - enemy2.pos.x) < cell_size*2) and (abs(player.pix_pos.y - enemy2.pos.y) < cell_size*2)):
            player.encounter()

        if ((abs(player.pix_pos.x - enemy1.pos.x) < cell_size*2) and (abs(player.pix_pos.y - enemy3.pos.y) < cell_size*2)):
            player.encounter()

        if ((abs(player.pix_pos.x - treasure1.pos.x) < cell_size) and (abs(player.pix_pos.y - treasure1.pos.y) < cell_size)):

            if ((0 in inventory) and (movecounter % 30 == 0)):
                i = 0
                condition = True
                while condition:
                    if inventory[i] == 0:
                        puzzle1 = True
                        condition = False
                    i += 1
                treasure1.resetpos()
                colorx = treasure1.givecolor()
                treasure1.resetcolor()

        if ((abs(player.pix_pos.x - treasure2.pos.x) < cell_size) and (abs(player.pix_pos.y - treasure2.pos.y) < cell_size)):

            if ((0 in inventory) and (movecounter % 30 == 0)):
                i = 0
                condition = True
                while condition:
                    if inventory[i] == 0:
                        puzzle1 = True
                        condition = False
                    i += 1
                treasure2.resetpos()
                colorx = treasure2.givecolor()
                treasure2.resetcolor()

        if ((abs(player.pix_pos.x - treasure3.pos.x) < cell_size) and (abs(player.pix_pos.y - treasure3.pos.y) < cell_size)):

            if ((0 in inventory) and (movecounter % 30 == 0)):
                i = 0
                condition = True
                while condition:
                    if inventory[i] == 0:
                        puzzle1 = True
                        condition = False
                    i += 1
                treasure3.resetpos()
                colorx = treasure3.givecolor()
                treasure3.resetcolor()
        if ((abs(player.pix_pos.x - stranger.pos.x) < cell_size) and (abs(player.pix_pos.y - stranger.pos.y) < cell_size)):

            if ((0 in inventory) and (movecounter % 30 == 0)):
                i = 0
                condition = True
                while condition:
                    if inventory[i] == 0:
                        puzzle = True
                        condition = False
                    i += 1
                stranger.resetpos()

        if puzzle1 == True:
            puzzlesurface = pygame.Surface((300,300))
            puzzlerect = puzzlesurface.get_rect(center = (308, 330))
            screen.blit(puzzlesurface, (puzzlerect))
        if puzzle1 == True: ####zagadki
            color1 = colorx
            font = pygame.font.Font(None, 32)
            done = False
            clock = pygame.time.Clock()
            input_box = pygame.Rect(218, 314, 140, 32)
            inactivecolor = pygame.Color(0,230,50)
            activecolor = pygame.Color(20,230,100)
            color = inactivecolor
            number1 = random.randint(0,10)
            number2 = random.randint(0,9)
            result = number1 * number2
            active = True
            text = str(number1) + ' * ' + str(number2) + ' = '
            lenght = 0


            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        puzzle1 = False

                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                if lenght == 1:
                                    textresult = text[-1]
                                else:
                                    textresult = text[-2] + text[-1]
                                if int(textresult) == result:
                                    done = True
                                    puzzle1 = False
                                    i = 0
                                    condition = True
                                    while condition:
                                        if inventory[i] == 0:
                                            condition = False
                                            signcolor = color1
                                            inventory[i] = signcolor
                                        i += 1
                                else:
                                    done = True
                                    puzzle1 = False
                                text = ''
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                                lenght -= 1
                            else:
                                text += event.unicode
                                lenght += 1


                txt_surface = font.render(text, True, color)
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.flip()



        if puzzle == True:
            puzzlesurface = pygame.Surface((300,300))
            puzzlerect = puzzlesurface.get_rect(center = (308, 330))
            screen.blit(puzzlesurface, (puzzlerect))
        if puzzle == True: ####zagadki
            font = pygame.font.Font(None, 32)
            done = False
            clock = pygame.time.Clock()
            input_box = pygame.Rect(218, 314, 140, 32)
            inactivecolor = pygame.Color(0,230,50)
            activecolor = pygame.Color(20,230,100)
            color = inactivecolor
            number1 = random.randint(0,10)
            number2 = random.randint(0,9)
            result = number1 * number2
            active = True
            text = str(number1) + ' * ' + str(number2) + ' = '
            lenght = 0


            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        puzzle = False
                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                if lenght == 1:
                                    textresult = text[-1]
                                else:
                                    textresult = text[-2] + text[-1]
                                if int(textresult) == result:
                                    done = True
                                    puzzle = False
                                    i = 0
                                    condition = True
                                    while condition:
                                        if inventory[i] == 0:
                                            condition = False
                                            signcolor = random.randint(1,4)
                                            inventory[i] = signcolor
                                        i += 1
                                else:
                                    done = True
                                    puzzle = False
                                text = ''
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                                lenght -= 1
                            else:
                                text += event.unicode
                                lenght += 1


                txt_surface = font.render(text, True, color)
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pygame.draw.rect(screen, color, input_box, 2)
                pygame.display.flip()

        # #### RYSUJE SIATK?? W TLE (testowo)####
        # for x in range((width//cell_number)*2):
        #     pygame.draw.line(screen, (0,0,90), (x*cell_number/2, 0), (x*cell_number/2, height))
        # for x in range((height//cell_size)*2):
        #     pygame.draw.line(screen, (0,0,90), (0, x*cell_size/2),(width, x*cell_size/2))

    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    for i in range (8):
        if inventory[i] == 1:
            counter1 += 1
        elif inventory[i] == 2:
            counter2 += 1
        elif inventory[i] == 3:
            counter3 += 1
        elif inventory[i] == 4:
            counter4 += 1
    if counter1 > 4 or counter2 > 4 or  counter3 > 4 or  counter4 > 4:
        screen.fill((0,0,0))
        text_font = pygame.font.SysFont('arial', 60)
        win = text_font.render("Wygra??e??!", True, (252,186,3))
        screen.blit(win, (200,250))
    else:
        if 0 not in inventory:
            screen.fill((0,0,0))
            text_font = pygame.font.SysFont('arial', 60)
            win = text_font.render("Przegra??e??!", True, (252,186,3))
            screen.blit(win, (200,250))



    pygame.display.update()
    pygame.display.set_caption("PIRS")
    clock.tick(60)
