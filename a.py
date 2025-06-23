import os
import webbrowser
import pywhatkit
from gen_ai import generate
from utils import play_youtube_video, markdown_to_plain_text, speak, listen, save_chat_history, clear_chat_history, sites as sites_list, apps as apps_list

chatStr = ""
App_Name = None

def load_name():
    global App_Name
    if App_Name is None:
        App_Name = os.environ.get("APP_NAME")
        if not App_Name:
            try:
                from credentials import APP_NAME as creds_app_name
                App_Name = creds_app_name
            except ImportError:
                App_Name = "Assistant"  # Default name if not set

def chat_with_google(prompt):
    """
    Uses Google Gemini to generate a response based on the provided prompt.
    
    :param prompt: The input text to generate a response for.
    :return: The generated response text.
    """
    global chatStr
    chatStr += f"User: {prompt}\nAssistant: "
    print(f"Generating Response")
    response_text = generate(chatStr)
    response_text = markdown_to_plain_text(response_text if response_text else "")  # Convert Markdown to plain text
    if response_text is None:
        response_text = "I'm sorry, I couldn't generate a response.\n"
    else:
        print(f"Response: {response_text}")
        chatStr += f"{response_text}\n"
    return response_text


if __name__ == "__main__":
    load_name()  # Load the application name
    sites = sites_list
    apps = apps_list
    Asst_App_Name = App_Name
    try:
        print(f"Hello, this is Assistant the {Asst_App_Name}.")
        print("I am here to help you with your tasks. What do you need?")
        speak(f"Hello, this is Assistant the {Asst_App_Name}.")
        speak("I am here to help you with your tasks. What do you need?")
        while True:
            command = listen()
            if command is None:
                continue
            if "exit" in command.lower() or "quit" in command.lower():
                save_chat_history(chatStr)
                chatStr = ""
                break
            elif "clear all chat" in command.lower():
                # Example: Clear chat history
                speak("Clearing all chat history.")
                chatStr = ""
                clear_chat_history()
            elif "open" in command.lower():
                found = False
                for site in sites:
                    if site[0].lower() in command.lower():
                        speak(f"Opening {site[0]}.")
                        webbrowser.open(site[1])
                        found = True
                        break
                for app in apps:
                    if app[0].lower() in command.lower():
                        speak(f"Opening {app[0]}.")
                        os.system(f"start {app[1]}")
                        found = True
                        break
                if not found:
                    speak("What would you like to open?")
            elif "search" in command.lower() and "wikipedia" in command.lower():
                query = command.lower().replace("search", "").replace("wikipedia", "").strip()
                if query:
                    speak(f"Searching Wikipedia for {query}.")
                    # webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
                    response = pywhatkit.info(query,5, True)
                    speak(f"Here are the search results for {query} on Wikipedia.")
                    speak(response)
                else:
                    speak("What would you like to search for on Wikipedia?")
            elif "search" in command.lower():
                query = command.lower().replace("search", "").strip()
                if query:
                    speak(f"Searching for {query}.")
                    # webbrowser.open(f"https://www.google.com/search?q={query}")
                    pywhatkit.search(query)
                    speak(f"Here are the search results for {query}.")
                else:
                    speak("What would you like to search for?")
            elif "play" in command.lower() or "song" in command.lower():   
                song_name = command.lower().replace("play", "").replace("song", "").strip()
                if song_name:
                    speak(f"Playing {song_name} on YouTube.")
                    play_youtube_video(song_name)
                    speak(f"Now playing {song_name}.")
                    break
                else:
                    speak("What song would you like to play?")

            else:
                # speak("I am not sure how to respond to that.")
                try:
                    speak("Generating response...")
                    response = chat_with_google(command)
                    speak(response)
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    speak("Oops, something went wrong. Please try again later.")
                # print(f"Response: {response}")
        speak("Goodbye!")
    except KeyboardInterrupt:
        speak("Exiting the program.\nGoodbye!")
        save_chat_history(chatStr)
        chatStr = ""
        