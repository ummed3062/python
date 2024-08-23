import speech_recognition as sr
recognizer = sr.Recognizer()        # Initialize recognizer
with sr.Microphone() as source:     # Use the microphone as the audio source

    print("Please speak something...")
    audio = recognizer.listen(source)       # Listen to the user's speech
    try:
        # Recognize and convert speech to text using Google's speech recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        f = open('data.txt', 'w')

        f.write(text)
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
    finally :
        f.close()
