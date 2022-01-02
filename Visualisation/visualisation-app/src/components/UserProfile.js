import React from "react";
// import "./UserProfile.css"

function UserProfile(props) {

    const { userData, languagesCount } = props
    
    let data = userData[0]

    console.log({data})

    let username = "n/a"
    let fullname = "n/a"
    let location = "n/a"
    let company = "n/a"
    let public_repos = "n/a"
    let follower_count = "n/a"
    let following_count = "n/a"
    let follower_ratio = "n/a"

    if("user" in data) {
        username=data["user"]
    }
    if("fullname" in data) {
        fullname=data.fullname
    }
    if("location" in data) {
        location=data.location
    }
    if("company" in data) {
        console.log("PROBLEM")
        company=data.company
    }
    if("public_repos" in data) {
        public_repos=data.public_repos
    }
    if("follower_count" in data) {
        follower_count=data.follower_count
    }
    if("following_count" in data) {
        following_count=data.following_count
    }
    if("follower_ratio" in data) {
        follower_ratio=data.follower_ratio
    }

    return (          
          <div className="user-details">
              <p><b>Username:</b> {username}</p>
              <p><b>Fullname:</b> {fullname}</p>
              <p><b>Location:</b> {location}</p>
              <p><b>Company:</b> {company}</p>
              <p><b>Public Repo Count:</b> {public_repos}</p>
              <p><b>Languages Count:</b> {languagesCount}</p>
              <p><b>Follower Count:</b> {follower_count}</p>
              <p><b>Following Count:</b> {following_count}</p>
              <p><b>Follower Ratio:</b> {follower_ratio}</p>
          </div>
    );
}

export default UserProfile;