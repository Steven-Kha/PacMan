import pygame
from settings import Settings
from imagerect import ImageRect
# import random
import time

class Player():
    P1_SIZE = 33
    def __init__(self, screen, mazefile, p1):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.p1_left = ['pacman1', 'pacman0']
        self.p1s = []
        size = Player.P1_SIZE

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
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        self.collide_x = True
                        if self.x_direction > 0:
                            print("I ran into the wall at the right")

                            # need to stop Pacman from touching the walls
                            # then get Pacman not colliding with anything
                            # -1 isn't good enough
                            self.x = self.x - 3
                            rect.x = self.x
                        elif self.x_direction < 0:
                            print("I ran into the wall at the left")
                            self.x = self.x + 3
                            rect.x = self.x

                        print ( "self.number.x: " + str(self.x))

                        # they can get stuck because pacman is too small
                        if time % 2 == 0:
                            self.x_direction *= -1

                        pygame.time.delay(100)


        if self.collide_x:
            self.y += 1 * self.y_direction
            for rect in self.p1s:
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):

                        if self.y_direction > 0:
                            self.y = self.y - 3
                            rect.y = self.y
                            print("I ran into the wall at the bottom")
                        elif self.y_direction < 0:
                            self.y = self.y + 3
                            rect.y = self.y
                            print("I ran into the wall at the top")
                        self.collide_x = False
                        print("self.number.y: " + str(self.y))

                        if time % 2 == 0:
                            self.y_direction *= -1

                        pygame.time.delay(100)


        # not_collide = False
        # if time % 2 == 0 and not not_collide:
        #     self.x += 1 * self.x_direction
        #     for rect in self.p1s:
        #         rect.x = self.x
        #         for rect2 in maze.bricks:
        #             if rect.colliderect(rect2):
        #                 self.x_direction *= -1
                        # not_collide = True
        # while time % 2 == 1 and not not_collide:
        #     self.y += 1 * self.y_direction
        #     for rect in self.p1s:
        #         rect.y = self.y
        #         for rect2 in maze.bricks:
        #             if rect.colliderect(rect2):
        #                 self.y_direction *= -1
        #                 not_collide = True





    def blitme(self):
        for rect in self.p1s:
            self.screen.blit(self.p1.image, rect)
