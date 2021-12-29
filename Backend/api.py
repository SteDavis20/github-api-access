from flask import Flask
from PopulateData import *

app = Flask(__name__)

pd = PopulateData()

# cannot return list in app.route methods, must convert to json using json.dumps(list)

# localhost:5000/SteDavis20/info        - for example
@app.route("/<username>/info")
def get_user_info(username):
    user = pd.getGithubUser(username)
    dictionary = pd.extractDataIntoDictionary(user)
    dictionary = pd.removeNullDataInDictionary(dictionary)
    return dictionary

@app.route("/<username>/followerInfo")
def get_follower_info(username):
    user = pd.getGithubUser(username)
    list = pd.getFollowerInfo(user, [])
    jsonString = json.dumps(list)    
    return jsonString

@app.route("/<username>/accumulatedRatio")
def get_accumulated_ratio(username):
    user = pd.getGithubUser(username)
    list = pd.countFollowersOfFollowers(user, [])
    jsonString = json.dumps(list)    
    return jsonString

# api is run on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
