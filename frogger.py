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

frogImg = pygame.image.load('frog10.gif')  # First row
yellowCarImg = pygame.image.load('yellowCar.gif')  # 2nd Row
dozerImg = pygame.image.load('dozer.gif')  # 3rd Row
purpleCarImg = pygame.image.load('purpleCar.gif')  # 4th Row
greenCarImg = pygame.image.load('greenCar.gif')  # 5th Row
truckImg = pygame.image.load('truck.gif')  # 6th Row
backgroundImg = pygame.image.load('background.gif')

done = False

# Objects


class Frog(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):  # Constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.rect = self.image.get_rect()
        self.image = frogImg
        self.rect.x = xpos
        self.rect.y = ypos


class Log:
    pass


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

        if (self.direction == -1 and self.rect.x - 100 > display_width):
            self.rect.x = -100
        elif (self.direction == 1 and self.rect.x + 100 < 0):
            self.rect.x = display_width + 100

        self.collision()

    def collision(self):
        if (self.rect.colliderect(frog)):
            frog.rect.x = 167.5
            frog.rect.y = 350
            frog.xpos = 167.5
            frog.ypos = 350


class Turtle:
    pass


# Creation of objects
frog = Frog(167.5, 350)
all_sprites.add(frog)

#(x, y, img, speed, direction, width, height)
for i in range(0, 12):
    if i < 3:
        all_sprites.add(Car(100 + 75 * (3 - i), 325, 'yellow', 7, 1, 25, 25))
    elif i < 6:
        all_sprites.add(Car(-150 + 75 * (6 - i), 300, 'dozer', 2, -1, 25, 25))
    elif i < 9:
        all_sprites.add(Car(50 + 75 * (9 - i), 275, 'purple', 5, 1, 25, 25))
    elif i < 10:
        all_sprites.add(Car(25 + 75 * (10 - i), 250, 'green', 14, -1, 25, 25))
    elif i < 12:
        all_sprites.add(Car(50 + 150 * (12 - i), 225, 'truck', 4, 1, 50, 25))


# Event handling loop (game loop)
while not done:
    for event in pygame.event.get():
        x_change = 0
        y_change = 0
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -25
            elif event.key == pygame.K_RIGHT:
                x_change = 25
            elif event.key == pygame.K_UP:
                y_change = -25
            elif event.key == pygame.K_DOWN:
                y_change = 25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                y_change = 0

    frog.rect.x += x_change
    if frog.rect.x + 25 > display_width or frog.rect.x < 0:
        frog.rect.x -= x_change

    frog.rect.y += y_change
    if frog.rect.y + 25 > display_height or frog.rect.y < 0:
        frog.rect.y -= y_change

    screen.blit(backgroundImg, (0, 0))
    # screen.fill(white)
    # screen.fill(black)

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
