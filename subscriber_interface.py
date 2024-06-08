from abc import ABC, abstractmethod

class SubscriberInterface(ABC):
    @abstractmethod
    def on_message(self):
        pass

   