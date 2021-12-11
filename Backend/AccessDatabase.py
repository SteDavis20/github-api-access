# docker engine (docker desktop) must be running for access to work

import pymongo          # for mongodb access
import pprint           # for pretty printing database data

class AccessDatabase:

    def getData(self, githubuser):
        for user in githubuser:
            pprint.pprint(user)
            print()

    def main(self):
        print("Trying to access mongo db database")

        # Establish a connection
        connection = "mongodb://localhost:27017"         # database must be running to make connection
        client = pymongo.MongoClient(connection)

        # Create a database object
        database = client.classDB

        # githubuser is the name of the collection
        # if you mistype the collection name, e.g., githubuserr, the data will be stored in the wrong place.
        githubuser = database.githubuser.find()
        self.getData(githubuser)