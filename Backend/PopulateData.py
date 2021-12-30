# import Github from the PyGithub library
from github import Github      # need to pip install the PyGithub library
import json                    # used for dictionary to string, need to install json library
import os.path                 # to save JSON data in visualisation src folder
import requests


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
        
        try:
            user = g.get_user(username)
        except:
            print("Invalid username, using default user of SteDavis20 instead.")
            user = g.get_user("SteDavis20")

        return user

    # no need to check for None value since we are not printing value in string format
    def extractDataIntoDictionary(self, user):
        followers = user.followers
        following = user.following
        try:
            ratio = followers/following
        except:
            print("Division by 0 because user is following 0 people.\nAssigning user minimum following value of 1.")
            following = 1
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
    def countFollowersOfFollowers(self, user, list):
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
        try:
            ratio = followerCount/followingCount
        except:
            print("Division by 0 because user is following 0 people.\nAssigning user minimum following value of 1.")
            followingCount = 1
            ratio = followerCount/followingCount
        
        dictionary = {
            #"user": names[user.login].replace(" ", ""),
            "user": user.login.replace(" ", ""),
            "public_repos": user.public_repos,
            "accumulated_Followers": followerCount,
            "accumulated_Following": followingCount,
            "accumulated_Ratio": ratio
        }
        list.append(dictionary)
        return list

    def getRepoNames(self, user):
        repos = user.get_repos()
        repoNames = []
        for repo in repos:
            repoNames.append(repo.name)
        
        return repoNames

    def getContributors(self, repo):
        contributors = []
        contributorsURL = repo.contributors_url
        page = 1
        while(True):
            request = requests.get(contributorsURL)
            data = request.json()

            for contributor in data:
                dictionary = {
                    "contributor": contributor['login'],
                    "contributions": contributor['contributions']
                }
                contributors.append(dictionary)

            amount_collected = len(data)
            if(amount_collected == 30):
                page = page + 1
                contributorsURL = contributorsURL + "?page=" + str(page)
            else:
                break
        return contributors        

    def getLanguageStats(self, user):
        repos = user.get_repos() 

        languageDictionary = {}

        for repo in repos:
            languageURL = repo.languages_url

            while(True):
                request = requests.get(languageURL)
                data = request.json()
                
                for key, value in dict(data).items():
                    if key in languageDictionary:
                        val = languageDictionary.get(key)
                        newVal = val + value
                        languageDictionary[key] = newVal
                    else:
                        languageDictionary[key] = value

                amount_collected = len(data)
                if(amount_collected == 30):
                    page = page + 1
                    contributorsURL = contributorsURL + "?page=" + str(page)
                else:
                    break

        list = []
        for key, value in dict(languageDictionary).items():
            rechartFriendlyDict = {
                "name": key,
                "value": value
            }
            list.append(rechartFriendlyDict)
            
        return list


    def main(self):
        username = input("Enter username to get data on: ")
        user = self.getGithubUser(username)

        #repoNames = self.getRepoNames(user)
        #print(repoNames)
     
        #repos = user.get_repos()

        #for repo in repos:
        #    contributors = self.getContributors(repo)
        #    print(contributors)

        languageStats = self.getLanguageStats(user)
        print(languageStats)

if __name__ == "__main__":
     PopulateData().main()