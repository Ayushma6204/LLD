from uuid import uuid4
import time 
class UserSession:
    def __init__(self,user_id,session_duration):
        self.session_id=str(uuid4())
        self.user_id=user_id 
        self.creation_time=time.time()
        self.expiry_time=self.creation_time+session_duration
    
    def is_expired(self):
        return time.time()>self.expiry_time
 