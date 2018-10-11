import pygame
from maze import Maze
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

        self.maze = Maze(self.screen, "images/PacMaze.txt", "square")

        self.blueGhost = BlueGhost(self.screen, 'images/PacMaze.txt', 'BlueGhost0')

        self.redGhost = RedGhost(self.screen, 'images/PacMaze.txt', 'RedGhost0')

        self.yellowGhost = YellowGhost(self.screen, 'images/PacMaze.txt', 'YellowGhost0')

        self.pinkGhost = PinkGhost(self.screen, 'images/PacMaze.txt', 'PinkGhost0')

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents()
            self.updateScreen()
            self.player_update()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.blueGhost.blitme()
        self.redGhost.blitme()
        self.yellowGhost.blitme()
        self.pinkGhost.blitme()
        pygame.display.flip()

    def player_update(self):
        self.blueGhost.update(self.maze)
        self.redGhost.update(self.maze)
        self.yellowGhost.update(self.maze)
        self.pinkGhost.update(self.maze)


pacSettings = Settings()
game = Game(pacSettings)
game.play()