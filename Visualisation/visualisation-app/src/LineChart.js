import "./LineChart.css";
import FollowerData from "./followerData.json"
import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts";

function LineChartFunction() {
  return (
    <LineChart className = "graph"
      width={1250}
      height={500}
      data={FollowerData}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="user" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line
        type="monotone"
        dataKey="follower_count"
        stroke="#8884d8"
        activeDot={{ r: 8 }}
      />
      <Line type="monotone" dataKey="following_count" stroke="#82ca9d" />
    </LineChart>
  );
}

export default LineChartFunction