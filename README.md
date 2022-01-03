# Measuring Software Engineering Through the Github API
The main topic I was interested in for this project was to see the quality of followers a given user has, where the quality of a follower is determined by their follower to following ratio. Let's say you have 2 users: user A and user B. User A has 100 followers and User B has 10 followers. Initiailly, User A would appear to be more impressive than User B. However, let's then say each of User B's 10 followers all have 100 followers each, whereas each of User A's 100 followers only have 2 followers each. Then, user A would have an accumulated follower count of 100x2 = 200 followers, and User B would have an accumulated follower count of 10x100 = 1,000 followers. Now User B appears to be more impressive.


In addition to this, I wanted to try and determine what causes a "good" follower to follower someone. Does the number of repositories a user have affect his/her follower count? Maybe it is nothing to do with the skill of the engineer, and it is just the case where if you follow a user they follow you back (this would be reflected by an even follower-following ratio)?


Language statistics can also play a part in your total follower count; some followers may follow users because they are skilled in a language that the follower is only beginning to learn.


# To Run the Project:
A valid github user token is required. My personal access token is used to run this project and is read from the "PersonalAccessToken.txt" file in this repo.

Make sure python, pip and node are installed.

Install all the relevant packages and dependencies; most of these can be achieved by running the install script:
cd Backend

.\install.sh


For front-end make sure node is installed.
Then in a separate terminal same again for front end:
cd Visualisation

cd visualisation-app

.\install-server.sh

## To run the backend api server:
cd Backend

venv\Scripts\activate

flask run


The api will be hosted on http://localhost:5000

## To run the frontend:
Open a separate terminal

cd Visualisation

cd visualisation-app

run-server.sh


The website will be hosted on http://localhost:3000


# Note on Tests
To run the test class, the file path specified here in the PopulateData.py file as "PersonalAccessToken.txt" needs to be replaced by the absolute file path of where you have this personal access token text file saved, for example, with "C:\Users\Stephen\Desktop\College_Year_3_S1\Software_Engineering\Assignments\Github_API_Access\github-api-access\PersonalAccessToken.txt"

![Screenshot of instructions for running unit tests](https://github.com/SteDavis20/github-api-access/blob/main/testing_instruction.png?raw=true)
