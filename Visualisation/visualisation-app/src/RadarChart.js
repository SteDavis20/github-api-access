import "./RadarChart.css";
import React from "react";
import { Radar, RadarChart, PolarGrid, Legend, PolarAngleAxis, PolarRadiusAxis } from 'recharts';

import FollowerData from "./followerData.json"

export default function App() {
  return (
    <RadarChart cx={300} cy={250} outerRadius={200} width={600} height={550} data={FollowerData}>
      <PolarGrid />
      <PolarAngleAxis dataKey="user" />
      <PolarRadiusAxis angle={30} domain={[0, 50]} />
      <Radar name="Followers" dataKey="follower_count" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
      <Radar name="Public Repos" dataKey="public_repos" stroke="#82ca9d" fill="#82ca9d" fillOpacity={0.6} />
      <Legend />
    </RadarChart>
  );
}
