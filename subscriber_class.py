from subscriber_interface import SubscriberInterface
from message import Message
class Subscriber(SubscriberInterface):
    def __init__(self,name):
        self.name=name
    def on_message(self,message):
        print(f"{self.name} is {message.content}")
       