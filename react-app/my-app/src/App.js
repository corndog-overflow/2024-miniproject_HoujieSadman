import logo from './gato.png';
import './App.css';

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <title>senior design</title>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to Sadman and Houjie's senior design mini project.
        </p>
        <p> Latest data from hardware: </p>
      </header>
      
    </div>
  );
}





export default App;
