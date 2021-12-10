# need to pip install the PyGithub library

# import Github from the PyGithub library
from github import Github

# save Personal Access Code in txt file
# note: when pasting file path, must replace "\" with "/".
with open("C:/Users/Brendan/Documents/PersonalAccessCode.txt") as file:
   token = file.readline()

g = Github(token)

print('This will be a github api visualisation project')

user = g.get_user()

if(user.login!=None):
   print("User: " + user.login)

if(user.name!=None):
   print("Name: " + user.name)

if(user.location!=None):
   print("Location: " + user.location)

if(user.company!=None):
   print("Company: " + user.company)
