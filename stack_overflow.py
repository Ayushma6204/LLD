from user import User
from threading import Lock
class StackOverflow:
    instance=None
    @staticmethod
    def getInstance():
        if StackOverflow.instance is None:
            StackOverflow.instance=StackOverflow()
        return StackOverflow.instance
    
    def __init__(self):
        self.list_of_question=[]
        self.list_of_answers={}
        self.comments={}
        self.users_list={}
        self.lock=Lock
    
    def register_users(self,user):
        self.users_list[user.id]=user 
        return self.users_list
    
    def user_login(self,email,password):
        for id in self.users_list:
            user=self.users_list[id]
            print(user)
            if user.email==email and user.password==password:
                user.log_in()
            else:
                print("Incorrect email and password")
    
    def post_question(self,question):
       print(question.__dict__)
       self.list_of_question.append(question)
       print(self.list_of_question)
       return self.list_of_question
    
    def post_answers(self,answers):
       self.list_of_answers[answers.question_id]=answers
       return self.list_of_answers
    
    def voting_answers(self,answers,val):
        with self.lock():
            answers.vote_count+=val 
            self.update_userReputation(answers.user,val)
            print(answers.__dict__)
            return answers
    def voting_questions(self,question,val):
        with self.lock():
            question.vote_count+=val
            self.update_userReputation(question.user,val)
            return question
    def update_userReputation(self,user,val):
        with self.lock():
            user.reputation+=val
            return user
    def search_Questions(self,tag,query):
        for ques in self.list_of_question:
            description=ques.description[0].split(" ")
            if  query in description or tag in ques.list_of_tag:
                print(ques.__dict__)
                return ques
            else:
                print("No question found with given query and tag")
           
        
        
        
        