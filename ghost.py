import pygame
from settings import Settings
from imagerect import ImageRect
# import random
import time

class BlueGhost():
    P1_SIZE = 33
    def __init__(self, screen, mazefile, p1):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.blueGhosts = ['images/BlueGhost0.png', 'images/BlueGhost1.png',
                           'images/BlueGhost2.png', 'images/BlueGhost3.png']
        self.p1s = []
        size = BlueGhost.P1_SIZE

        self.p1 = ImageRect(screen, p1, size, size)

        r = self.p1.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.p1s.append(pygame.Rect(330, 410, w, h))
        self.x_direction = .5
        self.y_direction = .5

        self.collide_x = False

        for rect in self.p1s:
            self.x = float(rect.x)
            self.y = float(rect.y)
    def update(self, maze):
        # add pacSettings to reverse movement
        time = pygame.time.get_ticks()
        # randx = random.randint(1, 10)
        # even = False
        # odd = False

        if not self.collide_x:
            self.x += 1 * self.x_direction
            for rect in self.p1s:
                rect.x = self.x
                for rect2 in maze.bricks: #rect2 is the rect of the bricks
                    if rect.colliderect(rect2):
                        self.collide_x = True
                        if self.x_direction > 0:
                            # print("I ran into the wall at the right")
                            self.image = pygame.image.load(self.blueGhosts[3])

                            # need to stop Pacman from touching the walls
                            # then get Pacman not colliding with anything
                            # -1 isn't good enough
                            self.x = self.x -1
                            rect.x = self.x
                        elif self.x_direction < 0:
                            self.image = pygame.image.load(self.blueGhosts[0])
                            # print("I ran into the wall at the left")
                            self.x = self.x + 1
                            rect.x = self.x

                        # print("self.number.x: " + str(self.x))

                        # they can get stuck because pacman is too small
                        if time % 2 == 0:
                            self.x_direction *= -1

                        # pygame.time.delay(100)


        if self.collide_x:
            self.y += 1 * self.y_direction
            for rect in self.p1s:
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):

                        if self.y_direction > 0:
                            self.image = pygame.image.load(self.blueGhosts[1])
                            self.y = self.y - 3
                            rect.y = self.y
                            # print("I ran into the wall at the bottom")
                        elif self.y_direction < 0:
                            self.image = pygame.image.load(self.blueGhosts[2])
                            self.y = self.y + 3
                            rect.y = self.y
                            # print("I ran into the wall at the top")
                        self.collide_x = False
                        # print("self.number.y: " + str(self.y))

                        if time % 2 == 0:
                            self.y_direction *= -1

                        # pygame.time.delay(100)

    def blitme(self):
        for rect in self.p1s:
            self.screen.blit(self.p1.image, rect)



class RedGhost():
    P1_SIZE = 33
    def __init__(self, screen, mazefile, red):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.redGhosts = ['images/BlueGhost0.png', 'images/BlueGhost1.png',
                           'images/BlueGhost2.png', 'images/BlueGhost3.png']
        self.reds = []
        size = BlueGhost.P1_SIZE

        self.red = ImageRect(screen, red, size, size)

        r = self.red.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.reds.append(pygame.Rect(330, 410, w, h))
        self.x_direction = -.5
        self.y_direction = .5

        self.collide_x = False

        for rect in self.reds:
            self.x = float(rect.x)
            self.y = float(rect.y)

    def update(self, maze):
        # add pacSettings to reverse movement
        time = pygame.time.get_ticks()
        # randx = random.randint(1, 10)
        # even = False
        # odd = False

        if not self.collide_x:
            self.x += 1 * self.x_direction
            for rect in self.reds:
                rect.x = self.x
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        self.collide_x = True
                        if self.x_direction > 0:
                            # print("I ran into the wall at the right")
                            # self.image = pygame.image.load(self.blueGhosts[3])

                            # need to stop Pacman from touching the walls
                            # then get Pacman not colliding with anything
                            # -1 isn't good enough
                            self.x = self.x - 3
                            rect.x = self.x
                        elif self.x_direction < 0:
                            # self.image = pygame.image.load(self.blueGhosts[0])
                            # print("I ran into the wall at the left")
                            self.x = self.x + 3
                            rect.x = self.x

                        # print("self.number.x: " + str(self.x))

                        # they can get stuck because pacman is too small
                        if time % 2 == 0:
                            self.x_direction *= -1

                        # pygame.time.delay(100)


        if self.collide_x:
            self.y += 1 * self.y_direction
            for rect in self.reds:
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):

                        if self.y_direction > 0:
                            # self.image = pygame.image.load(self.blueGhosts[1])
                            self.y = self.y - 3
                            rect.y = self.y
                            # print("I ran into the wall at the bottom")
                        elif self.y_direction < 0:
                            # self.image = pygame.image.load(self.blueGhosts[2])
                            self.y = self.y + 3
                            rect.y = self.y
                            # print("I ran into the wall at the top")
                        self.collide_x = False
                        # print("self.number.y: " + str(self.y))

                        if time % 2 == 0:
                            self.y_direction *= -1

                        # pygame.time.delay(100)

    def blitme(self):
        for rect in self.reds:
            self.screen.blit(self.red.image, rect)
                        
class YellowGhost():
    P1_SIZE = 33
    def __init__(self, screen, mazefile, yellow):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.yellowGhosts = ['images/BlueGhost0.png', 'images/BlueGhost1.png',
                           'images/BlueGhost2.png', 'images/BlueGhost3.png']
        self.yellows = []
        size = BlueGhost.P1_SIZE

        self.yellow = ImageRect(screen, yellow, size, size)

        r = self.yellow.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.yellows.append(pygame.Rect(330, 410, w, h))
        self.x_direction = .5
        self.y_direction = -.5

        self.collide_x = False

        for rect in self.yellows:
            self.x = float(rect.x)
            self.y = float(rect.y)

    def update(self, maze):
        # add pacSettings to reverse movement
        time = pygame.time.get_ticks()
        # randx = random.randint(1, 10)
        # even = False
        # odd = False

        if not self.collide_x:
            self.x += 1 * self.x_direction
            for rect in self.yellows:
                rect.x = self.x
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        self.collide_x = True
                        if self.x_direction > 0:
                            # print("I ran into the wall at the right")
                            # self.image = pygame.image.load(self.blueGhosts[3])

                            # need to stop Pacman from touching the walls
                            # then get Pacman not colliding with anything
                            # -1 isn't good enough
                            self.x = self.x - 3
                            rect.x = self.x
                        elif self.x_direction < 0:
                            # self.image = pygame.image.load(self.blueGhosts[0])
                            # print("I ran into the wall at the left")
                            self.x = self.x + 3
                            rect.x = self.x

                        # print("self.number.x: " + str(self.x))

                        # they can get stuck because pacman is too small
                        if time % 2 == 0:
                            self.x_direction *= -1

                        # pygame.time.delay(100)


        if self.collide_x:
            self.y += 1 * self.y_direction
            for rect in self.yellows:
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):

                        if self.y_direction > 0:
                            # self.image = pygame.image.load(self.blueGhosts[1])
                            self.y = self.y - 3
                            rect.y = self.y
                            # print("I ran into the wall at the bottom")
                        elif self.y_direction < 0:
                            # self.image = pygame.image.load(self.blueGhosts[2])
                            self.y = self.y + 3
                            rect.y = self.y
                            # print("I ran into the wall at the top")
                        self.collide_x = False
                        # print("self.number.y: " + str(self.y))

                        if time % 2 == 0:
                            self.y_direction *= -1

                        # pygame.time.delay(100)

    def blitme(self):
        for rect in self.yellows:
            self.screen.blit(self.yellow.image, rect)
            
class PinkGhost():
    P1_SIZE = 33
    def __init__(self, screen, mazefile, pink):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.pinkGhosts = ['images/BlueGhost0.png', 'images/BlueGhost1.png',
                           'images/BlueGhost2.png', 'images/BlueGhost3.png']
        self.pinks = []
        size = BlueGhost.P1_SIZE

        self.pink = ImageRect(screen, pink, size, size)

        r = self.pink.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.pinks.append(pygame.Rect(330, 410, w, h))
        self.x_direction = -.5
        self.y_direction = -.5

        self.collide_x = False

        for rect in self.pinks:
            self.x = float(rect.x)
            self.y = float(rect.y)

    def update(self, maze):
        # add pacSettings to reverse movement
        time = pygame.time.get_ticks()
        # randx = random.randint(1, 10)
        # even = False
        # odd = False

        if not self.collide_x:
            self.x += 1 * self.x_direction
            for rect in self.pinks:
                rect.x = self.x
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        self.collide_x = True
                        if self.x_direction > 0:
                            # print("I ran into the wall at the right")
                            # self.image = pygame.image.load(self.blueGhosts[3])

                            # need to stop Pacman from touching the walls
                            # then get Pacman not colliding with anything
                            # -1 isn't good enough
                            self.x = self.x - 3
                            rect.x = self.x
                        elif self.x_direction < 0:
                            # self.image = pygame.image.load(self.blueGhosts[0])
                            # print("I ran into the wall at the left")
                            self.x = self.x + 3
                            rect.x = self.x

                        # print("self.number.x: " + str(self.x))

                        # they can get stuck because pacman is too small
                        if time % 2 == 0:
                            self.x_direction *= -1

                        # pygame.time.delay(100)


        if self.collide_x:
            self.y += 1 * self.y_direction
            for rect in self.pinks:
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):

                        if self.y_direction > 0:
                            # self.image = pygame.image.load(self.blueGhosts[1])
                            self.y = self.y - 3
                            rect.y = self.y
                            # print("I ran into the wall at the bottom")
                        elif self.y_direction < 0:
                            # self.image = pygame.image.load(self.blueGhosts[2])
                            self.y = self.y + 3
                            rect.y = self.y
                            # print("I ran into the wall at the top")
                        self.collide_x = False
                        # print("self.number.y: " + str(self.y))

                        if time % 2 == 0:
                            self.y_direction *= -1

                        # pygame.time.delay(100)

    def blitme(self):
        for rect in self.pinks:
            self.screen.blit(self.pink.image, rect)