import unittest                 # testing framework

from ScriptClass import ScriptClass

class ScriptTest(unittest.TestCase):
    
    def testRetrieveData(self):
        sc = ScriptClass()
        self.assertEqual("SteDavis20Stephen DavisKildare", sc.retrieveData())

