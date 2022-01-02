import "./BarChart.css";
import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Graph(props) {
  const {comparingSingleUser, graphData} = props 
  return (
    // <ResponsiveContainer width={800} height="100%">
    <BarChart width={1250} height={500} data={graphData}>
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
      <CartesianGrid/>
      <Tooltip/>
      <Legend/>
      </BarChart>
      // </ResponsiveContainer>
  );
}

export default Graph