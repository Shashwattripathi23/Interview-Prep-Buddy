import spacy
import random
from spacy.training.example import Example

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")


train_data = [
    # Programming Languages
    (" Python is a versatile programming language.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Java is widely used in enterprise applications.",
     {"entities": [(1, 5, "TECH_SKILL")]}),
    (" C++ is known for its performance.",
     {"entities": [(1, 4, "TECH_SKILL")]}),
    (" JavaScript is essential for web development.",
     {"entities": [(1, 11, "TECH_SKILL")]}),
    (" Ruby is a dynamic, object-oriented language.",
     {"entities": [(0, 5, "TECH_SKILL")]}),
    (" PHP is commonly used for web development.",
     {"entities": [(1, 4, "TECH_SKILL")]}),
    (" Swift is Apple's programming language for iOS.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    (" Kotlin is used for Android app development.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Objective-C is used in iOS development.",
     {"entities": [(1, 12, "TECH_SKILL")]}),
    (" C# is a language developed by Microsoft.",
     {"entities": [(1, 3, "TECH_SKILL")]}),

    # Web Development
    (" HTML/CSS are fundamental for web design.",
     {"entities": [(1, 5, "TECH_SKILL"), (6, 9, "TECH_SKILL")]}),
    (" React is a popular library for building UIs.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    (" Angular is a robust front-end framework.",
     {"entities": [(1, 8, "TECH_SKILL")]}),
    (" Vue.js is known for its simplicity.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Node.js enables server-side JavaScript.",
     {"entities": [(1, 8, "TECH_SKILL")]}),
    (" Django is a high-level Python web framework.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Flask is a micro web framework for Python.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    (" Bootstrap simplifies web design.", {
     "entities": [(1, 10, "TECH_SKILL")]}),

    # Database Management
    (" SQL is used to manage relational databases.",
     {"entities": [(1, 4, "TECH_SKILL")]}),
    (" MySQL is a popular open-source database.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    (" PostgreSQL is known for its extensibility.",
     {"entities": [(1, 11, "TECH_SKILL")]}),
    (" MongoDB is a NoSQL document database.",
     {"entities": [(1, 8, "TECH_SKILL")]}),
    (" Oracle is a widely used relational database.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" SQLite is a lightweight, embedded database.",
     {"entities": [(1, 7, "TECH_SKILL")]}),

    # Cloud Computing
    (" Amazon Web Services (AWS) provides cloud services.",
     {"entities": [(22, 25, "TECH_SKILL")]}),
    (" Microsoft Azure offers cloud solutions.",
     {"entities": [(11, 16, "TECH_SKILL")]}),
    (" Google Cloud Platform (GCP) is known for its data services.",
     {"entities": [(1, 22, "TECH_SKILL")]}),

    # DevOps
    (" Docker simplifies application deployment.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Kubernetes orchestrates containerized applications.",
     {"entities": [(1, 11, "TECH_SKILL")]}),
    ("Jenkins automates the software delivery process.",
     {"entities": [(0, 7, "TECH_SKILL")]}),
    ("Ansible automates configuration management.",
     {"entities": [(0, 7, "TECH_SKILL")]}),
    ("Terraform is used for infrastructure as code.",
     {"entities": [(0, 9, "TECH_SKILL")]}),

    # Version Control
    (" Git is a distributed version control system.",
     {"entities": [(1, 4, "TECH_SKILL")]}),
    (" GitHub is a web-based platform for Git.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" GitLab provides Git repository management.",
     {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Bitbucket is a Git repository management solution.",
     {"entities": [(1, 10, "TECH_SKILL")]}),

    # Operating Systems
    (" Linux/Unix are open-source operating systems.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    (" Windows is a widely used operating system.",
     {"entities": [(1, 8, "TECH_SKILL")]}),
    (" macOS is Apple's operating system for Macs.",
     {"entities": [(1, 6, "TECH_SKILL")]}),

    # Networking
    (" TCP/IP is the fundamental suite of protocols.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    ("DNS resolves domain names to IP addresses.",
     {"entities": [(0, 3, "TECH_SKILL")]}),
    ("DHCP dynamically assigns IP addresses.",
     {"entities": [(0, 4, "TECH_SKILL")]}),
    ("VPN ensures secure communication over networks.",
     {"entities": [(0, 3, "TECH_SKILL")]}),
    ("Firewall management controls network traffic.",
     {"entities": [(0, 8, "TECH_SKILL")]}),

    # Cybersecurity
    ("Intrusion Detection Systems (IDS) monitor networks.",
     {"entities": [(0, 33, "TECH_SKILL")]}),
    ("Security Information and Event Management (SIEM) analyze security data.", {
     "entities": [(0, 34, "TECH_SKILL")]}),
    ("Encryption secures data through algorithms.",
     {"entities": [(0, 10, "TECH_SKILL")]}),
    ("Penetration Testing assesses system vulnerabilities.",
     {"entities": [(0, 19, "TECH_SKILL")]}),
    ("Firewalls protect against unauthorized access.",
     {"entities": [(0, 8, "TECH_SKILL")]}),

    # Mobile Development
    (" Android development uses Java and Kotlin.", {
     "entities": [(1, 20, "TECH_SKILL")]}),
    (" iOS development involves Swift and Objective-C.",
     {"entities": [(1, 16, "TECH_SKILL")]}),
    (" React Native enables cross-platform mobile development.",
     {"entities": [(1, 11, "TECH_SKILL")]}),
    ("Xamarin allows development for iOS and Android.",
     {"entities": [(0, 7, "TECH_SKILL")]}),

    # Data Analysis/Big Data
    ("Data Warehousing involves storing and managing large datasets.",
     {"entities": [(0, 14, "TECH_SKILL")]}),
    ("Hadoop is used for distributed storage and processing.",
     {"entities": [(0, 5, "TECH_SKILL")]}),
    ("Spark is a fast and general-purpose cluster computing system.",
     {"entities": [(0, 4, "TECH_SKILL")]}),
    (" Tableau is a powerful data visualization tool.",
     {"entities": [(1, 8, "TECH_SKILL")]}),
    (" Power BI is a business analytics tool by Microsoft.",
     {"entities": [(1, 9, "TECH_SKILL")]}),

    # Machine Learning and AI
    (" TensorFlow is an open-source machine learning framework.",
     {"entities": [(1, 11, "TECH_SKILL")]}),
    (" PyTorch is a deep learning framework.",
     {"entities": [(1, 8, "TECH_SKILL")]}),
    (" Scikit-Learn is a machine learning library.",
     {"entities": [(1, 13, "TECH_SKILL")]}),
    (" Natural Language Processing (NLP) involves language understanding.",
     {"entities": [(1, 34, "TECH_SKILL")]}),

    # Software Testing
    ("Unit Testing ensures individual units of code work correctly.",
     {"entities": [(0, 11, "TECH_SKILL")]}),
    ("Integration Testing verifies interactions between components.",
     {"entities": [(0, 19, "TECH_SKILL")]}),
    ("Test Automation automates the testing process.",
     {"entities": [(0, 16, "TECH_SKILL")]}),
    ("Selenium is used for automated testing of web applications.",
     {"entities": [(0, 8, "TECH_SKILL")]}),
    ("JUnit is a popular testing framework for Java.",
     {"entities": [(0, 5, "TECH_SKILL")]}),

    # Project Management Tools
    (" Jira is a project management and issue tracking tool.",
     {"entities": [(1, 5, "TECH_SKILL")]}),
    ("Trello is a web-based project management application.",
     {"entities": [(0, 6, "TECH_SKILL")]}),
    ("Asana is a work management and collaboration tool.",
     {"entities": [(0, 5, "TECH_SKILL")]}),
    ("Microsoft Project is a project management software.",
     {"entities": [(0, 17, "TECH_SKILL")]}),

    # Scripting
    ("Shell scripting automates repetitive tasks.",
     {"entities": [(0, 5, "TECH_SKILL")]}),
    ("PowerShell is a task automation framework.",
     {"entities": [(0, 10, "TECH_SKILL")]}),
    ("Bash is a shell and command language.",
     {"entities": [(0, 4, "TECH_SKILL")]}),

    # Virtualization
    ("VMware provides virtualization solutions.",
     {"entities": [(0, 6, "TECH_SKILL")]}),
    ("VirtualBox is a free and open-source hosted hypervisor.",
     {"entities": [(0, 10, "TECH_SKILL")]}),
    ("Hyper-V is a virtualization platform by Microsoft.",
     {"entities": [(0, 7, "TECH_SKILL")]}),

    # IoT
    ("MQTT is a lightweight messaging protocol for IoT.",
     {"entities": [(0, 4, "TECH_SKILL")]}),
    (" Raspberry Pi is a small, affordable computer for IoT projects.",
     {"entities": [(1, 13, "TECH_SKILL")]}),
    (" Arduino is an open-source electronics platform for IoT.",
     {"entities": [(1, 8, "TECH_SKILL")]}),

    # Web Services/APIs
    (" RESTful APIs enable communication between systems.",
     {"entities": [(1, 13, "TECH_SKILL")]}),
    ("SOAP is a protocol for exchanging structured information.",
     {"entities": [(0, 4, "TECH_SKILL")]}),
    ("GraphQL is a query language for APIs.",
     {"entities": [(0, 7, "TECH_SKILL")]}),

    # UI/UX Design
    (" Adobe Creative Suite includes Photoshop and Illustrator.",
     {"entities": [(1, 21, "TECH_SKILL")]}),
    (" Sketch is a design toolkit.", {"entities": [(1, 7, "TECH_SKILL")]}),
    (" Figma is a collaborative interface design tool.",
     {"entities": [(1, 6, "TECH_SKILL")]}),
    ("InVision is a digital product design platform.",
     {"entities": [(0, 8, "TECH_SKILL")]}),
    ("I am proficient in Java and Python.",
     {"entities": [(19, 23, "TECH_SKILL"), (28, 34, "TECH_SKILL")]}),
    ("My web development skills include HTML, CSS, and JavaScript.", {"entities": [
     (31, 35, "TECH_SKILL"), (37, 41, "TECH_SKILL"), (46, 56, "TECH_SKILL")]}),
    ("I have experience with React and Django frameworks.", {
     "entities": [(23, 28, "TECH_SKILL"), (33, 39, "TECH_SKILL")]}),
    ("In my previous job, I worked with SQLServer and PostgreSQL databases.",
     {"entities": [(34, 43, "TECH_SKILL"), (48, 58, "TECH_SKILL")]}),
    ("I am familiar with Docker and Git for version control.", {
     "entities": [(19, 25, "TECH_SKILL"), (30, 23, "TECH_SKILL")]}),
    ("My cybersecurity knowledge is basic, and I've used Packet Tracer for network simulation.", {
     "entities": [(3, 16, "TECH_SKILL"), (64, 76, "TECH_SKILL")]}),


]
# a = 0
# mx = 0
# for i in range(50):

# nlp = spacy.load(
#     r"C:\Users\SHASHWAT\Desktop\Python\Django\Interview Prep Buddy\IPB\Pymodel")

# Initialize and train a custom NER model
ner = nlp.get_pipe("ner")
for itn in range(12):
    random.shuffle(train_data)
    losses = {}
    for text, annotations in train_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, losses=losses)
    print(f"Iteration {itn}: Losses - {losses}")
    # Process the resume text using the trained NER model
    resume_text = """
                                    Languages : Java , C++ , Python , HTML/CSS , JavaScript , SQL , NoSQL
                                    Frameworks : ReactJs , Django ,Flask,
                                    Databases : SQLServer, PostgreSQL, MongoDB, MySQL
                                    Other Skills : RESTful APIs, Docker, Git, Linux
                                    Soft Skills : Communication, Leadership, Team Work, Decision Making, Public Speaking
        """

    doc = nlp(resume_text)

    # Extract entities (skills) with the correct label
    skills = [ent.text for ent in doc.ents if ent.label_ == 'TECH_SKILL']
    na = len(skills)
    # if na >= mx:
    #     mx = na
    #     a = i+1
    print("Skills extracted from the resume", ",".join(skills))

# Display the extracted skills
# a_str = str(a)
# mx_str = str(mx)

# Concatenate strings
# print("number of i" + a_str + "siz" + mx_str)
model_output_dir = r"C:\Users\SHASHWAT\Desktop\Python\Django\IPB\IPB\Pymodel\27"
nlp.to_disk(model_output_dir)
