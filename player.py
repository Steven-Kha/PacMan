import pygame
from imagerect import ImageRect
class Player():
    P1_SIZE = 35
    def __init__(self, screen, mazefile, p1):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.blueGhosts = ['images/BlueGhost0.png', 'images/BlueGhost1.png',
                           'images/BlueGhost2.png', 'images/BlueGhost3.png']
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

    def update(self, maze):
        # add pacSettings to reverse movement
        time = pygame.time.get_ticks()

        for rect in self.players:
            # if self.y_hit is not self.y:
            #     self.hit_right = False
            if self.moving_right:
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
                self.y += self.y_direction
                rect.y = self.y
                for rect2 in maze.bricks:
                    if rect.colliderect(rect2):
                        self.y = self.y - self.y_direction
                        rect.y = self.y
                        return

            if self.moving_left:
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