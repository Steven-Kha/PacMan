import pygame
from imagerect import ImageRect
import time
from timer import Timer
class Player():
    P1_SIZE = 35
    def __init__(self, screen, mazefile, p1):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.moveRight = ['images/pacman3.png', 'images/pacman4.png']
        self.moveLeft = ['images/pacman0.png', 'images/pacman1.png']
        self.moveUp = ['images/pacman5.png', 'images/pacman6.png']
        self.moveDown = ['images/pacman7.png', 'images/pacman8.png']

        self.players = []
        size = Player.P1_SIZE

        self.p1 = ImageRect(screen, p1, size, size)

        r = self.p1.rect
        w, h = r.width, r.height

        #                           x, y , width, height
        self.players.append(pygame.Rect(330, 410, w, h))
        # self.x_direction = .5
        # self.y_direction = .5

        # self.collide_x = False

        # movement
        for rect in self.players:
            self.x = float(rect.x)
            self.y = float(rect.y)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x_direction = 2
        self.y_direction = 2
        self.animate = 0

    def update(self, maze):
        # add pacSettings to reverse movement
        now = pygame.time.get_ticks()
        moveRightFrame = Timer(self.moveRight)


        for rect in self.players:
            # if self.y_hit is not self.y:
            #     self.hit_right = False
            if self.moving_right:
                if now % 15 == 0:
                    self.p1.image = pygame.image.load(self.moveRight[1])
                    # self.animate += 1
                elif now % 32 == 0:
                    self.p1.image = pygame.image.load(self.moveRight[0])
                    # self.animate = 0
                # self.p1.image = pygame.image.load(moveRightFrame.imagerect())
                # print("right animate frame: " + str(moveRightFrame.imagerect()))
                self.x += self.x_direction
                rect.x = self.x
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        # self.y_hit = self.y
                        # self.hit_right = True
                        self.x = self.x - self.x_direction
                        rect.x = self.x
                        return

            if self.moving_down:
                if now % 15 == 0:
                    self.p1.image = pygame.image.load(self.moveDown[1])
                elif now % 32 == 0:
                    self.p1.image = pygame.image.load(self.moveDown[0])
                self.y += self.y_direction
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                    # if pygame.sprite.collide_rect(rect, rect2):
                        self.y = self.y - self.y_direction
                        rect.y = self.y
                        return

            if self.moving_left:
                if now % 15 == 0:
                    self.p1.image = pygame.image.load(self.moveLeft[1])
                elif now % 32 == 0:
                    self.p1.image = pygame.image.load(self.moveLeft[0])
                self.x -= self.x_direction
                rect.x = self.x
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        # self.y_hit = self.y
                        # self.hit_right = True
                        self.x = self.x + self.x_direction
                        rect.x = self.x
                        return

            if self.moving_up:
                if now % 15 == 0:
                    self.p1.image = pygame.image.load(self.moveUp[1])
                elif now % 32 == 0:
                    self.p1.image = pygame.image.load(self.moveUp[0])
                self.y -= self.y_direction
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        self.y = self.y + self.y_direction
                        rect.y = self.y
                        return




    def blitme(self):
        for rect in self.players:
            self.screen.blit(self.p1.image, rect)