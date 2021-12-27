import os
import unittest                 # testing framework

from PopulateData import PopulateData

class PopulateDataTest(unittest.TestCase):
    
    # no need for this test because if it fails, all other tests would fail.
    # Since other tests pass, this method works.
    def testGetGithubUser(self):
        pd = PopulateData()
        username1 = "SteDavis20"
        user1 = pd.getGithubUser(username1)
        userType = (str)(type(user1))               # type objects cannot be split like strings can
        userTypeClassName = userType[8:34]          
        self.assertEqual("github.NamedUser.NamedUser", userTypeClassName)

    def testExtractDataIntoDictionary(self):
        pd = PopulateData()
        dictionary = {"user": "SteDavis20",
                    "fullname": "Stephen Davis",
                    "location": "Kildare",
                    "company": None,
                    "public_repos": 13,
                    "follower_count": 17,
                    "following_count": 20,
                    "follower_ratio": (17/20)
                    }
        user = pd.getGithubUser("SteDavis20")
        self.assertEqual(dictionary, pd.extractDataIntoDictionary(user))


    def testRemoveNullDataInDictionary(self):
        pd = PopulateData()
        dictionary = {"user": "SteDavis20",
                    "fullname": "Stephen Davis",
                    "location": "Kildare",
                    "company": None
                    }
        improvedDictionary = {
                    "user": "SteDavis20",
                    "fullname": "Stephen Davis",
                    "location": "Kildare"
        }
        self.assertEqual(improvedDictionary, pd.removeNullDataInDictionary(dictionary))

#-------------------------------------------------------------------------------------------------------

    # can only test count of followers, because testing collection of individual data would breach privacy of
    # follower
    # note: 17 followers at time of writing test, so test may fail as more or less followers will follow over time.
 #   def testGetFollowerInfo(self):
 #       pd = PopulateData()
 #       user = pd.getGithubUser("SteDavis20")
 #       self.assertEqual(17, pd.getAndStoreFollowerInfo(user))

#-------------------------------------------------------------------------------------------------------

    def testCountFollowersOfFollowers(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis20")
        dictionary = {
            "user": "SteDavis20",
            "public_repos": 13,
            "accumulated_Followers": 9272,
            "accumulated_Following": 50096,
            "accumulated_Ratio": 0.18508463749600768
        }
        self.assertEqual(dictionary, pd.countFollowersOfFollowers(user))

# cannot test Annonymisation and above methods at same time, comment/un-comment src code in PopulateData.py
# as appropriate for testing below function. 

#    def testAnnonymisation(self):
#        pd = PopulateData()
#        user = pd.getGithubUser("SteDavis20")
#        annonymisedDictionary = pd.extractDataIntoDictionary(user)
#        originalDictionary = {"user": "SteDavis20",
#                            "fullname": "Stephen Davis",
#                            "location": "Kildare",
#                            "company": None,
#                            "public_repos": 12
#                            }
#        self.assertEqual(False, originalDictionary == annonymisedDictionary)

#
    def testAppendDataToJsonFile(self):
        pd = PopulateData()
        data = [
            {
                "user": "SteDavis20",
                "fullname": "Stephen Davis",
                "location": "Kildare",
                "public_repos": 13,
                "follower_count": 17,
                "following_count": 20,
                "follower_ratio": 0.85
            }
        ]   
        fileName = "dataSampleTest.json"
        pd.appendDataToJSONFile(data, fileName)
        save_path = '../Visualisation/visualisation-app/src'
        name_of_file = fileName
        completeName = os.path.join(save_path, name_of_file)
        readData = open(completeName).read()
        self.assertEqual(data, readData)
