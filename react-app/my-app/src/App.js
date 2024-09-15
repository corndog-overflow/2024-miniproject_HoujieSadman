import logo from './gato.png';
import './App.css';

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAvUal2Xr2qGoR2oS1UEnDhHYJLTpPY0gU",
  authDomain: "sdk-seniordesign.firebaseapp.com",
  projectId: "sdk-seniordesign",
  storageBucket: "sdk-seniordesign.appspot.com",
  messagingSenderId: "431723260228",
  appId: "1:431723260228:web:0efb842e46ebee70b50f11",
  measurementId: "G-QP51QKWGRB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

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

const writeDataToFirestore = async (collection, data) => {
  try {
    const ref = firebase.firestore().collection(collection).doc()
    const response = await ref.set(data)
    return response
  } catch (error) {
    return error
  }
}


const data = {
  title: 'My first todo item',
  description: 'This is my first todo item',
  completed: false
}

writeDataToFirestore('2024-sen-des-mp', data)




export default App;
