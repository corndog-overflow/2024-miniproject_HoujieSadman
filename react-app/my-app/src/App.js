import logo from './gato.png';
import './App.css';

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

//get hardware data

const secret_key = "MBHJQKMNNFV2L7F3"


function fetchData() {
  fetch(`https://api.thingspeak.com/channels/2657449/fields/1.json?api_key=${secret_key}&results=3`)
    .then(res_fast => res_fast.json())
    .then(data => {
      console.log(data["feeds"][0]);
      document.getElementById("fast").innerText = data["feeds"][0]["field1"];
    });

  fetch(`https://api.thingspeak.com/channels/2657449/fields/2.json?api_key=${secret_key}&results=3`)
    .then(res_fast => res_fast.json())
    .then(data => {
      console.log(data["feeds"][1]);
      document.getElementById("slow").innerText = data["feeds"][1]["field2"];
    });

  fetch(`https://api.thingspeak.com/channels/2657449/fields/3.json?api_key=${secret_key}&results=3`)
    .then(res_fast => res_fast.json())
    .then(data => {
      console.log(data["feeds"][2]);
      document.getElementById("avg").innerText = data["feeds"][2]["field3"];
    });
    fetch(`https://api.thingspeak.com/channels/2657449/fields/4.json?api_key=${secret_key}&results=4`)
    .then(res_fast => res_fast.json())
    .then(data => {
      console.log(data["feeds"][3]);
      document.getElementById("score").innerText = data["feeds"][3]["field4"];
    });
}

// setInterval(fetchData, 5000);

fetchData();

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <title>senior design</title>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to Sadman and Houjie's senior design mini project.
        </p>
        <p>
        Latest data from hardware <br></br>
          Fastest Time: <span id = "fast">[NO DATA FOUND]</span>ms <br></br>
          Slowest Time: <span id = "slow">[NO DATA FOUND]</span>ms <br></br>
          Average Time: <span id = "avg">[NO DATA FOUND]</span>ms <br></br>
          Score: <span id = "score">[NO DATA FOUND]</span>ms <br></br>
        </p>
      </header>
      
    </div>
  );
}





export default App;
