import { useState, useEffect, Component } from 'react';
import './App.css';
import Graph from './Graph';
import LineChartFunction from './LineChart';
import PieChartFunction from './PieChart';
import RadarChartFunction from './RadarChart';
import SearchBar from './SearchBar';

class App extends Component {

  constructor() {
    super();
    this.state = {
      loading: false,
      username: '',
      userInfo: [],
      followerInfo: [],
      accumulatedCountData: []
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
  }
    

  // to get string version of JSON data use JSON.stringify(data)
  // recharts needs to use JSON object array so do not stringify to pass data into recharts
  fetchUserInfo() { 
    fetch("/"+this.state.username+"/info").then(
      res => res.json()
      ).then(
        data => {
          this.setState({userInfo: data});
          });
    console.log("User info: "+this.state.userInfo)
  }

  fetchFollowerInfo() {
    fetch("/"+this.state.username+"/followerInfo").then(
      res => res.json()
      ).then(
        data => {
          this.setState({followerInfo: data});
          this.setState({loading:false});
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

  render() {
    return (
      <div className="App">
        <h1>Github API Visualisation</h1>
        {/* <h3 className="instructions">Pass username you want to search into command line terminal</h3> */}
         {/* <header className="App-header"> */}
        
        <SearchBar  label="Search Username"
                    type="text"
                    id="header-search"
                    placeholder="Search Username"
                    name="s"
                    onChange={this.handleFormChange}
                    value={this.state.username}
                    handleUserFormSubmit={this.handleUserFormSubmit}
        />
        
        <h2>Basic Follower Ratio</h2>
          <p>The following graph illustrates the ratio of followers to following for a user. For example, a
            user with 10 followers who follows 20 github users would have a ratio of (10/20) = 0.5.
          </p>

          {/* { this.state.loading!==true && this.state.followerInfo!==null &&
            <Graph data={this.state.followerInfo}/>
          } */}
          {/* //       <h2>Follower vs Following Count</h2> */}
  {/* //       <p> The following graph illustrates the difference in follower count and following count of a github */}
  {/* //         user. The purpose of this graph is to see if there is a significant difference in these values, and */}
  {/* //         from this one could ask why? */}
  {/* //       </p> */}
          { !this.state.loading && this.state.followerInfo!=null &&
          <LineChartFunction data={this.state.followerInfo}> </LineChartFunction>
          }
  {/* //       <h2>Follower Ratio</h2> */}
  {/* //       <p>This graph highlights the basic follower ratio of each of the given user's followers. One could argue */}
  {/* //         that the higher the ratio a follower has, the more skilled they are since more people want to follow them, */}
  {/* //         than they want to follow. */}
  {/* //       </p> */}
  {/* //       <PieChartFunction/> */}
  {/* //       <h2>Followers VS Repo Count</h2> */}
  {/* //       <p>This graph measures the number of followers a user has vs the number of public repositories the user */}
  {/* //         has. Perhaps there is a relationship between these values? */}
  {/* //       </p> */}
  {/* //       <RadarChartFunction/> */}
  {/* //       <h2>Accumulated Follower Ratio</h2> */}
  {/* //       <p> Comparing the number of followers of one user against the number of followers of another user may */}
  {/* //         not be a truely accurate reflection on the "quality" of a software engineer. To get a more in-depth */}
  {/* //         comparison one could get the accumulated followers and accumulated number of users one is following. */}
  {/* //         The accumulated followers is calculated by finding the sum of the number of followers each of the */}
  {/* //         user's followers has. Likewise, the accumulated following value is calculated by finding the sum of the */}
  {/* //         number of users each follower of the user is following.  */}
  {/* //         The purpose here is to emphasise the "quality" of a follower. At first glance, a user who has 10 */}
  {/* //         followers may appear to be more followed than a user who has 5 followers. But if each of the 10 followers */}
  {/* //         of the 1st user has only 2 followers each, this value = 20 (10*2). If each of the 5 followers of the 2nd */}
  {/* //         user has 20 followers each, then this accumulated follower count = 100 (5*20). */}
  {/* //         One could conclude that the user with 5 followers actually has more valuable followers than the user with */}
  {/* //         10 followers. */}
  {/* //       </p> */}
         {/* */}
      {/* </header> */}
    </div>
  );
 }
}

export default App;
