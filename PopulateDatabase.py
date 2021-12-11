# need to pip install the PyGithub library

# import Github from the PyGithub library
from github import Github
import json                    # used for dictionary to string, need to install json library
import pymongo                 # for mongodb access, need to install pymongo

class PopulateDatabase:
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

    # remove null fields in dictionary so we only store actual data in the database.
    def removeNullDataInDictionary(self, dictionary):
        for key, value, in dict(dictionary).items():
            if value is None:
                del dictionary[key]

        return dictionary

    # remember to have the database running, using docker commands
    # need to import pymongo library to use the code in this function
    def storeDictionaryInDatabase(self, dictionary):
        # Establish a connection
        connection = "mongodb://localhost:27017"         # database must be running to make connection
        client = pymongo.MongoClient(connection)

        # Create a database object
        database = client.classDB

        # githubuser is the name of the collection
        # if you mistype the collection name, e.g., githubuserr, the data will be stored in the wrong place.
        
        # note: everytime code is ran, duplicate data is inserted into database
        database.githubuser.insert_many([dictionary])
        print("Successful storage of data in database!")

    def main(self):
        user = self.getGithubUser()
        
        print('This will be a github api visualisation project')
        data = self.retrieveData(user)
        print(data)

        dictionary = self.extractDataIntoDictionary(user)
        print("Dictionary is: " + json.dumps(dictionary))

        dictionary = self.removeNullDataInDictionary(dictionary)
        print("Dictionary is now cleaned such as: " + json.dumps(dictionary))

        self.storeDictionaryInDatabase(dictionary)
