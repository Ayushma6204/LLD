from subscriber_class import Subscriber
class Topic:
    def __init__(self,id,name):
        self.id=id 
        self.name=name 
        self.subscribers_set=set()
    
    def add_subscribers(self,subscriber):
        self.subscribers_set.add(subscriber)
    def remove_subscriber(self,subscriber):
        self.subscribers_set.remove(subscriber)
    
    def publish_message(self,message):
        for subscriber in self.subscribers_set:
            subscriber.on_message(message)