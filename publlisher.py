class Publisher:
    def __init__(self):
        self.topic_sets=set()
        
    def register_topic(self,topic):
        self.topic_sets.add(topic)
    
    def publish_message_to_topic(self,topic,message):
        if topic not in self.topic_sets:
            print("message can't be publish to the respective topic")
            return 
        else:
            topic.publish_message(message)
            print(topic.__dict__)
                