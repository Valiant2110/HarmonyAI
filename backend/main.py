# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from backend.gemini_client import generate_playlist

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/generate_playlist/")
def get_playlist(input: PromptInput):
    result = generate_playlist(input.prompt)
    return {"playlist": result}
