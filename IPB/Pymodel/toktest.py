import json
import random
patt = (r'C:\Users\SHASHWAT\Desktop\Python\Django\IPB\IPB\Pymodel\dataset.json')
# Load your skill dataset


def generate_questions_answers(skill_list, patt, num_questions):
    # Load your skill dataset
    with open(patt, 'r') as file:
        dataset = json.load(file)

    # Initialize a dictionary to store questions and answers for each skill
    skill_qa_dict = {}

    # Iterate through each skill in the input list
    for skill in skill_list:
        # Initialize lists to store questions and answers for the current skill
        skill_questions = []
        skill_answers = []

        # Search for the skill in the dataset
        for entry in dataset:
            if entry['skill'] == skill:
                # Append the question and answer to the respective lists
                skill_questions.append(entry['question'])
                skill_answers.append(entry['answer'])

        # Randomly select num_questions questions and answers for the current skill
        selected_indices = random.sample(
            range(len(skill_questions)), min(num_questions, len(skill_questions)))

        selected_questions = [skill_questions[i] for i in selected_indices]
        selected_answers = [skill_answers[i] for i in selected_indices]

        # Store the selected questions and answers for the current skill in the dictionary
        skill_qa_dict[skill] = {
            'questions': selected_questions, 'answers': selected_answers}

    return skill_qa_dict


# Example usage
input_skill_list = ["Python", "C++", "Java"]
result = generate_questions_answers(input_skill_list, patt, 5)

# Display the results
for skill, qa_data in result.items():
    print(f"Skill: {skill}")
    for i, (question, answer) in enumerate(zip(qa_data['questions'], qa_data['answers']), 1):
        print(f"Question {i}: {question}")
        print(f"Answer {i}: {answer}")
        print()
