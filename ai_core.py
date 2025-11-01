import httpx
import json
from dotenv import load_dotenv
import os
from typing import List, Dict
from google import genai
from google.genai import types

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def generate_questions_from_note(note_content: str) -> list[dict] | None:
    """
    Takes a user's note and generate a llist if Q/As list if dict
    if it fauls itbrerurns None
    """
    system_prompt ="""
    You are a helpful quiz bot. Based on the user's note below:
    1. Generate a short, clear `title` for the note.
    2. Generate 3 to 5 clear questions and concise answers.
    
    Return ONLY a valid JSON object with a 'title' key and a 'quiz' key.
    The 'quiz' key must contain a list of question/answer objects.

    Example Response:
    {{
        "title": "Introduction to Flask",
        "quiz": [
            {{"question": "What is Flask?", "answer": "A lightweight web framework"}},
            {{"question": "What is the syntax to create a Flask app?", "answer": "app = Flask()"}}
        ]
    }}"""
    client = genai.Client()
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, response_mime_type="application/json", temperature=0.5),
            contents=note_content
        )
        quiz_list = json.loads(response.text)
        if quiz_list and  isinstance(quiz_list, dict) and all(isinstance(d, dict) for d in quiz_list["quiz"]):
            return quiz_list
        else:
            print("LLM returned malformed JSON")
            return None
    except Exception as e:
        print(f"Ai core error: {e}")
        return None
