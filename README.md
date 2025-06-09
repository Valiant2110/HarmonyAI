# HarmonyAI

## Overview

**HarmonyAI** is an end-to-end AI-powered music assistant that helps you:

- Generate music playlists based on your mood or activity.
- Analyze the mood of an audio file.
- Generate song lyrics based on theme and mood.
- Create melodies from mood input.

The project is built with a **FastAPI** backend and a **React** frontend.

---

## Features

- 🎵 Generate playlists from text prompts using a Large Language Model (LLM).  
- 🎧 Analyze mood from uploaded audio files (`.mp3` or `.wav`).  
- ✍️ Generate lyrics based on theme and mood inputs.  
- 🎼 Generate melodies based on mood input.  
- 💻 Responsive React frontend with a sleek UI powered by Tailwind CSS.  

---

## Tech Stack

| Component        | Technology       |
| ---------------- | ---------------- |
| Backend          | FastAPI, Python  |
| Frontend         | React, Tailwind CSS |
| Machine Learning | Dummy mood prediction (replaceable with a real model) |
| Storage          | Temporary file storage in `/tmp/uploads` |
| CORS             | Enabled for localhost frontend URLs |

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- Node.js and npm or yarn  
- Git  

---

### Backend Setup

1. Clone the repository:

    ```bash
    git clone <your-repo-url>
    cd backend
    ```

2. Create and activate a Python virtual environment:

    ```bash
    python -m venv env
    # Linux/Mac
    source env/bin/activate
    # Windows
    env\Scripts\activate
    ```

3. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI backend server:

    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8080
    ```

5. The backend will be running at: `http://localhost:8080`

---

### Frontend Setup

1. Navigate to the frontend directory (if separate) or project root:

    ```bash
    cd frontend
    ```

2. Install frontend dependencies:

    ```bash
    npm install
    # or
    yarn install
    ```

3. Start the React development server:

    ```bash
    npm start
    # or
    yarn start
    ```

4. The frontend will be running at: `http://localhost:3000`

---

## Usage

- Use the **Generate Playlist** input box to describe your mood or activity and create a playlist.  
- Upload an audio file (`.mp3` or `.wav`) to **Analyze Mood** from the audio.  
- Enter a **Theme** and **Mood** to generate song lyrics.  
- Generate a melody based on a mood input.  

---

## Project Structure

backend/
├── main.py
├── gemini_client.py
├── mood_analyzer.py
├── utils/
│ └── audio_helpers.py
├── melody_generator.py

frontend/
├── src/
│ └── App.js



---

## Notes

- The current mood prediction is a dummy random choice in `mood_analyzer.py`. Replace with a real ML model for improved accuracy.  
- Uploaded audio files are temporarily saved in `/tmp/uploads`.  
- Generated melodies are served statically from `tmp/generated`.  

---

## License

This project is licensed under the [MIT License](LICENSE).
