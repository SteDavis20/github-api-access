# need to pip install the PyGithub library

# import Github from the PyGithub library
from github import Github
import json                    # used for dictionary to string, need to install json library

class ScriptClass:
# save Personal Access Code in txt file
# note: when pasting file path, must replace "\" with "/".

    def getGithubUser(self):
        with open("C:/Users/Brendan/Documents/PersonalAccessCode.txt") as file:
            token = file.readline()
   
        g = Github(token)
        user = g.get_user()
        return user

    def retrieveData(self, user):
        if(user.login!=None):
            print("User: " + user.login)

        if(user.name!=None):
            print("Name: " + user.name)

        if(user.location!=None):
            print("Location: " + user.location)

        if(user.company!=None):
            print("Company: " + user.company)

        return user.login+user.name+user.location

    # no need to check for None value since we are not printing value in string format
    def extractDataIntoDictionary(self, user):
        dictionary = {"user": user.login,
                    "fullname": user.name,
                    "location": user.location,
                    "company": user.company
        }
        return dictionary

  
    def main(self):
        user = self.getGithubUser()
        
        print('This will be a github api visualisation project')
        data = self.retrieveData(user)
        print(data)

        dictionary = self.extractDataIntoDictionary(user)
        print("Dictionary is: " + json.dumps(dictionary))

