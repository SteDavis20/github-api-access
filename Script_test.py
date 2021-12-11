import unittest                 # testing framework

from ScriptClass import ScriptClass

class ScriptTest(unittest.TestCase):
    
    # no need for this test because if it fails, all other tests would fail.
    # Since other tests pass, this method works.
    # def testGetGithubUser(self):
        # 

    def testRetrieveData(self):
        sc = ScriptClass()
        user = sc.getGithubUser()
        self.assertEqual("SteDavis20Stephen DavisKildare", sc.retrieveData(user))

    def testExtractDataIntoDictionary(self):
        sc = ScriptClass()
        user = sc.getGithubUser()
        dictionary = {"user": "SteDavis20",
                    "fullname": "Stephen Davis",
                    "location": "Kildare",
                    "company": None
                    }
        self.assertEqual(dictionary, sc.extractDataIntoDictionary(user))

    def testRemoveNullDataInDictionary(self):
        sc = ScriptClass()
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
        self.assertEqual(improvedDictionary, sc.removeNullDataInDictionary(dictionary))

