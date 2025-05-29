# backend/gemini_client.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_playlist(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text

def generate_lyrics(theme: str, mood: str) -> str:
    prompt = (
        f"Write original song lyrics based on the theme '{theme}' with a '{mood}' mood. "
        "Make it poetic and emotional, and structure it into verses and a chorus."
    )
    response = model.generate_content(prompt)
    return response.text