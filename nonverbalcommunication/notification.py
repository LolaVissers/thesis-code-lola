class Notification: 
    """
        This class is used to store characteristics of a notification.
    """  
    def __init__(self, urgency, message, name):
        self.urgency = urgency
        self.message = message
        self.name = name