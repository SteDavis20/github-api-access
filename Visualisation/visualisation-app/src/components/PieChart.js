import "./PieChart.css";
import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts";

let ultraRed = "#EF798A"
let etonBlue = "#7FC29B"
let cyberGrape = "#613F75"
let wildBlueYonder = "#8FA6CB"

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", ultraRed, etonBlue, cyberGrape, wildBlueYonder];

const RADIAN = Math.PI / 180;

const renderCustomizedLabel = ({
  cx,
  cy,
  midAngle,
  innerRadius,
  outerRadius,
  percent,
  index
}: any) => {
  const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
  const x = cx + radius * Math.cos(-midAngle * RADIAN);
  const y = cy + radius * Math.sin(-midAngle * RADIAN);

  return (
    <text
      x={x}
      y={y}
      fill="black"
      textAnchor={x > cx ? "start" : "end"}
      dominantBaseline="central"
    >
      {`${(percent * 100).toFixed(0)}%`}
    </text>
  );
};

function PieChartFunction(props) {
  const { usage, graphData } = props;
  let keyOfData = ""
  if(usage==="contributors") {
    keyOfData = "contributions"
  }
  else {
    keyOfData = "value"
  }

  return (
    <PieChart width={610} height={410}>
      <Pie
        data={graphData}
        cx={200}
        cy={200}
        labelLine={false}
        label={renderCustomizedLabel}
        outerRadius={200}
        fill="#8884d8"
        dataKey={keyOfData}
      >
        {graphData.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
        ))}
      </Pie>
      <Tooltip/>
      <Legend layout="vertical" verticalAlign="top" align="left"/>
    </PieChart>
  );
}

export default PieChartFunction