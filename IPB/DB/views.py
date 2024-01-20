import pyttsx3
import os
from deepmultilingualpunctuation import PunctuationModel
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import word_tokenize, pos_tag
import nltk
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import time
import wave
import io
from pydub import AudioSegment
import urllib.request
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from PyPDF2 import PdfReader
from django.views.decorators.csrf import csrf_exempt
import spacy
import random
import requests

import speech_recognition as sr

patt = r'C:\Users\SHASHWAT\Desktop\Python\Django\IPB\IPB\Pymodel\dataset.json'


def generate(request, name):
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
        dict_data = {'FlatList': flat_list, 'name': name}
        return render(request, 'ques.html', dict_data)

    return HttpResponse("no pdf")
    # return render(request, 'inp.html')


def regenerate(request, name):
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

            return render(request, 'ques.html', {'FlatList': flat_list, 'name': name})
        except json.JSONDecodeError as e:
            return HttpResponse("Invalid request method")

    return HttpResponse("Invalid request method")


def practise(request, name):
    return render(request, 'inter.html', {'name': name})


def vocabulary_richness(text):
    words = word_tokenize(text)
    unique_words = set(words)
    richness_percentage = (len(unique_words) / len(words)) * 100
    return richness_percentage


def sentence_structure(text):
    sentences = sent_tokenize(text)
    average_sentence_length = sum(len(sent.split())
                                  for sent in sentences) / len(sentences)
    return average_sentence_length


def conciseness(text):
    words = word_tokenize(text)
    unique_words = set(words)
    concise_percentage = (len(unique_words) / len(words)) * 100
    return concise_percentage


def parallelism(text):
    sentences = sent_tokenize(text)
    parallel_structures_count = sum(1 for sent in sentences if ',' in sent)
    return parallel_structures_count


sia = SentimentIntensityAnalyzer()


# def consistent_tone(text):
#     sentiment_scores = sia.polarity_scores(text)
#     tone_consistency = max(sentiment_scores['pos'], sentiment_scores['neg'])
#     return tone_consistency


def transition_words(text):
    transition_word_list = ["however", "moreover", "therefore", "consequently"]
    transition_count = sum(text.lower().count(word)
                           for word in transition_word_list)
    return transition_count


def calculate_overall_score(text):
    # Define weights for each criterion (you may adjust these based on importance)
    weights = {
        'vocabulary_richness': 0.4,
        'sentence_structure': 0.2,
        'conciseness': 0.2,
        'transition_words': 0.1,
        'parallelism': 0.1,
        # 'consistent_tone': 0.25
    }

    # Calculate scores for each criterion
    vr_score = vocabulary_richness(text)
    ss_score = sentence_structure(text)
    conciseness_score = conciseness(text)
    tw_score = transition_words(text)
    parallelism_score = parallelism(text)
    # tone_score = consistent_tone(text)

    # Calculate weighted sum to get overall score
    overall_score = (
        weights['vocabulary_richness'] * vr_score +
        weights['sentence_structure'] * ss_score +
        weights['conciseness'] * conciseness_score +
        weights['transition_words'] * tw_score +
        weights['parallelism'] * parallelism_score
        # weights['consistent_tone'] * tone_score
    )

    stats = {'os': overall_score,
             'vo': vr_score,
             'ss': ss_score,
             'co': conciseness_score,
             'tw': tw_score,
             'pa': parallelism_score,
             #  'ct': tone_score
             }

    return stats


pnm_path = 'PunModel'

# Create an instance of the PunctuationModel and load the model from the specified path
punmodel = PunctuationModel()
# punmodel = PunctuationModel()

transition_phrases = [
    "I appreciate the thorough explanation. Now, let's delve into another aspect",
    "Great insights! Building on that, let's shift our focus to",
    "Thank you . Moving forward, I'd like to explore",
    "Excellent response. Before we move on, could you also elaborate on",
    "I find your approach quite interesting. As we transition, let's talk about",
    "Your perspective is valuable. Now, let's move on to the next question",
    "Impressive! Before we wrap up , can you also touch upon",
    "Thank you for the detailed response. Shifting gears a bit, how about we discuss",
    "Very Good!, let's now talk about",
    "You've provided valuable insights. Before we conclude this part, could you address",
    "Your experience shines through. As we progress, I'd like to hear more about",
    "Well articulated! Before we move on, I'd like to explore another aspect",
    "I'm intrigued by your approach. Now, let's shift the conversation to",
    "Thank you for the comprehensive response. As we transition, I'm curious to know more about"
]


@csrf_exempt
def recognize_speech(request):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            result = punmodel.restore_punctuation(text)

            print(f"You said: {result}")
            print(calculate_overall_score(result)['os'])
            print(calculate_overall_score(result)['vo'])
            print(calculate_overall_score(result)['ss'])
            print(calculate_overall_score(result)['co'])
            print(calculate_overall_score(result)['tw'])
            print(calculate_overall_score(result)['pa'])
            # print(calculate_overall_score(text)['ct'])
            return JsonResponse({'result': f'You said: {text}'})
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return JsonResponse({'result': 'Sorry, could not understand audio.'})
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return JsonResponse({'result': f'Error connecting to Google API: {e}'})


general_ques = ['tell me  something about yourself?',
                'What interests you about this position and our company?',
                'Describe a challenging situation you faced at work and how you handled it',
                'What skills or strengths do you possess that make you the ideal candidate for this role?'
                ]
mouth = pyttsx3.init()
recognizer = sr.Recognizer()


def listenn():
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            result = punmodel.restore_punctuation(text)
            return result
        except sr.UnknownValueError:
            mouth.say("Sorry, I did not get that,Please repeat your answer.")
            mouth.startLoop(False)
            mouth.iterate()
            mouth.endLoop()
            try:
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                result = punmodel.restore_punctuation(text)
                return result
            except:
                mouth.say("I could not hear you but let's move on")
                mouth.startLoop(False)
                mouth.iterate()
                mouth.endLoop()
                return "No Audio"
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return "No Audio"


def queAns(ques):
    mouth.say(ques)
    mouth.startLoop(False)
    mouth.iterate()
    mouth.endLoop()
    ans = listenn()
    mouth.say(random.choice(transition_phrases))
    mouth.startLoop(False)
    mouth.iterate()
    mouth.endLoop()

    stat = calculate_overall_score(ans)
    return stat


@csrf_exempt
def start(request, name):
    result = {
        'total': 0,
        'voc': [],
        'con': [],
        'tran': [],
        'par': [],
        'ss': [],
        'voc_tot': 0,
        'con_tot': 0,
        'tran_tot': 0,
        'par_tot': 0,
        'ss_tot': 0
    }
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

    # speak intro
    mouth.say(f"Let's start with your interview, {name}")
    mouth.startLoop(False)
    mouth.iterate()
    mouth.endLoop()
    # mouth.say("Let's start with your interview")
    # mouth.runAndWait()
    print("completed")

    # start with general ques [0] and general ques[1
    for i in range(2):
        print("asking", general_ques[i])
        temS = queAns(general_ques[i])
        score(temS, result)
        request.session['result'] = result

    ques_list = request.session.pop('flat_list', [])
    random.shuffle(ques_list)

    # start with 5 tech ques

    for index, ques in enumerate(ques_list):
        if index < 6:  # Process only the first 6 questions

            temS = queAns(ques['question'])
            score(temS, result)
            request.session['result'] = result

    for i in range(2, 4):
        temS = queAns(general_ques[i])
        score(temS, result)
        request.session['result'] = result

    for index, ques in enumerate(ques_list):
        if index >= 6:  # Process only the first 6 questions

            temS = queAns(ques['question'])
            score(temS, result)
            request.session['result'] = result
    return render(request, 'final.html', {'stats': result})


def score(stats, result):
    result['total'] += stats['os']
    result['voc'].append(stats['vo'])
    result['con'].append(stats['co'])
    result['tran'].append(stats['tw'])
    result['par'].append(stats['pa'])
    result['ss'].append(stats['ss'])

    result['voc_tot'] = sum(result['voc']) / len(result['voc'])
    result['con_tot'] = sum(result['con']) / len(result['voc'])
    result['tran_tot'] = sum(result['tran']) / len(result['voc'])
    result['par_tot'] = sum(result['par']) / len(result['voc'])
    result['ss_tot'] = sum(result['ss']) / len(result['voc'])


@csrf_exempt
def end(request, name):
    result = request.session.get('result', {})
    return render(request, 'final.html', {'stats': result})
