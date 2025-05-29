# backend/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from backend.gemini_client import generate_playlist , generate_lyrics
import shutil
import os
from backend.mood_analyzer import predict_mood, generate_mood_description
from backend.utils.audio_helpers import extract_features
from backend.melody_generator import generate_melody

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class PromptInput(BaseModel):
    prompt: str

@app.post("/generate_playlist/")
def get_playlist(input: PromptInput):
    result = generate_playlist(input.prompt)
    return {"playlist": result}


@app.post("/analyze_mood/")
async def analyze_mood(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type not in ["audio/mpeg", "audio/wav"]:
        raise HTTPException(status_code=400, detail="Invalid audio format. Upload .mp3 or .wav only.")

    # Save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract features
    features = extract_features(file_path)

    # Predict mood
    mood = predict_mood(features)

    # Generate description
    description = generate_mood_description(mood)

    # Clean up (optional)
    os.remove(file_path)

    return {
        "mood": mood,
        "description": description
    }

class LyricsInput(BaseModel):
    theme: str
    mood: str

@app.post("/generate_lyrics/")
def get_lyrics(input: LyricsInput):
    lyrics = generate_lyrics(theme=input.theme, mood=input.mood)
    return {"lyrics": lyrics}

@app.post("/generate_melody/")
def melody_from_mood(mood: str):
    try:
        wav_path = generate_melody(mood)
        return {
            "melody_url": f"/files/{os.path.basename(wav_path)}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add static file route
from fastapi.staticfiles import StaticFiles
app.mount("/files", StaticFiles(directory="generated"), name="files")