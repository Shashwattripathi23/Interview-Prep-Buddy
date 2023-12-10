import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Calibrate the recognizer with ambient noise
with sr.Microphone() as source:
    print("Calibrating ambient noise. Please be silent for a few seconds.")
    r.adjust_for_ambient_noise(source, duration=5)
    print("Calibration complete. You can start speaking.")

# List of questions
questions = ['question1', 'question2', 'question3']

# Use the microphone as the source for input.
with sr.Microphone() as source:
    # Loop through the questions
    for question in questions:
        SpeakText(question)

        try:
            # Listens for the user's input
            audio = r.listen(source, timeout=3)

            # Using Google to recognize audio
            user_response = r.recognize_google(audio).lower()

            print("Did you say:", user_response)
            # SpeakText(user_response)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            break  # Exit the loop on error
        except sr.UnknownValueError:
            print("No speech detected")
            continue  # Continue to the next iteration if no speech is detected

    # Additional logic after the loop (if needed)
    print("End of script")
