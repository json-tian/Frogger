# Frogger
# 07/16/18
# Author: Jason Tian

import pygame

pygame.init()

display_width = 350
display_height = 400

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
turtles = pygame.sprite.Group()
frogs = pygame.sprite.Group()

frogUpImg = pygame.image.load('frog10.gif')
frogLeftImg = pygame.image.load('frog00.gif')
frogRightImg = pygame.image.load('frog20.gif')
frogDownImg = pygame.image.load('frog30.gif')

yellowCarImg = pygame.image.load('yellowCar.gif')  # 2nd Row
dozerImg = pygame.image.load('dozer.gif')  # 3rd Row
purpleCarImg = pygame.image.load('purpleCar.gif')  # 4th Row
greenCarImg = pygame.image.load('greenCar.gif')  # 5th Row
truckImg = pygame.image.load('truck.gif')  # 6th Row

logShortImg = pygame.image.load('logShort.gif')
logMediumImg = pygame.image.load('logMedium.gif')
logLongImg = pygame.image.load('logLong.gif')

turtleTwoImg = pygame.image.load('turtletwo.gif')
turtleTwoDownImg = pygame.image.load('turtletwodown.gif')
turtleThreeImg = pygame.image.load('turtlethree.gif')
turtleThreeDownImg = pygame.image.load('turtlethreedown.gif')

backgroundImg = pygame.image.load('background.gif')

done = False
turtleCounter = 0
# Objects

# Turtle Object


class Turtle(pygame.sprite.Sprite):
    def __init__(self, dive, size, startX, startY, width, height, speed):  # Constructor
        pygame.sprite.Sprite.__init__(self)
        self.dive = dive  # 1 - does not dive. 2 - dives
        self.size = size
        self.speed = speed
        self.width = width
        self.height = height
        self.state = 0  # State 0 - Not diving. State 1 - Diving

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY

        if (self.size == 2):
            self.image = turtleTwoImg
        elif (self.size == 3):
            self.image = turtleThreeImg

    def update(self):
        self.rect.x += self.speed

        if (self.size == 2):
            if (self.rect.x + 50 < 0):
                self.rect.x = display_width + 50
        elif (self.size == 3):
            if (self.rect.x + 75 < 0):
                self.rect.x = display_width + 75

        self.collision()

    def collision(self):
        for f in frogs:
            if f.rect.colliderect(self):
                if self.state == 1:
                    f.die()
                else:
                    f.rect.x += self.speed


# Frog Object
class Frog(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.rect = self.image.get_rect()
        self.image = frogUpImg
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):
        # If frog is in the river
        if self.rect.y <= 175 and self.rect.y != 50:
            crash = False
            for x in all_sprites:
                if x.rect.colliderect(self):
                    crash = True
                    break
            for x in turtles:
                if x.rect.colliderect(self):
                    crash = True
                    break
            if crash == False:
                self.die()

    def die(self):
        self.rect.x = 167.5
        self.rect.y = 350


class Log(pygame.sprite.Sprite):
    def __init__(self, startX, startY, size, width, height, speed):  # Constructor
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.speed = speed
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY

        if (self.size == 'short'):
            self.image = logShortImg
        elif (self.size == 'medium'):
            self.image = logMediumImg
        elif (self.size == 'long'):
            self.image = logLongImg

    def update(self):
        self.rect.x += self.speed

        if (self.size == 'short' or self.size == 'medium'):
            if (self.rect.x - 100 > display_width):
                self.rect.x = -100
        else:
            if (self.rect.x - 200 > display_width):
                self.rect.x = -200

        self.collision()

    def collision(self):
        for f in frogs:
            if f.rect.colliderect(self):
                f.rect.x += self.speed


# Car Object
class Car(pygame.sprite.Sprite):
    def __init__(self, startX, startY, img, speed, direction, width, height):  # Constructor
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.speed = speed
        self.direction = direction  # (-1)-left (1)-right
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY

        if (self.img == 'yellow'):
            self.image = yellowCarImg
        elif (self.img == 'green'):
            self.image = greenCarImg
        elif (self.img == 'truck'):
            self.image = truckImg
        elif (self.img == 'dozer'):
            self.image = dozerImg
        elif (self.img == 'purple'):
            self.image = purpleCarImg

    def update(self):
        if (self.direction == -1):
            self.rect.x += self.speed
        elif (self.direction == 1):
            self.rect.x -= self.speed

        if (self.direction == -1 and self.rect.x - 75 > display_width):
            self.rect.x = -75
        elif (self.direction == 1 and self.rect.x + 75 < 0):
            self.rect.x = display_width + 75
        self.collision()

    def collision(self):
        for f in frogs:
            if (self.rect.colliderect(f)):
                f.die()


# Creation of objects

#(x, y, img, speed, direction, width, height)
for i in range(0, 12):
    if i < 3:
        all_sprites.add(Car(100 + 75 * (3 - i), 325, 'yellow', 6, 1, 25, 25))
    elif i < 6:
        all_sprites.add(Car(-150 + 75 * (6 - i), 300, 'dozer', 2, -1, 25, 25))
    elif i < 9:
        all_sprites.add(Car(50 + 75 * (9 - i), 275, 'purple', 4, 1, 25, 25))
    elif i < 10:
        all_sprites.add(Car(25 + 75 * (10 - i), 250, 'green', 10, -1, 25, 25))
    elif i < 12:
        all_sprites.add(Car(50 + 150 * (12 - i), 225, 'truck', 3, 1, 50, 25))

for i in range(0, 9):
    if i < 3:
        all_sprites.add(Log(-100 + 150 * (3 - i), 150, 'short', 62.5, 25, 3))
    elif i < 6:
        all_sprites.add(Log(-150 + 200 * (6 - i), 125, 'long', 150, 25, 4))
    elif i < 9:
        all_sprites.add(Log(-100 + 150 * (3 - i), 75, 'medium', 87.5, 25, 6))

for i in range(0, 8):
    # dive, size, startX, startY, width, height, speed
    if i < 4:
        if i == 2:
            turtles.add(Turtle(2, 3, 100 * (4 - i), 175, 75, 25, -2))
        else:
            turtles.add(Turtle(1, 3, 100 * (4 - i), 175, 75, 25, -2))
    elif i < 8:
        if i == 7:
            turtles.add(Turtle(2, 2, 87.5 * (8 - i), 100, 50, 25, -2))
        else:
            turtles.add(Turtle(1, 2, 87.5 * (8 - i), 100, 50, 25, -2))

frog = Frog(167.5, 350)
frogs.add(frog)


# Event handling loop (game loop)
while not done:
    for event in pygame.event.get():
        x_change = 0
        y_change = 0
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = -25
                frog.image = frogLeftImg
            elif event.key == pygame.K_RIGHT:
                x_change = 25
                frog.image = frogRightImg
            elif event.key == pygame.K_UP:
                y_change = -25
                frog.image = frogUpImg
            elif event.key == pygame.K_DOWN:
                y_change = 25
                frog.image = frogDownImg

    frog.rect.x += x_change
    if frog.rect.x + 25 > display_width or frog.rect.x < 0:
        frog.rect.x -= x_change

    frog.rect.y += y_change
    if frog.rect.y + 25 > display_height or frog.rect.y < 0:
        frog.rect.y -= y_change

    x_change = 0
    y_change = 0

    screen.blit(backgroundImg, (0, 0))

    all_sprites.update()
    all_sprites.draw(screen)
    turtles.update()
    turtles.draw(screen)
    frogs.update()
    frogs.draw(screen)

    pygame.display.update()
    clock.tick(30)
    turtleCounter += 1
    if turtleCounter == 50:
        turtleCounter = 0
        for t in turtles:
            if t.dive == 2:
                if t.state == 0:
                    t.state = 1
                    if t.size == 2:
                        t.image = turtleTwoDownImg
                    else:
                        t.image = turtleThreeDownImg
                else:
                    t.state = 0
                    if t.size == 2:
                        t.image = turtleTwoImg
                    else:
                        t.image = turtleThreeImg

pygame.quit()
quit()
