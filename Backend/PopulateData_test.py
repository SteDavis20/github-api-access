import os
import unittest                 # testing framework

from PopulateData import PopulateData

class PopulateDataTest(unittest.TestCase):
    
    #----------------------------------------------------------------------------------------------------------

    #       TESTS MAY FAIL AS NUMBER OF FOLLOWERS AND FOLLOWING CHANGES OVER TIME

    #----------------------------------------------------------------------------------------------------------

    # no need for this test because if it fails, all other tests would fail.
    # Since other tests pass, this method works.
    def testGetGithubUser(self):
        pd = PopulateData()
        username1 = "SteDavis20"
        user1 = pd.getGithubUser(username1)
        userType = (str)(type(user1))               # type objects cannot be split like strings can
        userTypeClassName = userType[8:34]          
        self.assertEqual("github.NamedUser.NamedUser", userTypeClassName)

    def testGetGithubUserInvalidUsername(self):
        pd = PopulateData()
        username1 = "vfvsacasc"
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

    def testExtractDataIntoDictionaryInvalidUser(self):
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
        user = pd.getGithubUser("schsvbhsvbsd")
        self.assertEqual(dictionary, pd.extractDataIntoDictionary(user))

    def testExtractDataIntoDictionaryDivideByZeroFollowing(self):
        pd = PopulateData()
        
        # need some user following 0 people for test purposes
        
        user = pd.getGithubUser("SteDavis27")
        dictionary = {"user": "SteDavis27",
                    "fullname": None,
                    "location": None,
                    "company": None,
                    "public_repos": 0,
                    "follower_count": 0,
                    "following_count": 1,
                    "follower_ratio": 0
                    }
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
        dictionary = [{
            "user": "SteDavis20",
            "public_repos": 13,
            "accumulated_Followers": 9279,
            "accumulated_Following": 50097,
            "accumulated_Ratio": 0.18522067189652075
        }]
        self.assertEqual(dictionary, pd.countFollowersOfFollowers(user, []))

    
    def testCountFollowersOfFollowersInvalidUser(self):
        pd = PopulateData()
        user = pd.getGithubUser("sncxnvjsjdnvjvn")
        dictionary = [{
            "user": "SteDavis20",
            "public_repos": 13,
            "accumulated_Followers": 9279,
            "accumulated_Following": 50097,
            "accumulated_Ratio": 0.18522067189652075
        }]
        self.assertEqual(dictionary, pd.countFollowersOfFollowers(user, []))

    # use github user with no followers and not following anyone
    def testCountFollowersOfFollowersDivideByZeroFollowing(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis27")
        dictionary = [{
            "user": "SteDavis27",
            "public_repos": 0,
            "accumulated_Followers": 0,
            "accumulated_Following": 1,
            "accumulated_Ratio": 0
        }]
        self.assertEqual(dictionary, pd.countFollowersOfFollowers(user, []))

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


    def testGetRepoNames(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis20")
        repos = [
                'College', 'Computer_Networks', 'Flow_Forwarding', 'Functional_Programming',
                'github-api-access', 'LearnPrologNow', 'measuring-engineering-report',
                'My-Processing-Projects', 'My_Python_Files', 'Software_Engineer_Biography',
                'Stock-Market-Price-Visualisation', 'SWENG', 'Web_Development'
        ]
        self.assertEqual(repos, pd.getRepoNames(user))


    def testGetRepoNamesNoRepos(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis27")
        repos = []
        self.assertEqual(repos, pd.getRepoNames(user))




    def testGetRepoContributors(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis20")
        repos = user.get_repos()
        repo = repos[0]
        contributors = [
            {   "contributor": "SteDavis20",
                "contributions": 76
            }
        ]
        self.assertEqual(contributors, pd.getContributors(repo))


    # can occur when user has not logged in to bash with github profile's gmail account
    def testGetRepoNoContributors(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis20")
        repos = user.get_repos()
        repo = repos[1]
        contributors = [
        ]
        self.assertEqual(contributors, pd.getContributors(repo))

    def testGetLanguageStats(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis20")
        languageStats = [
            {
                'Java': 164758, 'Assembly': 76972, 'Processing': 104064, 'Haskell': 5923, 'Python': 16787930,
                'C': 42265, 'JavaScript': 21779, 'PowerShell': 18930, 'CSS': 8113, 'HTML': 7522, 'Batchfile': 1375,
                'Shell': 265, 'Prolog': 25349
            }
        ]
        self.assertEqual(languageStats, pd.getLanguageStats(user))

    def testGetLanguageStatsNoRepos(self):
        pd = PopulateData()
        user = pd.getGithubUser("SteDavis27")
        languageStats = [
            {}
        ]
        self.assertEqual(languageStats, pd.getLanguageStats(user))
