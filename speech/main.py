import speech_recognition as sr

def save_speech_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise

        while True:
            print("Listening... (Press 'q' to quit)")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='ru-RU')  # Convert speech to text
                print("Recognized Text:", text)

                with open('speech.txt', 'a') as file:
                    file.write(text + '\n')  # Save text to file

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

            # may not work well
            if text.lower() == 'q':
                break

if __name__ == "__main__":
    save_speech_to_text()