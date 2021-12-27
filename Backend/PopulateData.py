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

    def getGithubUser(self, username):
        with open("C:/Users/Brendan/Documents/PersonalAccessCode.txt") as file:
            token = file.readline()
        g = Github(token)
        user = g.get_user(username)
        return user

    # no need to check for None value since we are not printing value in string format
    def extractDataIntoDictionary(self, user):
        followers = user.followers
        following = user.following
        ratio = followers/following
        dictionary = {#"user": names[user.login].replace(" ", ""),   # username provides 2 names, so remove whitespace
                    
                    #"fullname": names[user.name],                          # annonymise name
                    "user": user.login.replace(" ", ""),
                    "fullname": user.name,
                    "location": user.location,
                    "company": user.company,
                    "public_repos": user.public_repos,
                    "follower_count": followers,
                    "following_count": following,
                    "follower_ratio": ratio
        }
        return dictionary

    # remove null fields in dictionary so we only store actual data in the database.
    def removeNullDataInDictionary(self, dictionary):
        for key, value, in dict(dictionary).items():
            if value is None:
                del dictionary[key]

        return dictionary

    def getFollowerInfo(self, user, list):
        # followerCount = user.followers
        followers = user.get_followers()
        for follower in followers:
            dictionary = self.extractDataIntoDictionary(follower)
            dictionary = self.removeNullDataInDictionary(dictionary)
            list.append(dictionary)
            # self.appendDataToJSONFile(dictionary)
            # print("follower: " + json.dumps(dictionary))
        return list


    # finding "quality" of followers, by dividing followers by number of people they're following,
    # 3 levels:
    #           me:
    #               my followers:
    #                               followers of my followers
    def countFollowersOfFollowers(self, user):
        followers = user.get_followers()
        followerCount = 0
        followingCount = 0
        ratio = 0
        for follower in followers:
            followerFollowers = follower.get_followers()
            #count += follower.followers               # add number of followers each follower has
            for followerFollower in followerFollowers: 
                followerCount += followerFollower.followers               # add number of followers each follower has
                followingCount += followerFollower.following
        ratio = followerCount/followingCount
        dictionary = {
            #"user": names[user.login].replace(" ", ""),
            "user": user.login.replace(" ", ""),
            "public_repos": user.public_repos,
            "accumulated_Followers": followerCount,
            "accumulated_Following": followingCount,
            "accumulated_Ratio": ratio
        }
        return dictionary

    def appendDataToJSONFile(self, list, fileName):
        save_path = '../Visualisation/visualisation-app/src'
        name_of_file = fileName
        completeName = os.path.join(save_path, name_of_file)
        with open(completeName, 'a') as output_file:
            json_object = json.dumps(list, indent = 4)
            output_file.write(json_object)

    def main(self):
        username = input("Enter username to get data on: ")
        user = self.getGithubUser(username)

        dictionary = self.extractDataIntoDictionary(user)
        #print("Dictionary is: " + json.dumps(dictionary))

        dictionary = self.removeNullDataInDictionary(dictionary)
        #print("Dictionary is now cleaned such as: " + json.dumps(dictionary))


        # NEED TO CREATE 3 json files before appending to them below

        dataOnUser = []
        dataOnUser.append(dictionary)
        self.appendDataToJSONFile(dataOnUser, "dataSampleTest.json")

        followerData = []
        followerData = self.getFollowerInfo(user, followerData)
        self.appendDataToJSONFile(followerData, "followerData.json")

        dataOnFollowersOfFollowers = self.countFollowersOfFollowers(user)
        self.appendDataToJSONFile(dataOnFollowersOfFollowers, "accumulatedCount.json")

if __name__ == "__main__":
    PopulateData().main()