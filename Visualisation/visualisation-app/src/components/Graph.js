import "./Graph.css";
import React from "react";
import { BarChart, Bar, XAxis, YAxis } from "recharts";

function Graph({data}) {
  return (
    <BarChart className="graph" width={1400} height={500} data={data}>
      <XAxis dataKey="user"/>
      <YAxis dataKey="follower_ratio"/>
      <Bar dataKey="follower_ratio" fill="#8884d8" />
    </BarChart>
  );
}

export default Graph