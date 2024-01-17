from gtts import gTTS
from pygame import mixer, time
import os  

def play_sound(text, file):
    """ This function generates a voice which reads the input text out loud. 
    A temporary file has been created to temporary save the audio.

    Args:
        text (String): text that needs to be spoken out loud
        file (String): name of the temporary file
    """
    myobj = gTTS(text=text, lang='nl')
    myobj.save(file)
    
    mixer.init()
    sound = mixer.Sound(file)
    channel = sound.play()

    while channel.get_busy():
        time.wait(10) 
        
    os.remove(file)
