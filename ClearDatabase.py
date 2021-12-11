# docker engine (docker desktop) must be running for access to work

import pymongo          # for mongodb access
import pprint           # for pretty printing database data

class ClearDatabase:

    def clearData(self):
        # Establish a connection
        connection = "mongodb://localhost:27017"         # database must be running to make connection
        client = pymongo.MongoClient(connection)

        # Create a database object
        database = client.classDB

        # githubuser is the name of the collection
        # this deletes everything in the database.
        database.githubuser.delete_many({})
        print("Database cleared, now empty!")

    def main(self):
        print("Trying to clear mongo db database")
        self.clearData()