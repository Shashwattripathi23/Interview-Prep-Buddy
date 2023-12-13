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
let mediaRecorder; // Variable to store the media recorder instance
let audioChunks = []; // Array to store audio chunks

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
document
  .getElementById("startRecording")
  .addEventListener("click", startRecording);

// Event listener for stopping audio recording
document
  .getElementById("stopRecording")
  .addEventListener("click", stopRecording);

function startRecording() {
  // Request access to the user's microphone
  navigator.mediaDevices
    .getUserMedia({ audio: true })
    .then(function (stream) {
      // Store the microphone stream for later use
      const microphoneStream = stream;

      // Create a new MediaRecorder instance for audio recording
      mediaRecorder = new MediaRecorder(microphoneStream);

      // Event handler for collecting audio data in chunks
      mediaRecorder.ondataavailable = function (event) {
        if (event.data.size > 0) {
          audioChunks.push(event.data);
        }
      };

      // Event handler for when recording stops
      mediaRecorder.onstop = function () {
        const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

        // Send the audio data to the Django backend
        sendAudioData(audioBlob);

        // Clear the audio chunks for the next recording
        audioChunks = [];
      };

      // Start recording
      mediaRecorder.start();

      // Disable the start button and enable the stop button
      document.getElementById("startRecording").disabled = true;
      document.getElementById("stopRecording").disabled = false;
    })
    .catch(function (error) {
      console.error("Error accessing microphone:", error);
    });
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state === "recording") {
    // Stop the recording
    mediaRecorder.stop();

    // Disable the stop button and enable the start button
    document.getElementById("startRecording").disabled = false;
    document.getElementById("stopRecording").disabled = true;
  }
}

function sendAudioData(audioBlob) {
  // Use the Fetch API to send the audio data to the Django backend
  fetch("/your-backend-endpoint", {
    method: "POST",
    body: audioBlob,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log("Response from backend:", data);
    })
    .catch((error) => {
      console.error("Error sending audio data to backend:", error);
    });
}
