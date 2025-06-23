# Jarvis Project Setup

Follow these steps to install all required plugins and securely store your API key.

## 1. Clone the Repository

```bash
git clone https://github.com/Soumodip-Paul/Jarvis.git
cd Jarvis
```

## 2. Install Dependencies

Make sure you have Python 3.x installed. Then, install all required plugins using pip:

```bash
pip install -r requirements.txt
```

If you have additional plugins, install them as needed:

```bash
pip install plugin-name
```

## 3. Setup Your Google-GenAI for the project

Go to [Google Ai Studio](https://aistudio.google.com/) select your preffered Model, 
- For Free usage use Gemma Models
- For Paid version use Gemini Models

>In this project we are using Gemma models

After Generating theb API key create a file named `credentials.py` in the project root directory to store your API key:

```python
# credentials.py

API_KEY = "your_api_key_here"
```

Also you can set-up an Environmemnt Variable with name ```API_KEY```

**Important:**  
Do not share your `credentials.py` file or commit it to version control. Add it to your `.gitignore`:

```
credentials.py
```

## 4. Run the Project

Now you can run the `a.py` file as described in the main documentation.


# Features
This is an Personal Ai assistance. It has many features like,
* You can chat with it like a personal assistant
* You can ask it to generate any content (except Audio-Visual contents) by telling `Using Artificial Intelligence` followed by your command
* It can open some regularly used websites like Google, Youtube and others 
* It can also open Excel, VS Code, Browswer etc. 
