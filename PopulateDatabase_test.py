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

    def testExtractDataIntoDictionary(self):
        pd = PopulateDatabase()
        user = pd.getGithubUser()
        dictionary = {"user": "SteDavis20",
                    "fullname": "Stephen Davis",
                    "location": "Kildare",
                    "company": None
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

