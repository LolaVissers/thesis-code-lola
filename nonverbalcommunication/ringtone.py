import multiprocessing
from playsound import playsound
from time import sleep

class Tone: 
    def __init__(self):
        self.running = True
        
    # Make the thread stoppable
    def stop(self):
        self.running = False
        
    # Return the name of the cue
    def name_cue(self):
        return "Ringtone" 
        
    # This function plays the ringtone on repeat
    def play_sound(self):
        while True:
            ringtone = 'Lola/nonverbalcommunication/notification sound/marimba-for-smartphone-151931.mp3'
            playsound(ringtone)   
    
    def ringtone(self):
        """
        This function plays a ringtone with a thread. Such that the thread can
        be stopped when the cue needs to terminate.
        """
        while True: 
            thread = multiprocessing.Process(target=self.play_sound)
            thread.start()
            while (self.running):
                if not self.running: 
                    thread.terminate()
            if not self.running: 
                thread.terminate()
                return 