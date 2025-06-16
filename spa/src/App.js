import logo from './logo.svg';
import './App.css';
import Cricket from './components/cricket';
function App() {
  return (
    <div>
      <Cricket target={200} totalOvers={10} />
      <br></br>
    </div>
  );
}

export default App;
