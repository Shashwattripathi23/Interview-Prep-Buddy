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
let mediaRecorder;
// let audioChunks = [];

const startRecordingButton = document.getElementById("startRecording");
const stopRecordingButton = document.getElementById("stopRecording");
const audioPlayer = document.getElementById("audioPlayer");

audioChunks = [];
navigator.mediaDevices
  .getUserMedia({ audio: true })
  .then((stream) => {
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        audioChunks.push(event.data);
      }
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
      const audioUrl = URL.createObjectURL(audioBlob);
      audioPlayer.src = audioUrl;
      document.getElementById("audioUrlI").value = audioUrl;
    };

    startRecordingButton.addEventListener("click", () => {
      mediaRecorder.start();
      startRecordingButton.disabled = true;
      stopRecordingButton.disabled = false;
    });

    stopRecordingButton.addEventListener("click", () => {
      mediaRecorder.stop();
      startRecordingButton.disabled = false;
      stopRecordingButton.disabled = true;
      if (audioChunks.length > 0) {
        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

        // Assuming you have a function sendToBackend to send the audio data
        sendToBackend(audioBlob);
      } else {
        console.error("No audio data to submit");
      }
    });
  })
  .catch((error) => console.error("Error accessing microphone:", error));

function sendToBackend(audioBlob) {
  // Create a FormData object to send the audio Blob to the backend
  const formData = new FormData();
  formData.append("audio", audioBlob, "audio.wav");

  // Use fetch or another method to send the FormData to the backend
  fetch("upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Backend response:", data);
      // Add any further handling based on the backend response
    })
    .catch((error) => {
      console.error("Error sending audio to backend:", error);
    });
  audioChunks = [];
}
const sub = document.getElementById("submitRecording");
sub.addEventListener("click", () => {
  if (audioChunks.length > 0) {
    const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

    // Assuming you have a function sendToBackend to send the audio data
    sendToBackend(audioBlob);
  } else {
    console.error("No audio data to submit");
  }
});
