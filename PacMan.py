import pygame
from maze import Maze
from maze import Pellets
from player import Player
from ghost import BlueGhost
from ghost import RedGhost
from ghost import YellowGhost
from ghost import PinkGhost
from settings import Settings
from eventloop import EventLoop

class Game():
    def __init__(self, pacSettings):
        pygame.init()
        self.screen = pygame.display.set_mode((pacSettings.screen_width , pacSettings.screen_height))
        pygame.display.set_caption("Pacman Portal")

        self.player = Player(self.screen, 'images/PacMaze.txt', 'pacman0')

        self.maze = Maze(self.screen, "images/PacMaze.txt", "square")

        self.pellets = Pellets(self.screen, "images/PacMaze.txt", "pacman0")

        self.blueGhost = BlueGhost(self.screen, 'images/PacMaze.txt', 'BlueGhost0')

        self.redGhost = RedGhost(self.screen, 'images/PacMaze.txt', 'RedGhost0')

        self.yellowGhost = YellowGhost(self.screen, 'images/PacMaze.txt', 'YellowGhost0')

        self.pinkGhost = PinkGhost(self.screen, 'images/PacMaze.txt', 'PinkGhost0')

        self.spaceNumber = 1

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents()
            self.updateScreen()
            self.check_events()
            self.player_update()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.pellets.blitme()
        self.blueGhost.blitme()
        self.redGhost.blitme()
        self.yellowGhost.blitme()
        self.pinkGhost.blitme()
        self.player.blitme()
        pygame.display.flip()

    def player_update(self):
        self.blueGhost.update(self.maze)
        self.redGhost.update(self.maze)
        self.yellowGhost.update(self.maze)
        self.pinkGhost.update(self.maze)
        self.player.update(self.maze)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # print("Key was pressed down")
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                    self.player.moving_left = False
                    self.player.moving_up = False
                    self.player.moving_down = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.moving_right = False
                    self.player.moving_left = False
                    self.player.moving_up = False
                    self.player.moving_down = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.moving_right = False
                    self.player.moving_left = True
                    self.player.moving_up = False
                    self.player.moving_down = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.moving_right = False
                    self.player.moving_left = False
                    self.player.moving_up = True
                    self.player.moving_down = False
                elif event.key == pygame.K_SPACE:
                    print ("location: " + str(self.spaceNumber))
                    print("player.x: " + str(self.player.x))
                    print("player.y: " + str(self.player.y))
                    self.spaceNumber += 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.moving_down = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.moving_up = False



pacSettings = Settings()
game = Game(pacSettings)
game.play()