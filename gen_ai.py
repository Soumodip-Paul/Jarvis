# To run this code you need to install the following dependencies:
# pip install google-genai

from google import genai
from google.genai import types
import os
API_KEY = None

# Attempt to get the API key from environment variables
# If not found, try to import it from a credentials.py file
def load_api_key():
    global API_KEY
    if API_KEY is None:
        API_KEY = os.environ.get("GEMINI_API_KEY")
        if not API_KEY:
            try:
                from credentials import API_KEY as creds_api_key
                API_KEY = creds_api_key
            except ImportError:
                raise ValueError("API key is not set. Please set the GEMINI_API_KEY environment variable or create a credentials.py file with the API_KEY variable.")

def generate(prompt):
    response = ""
    load_api_key()  # Ensure the API key is loaded before making requests
    client = genai.Client(
        # api_key=os.environ.get("GEMINI_API_KEY"),
        api_key=API_KEY,
    )

    model = "gemma-3n-e4b-it" # edit this to use a different model
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        # print(chunk.text, end="")
        response += chunk.text if chunk.text else ""

    return response

# if __name__ == "__main__":
#     generate()
