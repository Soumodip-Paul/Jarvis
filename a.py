import os
import win32com.client
import speech_recognition as sr


def speak(text):
    """
    Uses the Windows SAPI to speak the given text.
    
    :param text: The text to be spoken.
    """
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def listen():
    """
    Uses the speech_recognition library to listen for audio and return the recognized text.
    
    :return: The recognized text from the audio input.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Adjust the pause threshold as needed
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None


if __name__ == "__main__":
    speak("Hello, this is a test of the SAPI voice Assistance.")
    while True:
        command = listen()
        if command is None:
            continue
        if "exit" in command.lower() or "quit" in command.lower():
            break
        elif "hello" in command.lower():
            speak("Hello! How can I assist you today?")
        elif "time" in command.lower():
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        elif "assistant" in command.lower():
            speak("I am here to help you with your tasks. What do you need?")
            while True:
                sub_command = listen()
                if sub_command is None:
                    continue
                if "exit" in sub_command.lower() or "quit" in sub_command.lower():
                    exit()
                elif "back" in sub_command.lower():
                    break
                elif "excel" in sub_command.lower():
                    # Example: Open Excel
                    speak("Opening Excel.")
                    os.system("start excel")
                elif "code" in sub_command.lower():
                    # Example: Open a code editor
                    speak("Opening Visual Studio Code.")   
                    os.system("start code")
                elif "browser" in sub_command.lower():  
                    # Example: Open a web browser
                    speak("Opening your web browser.")
                    os.system("start msedge")
                elif "open" in sub_command.lower():
                    speak("What would you like to open?")   
                else:
                    speak("I am not sure how to respond to that.")
        else:
            speak(command)
    speak("Goodbye!")