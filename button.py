import pygame.font

class Button():

    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pac_settings = settings
        # set the dimension and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont(None, 48)
        # Build the button's rect object and center it.

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centery = self.screen_rect.bottom - 200
        # The button message needs to be prepped only once.

        self.hi_rect = pygame.Rect(0, 0, self.width, self.height)
        self.hi_rect.center = self.screen_rect.center
        self.hi_rect.centery = self.screen_rect.bottom - 100

        self.prep_msg(msg)

        # self.prep_hiscoring()

        self.prep_hiscore()
        self.prep_hiscores(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()

        #place it ontop of play button
        self.msg_image_rect.center = self.rect.center

    def prep_hiscore(self):
        high_score_str = "Hi Score:"

        self.hiscore_img = self.font.render(high_score_str, True,
                            self.text_color, self.button_color)

        self.hiscore_rect = self.hiscore_img.get_rect()

        self.hiscore_rect.center = self.hi_rect.center

    def prep_hiscores(self, msg):
        self.hi_img = self.font.render(msg, True, self.text_color,
                                       self.button_color)
        self.hi_img_rect = self.hi_img.get_rect()
        self.hi_img_rect.centerx = self.screen_rect.centerx
        self.hi_img_rect.bottom = self.screen_rect.bottom

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.hiscore_img, self.hiscore_rect)

    def show_hiscore(self):
        self.screen.blit(self.hi_img, self.hi_img_rect)




