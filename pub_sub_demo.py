from topic import Topic 
from publlisher import Publisher 
from message import Message 
from subscriber_class import Subscriber 

def run():
    message_1=Message(1,"Django is Python framework")
    message_2=Message(2,"IIT Jeee is toughest exam of all year")
    subscriber_1=Subscriber("Subscriber 1")
    subscriber_2=Subscriber("Subscriber 2")
    topic=Topic(101,"Django")
    topic.add_subscribers(subscriber_1)
    topic.add_subscribers(subscriber_2)
    topic.remove_subscriber(subscriber_2)
    topic_1=Topic(101,"MindBlowig")
    # topic_1.add_subscribers(subscriber_2)
    publisher=Publisher()
    publisher.register_topic(topic)
    publisher.register_topic(topic_1)
    publisher.publish_message_to_topic(topic,message_1)
    publisher.publish_message_to_topic(topic,message_2)
    # subscriber_1.on_message(message_1)
    
    

if __name__=='__main__':
    run()
    