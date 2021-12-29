import "./Graph.css";
import React/*, { useState, useEffect }*/ from "react";
import { BarChart, Bar, XAxis, YAxis } from "recharts";
// import Data from "./data.csv"
// import { csv } from "d3";
// import FollowerData from "./followerData.json"

/*const data = [
  {
    name: "Page A",
    uv: 4000,
    pv: 2400,
    amt: 2400
  },
  {
    name: "Page B",
    uv: 3000,
    pv: 1398,
    amt: 2210
  },
  {
    name: "Page C",
    uv: 2000,
    pv: 9800,
    amt: 2290
  },
  {
    name: "Page D",
    uv: 2780,
    pv: 3908,
    amt: 2000
  },
  {
    name: "Page E",
    uv: 1890,
    pv: 4800,
    amt: 2181
  },
  {
    name: "Page F",
    uv: 2390,
    pv: 3800,
    amt: 2500
  },
  {
    name: "Page G",
    uv: 3490,
    pv: 4300,
    amt: 2100
  }
];
*/

function Graph({data}) {
  console.log(data);
  return (
    <BarChart className="graph" width={1400} height={500} data={data}>
      <XAxis dataKey="user"/>
      <YAxis dataKey="follower_ratio"/>
      <Bar dataKey="follower_ratio" fill="#8884d8" />
    </BarChart>
  );
}

export default Graph