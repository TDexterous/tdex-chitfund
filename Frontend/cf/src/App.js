import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';

function App() {
  return (
    <>
    <Navbar/>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <h1> Welcome </h1> 
          <h3>to T-Dex ChitFunds. </h3>
          "Your Future, Our Priority"
        </p>
        <a
          className="App-link"
          href="https://www.technodexterous.com/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn latest technologies from Home 
        </a>
      </header>
    </div>
    </>
  );
}

export default App;
