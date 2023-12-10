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
function toggleshadow(element) {
  // Remove the 'inpp-hovered' class from all elements
  var elements = document.getElementsByClassName("inpp");
  for (var i = 0; i < elements.length; i++) {
    elements[i].classList.remove(".inpp:not(:hover)");
  }

  // Add the 'inpp-hovered' class to the hovered element
  element.classList.add("inpp-hovered");
}

// if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//   navigator.mediaDevices
//     .getUserMedia({ video: true, audio: false })
//     .then(function (stream) {
//       const webcam = document.getElementById("webcam");
//       webcam.srcObject = stream;
//     })
//     .catch(function (error) {
//       console.error("Error accessing webcam:", error);
//     });
// } else {
//   console.error("getUserMedia is not supported in this browser.");
// }

// document
//   .getElementById("startRecording")
//   .addEventListener("click", startRecording);
// document
//   .getElementById("stopRecording")
//   .addEventListener("click", stopRecording);

// function startRecording() {
//   navigator.mediaDevices
//     .getUserMedia({ audio: true })
//     .then(function (stream) {
//       mediaRecorder = new MediaRecorder(stream);

//       mediaRecorder.ondataavailable = function (event) {
//         if (event.data.size > 0) {
//           audioChunks.push(event.data);
//         }
//       };

//       mediaRecorder.onstop = function () {
//         const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

//         // Send the audio data to the Django backend
//         sendAudioData(audioBlob);
//       };

//       mediaRecorder.start();
//       document.getElementById("startRecording").disabled = true;
//       document.getElementById("stopRecording").disabled = false;
//     })
//     .catch(function (error) {
//       console.error("Error accessing microphone:", error);
//     });
// }

// function stopRecording() {
//   if (mediaRecorder && mediaRecorder.state === "recording") {
//     mediaRecorder.stop();
//     document.getElementById("startRecording").disabled = false;
//     document.getElementById("stopRecording").disabled = true;
//   }
// }

// function sendAudioData(audioBlob) {
//   // Use the Fetch API to send the audio data to the Django backend
//   fetch("/your-backend-endpoint", {
//     method: "POST",
//     body: audioBlob,
//   })
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Network response was not ok");
//       }
//       return response.json();
//     })
//     .then((data) => {
//       console.log("Response from backend:", data);
//     })
//     .catch((error) => {
//       console.error("Error sending audio data to backend:", error);
//     });
// }
