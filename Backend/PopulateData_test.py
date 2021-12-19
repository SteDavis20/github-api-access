import unittest                 # testing framework

from PopulateData import PopulateData

class PopulateDataTest(unittest.TestCase):
    
    # no need for this test because if it fails, all other tests would fail.
    # Since other tests pass, this method works.
    # def testGetGithubUser(self):
        # 

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


    # can only test count of followers, because testing collection of individual data would breach privacy of
    # follower
    # note: 17 followers at time of writing test, so test may fail as more or less followers will follow over time.
    def testGetFollowerData(self):
        pd = PopulateData()
        user = pd.getGithubUser()
        self.assertEqual(17, pd.getAndStoreFollowerInfo(user))

    
    def testAnnonymisation(self):
        pd = PopulateData()
        user = pd.getGithubUser()
        annonymisedDictionary = pd.extractDataIntoDictionary(user)
        originalDictionary = {"user": "SteDavis20",
                            "fullname": "Stephen Davis",
                            "location": "Kildare",
                            "company": None,
                            "public_repos": 12
                            }
        self.assertEqual(False, originalDictionary == annonymisedDictionary)