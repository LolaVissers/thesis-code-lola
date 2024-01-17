import pygame
import sys
import time

class Wave:
    def __init__(self, screen, zwaai1, zwaai2, zwaai3, background, handen, front):
        # Define visualizations Lizz
        self.screen = screen
        self.zwaai1 = zwaai1
        self.zwaai2 = zwaai2
        self.zwaai3 = zwaai3
        self.background = background
        self.handen = handen
        self.front = front
        self.running = True
        
    # Make the thread stoppable
    def stop(self):
        self.running = False
        
    # Return the name of the cue
    def name_cue(self):
        return "Wave"

    def hands(self):
        """Display frames of Lizz waving after each other to generate a waving motion
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for i in range(5): 
                if not self.running: return
                self.screen.fill((255,255,255), (0,self.screen.get_height()//2.8,self.screen.get_width(), self.screen.get_height()))
                self.screen.blit(self.background, (30,300))
                self.screen.blit(self.front, (-100, -200))
                self.screen.blit(self.zwaai1, (-100, -200)) 
                pygame.display.flip()
                time.sleep(0.1) 
                self.screen.fill((255,255,255), (0,self.screen.get_height()//2.8,self.screen.get_width(), self.screen.get_height()))
                self.screen.blit(self.background, (30,300))
                self.screen.blit(self.front, (-100, -200))
                self.screen.blit(self.zwaai2, (-100, -200)) 
                pygame.display.flip()
                time.sleep(0.1)
                self.screen.fill((255,255,255), (0,self.screen.get_height()//2.8,self.screen.get_width(), self.screen.get_height()))
                self.screen.blit(self.background, (30,300))
                self.screen.blit(self.front, (-100, -200))
                self.screen.blit(self.zwaai3, (-100, -200))
                pygame.display.flip()
                time.sleep(0.5)
            if not self.running: return
            self.screen.fill((255,255,255), (0,self.screen.get_height()//2.8,self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(self.background, (30,300))
            self.screen.blit(self.front, (-100, -200))
            self.screen.blit(self.handen, (-100, -200))
            pygame.display.flip()
            time.sleep(0.5)
            


 






