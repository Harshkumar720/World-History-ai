# World History AI

An AI-powered web application that helps users explore world history through an interactive chat interface.
Users can ask questions about historical events, civilizations, and timelines, and the AI provides informative responses.

## Project Structure

```
world-history-ai
│
├ backend
│   ├ main.py
│   ├ ai_engine.py
│   ├ config.py
│   ├ requirements.txt
│   ├ routes
│   │   └ chat.py
│   └ utils
│       └ prompts.py
│
├ frontend
│   └ index.html
│
└ README.md
```

## Features

* AI-powered historical question answering
* Simple web interface
* Backend API for AI responses
* Organized backend structure with routes and utilities

## Technologies Used

* Python
* FastAPI
* HTML / CSS / JavaScript
* AI API (Groq / OpenAI)

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/your-username/world-history-ai.git
```

2. Go to the project folder

```
cd world-history-ai/backend
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the server

```
uvicorn main:app --reload
```

5. Open the frontend

Open `frontend/index.html` in your browser.

## Future Improvements

* Add historical timeline visualization
* Add voice interaction
* Improve AI response accuracy
* Deploy the app online

## Author

Harsh Kumar

