import pygame
import time
from playsound import playsound


class Cough:

    def __init__(self, screen, background, onevuist, onehand, front, handen, monddicht):
        # Initializing images important for representing the cough
        self.screen = screen
        self.background = background
        self.onevuist = onevuist
        self.onehand = onehand
        self.front = front
        self.handen = handen
        self.monddicht = monddicht
        self.running = True

    # Make the thread stoppable
    def stop(self):
        self.running = False
        
    # Return the name of the cue
    def name_cue(self):
        return "Cough"

    def cough(self):
        """Display all the images of Lizz coughing after each other and play the sound of Lizz
        coughing.
        """
        while True:
            if not self.running:
                return
            self.screen.fill((255, 255, 255), (0, self.screen.get_height(
            )//2.8, self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.background, (30, 300))
            self.screen.blit(self.onevuist, (-100, -200))
            self.screen.blit(self.onehand, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            pygame.display.flip()
            time.sleep(0.1) 
            self.screen.fill((255, 255, 255), (0, self.screen.get_height(
            )//2.8, self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.background, (30, 300))
            self.screen.blit(self.onevuist, (-200, -250))
            self.screen.blit(self.onehand, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            pygame.display.flip()
            time.sleep(0.1)
            self.screen.fill((255, 255, 255), (0, self.screen.get_height(
            )//2.8, self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.background, (30, 300))
            self.screen.blit(self.onevuist, (-260, -350))
            self.screen.blit(self.onehand, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            pygame.display.flip()
            time.sleep(0.1)

            self.screen.fill((255, 255, 255), (0, self.screen.get_height(
            )//2.8, self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.background, (30, 300))
            self.screen.blit(self.onevuist, (-300, -420))
            self.screen.blit(self.onehand, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            pygame.display.flip()
            time.sleep(0.5) 

            self.screen.fill((255, 255, 255), (0, self.screen.get_height(
            )//2.8, self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.onevuist, (-300, -420))
            self.screen.blit(self.background, (30, 300))
            self.screen.blit(self.onehand, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            pygame.display.flip()
            for i in range(2):
                playsound('nonverbalcommunication/cough.mp3')
            time.sleep(0.3)
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (30, 300))
            self.screen.blit(self.handen, (-100, -200))
            self.screen.blit(self.monddicht, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            pygame.display.flip()
            time.sleep(1)
