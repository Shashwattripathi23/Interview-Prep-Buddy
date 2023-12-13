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
