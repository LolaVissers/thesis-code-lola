import pygame
import sys
import time

class PopUp:
    def __init__(self, screen, width, height, background, handen, front):
        # Define visualizations Lizz
        self.screen = screen
        self.width = width
        self.height = height
        self.background = background
        self.handen = handen
        self.front = front
        
        # Define colors
        self.light_pink = (255, 182, 193)
        self.beige = (255, 248, 232)
        self.black = (0, 0, 0)


        # Set font 
        self.font = pygame.font.Font("freesansbold.ttf", 14)

        # Define images for feedback notification
        self.thumbs_up = pygame.image.load(
            'Liz images(NML)/faces & hands/thumbsup.png').convert_alpha()

        self.thumbs_down = pygame.image.load(
            'Liz images(NML)/faces & hands/thumbsdown.png').convert_alpha()

        self.thumbs_up = pygame.transform.scale(self.thumbs_up, (60, 60))
        self.thumbs_down = pygame.transform.scale(self.thumbs_down, (60, 60))

    
    def show_popup(self, message):
        """This function generates and displays the popup
        with the message that should appear on the belly of Lizz.

        Args:
            message (String): Message that should be displayed
        """
        
        # Resize messages to fit on screen
        if message == 'Hallo Is het misschien een idee om naar buiten te gaan vandaag?':
            message = 'Tijd om naar buiten te gaan?'
        else: 
            message = 'Tijd voor uw medicatie?'

        # Define sizes popup
        popup_width, popup_height = 400, 200
        popup_x = 50
        popup_y = 350
        
        # Draw box for popup
        pygame.draw.rect(self.screen, self.light_pink, (popup_x,
                         popup_y, popup_width, popup_height), border_radius=15)

        # Draw text in popup
        text = self.font.render(message, True, self.black)
        text_rect = text.get_rect(center=(popup_x + popup_width // 2, popup_y + 40))
        self.screen.blit(text, text_rect)

        # define and draw boxes to put thumbs up and down in
        yes_button_rect = pygame.Rect(popup_x + 40, popup_y + 80, 120, 60)
        no_button_rect = pygame.Rect(popup_x + popup_width - 150, popup_y + 80, 120, 60)
        pygame.draw.rect(self.screen, self.beige,yes_button_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.beige,no_button_rect, border_radius=10)

        # define and put images inside boxes thumbs up and down
        yes_image = self.thumbs_up.get_rect(center=yes_button_rect.center)
        self.screen.blit(self.thumbs_up, yes_image)
        no_image = self.thumbs_down.get_rect(center=no_button_rect.center)
        self.screen.blit(self.thumbs_down, no_image)
        pygame.display.flip()
        time.sleep(1)

        # Display message for 60 seconds
        t_end = time.time() + 60
        while time.time() < t_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # If there has been clicked on one of the thumbs close message
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if yes_button_rect.collidepoint(mouse_pos):
                        print(True)
                        t_end = time.time()
                    elif no_button_rect.collidepoint(mouse_pos):
                        print(False)
                        t_end = time.time()
        self.screen.blit(self.background, (30, 300))
        self.screen.blit(self.handen, (-100, -200))
        self.screen.blit(self.front, (-100, -200))
        pygame.display.flip()
        time.sleep(1)

    