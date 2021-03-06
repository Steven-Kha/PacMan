import pygame

from maze import Maze
from maze import Pellets
from player import Player
from ghost import BlueGhost
from ghost import RedGhost
from ghost import YellowGhost
from ghost import PinkGhost
from maze import Nodes
from button import Button
from settings import Settings
from game_stats import GameStats
from eventloop import EventLoop
from cutscene import PacMan
from cutscene import Blue
from cutscene import Red
from cutscene import Yellow
from cutscene import Pink
from scoreboard import Scoreboard
from scores import Scores

class Game():
    def __init__(self, pacSettings):
        pygame.init()
        self.screen = pygame.display.set_mode((pacSettings.screen_width , pacSettings.screen_height))
        pygame.display.set_caption("Pacman Portal")

        self.player = Player(self.screen, 'images/PacMaze.txt', 'pacman0')

        self.maze = Maze(self.screen, "images/PacMaze.txt", "square")

        self.pellets = Pellets(self.screen, "images/PacMaze.txt", "pellets")

        self.nodes = Nodes(self.screen, "images/PacMaze.txt", "node")

        self.blueGhost = BlueGhost(self.screen, 'images/PacMaze.txt', 'BlueGhost0')

        self.redGhost = RedGhost(self.screen, 'images/PacMaze.txt', 'RedGhost0')

        self.yellowGhost = YellowGhost(self.screen, 'images/PacMaze.txt', 'YellowGhost0')

        self.pinkGhost = PinkGhost(self.screen, 'images/PacMaze.txt', 'PinkGhost0')

        self.stats = GameStats(pacSettings)

        self.playButton = Button(pacSettings, self.screen, "Play")

        self.pac = PacMan(self.screen, "pacman0")

        self.yellow = Yellow(self.screen, 'YellowGhost0')

        self.pink = Pink(self.screen, 'PinkGhost0')

        self.red = Red(self.screen, 'RedGhost0')

        self.blue = Blue(self.screen, "BlueGhost0")

        self.oldHiscore = 0

        self.scores = Scores(pacSettings, self.screen, self.stats)

        fo = open("foo.txt", "r+")
        self.stats.high_score = int(fo.readline())
        fo.close()
        self.oldHiscore = self.stats.high_score
        self.title = Scoreboard(self.screen, "pacmantitle")

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.checkEvents(self)
            self.updateScreen()
            # self.check_events()
            self.player_update()

    def updateScreen(self):
        self.screen.fill((0, 0, 0))
        #put main menu here
        # if game.stats_active

        if self.stats.game_active == False:
            self.player.lives = 2
            self.stats.score = 0
            self.screen.fill((0, 0, 0))
            self.pac.blitme()
            self.blue.blitme()
            self.red.blitme()
            self.yellow.blitme()
            self.pink.blitme()
            self.playButton.draw_button()
            self.title.blitme()
            if self.stats.high_score_active == True:
                self.playButton.prep_hiscores(str(self.stats.high_score))
                self.playButton.show_hiscore()


        else:
            self.nodes.blitme()
            self.maze.blitme()
            self.pellets.blitme()
            self.blueGhost.blitme()
            self.redGhost.blitme()
            self.yellowGhost.blitme()
            self.pinkGhost.blitme()
            self.player.blitme()
            self.scores.show_score()

        pygame.display.flip()

    def player_update(self):
        if self.stats.game_active == True:
            if self.player.lives == 0:
                self.stats.game_active = False
                self.pellets.build()
                pygame.mouse.set_visible(True)
                if self.oldHiscore < self.stats.high_score:
                    foo = open("foo.txt", "w")
                    foo.write(str(self.stats.high_score))
                    foo.close()
            self.blueGhost.update(self.maze)
            self.redGhost.update(self.maze)
            self.yellowGhost.update(self.maze)
            self.pinkGhost.update(self.maze)
            self.player.update(self.maze, self.pellets, self.blueGhost,
                               self.redGhost, self.yellowGhost, self.pinkGhost,
                               self.stats, self.scores)
            self.scores.show_score()
        else:
            self.pac.update()
            self.blue.update()
            self.red.update()
            self.yellow.update()
            self.pink.update()



pacSettings = Settings()
game = Game(pacSettings)
game.play()