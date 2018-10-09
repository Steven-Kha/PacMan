import pygame
from imagerect import ImageRect

class Maze():
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    BRICK_SIZE = 15
    def __init__(self, screen, mazefile, brickfile):#, portalfile, shieldfile, pointfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.bricks = []
        sz = Maze.BRICK_SIZE

        self.brick = ImageRect(screen, brickfile, sz, sz)
        #                      screen, square, height, width

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "X":
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
