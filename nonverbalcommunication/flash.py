import pygame
import sys

class Flash:
    
    def __init__(self, screen, handen, front, background):
        # Initializing images important for representing the cough
        self.screen = screen
        self.handen = handen 
        self.front = front
        self.background = background
        self.running = True
        
    # Make the thread stoppable
    def stop(self):
        self.running = False
     
    # Return the name of the cue   
    def name_cue(self):
        return "Flash"

    def flash(self):
        """
        This function fills a circle more and more with blue to flash. It starts with
        a black circle and ends with a blue circle. After this it starts again.
        """
        while True:
            if not self.running: 
                self.screen.blit(self.background, (30,300))
                self.screen.blit(self.handen, (-100, -200))
                self.screen.blit(self.front, (-100, -200))
                return
            # Set initial state
            alpha = 0  # Alpha value for black screen
            while alpha!=254:
                if not self.running: 
                    self.screen.blit(self.background, (30,300))
                    self.screen.blit(self.handen, (-100, -200))
                    self.screen.blit(self.front, (-100, -200))
                    return
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                # Increase alpha to gradually lighten the screen
                alpha = min(alpha + 1, 255)

                # Draw background with alpha value
                pygame.draw.circle(self.screen, (0, alpha, alpha), (250,520), 210)
                self.screen.blit(self.handen, (-100, -200))
                self.screen.blit(self.front, (-100, -200))

                # Update the display
                pygame.display.flip()

                # Control the frame rate
                pygame.time.Clock().tick(500)

 





