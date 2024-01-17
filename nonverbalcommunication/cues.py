import pygame
import time
import threading
from nonverbalcommunication.cough import Cough
from nonverbalcommunication.wave import Wave
from nonverbalcommunication.lightup import LightUp
from nonverbalcommunication.music import Music
from nonverbalcommunication.ringtone import Tone
from nonverbalcommunication.flash import Flash

"""
This class creates a PyGame screen to display/present the cues. It extracts the 
cues from other classes.
"""
class Cues():
    def __init__(self):
    
        pygame.init()
        
        # Initializing size Lizz
        self.width = 500
        self.height = 813
        
        # Set up the display
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Load your images Lizz
        monddicht = pygame.image.load(
            'Liz images(NML)/faces & hands/Neutraal mond dicht.png').convert_alpha()

        mondopen = pygame.image.load(
            'Liz images(NML)/faces & hands/Neutraal mond open.png').convert_alpha()

        cough1 = pygame.image.load(
            'Liz images(NML)/faces & hands/Cough 1.png').convert_alpha()

        cough2 = pygame.image.load(
            'Liz images(NML)/faces & hands/Cough 2.png').convert_alpha()

        oogdicht = pygame.image.load(
            'Liz images(NML)/faces & hands/Neutraal ogen dicht.png').convert_alpha()

        ooghalf = pygame.image.load(
            'Liz images(NML)/faces & hands/Neutraal ogen halfdicht.png').convert_alpha()

        handen = pygame.image.load(
            'Liz images(NML)/faces & hands/handen.png').convert_alpha()

        vuist = pygame.image.load(
            'Liz images(NML)/faces & hands/neutraal vuist.png').convert_alpha()

        front = pygame.image.load(
            'Liz images(NML)/faces & hands/Liz front.png').convert_alpha()

        onehand = pygame.image.load(
            'Liz images(NML)/faces & hands/one_hand.png').convert_alpha()

        background = pygame.image.load(
            'Liz images(NML)/faces & hands/achtergrond_Lizz.jpg').convert_alpha()

        onevuist = pygame.image.load(
            'Liz images(NML)/faces & hands/one_vuist.png').convert_alpha()

        zwaai1 = pygame.image.load(
            'Liz images(NML)/faces & hands/zwaaien 1.png').convert_alpha()

        zwaai2 = pygame.image.load(
            'Liz images(NML)/faces & hands/zwaaien 2.png').convert_alpha()

        zwaai3 = pygame.image.load(
            'Liz images(NML)/faces & hands/zwaaien 3.png').convert_alpha()
        
        # Set up the display
        height = self.height * 1.4
        width = self.width * 1.4
        
        # Rescale the images
        self.monddicht = pygame.transform.scale(monddicht, (width, height))
        self.mondopen = pygame.transform.scale(mondopen, (width, height))
        self.cough1 = pygame.transform.scale(cough1, (width, height))
        self.cough2 = pygame.transform.scale(cough2, (width, height))
        self.oogdicht = pygame.transform.scale(oogdicht, (width, height))
        self.ooghalf = pygame.transform.scale(ooghalf, (width, height))
        self.handen = pygame.transform.scale(handen, (width, height))
        self.vuist = pygame.transform.scale(vuist, (width, height))
        self.front = pygame.transform.scale(front, (width, height))
        self.onehand = pygame.transform.scale(onehand, (width, height))
        self.background = pygame.transform.scale(background, (450, 450))
        self.onevuist = pygame.transform.scale(onevuist, (width, height))
        self.zwaai1 = pygame.transform.scale(zwaai1, (width, height))
        self.zwaai2 = pygame.transform.scale(zwaai2, (width, height))
        self.zwaai3 = pygame.transform.scale(zwaai3, (width, height))
        
    def lizz(self):
        """This function is useful at the start of the program it is used to display Lizz for the first time.

        Returns:
            characteristic objects
        """
        self.screen.fill((255,255,255))
        self.screen.blit(self.background, (30,300))
        self.screen.blit(self.handen, (-100, -200))
        self.screen.blit(self.mondopen, (-100, -200))
        self.screen.blit(self.front, (-100, -200))
        pygame.display.flip()
        time.sleep(1)
        return self.background, self.screen, self.handen, self.front, self.monddicht, self.oogdicht, self.ooghalf, self.width, self.height

    def light_up(self):
        """This function initializes the thread and class to start the cue light up

        Returns:
            thread, target: thread represents the thread that should be started when this cue
            should be presented. Target represents the class that is being used for this.
        """
        target = LightUp(self.screen, self.handen, self.front, self.background)
        thread = threading.Thread(target=target.lightup)
        return thread, target
        
    def flash(self):
        """This function initializes the thread and class to start the cue flash

        Returns:
            thread, target: thread represents the thread that should be started when this cue
            should be presented. Target represents the class that is being used for this.
        """
        target = Flash(self.screen, self.handen, self.front, self.background)
        thread = threading.Thread(target=target.flash)
        return thread, target

    def cough(self):
        """This function initializes the thread and class to start the cue cough

        Returns:
            thread, target: thread represents the thread that should be started when this cue
            should be presented. Target represents the class that is being used for this.
        """
        target = Cough(self.screen, self.background, self.onevuist, self.onehand, self.front, self.handen, self.monddicht)
        thread = threading.Thread(target=target.cough)
        return thread, target

    def wave(self):
        """This function initializes the thread and class to start the cue wave

        Returns:
            thread, target: thread represents the thread that should be started when this cue
            should be presented. Target represents the class that is being used for this.
        """
        target = Wave(self.screen, self.zwaai1, self.zwaai2, self.zwaai3, self.background, self.handen, self.front)
        thread = threading.Thread(target=target.hands)
        return thread, target
    
    def music(self):
        """This function initializes the thread and class to start the cue music

        Returns:
            thread, target: thread represents the thread that should be started when this cue
            should be presented. Target represents the class that is being used for this.
        """
        target = Music()
        thread = threading.Thread(target=target.playsong)
        return thread, target
        
    def tone(self):
        """This function initializes the thread and class to start the cue tone

        Returns:
            thread, target: thread represents the thread that should be started when this cue
            should be presented. Target represents the class that is being used for this.
        """
        target = Tone()
        thread = threading.Thread(target=target.ringtone)
        return thread, target

