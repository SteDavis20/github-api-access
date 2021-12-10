# need to pip install the PyGithub library

# import Github from the PyGithub library
from github import Github

class ScriptClass:
# save Personal Access Code in txt file
# note: when pasting file path, must replace "\" with "/".

    def retrieveData(self):
        with open("C:/Users/Brendan/Documents/PersonalAccessCode.txt") as file:
            token = file.readline()
   
        g = Github(token)
        user = g.get_user()
   
        if(user.login!=None):
            print("User: " + user.login)

        if(user.name!=None):
            print("Name: " + user.name)

        if(user.location!=None):
            print("Location: " + user.location)

        if(user.company!=None):
            print("Company: " + user.company)

        return user.login+user.name+user.location

    def main(self):
        print('This will be a github api visualisation project')
        data = self.retrieveData()
        print(data)
