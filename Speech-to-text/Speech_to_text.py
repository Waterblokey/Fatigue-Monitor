import speech_recognition as sr
from Sentiment_Analysis import *
import serial
import time

# Initialize the recognizer
r = sr.Recognizer()

# Inizialize serial for sending data to arduino
ser = serial.Serial('COM3', 9600, timeout=1)

def Listen_audio():
    """ Constantly listen for incoming speech, then analyze the sentiment and send to arduino """
    with sr.Microphone() as source:    # Define the microphone as the audio source
        print("Listening...")

        while True:
            # Adjust the energy threshold dynamically based on ambient noise
            r.adjust_for_ambient_noise(source)

            # Capture audio from the microphone
            audio = r.listen(source)

            try:
                # Recognize speech using Google Speech Recognition
                text = r.recognize_google(audio)

                print("Recognized:", text)
                
                # Analyze sentiment of speech
                sentiment = analyze(text)

                # Slice text to fit on LCD Display
                if len(text) > 16:
                    for i in range(0,len(text),16):
                        shorten_text = text[i:i+16]
                        ser.write((shorten_text + '\n').encode()) 
                        ser.write((sentiment + '\n').encode())   
                    print(sentiment)

                else:
                    ser.write((text + '\n').encode())
                    ser.write((sentiment + '\n').encode())
                

            except sr.UnknownValueError:
                print("Could not understand audio")

            except sr.RequestError as e:
                print("Error:", e)



if __name__ == "__main__":
    Listen_audio()

