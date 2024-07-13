from abc import ABC,abstractmethod 
class Router(ABC):
    @abstractmethod 
    def withRoute(path,result):
        pass 
    @abstractmethod 
    def route(path):
        pass 
    