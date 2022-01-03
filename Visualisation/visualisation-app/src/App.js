import { Component } from 'react';
import './App.css';
import UserProfile from './components/UserProfile'
import BarChart from './components/BarChart';
import LineChartFunction from './components/LineChart';
import PieChartFunction from './components/PieChart';
import RadarChartFunction from './components/RadarChart';
import SearchBar from './components/SearchBar';
import Dropdown from './components/Dropdown';

class App extends Component {

  constructor() {
    super();
    this.state = {
      loading: false,
      loadingRepoContributors: false,
      username: '',
      userInfo: [],
      followerInfo: [],
      accumulatedInfo: [],
      languageStats: [],
      repoDropdownData: [],
      dropdownRepoChoice: '',
      repoContributorData: [],
      languagesCount: 0
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
          this.setState({loading: false})
    });
  }

  fetchFollowerInfo() {
    fetch("/"+this.state.username+"/followerInfo").then(
      res => res.json()
      ).then(
        data => {
          this.setState({followerInfo: data});
          this.fetchAccumulatedInfo()
    });
  }

  fetchAccumulatedInfo() {
    fetch("/"+this.state.username+"/accumulatedCounts").then(
      res => res.json()
      ).then(
        data => {
          this.setState({accumulatedInfo: data});
    });
  }

  fetchLanguageStats() {
    fetch("/"+this.state.username+"/languageStats").then(
      res => res.json()
      ).then(
        data => {
          this.setState({languageStats: data});
          this.setState({languagesCount: data.length});
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

  fetchRepoContributors() {
    fetch("/"+this.state.username+"/"+this.state.dropdownRepoChoice+"/contributors").then(
      res => res.json()
      ).then(
        data => {
          this.setState({repoContributorData: data});
          this.setState({loadingRepoContributors:false});
    });
  }  

  render() {

    let dropdownHeading = "View List of "+ this.state.username +"'s Public Repos By Clicking Button Below"

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
        this.state.accumulatedInfo.length>0 && this.state.languageStats.length>0 &&
          <>
            <h2>{this.state.username}'s Details</h2>        
            <UserProfile 
              userData={this.state.userInfo}
              languagesCount={this.state.languagesCount}
              accumulatedData={this.state.accumulatedInfo}
            />
    
            <h2>{this.state.username}'s Repo vs Follower vs Following Count</h2>
            <p>This graph measures the number of followers a user has vs the number of public repositories the user
               has. Perhaps there is a relationship between these values?
            </p>

            <BarChart comparingSingleUser={true} graphData={this.state.userInfo}/>
          </>
        }

        { !this.state.loading && this.state.languageStats.length>0 &&
          <>
            <h2>{this.state.username}'s Language Stats</h2>
            <p>The following pie chart illustrates the usage of different languages seen 
              throughout {this.state.username}'s repositories.
            </p>

        {/* Have list of the languages in bullet points */}
          <PieChartFunction 
            usage="languages"
            graphData={this.state.languageStats}/>

            <h2>{dropdownHeading}</h2>
            <Dropdown 
                      list={this.state.repoDropdownData}
                      title="View Repos"
            />

          </>
        }

        { !this.state.loading && this.state.followerInfo.length>0 &&
          <>        
          <h2>Followers VS Repo Count of {this.state.username}'s Followers</h2>
            <p>This graph measures the number of followers a user has vs the number of public repositories the user
               has. Perhaps there is a relationship between these values?
            </p>

            <RadarChartFunction graphData={this.state.followerInfo}/>

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

            <BarChart comparingSingleUser={false} graphData={this.state.followerInfo}/>

            {/* <h2>{dropdownHeading}</h2>
            <Dropdown 
                      list={this.state.repoDropdownData}
                      title="View Repos"
            /> */}

          </>
        }             

        {/* { !this.state.loadingRepoContributors && this.state.repoContributorData.length>0 &&
            <>
            <h2>Contributors to {this.state.username}'s {this.state.dropdownRepoChoice} Repo</h2>
            <PieChartFunction
              usage="contributors"
              graphData={this.state.repoContributorData}
            />
            </>

        } */}

      </header>
    </div>
  );
 }
}

export default App;
