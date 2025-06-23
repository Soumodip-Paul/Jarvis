
import os
import pywhatkit
import speech_recognition as sr
import win32com.client
from bs4 import BeautifulSoup
from datetime import datetime
from markdown2 import markdown



sites = [
        ["Google", "https://www.google.com"],
        ["YouTube", "https://www.youtube.com"],
        ["Facebook", "https://www.facebook.com"],
        ["Twitter", "https://www.twitter.com"],
        ["Instagram", "https://www.instagram.com"],
        ["LinkedIn", "https://www.linkedin.com"],
        ["Reddit", "https://www.reddit.com"],
        ["Wikipedia", "https://www.wikipedia.org"],
        ["Amazon", "https://www.amazon.com"],
        ["eBay", "https://www.ebay.com"]
    ]

apps = [
        ["Microsoft Excel", "excel"],
        ["Visual Studio Code", "code"],
        ["Notepad", "notepad"],
        ["Microsoft Edge", "msedge"],
        ["Google Chrome", "chrome"],
        ["Mozilla Firefox", "firefox"]
    ]

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

# Function to load application name from a file
def load_name():
    """
    Loads the application name from a file named 'app_name.txt'.
    If the file does not exist, it creates one with a default name.
    """
    global App_Name
    if os.path.exists("app_name.txt"):
        with open("app_name.txt", "r", encoding="utf-8") as file:
            App_Name = file.read().strip()
    else:
        App_Name = "Assistant"
        with open("app_name.txt", "w", encoding="utf-8") as file:
            file.write(App_Name)
    print(f"Application Name: {App_Name}")

def play_youtube_video(query):
    """
    Searches for a video on YouTube and plays the first result.
    
    Args:
        query (str): The song title and/or artist to search for.
    """
    if not query:
        print("Error: Please provide a song name or search query.")
        return
        
    try:
        print(f"Searching for '{query}' on YouTube...")
        # This command searches for the query and plays the top video result
        pywhatkit.playonyt(query)
        print("✅ Success! The video should be playing in your browser.")
    except Exception as e:
        # This catches potential errors, like no internet connection
        print(f"An error occurred: {e}")
        print("Please check your internet connection and try again.")

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

#function to convert text to image and store it in the /ai/images folder with filename as current date and time
def text_to_image(text):
    """
    Converts text to an image and saves it in the /ai/images folder with the current date and time as the filename.
    
    :param text: The text to be converted to an image.
    """
    if not os.path.exists("ai/images"):
        os.makedirs("ai/images")
    
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.png")
    filepath = os.path.join("ai/images", filename)
    
    try:
        pywhatkit.text_to_handwriting(text, save_to=filepath)
        print(f"Image saved to {filepath}")
    except Exception as e:
        print(f"Error converting text to image: {e}")

# function to load chat history from a file
def load_chat_history(filename):
    """
    Loads chat history from a file in the /ai/chats folder.
    
    :param filename: The name of the file to load the chat history from.
    :return: The chat history as a string, or None if the file does not exist.
    """
    filepath = os.path.join("ai/chats", filename)
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    else:
        print(f"Chat history file {filename} does not exist.")
        return None

# clear chat history command
def clear_chat_history():
    """
    Clears the chat history by deleting all files in the /ai/chats folder.
    """
    chat_folder = "ai/chats"
    if os.path.exists(chat_folder):
        for filename in os.listdir(chat_folder):
            file_path = os.path.join(chat_folder, filename)
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    else:
        print("Chat history folder does not exist.")

def clear_responses():
    """
    Clears the responses by deleting all files in the /ai/responses folder.
    """
    response_folder = "ai/responses"
    if os.path.exists(response_folder):
        for filename in os.listdir(response_folder):
            file_path = os.path.join(response_folder, filename)
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    else:
        print("Response folder does not exist.")
