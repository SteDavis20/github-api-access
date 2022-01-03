import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function Graph(props) {
  const {comparingSingleUser, graphData} = props 
  
  let ultraRed = "#EF798A"
  let etonBlue = "#7FC29B"
  let cyberGrape = "#613F75"
  
  return (
    <BarChart width={1250} height={500} data={graphData}>
      { comparingSingleUser===false &&
        <>
          <XAxis dataKey="user"/>
          <YAxis dataKey="follower_ratio"/>
          <Bar dataKey="follower_ratio" fill={ultraRed} />
        </>
      }

      { comparingSingleUser===true &&
        <>
          <XAxis dataKey="user"/>
          <YAxis dataKey="follower_count"/>
          <Bar dataKey="public_repos" fill={etonBlue} />
          <Bar dataKey="follower_count" fill={ultraRed} />
          <Bar dataKey="following_count" fill={cyberGrape} />
        </>
      }
      <CartesianGrid/>
      { comparingSingleUser===false &&
        <Tooltip/>
      }
      <Legend/>
      </BarChart>
  );
}

export default Graph