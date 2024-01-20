var tog = false;
function togg() {
  if (tog == false) {
    document.getElementById("men").style.transform = "translateY(38vh)";
    tog = true;
  } else {
    document.getElementById("men").style.transform = "translateY(0vh)";
    tog = false;
  }
}

let webcamStream; // Variable to store the webcam stream
// let mediaRecorder; // Variable to store the media recorder instance
// let audioChunks = []; // Array to store audio chunks for the current cycle
let completeAudioChunks = []; // Array to store complete audio clips

// Check if the browser supports getUserMedia
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  // Access the webcam and start it as soon as the page loads
  navigator.mediaDevices
    .getUserMedia({ video: true, audio: false })
    .then(function (stream) {
      const webcam = document.getElementById("webcam");
      webcam.srcObject = stream;
      webcamStream = stream; // Store the webcam stream for later use
    })
    .catch(function (error) {
      console.error("Error accessing webcam:", error);
    });
} else {
  console.error("getUserMedia is not supported in this browser.");
}

// Event listener for starting audio recording
// let mediaRecorder;
// // let audioChunks = [];

const startRecordingButton = document.getElementById("startRecording");
const stopRecordingButton = document.getElementById("stopRecording");

const namea = "{{name}}";
startRecordingButton.addEventListener("click", function () {
  fetch("start", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("output").innerText = data.result;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
stopRecordingButton.addEventListener("click", function () {
  fetch("end", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("output").innerText = data.result;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
