import multiprocessing
import random
from playsound import playsound
import pygame


class Music:
    def __init__(self):
        self.running = True

    # Make the thread stoppable
    def stop(self):
        self.running = False
        
    # Return the name of the cue
    def name_cue(self):
        return "Music"

    def playsong(self):
        """
        This function plays a song with a thread. Such that the thread can
        be stopped when the cue needs to terminate.
        """
        musicsounds = [
            'nonverbalcommunication/music/ambient-piano-and-strings-10711.mp3']
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            music = random.choice(musicsounds)
            thread = multiprocessing.Process(target=playsound, args=(music,))
            thread.start()
            while (self.running):
                if not self.running:
                    thread.terminate()
            if not self.running:
                thread.terminate()
                return
