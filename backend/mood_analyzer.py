import random
from typing import List

MOODS = ["happy", "sad", "energetic", "calm", "melancholic"]

def predict_mood(features) -> str:
    # Dummy random mood (replace with ML model.predict(features) if available)
    return random.choice(MOODS)

def generate_mood_description(mood: str) -> str:
    descriptions = {
        "happy": "The audio radiates cheerful and uplifting vibes, perfect for brightening your day.",
        "sad": "This track carries a somber and reflective mood, evoking deep emotions.",
        "energetic": "Packed with energy and enthusiasm, this audio is great for motivation.",
        "calm": "Soft and soothing, this mood brings a sense of peace and relaxation.",
        "melancholic": "A bittersweet tone pervades this piece, stirring nostalgic feelings.",
    }
    return descriptions.get(mood, "An intriguing mood, hard to describe in words.")
