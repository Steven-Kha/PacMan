import pygame
import sys

class EventLoop():
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def checkEvents(Game):
        # put keyboard events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # new function to make this function easier to add code
                check_keydown_events(event, Game.player)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event, Game.player)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_buttton(Game, mouse_x, mouse_y)

def check_play_buttton(Game, mouse_x, mouse_y):
    button_clicked = Game.playButton.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not Game.stats.game_active:
        pygame.mouse.set_visible(False)
        Game.stats.game_active = True

def check_keydown_events(event, player):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        player.moving_right = True
        player.moving_left = False
        player.moving_up = False
        player.moving_down = False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        player.moving_right = False
        player.moving_left = False
        player.moving_up = False
        player.moving_down = True
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        player.moving_right = False
        player.moving_left = True
        player.moving_up = False
        player.moving_down = False
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        player.moving_right = False
        player.moving_left = False
        player.moving_up = True
        player.moving_down = False
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, player):
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        player.moving_down = False
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        player.moving_up = False



#keydown events outside of the Eventloop