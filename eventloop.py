import pygame
import sys

class EventLoop():
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def checkEvents():
        # put keyboard events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


#keydown events outside of the Eventloop