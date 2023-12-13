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
window.onload = function () {
  console.log("log");
};
const skills = [
  "Python",
  "Java",
  "C++",
  "JavaScript",
  "Ruby",
  "PHP",
  "Swift",
  "Kotlin",
  "Objective-C",
  "C#",
  "HTML/CSS",
  "React",
  "Angular",
  "Vue.js",
  "Node.js",
  "Django",
  "Flask",
  "Bootstrap",
  "SQL",
  "MySQL",
  "PostgreSQL",
  "MongoDB",
  "Oracle",
  "SQLite",
  "Amazon Web Services (AWS)",
  "Microsoft Azure",
  "Google Cloud Platform (GCP)",
  "Docker",
  "Kubernetes",
  "Jenkins",
  "Ansible",
  "Terraform",
  "Git",
  "GitHub",
  "GitLab",
  "Bitbucket",
  "Linux/Unix",
  "Windows",
  "macOS",
  "TCP/IP",
  "DNS",
  "DHCP",
  "VPN",
  "Firewall management",
  "Intrusion Detection Systems (IDS)",
  "Security Information and Event Management (SIEM)",
  "Encryption",
  "Penetration Testing",
  "Firewalls",
  "Android (Java/Kotlin)",
  "iOS (Swift/Objective-C)",
  "React Native",
  "Xamarin",
  "Data Warehousing",
  "Hadoop",
  "Spark",
  "Tableau",
  "Power BI",
  "TensorFlow",
  "PyTorch",
  "Scikit-Learn",
  "Natural Language Processing (NLP)",
  "Unit Testing",
  "Integration Testing",
  "Test Automation",
  "Selenium",
  "JUnit",
  "Jira",
  "Trello",
  "Asana",
  "Microsoft Project",
  "Shell scripting",
  "PowerShell",
  "Bash",
  "VMware",
  "VirtualBox",
  "Hyper-V",
  "MQTT",
  "Raspberry Pi",
  "Arduino",
  "RESTful APIs",
  "SOAP",
  "GraphQL",
  "Adobe Creative Suite (Photoshop, Illustrator)",
  "Sketch",
  "Figma",
  "InVision",
];

const skillInput = document.getElementById("skillInput");
const suggestionList = document.getElementById("suggestionList");

skillInput.addEventListener("input", function () {
  console.log("inputting");
  const inputText = skillInput.value.toLowerCase();
  const filteredSuggestions = skills.filter((skill) =>
    skill.toLowerCase().includes(inputText)
  );

  // Display or hide the suggestion list
  if (filteredSuggestions.length > 0) {
    suggestionList.style.display = "inline";
  } else {
    suggestionList.style.display = "none";
  }

  // Update the suggestion list
  suggestionList.innerHTML = "";
  filteredSuggestions.forEach((suggestion) => {
    const listItem = document.createElement("li");
    listItem.textContent = suggestion;
    listItem.onclick = function () {
      skillInput.value = suggestion;
      suggestionList.style.display = "none"; // Hide after selection
    };
    suggestionList.appendChild(listItem);
  });
});

// Hide the suggestion list when clicking outside the input
document.addEventListener("click", function (event) {
  if (!event.target.matches("#skillInput")) {
    suggestionList.style.display = "none";
  }
});

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

// const selectedSkills = [];

// // Function to update the UI with selected skills
// function updateSelectedSkillsUI() {
//   const selectedSkillsContainer = document.getElementById("selectedSkills");

//   // Clear the container before updating
//   selectedSkillsContainer.innerHTML = "";

//   // Update the UI for each selected skill
//   selectedSkills.forEach((skill) => {
//     const skillItem = document.createElement("div");
//     skillItem.className = "skill-item";

//     // Display the skill
//     skillItem.textContent = skill;

//     // Create a delete button for each skill
//     const deleteButton = document.createElement("button");
//     deleteButton.textContent = "X";
//     deleteButton.className = "delete-button";

//     // Add an event listener to delete the skill when the button is clicked
//     deleteButton.addEventListener("click", function () {
//       // Remove the skill from the array
//       const index = selectedSkills.indexOf(skill);
//       if (index !== -1) {
//         selectedSkills.splice(index, 1);
//       }

//       // Update the UI
//       updateSelectedSkillsUI();
//     });

//     // Append the delete button to the skill item
//     skillItem.appendChild(deleteButton);

//     // Append the skill item to the container
//     selectedSkillsContainer.appendChild(skillItem);
//   });
// }

// // Assuming you have a button with id "addSkillButton"
// const addSkillButton = document.getElementById("AddS");

// addSkillButton.addEventListener("click", function () {
//   const skillInput = document.getElementById("skillInput");
//   const selectedSkill = skillInput.value.trim();

//   // Check if the skill is not empty and not already in the list
//   if (selectedSkill !== "" && !selectedSkills.includes(selectedSkill)) {
//     // Add the skill to the list
//     selectedSkills.push(selectedSkill);

//     // Update the UI
//     updateSelectedSkillsUI();

//     // Clear the input field
//     skillInput.value = "";
//   }
// });

// function sendSkillsToBackend(selectedSkills) {
//   // Make an AJAX request to your Django view
//   fetch("/regenerate/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ skills: skills }),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log("Skills sent to backend:", data);
//       // You can handle the response from the backend here
//     })
//     .catch((error) => {
//       console.error("Error sending skills to backend:", error);
//     });
// }

// const regen = document.getElementById("regen");
// regen.addEventListener("click", function sendSkillsToBackend(selectedSkills) {
//   // Make an AJAX request to your Django view
//   fetch("/regenerate/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ skills: skills }),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log("Skills sent to backend:", data);
//       // You can handle the response from the backend here
//     })
//     .catch((error) => {
//       console.error("Error sending skills to backend:", error);
//     });
// });

const selectedSkills = [];

const updateSelectedSkillsUI = () => {
  const selectedSkillsList = document.getElementById("selectedSkills");

  // Ensure the element is found before proceeding
  if (!selectedSkillsList) {
    console.error("Element with ID 'selectedSkillsList' not found.");
    return;
  }

  // Clear the existing list
  selectedSkillsList.innerHTML = "";

  // Add each selected skill to the list
  selectedSkills.forEach((skill) => {
    const listItem = document.createElement("li");
    listItem.textContent = skill;

    // Add a delete button for each skill
    const deleteButton = document.createElement("button");
    deleteButton.textContent = "X";
    deleteButton.addEventListener("click", () => removeSkill(skill));

    // Append the skill and delete button to the list item
    listItem.appendChild(deleteButton);
    selectedSkillsList.appendChild(listItem);
  });

  // Update the hidden input field with the selected skills
  const selectedSkillsInput = document.getElementById("selectedSkillsInput");
  selectedSkillsInput.value = JSON.stringify(selectedSkills);
};

const addSkill = () => {
  const skillInput = document.getElementById("skillInput");
  const selectedSkill = skillInput.value.trim();

  if (selectedSkill !== "" && !selectedSkills.includes(selectedSkill)) {
    // Add the skill to the list
    selectedSkills.push(selectedSkill);

    // Update the UI
    updateSelectedSkillsUI();

    // Clear the input field
    skillInput.value = "";
  }
};

const removeSkill = (skillToRemove) => {
  // Remove the skill from the list
  const index = selectedSkills.indexOf(skillToRemove);
  if (index !== -1) {
    selectedSkills.splice(index, 1);

    // Update the UI
    updateSelectedSkillsUI();
  }
};

// Assuming you have a button with id "addSkillButton"
const addSkillButton = document.getElementById("AddS");

addSkillButton.addEventListener("click", addSkill);

const skillsForm = document.getElementById("skillsForm");

// Add a submit event listener to the form
skillsForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // Prevent the default form submission

  try {
    const response = await fetch(skillsForm.action, {
      method: skillsForm.method,
      body: new FormData(skillsForm),
    });

    if (!response.ok) {
      console.error("Error sending skills to backend:", response.statusText);
      return;
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error sending skills to backend:", error);
  }
});
const regenButton = document.getElementById("regen");
regenButton.addEventListener("click", function () {
  skillsForm.submit();
});
