# Measuring Software Engineering Through the Github API
The main topic I was interested in for this project was to try and determine why some Github users have more followers than others. Does the number of repositories a user have affect his/her follower count? Maybe it is nothing to do with the skill of the engineer, and it is just the case where if you follow a user they follow you back (this would be reflected by an even follower-following ratio)?


In addition to this, this project was undertaken to compare the quality of followers a given user has. Initially, one user, let's say user A, with 100 followers, would appear to be more impressive than a user, let's say user B, who has 10 followers. But what if each of user A's 100 followers only has 2 followers each, whereas each of user B's 10 followers all have 100 followers each. Then, user A would have an accumulated follower count of 100x2 = 200 followers, and user B would have 10x100 = 1,000 followers.


Another factor worth analysing is the follower-ratio of a user, measured by dividing the number of followers a user has, by the number of people the user is following.


Language statistics can also play a part in your total follower count; some followers may follow users because they are skilled in a language that the follower is only beginning to learn.


Work ethic may also play a role in determining the number of followers a user has. To analyse this, the percentage contribution a user makes towards a repo is displayed in this project. The best uses of this metric are when the repo has multiple contributors.


# To Run the Project:
A valid github user token is required, details to follow...

Install all the relevant packages and dependencies; most of these can be achieved by running the install script:

.\install.sh


Just make sure you are in the right directory before trying to run this script.

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