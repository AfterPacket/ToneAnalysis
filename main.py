import speech_recognition as sr
from textblob import TextBlob

# Create a recognizer object
r = sr.Recognizer()

# Prompt the user to speak
print("Please speak into the microphone")

# Obtain the audio data from the microphone
with sr.Microphone() as source:
    audio_data = r.listen(source)

# Recognize the speech in the audio data
try:
    text = r.recognize_google(audio_data)
    print("You said: " + text)
    
    # Use TextBlob to analyze the tone of the text
    tb = TextBlob(text)
    print("Tone: " + tb.sentiment.polarity)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said")
except sr.RequestError as e:
    print("Error: " + str(e))
