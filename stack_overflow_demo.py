from stack_overflow import StackOverflow
from user import User
from question import Question
from answer import Answer
from tag import Tag
def run():
    m=StackOverflow.getInstance()
    user=User(101,"Ayushma","bahugunaayushma@gmail.com","Welcome",0)
    m.register_users(user)
    m.user_login("bahugunaayushma@gmail.com","Welcome")
    tag=Tag(11,"Django puzzles")
    tag1=Tag(12,"Djago Mystery")
    ques=Question(101,user,[tag,tag1],["Make migration is getting failed"],0,None,None)
    ans=Answer(201,user,101,0,None)
    m.post_question(ques)
    m.post_answers(ans)
    m.voting_answers(ans,10)
    m.search_Questions([],"migration")
    
    
    
if __name__=="__main__":
    run()