# need to pip install the PyGithub library

# import Github from the PyGithub library
from github import Github
# import os                   # necessary to set github access token via environment variable 

# save Personal Access Code in txt file
# note: when pasting file path, must replace "\" with "/".
with open("C:/Users/Brendan/Documents/PersonalAccessCode.txt") as file:
   token = file.readline()

g = Github(token)

print('This will be a github api visualisation project')

user = g.get_user()

print("User: " + user.login)
print("Name: " + user.name)
print("Location: " + user.location)
