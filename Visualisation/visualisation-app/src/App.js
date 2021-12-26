import './App.css';
import Graph from './Graph';
import LineChartFunction from './LineChart';
import PieChartFunction from './PieChart';
import RadarChartFunction from './RadarChart';

function App() {
  return (
    <div className="App">
      <h1>Github API Visualisation</h1>
      <header className="App-header">
        <h2>Bar Chart Heading</h2>
        <Graph/>
        <h2>Line Chart Heading</h2>
        <LineChartFunction/>
        <h2>Pie Chart Heading</h2>
        <PieChartFunction/>
        <h2>Radar Chart Heading</h2>
        <RadarChartFunction/>
      </header>
    </div>
  );
}

export default App;
