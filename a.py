import os
import webbrowser
from gen_ai import generate
from utils import markdown_to_plain_text, speak, listen, save_chat_history

chatStr = ""

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
    speak("Hello, this is a test of the SAPI voice Assistance.")
    speak("I am here to help you with your tasks. What do you need?")
    while True:
        command = listen()
        if command is None:
            continue
        if "exit" in command.lower() or "quit" in command.lower():
            save_chat_history(chatStr)
            chatStr = ""
            break
        elif "excel" in command.lower():
            # Example: Open Excel
            speak("Opening Excel.")
            os.system("start excel")
        elif "code" in command.lower():
            # Example: Open a code editor
            speak("Opening Visual Studio Code.")   
            os.system("start code")
        elif "browser" in command.lower():  
            # Example: Open a web browser
            speak("Opening your web browser.")
            os.system("start msedge")
        elif "notepad" in command.lower():
            # Example: Open Notepad
            speak("Opening Notepad.")
            os.system("start notepad")
        elif "open" in command.lower():
            found = False
            for site in sites:
                if site[0].lower() in command.lower():
                    speak(f"Opening {site[0]}.")
                    webbrowser.open(site[1])
                    found = True
                    break
            if not found:
                speak("What would you like to open?")
        else:
            # speak("I am not sure how to respond to that.")
            response = chat_with_google(command)
            speak(response)
            # print(f"Response: {response}")
    speak("Goodbye!")