import os
from dotenv import load_dotenv
from openai import OpenAI
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ---------- OpenAI ----------
def ask_openai(question):

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a world history expert."},
            {"role": "user", "content": question}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content


# ---------- Groq ----------
def ask_groq(question):

    prompt = f"""
You are a world history expert.

Answer the question clearly in bullet points.

Rules:
- Use 5 bullet points
- Each bullet point must start with "-"
- Keep each point short and clear
- Focus on important historical facts
- Each point must be on a new line

Example format:

- Point one
- Point two
- Point three
- Point four
- Point five

Question:
{question}
"""

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a world history expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content


# ---------- Main function used by API ----------
def ask_history_ai(question, provider="groq"):

    q = question.lower().strip()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]

    if q in greetings:
        return """Hello. I am WorldHistoryAI — your assistant for exploring world history. 
You can ask me about historical events, famous leaders, civilizations, wars, revolutions, or important dates in world history."""

    if provider == "openai":
        return ask_openai(question)

    return ask_groq(question)