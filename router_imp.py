from router import Router 
class RouterImp(Router):
    def __init__(self):
        self.routes={}
    def withRoute(self,path,result):
        if path not in self.routes:
            self.routes[path]=result 
    def match(self,given_path,path_to_match):
        if len(given_path)!=len(path_to_match):
            return False
        for i in range(len(given_path)):
            if given_path[i]!=path_to_match[i] and path_to_match[i]!='*':
                return False 
        return True
            
    def route(self,path):
        if path in self.routes.keys():
            return self.routes[path]
        
        path1=path.split("/")
        for m,v in self.routes.items():
            m1=m.split("/")
            print("Ayushma")
            if self.match(m1,path1):
                return v  
        return -1
       
        
    
    
    
            
        