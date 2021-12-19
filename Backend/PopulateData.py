# import Github from the PyGithub library
from github import Github      # need to pip install the PyGithub library
import json                    # used for dictionary to string, need to install json library
import os.path                 # to save JSON data in visualisation src folder

# Import faker library - must install faker!
from faker import Faker     # for anonymising names
from collections import defaultdict

faker  = Faker()
names  = defaultdict(faker.name)

class PopulateData(object):
# save Personal Access Code in txt file
# note: when pasting file path, must replace "\" with "/".

    def getGithubUser(self):
        with open("C:/Users/Brendan/Documents/PersonalAccessCode.txt") as file:
            token = file.readline()
   
        g = Github(token)
        user = g.get_user()
        return user

    # no need to check for None value since we are not printing value in string format
    def extractDataIntoDictionary(self, user):
        dictionary = {"user": names[user.login].replace(" ", ""),   # username provides 2 names, so remove whitespace
                    "fullname": names[user.name],                          # annonymise name
                    "location": user.location,
                    "company": user.company,
                    "public_repos": user.public_repos
        }
        return dictionary

    # remove null fields in dictionary so we only store actual data in the database.
    def removeNullDataInDictionary(self, dictionary):
        for key, value, in dict(dictionary).items():
            if value is None:
                del dictionary[key]

        return dictionary

    def getAndStoreFollowerInfo(self, user, list):
        followerCount = user.followers
        followers = user.get_followers()
        for follower in followers:
            dictionary = self.extractDataIntoDictionary(follower)
            dictionary = self.removeNullDataInDictionary(dictionary)
            list.append(dictionary)
            #self.appendDataToJSONFile(dictionary)
            #print("follower: " + json.dumps(dictionary))
        return list

    def appendDataToJSONFile(self, list):
        save_path = '../Visualisation/visualisation-app/src'
        name_of_file = "dataSampleTest.json"
        completeName = os.path.join(save_path, name_of_file)
        with open(completeName, 'a') as output_file:
            json_object = json.dumps(list, indent = 4)
            output_file.write(json_object)

    def main(self):
        user = self.getGithubUser()

        dictionary = self.extractDataIntoDictionary(user)
        print("Dictionary is: " + json.dumps(dictionary))

        dictionary = self.removeNullDataInDictionary(dictionary)
        print("Dictionary is now cleaned such as: " + json.dumps(dictionary))

        dataAsList = []
        dataAsList.append(dictionary)
        #self.appendDataToJSONFile(dictionary)
        dataAsList = self.getAndStoreFollowerInfo(user, dataAsList)
        self.appendDataToJSONFile(dataAsList)

if __name__ == "__main__":
    PopulateData().main()