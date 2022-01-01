import { Component } from 'react';
import './App.css';
import Graph from './components/Graph';
import LineChartFunction from './components/LineChart';
import PieChartFunction from './components/PieChart';
// import RadarChartFunction from './components/RadarChart';
import SearchBar from './components/SearchBar';
import Dropdown from './components/Dropdown';

class App extends Component {

  constructor() {
    super();
    this.state = {
      loading: false,
      username: '',
      userInfo: [],
      followerInfo: [],
      // accumulatedCountData: [],
      languageStats: [],
      // location: [
      //   {
      //       id: 0,
      //       title: 'New York',
      //       selected: false,
      //       key: 'location'
      //   },
      //   {
      //       id: 1,
      //       title: 'Dublin',
      //       selected: false,
      //       key: 'location'
      //   },
      //   {
      //       id: 2,
      //       title: 'California',
      //       selected: false,
      //       key: 'location'
      //   },
      //   {
      //       id: 3,
      //       title: 'Istanbul',
      //       selected: false,
      //       key: 'location'
      //   },
      //   {
      //       id: 4,
      //       title: 'Izmir',
      //       selected: false,
      //       key: 'location'
      //   },
      //   {
      //       id: 5,
      //       title: 'Oslo',
      //       selected: false,
      //       key: 'location'
      //   }
      // ],
      repoDropdownData: []
      // repoNames: [
      //   {
      //     id: 0,
      //     title: "repo-name",
      //     selected: false,
      //     key: 'location'
      //   }
      // ]
    }
    this.handleUserFormSubmit = this.handleUserFormSubmit.bind(this);
    this.handleFormChange= this.handleFormChange.bind(this);
  }
 
  handleFormChange(event) {
    this.setState({username: event.target.value});  
  }

  handleUserFormSubmit(event) {
    event.preventDefault();
    this.setState({loading: true});
    this.fetchUserInfo()
    this.fetchFollowerInfo()
    // this.fetchUserAccmulatedCount()
    this.fetchLanguageStats()
    this.fetchRepoDropdownData()
  }
    
  // to get string version of JSON data use JSON.stringify(data)
  // recharts needs to use JSON object array so do not stringify to pass data into recharts
  fetchUserInfo() { 
    fetch("/"+this.state.username+"/info").then(
      res => res.json()
      ).then(
        data => {
          let list = [];
          list.push(data);
          this.setState({userInfo: list});
    });
  }

  fetchFollowerInfo() {
    fetch("/"+this.state.username+"/followerInfo").then(
      res => res.json()
      ).then(
        data => {
          this.setState({followerInfo: data});
    });
  }

  // fetchUserAccmulatedCount() {
  //   fetch("/"+this.state.username+"/accumulatedRatio").then(
  //     res => res.json()
  //     ).then(
  //       data => {
  //         this.setState({accumulatedCountData: data});
  //   });
  // }

  fetchLanguageStats() {
    fetch("/"+this.state.username+"/languageStats").then(
      res => res.json()
      ).then(
        data => {
          this.setState({languageStats: data});
    });
  }

  fetchRepoDropdownData() {
    fetch("/"+this.state.username+"/repoDropdownData").then(
      res => res.json()
      ).then(
        data => {
          this.setState({repoDropdownData: data});
          this.setState({loading:false});
    });
  }

  resetThenSet = (id, key) => {
    const temp = [...this.state[key]];
  
    temp.forEach((item) => item.selected = false);
    temp[id].selected = true;
  
    this.setState({
      [key]: temp,
    });
  }  

  render() {

    let dropdownHeading = "Select one of "+ this.state.username +"'s repos to see if he is a key contributor"

    return (
      <div className="App">
        <h1>Github API Visualisation</h1>
        <h3 className="note">If invalid username is submitted, default user "SteDavis20" will be searched.</h3>
        <header className="App-header">

        <SearchBar  label="Search Username"
                    type="text"
                    id="header-search"
                    placeholder="Search Username"
                    name="s"
                    onChange={this.handleFormChange}
                    value={this.state.username}
                    handleUserFormSubmit={this.handleUserFormSubmit}
        />

        { !this.state.loading && this.state.userInfo.length>0 &&
          <>
            <h2>Basic User Details</h2>        
          
    
            <h2>Followers VS Repo Count</h2>
            <p>This graph measures the number of followers a user has vs the number of public repositories the user
               has. Perhaps there is a relationship between these values?
            </p>

            <Graph comparingSingleUser={true} graphData={this.state.userInfo}/>

            <h2>Followers VS Following Count</h2>
            <p>This graph measures the number of followers a user has vs the number of people the user is following
              . Perhaps there is a relationship between these values?
            </p>
          {/* <RadarChartFunction data={this.state.userInfo}/> */}
          </>
        }

        { !this.state.loading && this.state.languageStats.length>0 &&
          <>
            <h2>{this.state.username}'s Language Stats</h2>
            <p>The following pie chart illustrates the usage of different languages seen throughout
              {this.state.username}'s repositories.
            </p>

        {/* Have list of the languages in bullet points */}
            <PieChartFunction data={this.state.languageStats}/>
          </>
        }

        { !this.state.loading && this.state.followerInfo.length>0 &&
          <>        
        {/* check 'rating' of user's followers by analysing their follower ratio */}
            <h2>Follower vs Following Count of {this.state.username}'s Followers</h2>
            <p>The following graph illustrates the difference in followers to following for a user's followers.
              For example, a user with 10 followers who follows 20 github users would have a ratio of (10/20) = 0.5.
            </p>

            <LineChartFunction data={this.state.followerInfo}/>
        
            <h2>Basic Follower Ratio of {this.state.username}'s Followers</h2>
            <p>This graph highlights the basic follower ratio of each of the given user's followers. One could argue
              that the higher the ratio a follower has, the more skilled they are since more people want to follow them,
              than they want to follow.
            </p>

            <Graph comparingSingleUser={false} graphData={this.state.followerInfo}/>

            <h2>{dropdownHeading}</h2>
            <Dropdown 
                      title="Select repo"
                      // list={this.state.location}
                      list={this.state.repoDropdownData}
                      resetThenSet={this.resetThenSet}
            />

          </>
        }             

        {/* <h2>Accumulated Follower Ratio</h2>
        <p> Comparing the number of followers of one user against the number of followers of another user may
           not be a truely accurate reflection on the "quality" of a software engineer. To get a more in-depth
           comparison one could get the accumulated followers and accumulated number of users one is following.
           The accumulated followers is calculated by finding the sum of the number of followers each of the
           user's followers has. Likewise, the accumulated following value is calculated by finding the sum of the
           number of users each follower of the user is following. 
          The purpose here is to emphasise the "quality" of a follower. At first glance, a user who has 10
           followers may appear to be more followed than a user who has 5 followers. But if each of the 10 followers
           of the 1st user has only 2 followers each, this value = 20 (10*2). If each of the 5 followers of the 2nd
           user has 20 followers each, then this accumulated follower count = 100 (5*20).
           One could conclude that the user with 5 followers actually has more valuable followers than the user with
           10 followers.
        </p>    */}
      </header>
    </div>
  );
 }
}

export default App;
