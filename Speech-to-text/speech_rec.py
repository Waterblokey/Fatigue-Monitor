import speech_recognition as sr
import pyaudio

# Initialize the recognizer
r = sr.Recognizer()

# Define the microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    while True:
        # Adjust the energy threshold dynamically based on ambient noise
        r.adjust_for_ambient_noise(source)

        # Capture audio from the microphone
        audio = r.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)

            # Append the recogniz
            # ed text to a .txt file
            with open("output.txt", "a") as f:
                f.write(text + "\n")

            print("Recognized:", text)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Error:", e)