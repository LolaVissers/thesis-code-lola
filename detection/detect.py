import cv2

class Detection: 
    def __init__(self) -> None:
         # Initialize the camera
        self.cap = cv2.VideoCapture(0)  
        
         # Load the pre-trained face detection model
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
    
    def detection(self):
        """This function detects whether there is a face in the frame of the camera.
        It uses the a haarcascade from OpenCV for this. 

        Returns:
            Boolean: Return true if face has been detected.
        """
        # Counter for detected faces
        face_counter = 0  
        
        # Keep detecting until face has been detected
        while True:
            
            # Read a frame from the camera
            ret, frame = self.cap.read()

            if not ret:
                break
            
            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            frame = cv2.resize(frame, (810, 480))
            
            # Check if a face is detected
            if len(faces) > 0:
                print("Face detected")
                face_counter += 1

            # Check if a face has been detected three times
            if face_counter >= 5:
                return True

            if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
                break

        self.cap.release()
        cv2.destroyAllWindows()
