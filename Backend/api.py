from flask import Flask
from PopulateData import *

app = Flask(__name__)

pd = PopulateData()

# localhost:5000/testing
@app.route("/testing")
def get_test_values():
    return {"test": ["Test1", "Test2"]}

@app.route("/<username>")
def get_front_end_input(username):
    user = pd.getGithubUser(username)
    dictionary = pd.extractDataIntoDictionary(user)
    dictionary = pd.removeNullDataInDictionary(dictionary)
    return dictionary

# api is run on localhost:5000
if __name__ == "__main__":
    app.run(debug=True)
