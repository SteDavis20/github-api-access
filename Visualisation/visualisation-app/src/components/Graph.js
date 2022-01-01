import "./Graph.css";
import React from "react";
import { BarChart, Bar, XAxis, YAxis } from "recharts";

function Graph(props) {
  const {comparingSingleUser, graphData} = props 
  return (
    <BarChart className="graph" width={800} height={400} data={graphData}>
      { comparingSingleUser===false &&
        <>
          <XAxis dataKey="user"/>
          <YAxis dataKey="follower_ratio"/>
          <Bar dataKey="follower_ratio" fill="#8884d8" />
        </>
      }

      { comparingSingleUser===true &&
        <>
          <XAxis dataKey="user"/>
          <YAxis dataKey="follower_count"/>
          <Bar dataKey="public_repos" fill="#8884d8" />
          <Bar dataKey="follower_count" fill="#8884d8" />
        </>
      }

      </BarChart>
  );
}

export default Graph