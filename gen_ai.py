# To run this code you need to install the following dependencies:
# pip install google-genai

from google import genai
from google.genai import types
from credentials import API_KEY


def generate(prompt):
    response = ""
    client = genai.Client(
        # api_key=os.environ.get("GEMINI_API_KEY"),
        api_key=API_KEY,
    )

    model = "gemma-3n-e4b-it"
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
