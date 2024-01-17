import pygame
import time
import sys
class Winking:
    
    def __init__(self, screen, handen, front, monddicht, oogdicht, ooghalf):
        # Define visualizations Lizz
        self.screen = screen
        self.handen = handen 
        self.front = front
        self.monddicht = monddicht
        self.oogdicht = oogdicht
        self.ooghalf = ooghalf

    def eyes(self):
        """This function display frames of Lizz winking after each other to generate a winking motion
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((255,255,255), (0,0,self.screen.get_width(), self.screen.get_height()//3.5))#2.72
            self.screen.blit(self.monddicht, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
    
            pygame.display.flip()
            time.sleep(2.5)
            self.screen.fill((255,255,255), (0,0,self.screen.get_width(), self.screen.get_height()//3.5))
            self.screen.blit(self.ooghalf, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            
            pygame.display.flip()
            time.sleep(0.1)
            self.screen.fill((255,255,255), (0,0,self.screen.get_width(), self.screen.get_height()//3.5))
            self.screen.blit(self.oogdicht, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
        
            pygame.display.flip()
            time.sleep(0.3)
            self.screen.fill((255,255,255), (0,0,self.screen.get_width(), self.screen.get_height()//3.5))
            self.screen.blit(self.oogdicht, (-100, -200))
            self.screen.blit(self.front, (-100, -200))
            
            pygame.display.flip()
            time.sleep(0.1)


 





