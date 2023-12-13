from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from PyPDF2 import PdfReader
from django.views.decorators.csrf import csrf_exempt
import spacy
import random

patt = r'C:\Users\SHASHWAT\Desktop\Python\Django\IPB\IPB\Pymodel\dataset.json'


def generate(request):
    print(request.FILES)
    pdf_file = request.FILES.get('pdfFile')

    if request.method == 'POST' and pdf_file:
        if pdf_file.content_type != 'application/pdf':
            return HttpResponse('Invalid file format. Please upload a PDF file.')

        pdf_reader = PdfReader(pdf_file)
        resume_text = ''
        for page in pdf_reader.pages:
            resume_text += page.extract_text()
            print(resume_text)

        try:
            nlp = spacy.load(
                r"C:\Users\SHASHWAT\Desktop\Python\Django\IPB\IPB\Pymodel\27")
        except Exception as e:
            return HttpResponse(f'Error loading spaCy model: {str(e)}')

        doc = nlp(resume_text)
        extracted_skills = [
            ent.text for ent in doc.ents if ent.label_ == 'TECH_SKILL']

        with open(patt, 'r') as file:
            dataset = json.load(file)

        # Filter extracted skills based on those present in the JSON file
        valid_skills = [skill for skill in extracted_skills if any(
            entry['skill'] == skill for entry in dataset)]

        if not valid_skills:
            return HttpResponse('No matching skills found in the dataset.')

        skill_frequency = {}
        for skill in valid_skills:
            skill_frequency[skill] = skill_frequency.get(skill, 0) + 1

        # Initialize a list to store dictionaries for each skill
        unique_skills = list(set(valid_skills))
        skills_with_frequency = [
            {'skill': skill, 'freq': skill_frequency[skill]} for skill in unique_skills]

        # Initialize a list to store dictionaries for each skill
        skills_data = []

        for skill_data in skills_with_frequency:
            skill = skill_data['skill']
            frequency = skill_data['freq']

            ratio = frequency / len(valid_skills)
            num_questions = int(round(60 * ratio))

            # Initialize lists to store questions and answers for the current skill
            skill_questions = []
            skill_answers = []

            # Search for the skill in the dataset
            for entry in dataset:
                if entry['skill'] == skill:
                    skill_questions.append(entry['question'])
                    skill_answers.append(entry['answer'])

            # Randomly select questions and answers for the current skill
            selected_indices = random.sample(
                range(len(skill_questions)), min(num_questions, len(skill_questions)))

            selected_questions = [skill_questions[i] for i in selected_indices]
            selected_answers = [skill_answers[i] for i in selected_indices]
            # Append the data for the current skill to the list
            skills_data.append({
                'skill': skill,
                'qa_pairs': list(zip(selected_questions, selected_answers)),
            })
        flat_list = []
        for skill_data in skills_data:
            skill = skill_data['skill']
            for question, answer in skill_data['qa_pairs']:

                flat_list.append(
                    {'skill': skill, 'question': question, 'answer': answer})

                # print(
                #     f'Skill: {skill}, Question: {question}, Answer: {answer}')
        # random.shuffle(flat_list)
        request.session['flat_list'] = flat_list
        return render(request, 'ques.html', {'FlatList': flat_list})

    return HttpResponse("no pdf")
    # return render(request, 'inp.html')


# def regenerate(request):
#     if request.method == 'POST':
#         try:
#             # Assuming you have a hidden input named "selected_skills"
#             selected_skills_json = request.POST.get('selected_skills', '[]')
#             selected_skills = json.loads(selected_skills_json)

#             # Retrieve flat_list from the session
#             flat_list = request.session.pop('flat_list', [])
#             skills_data = flat_list
#             # Process the received skills and flat_list here
#             skill_questions = []
#             skill_answers = []
#             with open(patt, 'r') as file:
#                 dataset = json.load(file)
#             # Search for the skill in the dataset
#             for item in selected_skills:
#                 for entry in dataset:
#                     if entry['skill'] == item:
#                         skill_questions.append(entry['question'])
#                         skill_answers.append(entry['answer'])

#                 # Randomly select questions and answers for the current skill
#                     selected_indices = random.sample(
#                         range(len(skill_questions)), min(10, len(skill_questions)))

#                     selected_questions = [skill_questions[i]
#                                           for i in selected_indices]
#                     selected_answers = [skill_answers[i]
#                                         for i in selected_indices]
#                 # Append the data for the current skill to the list
#                     skills_data.append({
#                         'skill': skill,
#                         'qa_pairs': list(zip(selected_questions, selected_answers)),
#                     })
#             flat_listn = []
#             for skill_data in skills_data:
#                 skill = skill_data['skill']
#                 for question, answer in skill_data['qa_pairs']:

#                     flat_listn.append(
#                         {'skill': skill, 'question': question, 'answer': answer})

#                 # print(
#                 #     f'Skill: {skill}, Question: {question}, Answer: {answer}')
#         # random.shuffle(flat_list)
#             request.session['flat_list'] = flat_listn
#             return render(request, 'ques.html', {'FlatList': flat_listn})
#         except json.JSONDecodeError as e:
#             return HttpResponse("Invalid request method")

#     return HttpResponse("Invalid request method")


def regenerate(request):
    if request.method == 'POST':
        try:
            selected_skills_json = request.POST.get('selected_skills', '[]')
            selected_skills = json.loads(selected_skills_json)

            # Retrieve flat_list from the session
            flat_list = request.session.pop('flat_list', [])

            with open(patt, 'r') as file:
                dataset = json.load(file)

            skills_data = []

            for selected_skill in selected_skills:
                # Filter dataset for the selected skill
                skill_entries = [
                    entry for entry in dataset if entry['skill'] == selected_skill]

                # If entries are found for the skill
                if skill_entries:
                    skill_questions = [entry['question']
                                       for entry in skill_entries]
                    skill_answers = [entry['answer']
                                     for entry in skill_entries]

                    # Randomly select questions and answers for the current skill
                    selected_indices = random.sample(
                        range(len(skill_questions)), min(10, len(skill_questions)))

                    selected_questions = [skill_questions[i]
                                          for i in selected_indices]
                    selected_answers = [skill_answers[i]
                                        for i in selected_indices]

                    # Append the data for the current skill to the list
                    skills_data.append({
                        'skill': selected_skill,
                        'qa_pairs': list(zip(selected_questions, selected_answers)),
                    })
            # flat_listn = []
            for skill_data in skills_data:
                skill = skill_data['skill']
                for question, answer in skill_data['qa_pairs']:

                    flat_list.append(
                        {'skill': skill, 'question': question, 'answer': answer})

            flat_list.extend(skills_data)
            request.session['flat_list'] = flat_list

            return render(request, 'ques.html', {'FlatList': flat_list})
        except json.JSONDecodeError as e:
            return HttpResponse("Invalid request method")

    return HttpResponse("Invalid request method")


def practise(request):
    return render(request, 'inter.html')
