import time
import threading
import random
from nonverbalcommunication.cues import Cues
from nonverbalcommunication.winking import Winking
from nonverbalcommunication.popup import PopUp
from nonverbalcommunication.notification import Notification
from detection.detect import Detection
from gaze.gaze import Gaze
from text_to_speech import play_sound

def main():
    # PLEASE WRITE DOWN THE NAME OF THE PARTICIPANT
    name = "name.txt"

    # Define notifications
    urgencies = ['low', 'high', 'baseline']
    low_urgeny_message = Notification(
        urgencies[0], 'Hallo Is het misschien een idee om naar buiten te gaan vandaag?', 'low_urgency_messages')
    high_urgeny_message = Notification(
        urgencies[1], 'Hallo! Het is tijd om uw medicatie in te nemen.', 'medium_urgency_messages')
    low_urgency_baseline_message = Notification(
        urgencies[2], 'Hallo Is het misschien een idee om naar buiten te gaan vandaag?', 'low_urgency_baseline_messages')
    high_urgency_baseline_message = Notification(
        urgencies[2], 'Hallo! Het is tijd om uw medicatie in te nemen.', 'medium__urgency_baseline_messages')
    messages = [low_urgeny_message, high_urgeny_message, low_urgency_baseline_message, high_urgency_baseline_message]

    # Shuffle order notifications are presented
    random.shuffle(messages)
    
    # Initialize Lizz
    lizz = Cues()

    # Display Lizz and let Lizz wink
    background, screen, handen, front, monddicht, oogdicht, ooghalf, width, height = lizz.lizz()
    wink = threading.Thread(target=Winking(screen, handen, front, monddicht, oogdicht, ooghalf).eyes)
    wink.start()

    # Initialize popup message
    popup = PopUp(screen, width, height, background, handen, front)

    # Write order notifications to file participant
    f = open(name, "w")
    f.write(messages[0].name + ' ' + messages[1].name + ' ' + messages[2].name +
            ' ' + messages[3].name + "\n")
    f.close()
    
    # Loop through all the notifications
    for message in messages:
        
        # Initialize all the cues
        wave = lizz.wave()
        light_up = lizz.light_up()
        cough = lizz.cough()
        
        # Cues are implemented but not used
        # flash = lizz.flash()
        # music = lizz.music()
        # tone = lizz.tone()
        
        # Classify cues
        subtle_cues = [wave, light_up]
        intrusive_cues = [cough]
        
        # Time between each notification
        time.sleep(480)

        # Initialize presence detection
        detection_face = Detection()
        
        # Initialize attention detection
        gaze = Gaze()
        
        # Detect whether the participant is in the room or if it is a baseline case
        if (message.urgency != 'baseline' and detection_face.detection()):
            
            # If participant is present, check urgency
            if message.urgency == 'low':
                
                # Start attracting attention in a subtle way
                cue, target = random.choice(subtle_cues)

                # Write down the chosen cue
                f = open(name, "a")
                f.write(str(target.name_cue()) + ' ' +
                        str(message.urgency) + '\n')
                f.close()

                # Start presenting cue
                cue.start()
                
                # Check if you have attention
                if (gaze.gaze()):
                    
                    # If you have attention stop cue and present message
                    target.stop()
                    cue.join()
                    speech = threading.Thread(
                        target=play_sound, args=(message.message, 'Notification.mp3',))
                    speech.start()
                    popup.show_popup(message.message)
                    speech.join()

                # If you do not have attention after 20 seconds, stop cue and do not present message
                target.stop()
                cue.join()

            elif message.urgency == 'high':
                
                # Start attracting attention in a subtle way
                cue, target = random.choice(subtle_cues)

                # Write down the chosen cue
                f = open(name, "a")
                f.write(str(target.name_cue()) + ' ' +
                        str(message.urgency) + '\n')
                f.close()

                # Start presenting cue
                cue.start()

                # Check whether attention has been gained by first cue
                attention = False
                
                # Check if you have attention
                if (gaze.gaze()):
                    
                    # If you have attention stop cue and present message
                    attention = True
                    target.stop()
                    cue.join()
                    speech = threading.Thread(
                        target=play_sound, args=(message.message, 'Notification.mp3',))
                    speech.start()
                    popup.show_popup(message.message)
                    speech.join()

                # If you do not have attention after 20 seconds, stop cue and start attracting attention in a less subtle way
                if (attention == False):
                    target.stop()
                    cue.join()
                    gaze = Gaze()
                    
                    # Choose intrusive cue
                    cue, target = random.choice(intrusive_cues)

                    # Write down the chosen cue
                    f = open(name, "a")
                    f.write(str(target.name_cue()) + ' ' +
                            str(message.urgency) + '\n')
                    f.close()

                    # Start presenting cue
                    cue.start()
                    
                    # Check if you have attention
                    if (gaze.gaze()):
                        
                        # If you have attention stop cue and present message
                        attention = True
                        target.stop()
                        cue.join()
                        thread_speech = threading.Thread(
                            target=play_sound, args=(message.message, 'Notification.mp3',))
                        thread_speech.start()
                        popup.show_popup(message.message)
                        thread_speech.join()

                    # If you do not have attention after 30 seconds, stop cue and do not present message
                    target.stop()
                    cue.join() 
                               
        # The baseline case
        else:
            # Present message
            thread_speech = threading.Thread(
                target=play_sound, args=(message.message, 'Notification.mp3',))
            thread_speech.start()
            popup.show_popup(message.message)
            thread_speech.join()
            
    wink.join()


if __name__ == "__main__":
    main()
