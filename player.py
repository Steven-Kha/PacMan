import pygame
from settings import Settings
from imagerect import ImageRect

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

        for rect in self.p1s:
            self.x = float(rect.x)
    def update(self, maze):
        # add pacSettings to reverse movement
        self.x += 1 * 3
        for rect in self.p1s:
            rect.x = self.x
            for rect2 in maze.bricks:
                if rect.colliderect(rect2):
                    self.x -= 1*3

    def blitme(self):
        for rect in self.p1s:
            self.screen.blit(self.p1.image, rect)
