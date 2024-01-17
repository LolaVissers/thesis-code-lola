import cv2
import time
import pygame

class Gaze:
    def __init__(self) -> None:
        # Load the pre-trained face and eye detection models
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

         # Initialize the camera
        self.cap = cv2.VideoCapture(0)  

    def gaze(self):
        """This function measures attention by measuring if someone is looking at Lizz (therefore looking at the screen).
        This has been measured using a face and eye cascade from OpenCV.

        Returns:
            Boolean: Return if attention has been detected.
        """
        counter = 0

        # Measure gaze for 30 seconds
        t_end = time.time() + 20   
        
        while (time.time() < t_end):
            # Capture a frame
            _, frame = self.cap.read()

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            # For each detected face, check if eyes are looking towards the screen
            for (x, y, w, h) in faces:
                
                # Define region of interest
                face = frame[y:y + h, x:x + w]
                eyes = self.eye_cascade.detectMultiScale(face)

                # Assuming both eyes are detected
                if len(eyes) >= 2:  
                    
                    # Calculate the center of both eyes
                    eye1_x, eye1_y, eye1_w, eye1_h = eyes[0]
                    eye2_x, eye2_y, eye2_w, eye2_h = eyes[1]
                    eye1_center = (x + eye1_x + eye1_w // 2, y + eye1_y + eye1_h // 2)
                    eye2_center = (x + eye2_x + eye2_w // 2, y + eye2_y + eye2_h // 2)

                    # Calculate the midpoint between both eyes
                    gaze_midpoint = ((eye1_center[0] + eye2_center[0]) // 2, (eye1_center[1] + eye2_center[1]) // 2)

                    # Define screen region based on your setup
                    screen_x, screen_y, screen_width, screen_height = 0, 0, 1920, 1080
                    
                    # Check if the gaze midpoint is within the screen region
                    if screen_x <= gaze_midpoint[0] <= screen_x + screen_width and \
                            screen_y <= gaze_midpoint[1] <= screen_y + screen_height:
                        print("Looking at the screen")
                        # Increase counter if user is looking at screen
                        counter+=1
            
            # If user is looking at screen for at least 4 frames
            if counter >= 4:
                print("Yay, looking at the screen long enough")
                return True
            
            if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
                break

        self.cap.release()
        cv2.destroyAllWindows()
        
    def gaze2(self): 
        """This function manually measures gaze. The researcher clicks on the screen 
        if gaze has been detected

        Returns:
           Boolearn: Detects whether gaze has been detected
        """
        
        # Measure gaze for 30 seconds
        t_end = time.time() + 30  
         
        while (time.time() < t_end):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                # If researcher clicks on the screen return true
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        return False
