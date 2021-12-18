import unittest                 # testing framework

from PopulateDatabase import PopulateDatabase

class PopulateDatabaseTest(unittest.TestCase):
    
    # no need for this test because if it fails, all other tests would fail.
    # Since other tests pass, this method works.
    # def testGetGithubUser(self):
        # 

    def testRetrieveData(self):
        pd = PopulateDatabase()
        user = pd.getGithubUser()
        self.assertEqual("SteDavis20Stephen DavisKildare", pd.retrieveData(user))

    # note: 12 repos at time of testing, this test may fail as more repos will be created over time.
    def testExtractDataIntoDictionary(self):
        pd = PopulateDatabase()
        user = pd.getGithubUser()
        dictionary = {"user": "SteDavis20",
                    "fullname": "Stephen Davis",
                    "location": "Kildare",
                    "company": None,
                    "public_repos": 12
                    }
        self.assertEqual(dictionary, pd.extractDataIntoDictionary(user))

    def testRemoveNullDataInDictionary(self):
        pd = PopulateDatabase()
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
        pd = PopulateDatabase()
        user = pd.getGithubUser()
        self.assertEqual(17, pd.getFollowerInfo(user))

    
    def testAnnonymisation(self):
        pd = PopulateDatabase()
        user = pd.getGithubUser()
        annonymisedDictionary = pd.extractDataIntoDictionary(user)
        originalDictionary = {"user": "SteDavis20",
                            "fullname": "Stephen Davis",
                            "location": "Kildare",
                            "company": None,
                            "public_repos": 12
                            }
        self.assertEqual(False, originalDictionary == annonymisedDictionary)