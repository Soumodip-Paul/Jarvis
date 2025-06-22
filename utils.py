
import os
import speech_recognition as sr
import win32com.client
from bs4 import BeautifulSoup
from datetime import datetime
from markdown2 import markdown

def markdown_to_plain_text(markdown_text):
    # Convert Markdown to HTML
    html = markdown(markdown_text)
    # Strip HTML tags to get plain text
    soup = BeautifulSoup(html, "html.parser")
    plain_text = soup.get_text()
    return plain_text

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
            text = recognizer.recognize_google(audio,language='en-IN')
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def save_chat_history(chat_str):
    """
    Saves the chat history to a file in the /ai/chats folder with the current date and time as the filename.
    
    :param chat_str: The chat history string to be saved.
    """
    if not os.path.exists("ai/chats"):
        os.makedirs("ai/chats")
    
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
    filepath = os.path.join("ai/chats", filename)
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(chat_str)
    
    print(f"Chat history saved to {filepath}")


def save_response(response):
    """
    Saves the response to a file in the /ai/responses folder with the current date and time as the filename.
    
    :param response: The response string to be saved.
    """
    if not os.path.exists("ai/responses"):
        os.makedirs("ai/responses")
    
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_response.txt")
    filepath = os.path.join("ai/responses", filename)
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(response)
    
    print(f"Response saved to {filepath}")
