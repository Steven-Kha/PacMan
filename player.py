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

        self.dying = ['images/PacHit0.png', 'images/PacHit1.png', 'images/PacHit2.png',
                      'images/PacHit3.png', 'images/PacHit4.png', 'images/PacHit5.png',
                      'images/PacHit6.png']

        self.vistedNode = []
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

        self.hit = False
        self.animate = 0

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x_direction = 2
        self.y_direction = 2
        self.animate = 0

        self.lives = 2

    def center(self):
        for rect in self.players:
            self.x = 330
            self.y = 410
            rect.x = self.x
            rect.y = self.y

    def update(self, maze, pellets, blueGhost,
                redGhost, yellowGhost, pinkGhost,
               stats, scores):
        # add pacSettings to reverse movement
        now = pygame.time.get_ticks()
        moveRightFrame = Timer(self.moveRight)


        for rect in self.players:

            #PacMan hit by ghosts
            for blueRect in blueGhost.p1s:
                if rect.colliderect(blueRect):
                    self.hit = True

            for redRect in redGhost.reds:
                if rect.colliderect(redRect):
                    self.hit = True

            for yellowRect in yellowGhost.yellows:
                if rect.colliderect(yellowRect):
                    self.hit = True


            for pinkRect in pinkGhost.pinks:
                if rect.colliderect(pinkRect):
                    self.hit = True


            # hit animation
            if self.hit:

                if self.animate == 0 and now % 55 == 0:
                    self.p1.image = pygame.image.load(self.dying[0])
                    self.animate += 1


                elif self.animate == 1 and now % 55 == 0:
                    self.animate += 1
                    self.p1.image = pygame.image.load(self.dying[1])

                elif self.animate == 2 and now % 55 == 0:
                    self.animate += 1
                    self.p1.image = pygame.image.load(self.dying[2])

                elif self.animate == 3 and now % 55 == 0:
                    self.animate += 1
                    self.p1.image = pygame.image.load(self.dying[3])

                elif self.animate == 4 and now % 55 == 0:
                    self.animate += 1
                    self.p1.image = pygame.image.load(self.dying[4])

                elif self.animate == 5 and now % 55 == 0:
                    self.animate += 1
                    self.p1.image = pygame.image.load(self.dying[5])

                elif self.animate == 6 and now % 55 == 0:
                    self.animate += 1
                    self.p1.image = pygame.image.load(self.dying[6])

                elif self.animate == 7 and now % 55 == 0:
                    self.p1.image = pygame.image.load(self.moveRight[1])
                    self.hit = False
                    self.animate = 0
                    self.center()
                    self.lives -= 1

            # eat the pellets
            for pelletRect in pellets.pelletList:
                if rect.colliderect(pelletRect):
                    pellets.pelletList.remove(pelletRect)
                    stats.score += 100
                    scores.prep_score()

            if stats.score > stats.high_score:
                stats.high_score = stats.score
                scores.prep_high_score()


            # moving around the map
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