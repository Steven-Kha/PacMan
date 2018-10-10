import pygame
from maze import Maze
from player import Player
from settings import Settings
from eventloop import EventLoop

class Game():
    def __init__(self, pacSettings):
        pygame.init()

        self.screen = pygame.display.set_mode((pacSettings.screen_width , pacSettings.screen_height))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, "images/PacMaze.txt", "square")

        self.player = Player(self.screen, 'images/PacMaze.txt', 'pacman0')


    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents()
            self.updateScreen()
            self.player_update()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.player.blitme()
        pygame.display.flip()

    def player_update(self):
        self.player.update(self.maze)


pacSettings = Settings()
game = Game(pacSettings)
game.play()