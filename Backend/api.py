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
    followerInfo = pd.getFollowerInfo(user, [])
    jsonString = json.dumps(followerInfo)    
    return jsonString

@app.route("/<username>/languageStats")
def get_language_stats(username):
    user = pd.getGithubUser(username)
    list = pd.getLanguageStats(user)
    jsonString = json.dumps(list)    
    return jsonString

@app.route("/<username>/repoDropdownData")
def get_repo_dropdown_data(username):
    user = pd.getGithubUser(username)
    list = pd.getRepoDropdownData(user)
    jsonString = json.dumps(list)    
    return jsonString

@app.route("/<username>/<repoName>/contributors")
def get_repo_contributors(username, repoName):
    user = pd.getGithubUser(username)
    repo = user.get_repo(repoName)
    list = pd.getContributors(repo)
    jsonString = json.dumps(list)    
    return jsonString

# api is run on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
